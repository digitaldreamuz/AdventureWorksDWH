import sys
import pyodbc
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.dialects.postgresql import UUID

# Fix UnicodeEncodeError in Windows terminal
sys.stdout.reconfigure(encoding='utf-8')

# SQL Server Connection Details
SQL_SERVER = "WIN-L8VFDJ1G756"
SQL_DATABASE = "AdventureWorks2022"
SQL_USERNAME = "K7"
SQL_PASSWORD = "123456"

# PostgreSQL Connection Details
PG_USER = "postgres"
PG_PASSWORD = "123456"
PG_HOST = "localhost"
PG_PORT = "5432"  # Default PostgreSQL port
PG_DATABASE = "raw"
PG_SCHEMA = "HumanResources"  # Schema for the Person tables

# Establish SQL Server connection
try:
    sql_conn = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                              f"SERVER={SQL_SERVER};"
                              f"DATABASE={SQL_DATABASE};"
                              f"UID={SQL_USERNAME};"
                              f"PWD={SQL_PASSWORD}")
    print("✅ Connected to SQL Server successfully.")
except Exception as e:
    print(f"❌ SQL Server connection failed: {e}")
    exit()

# Establish PostgreSQL connection using pg8000
try:
    pg_engine = create_engine(
        f'postgresql+pg8000://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}'
    )
    print("✅ Connected to PostgreSQL successfully.")
except Exception as e:
    print(f"❌ PostgreSQL connection failed: {e}")
    exit()

# Ensure schema exists in PostgreSQL
def ensure_schema(schema_name):
    try:
        with pg_engine.connect() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name};"))
            print(f"🛠️ Ensured schema '{schema_name}' exists in PostgreSQL.")
    except Exception as e:
        print(f"⚠️ Error creating schema '{schema_name}': {e}")

# Ensure 'Person' schema exists
ensure_schema(PG_SCHEMA)

# Define SQL query for Person.Address table
sql_query = """
SELECT 
    BusinessEntityID, 
    NationalIDNumber, 
    LoginID, 
    CAST(OrganizationNode AS VARCHAR(255)) AS OrganizationNode, 
    OrganizationLevel, 
    JobTitle, 
    BirthDate, 
    MaritalStatus, 
    Gender, 
    HireDate, 
    SalariedFlag, 
    VacationHours, 
    SickLeaveHours, 
    CurrentFlag, 
    CAST(rowguid AS VARCHAR(36)) AS rowguid, 
    ModifiedDate 
FROM HumanResources.Employee
"""

try:
    print("🔄 Fetching Employee data from SQL Server...")
    df = pd.read_sql(sql_query, sql_conn)

    # Convert rowguid column to UUID format
    df["rowguid"] = df["rowguid"].astype(str)

    # Load data into PostgreSQL under 'Person' schema
    print("🚀 Loading Employee data into PostgreSQL...")
    df.to_sql("Employee", pg_engine, schema=PG_SCHEMA, if_exists='replace', index=False, chunksize=5000, dtype={"rowguid": UUID})

    print("✅ HumanResources.Employee table transferred successfully!")
except Exception as e:
    print(f"❌ Error transferring HumanResources.Employee table: {e}")

# Close SQL Server connection
sql_conn.close()
print("🎉 Data migration completed successfully!")
