import sys
import pyodbc
import pandas as pd
from sqlalchemy import create_engine, inspect, text

# Fix UnicodeEncodeError for Windows command prompt
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
PG_SCHEMA = "HumanResources"  # Target schema in PostgreSQL

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

# Ensure the schema exists in PostgreSQL
def ensure_schema(schema_name):
    try:
        with pg_engine.connect() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name};"))
            print(f"🛠️ Ensured schema '{schema_name}' exists in PostgreSQL.")
    except Exception as e:
        print(f"⚠️ Error creating schema '{schema_name}': {e}")

# Ensure 'person' schema exists
ensure_schema(PG_SCHEMA)

# Function to create a PostgreSQL table dynamically inside the schema
def create_pg_table(schema, table_name, df):
    try:
        with pg_engine.connect() as conn:
            inspector = inspect(pg_engine)
            full_table_name = f"{schema}.{table_name}"

            if table_name in inspector.get_table_names(schema=schema):
                print(f"🛠️ Table '{full_table_name}' already exists.")
                return

            # Generate a CREATE TABLE statement dynamically
            create_sql = f"CREATE TABLE {full_table_name} ("
            for col, dtype in zip(df.columns, df.dtypes):
                if "int" in str(dtype):
                    col_type = "INTEGER"
                elif "float" in str(dtype):
                    col_type = "FLOAT"
                elif "datetime" in str(dtype):
                    col_type = "TIMESTAMP"
                elif "bool" in str(dtype):
                    col_type = "BOOLEAN"
                else:
                    col_type = "TEXT"
                create_sql += f"{col} {col_type}, "
            create_sql = create_sql.rstrip(", ") + ");"

            conn.execute(text(create_sql))
            print(f"🛠️ Created table '{full_table_name}' in PostgreSQL.")
    except Exception as e:
        print(f"⚠️ Error creating table '{full_table_name}': {e}")

# Fetch list of tables from the 'Person' schema in SQL Server
table_query = """
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = 'HumanResources'
"""

try:
    tables_df = pd.read_sql(table_query, sql_conn)
    tables = tables_df['TABLE_NAME'].tolist()
    print(f"📌 Tables to transfer from 'Person' schema: {tables}")
except Exception as e:
    print(f"❌ Error fetching table names for 'Person' schema: {e}")
    exit()

# Loop through each table and migrate data
for table in tables:
    try:
        print(f"🔄 Transferring table: Person.{table}...")

        # Read table from SQL Server
        sql_query = f"SELECT * FROM HumanResources.{table}"
        df = pd.read_sql(sql_query, sql_conn)

        if df.empty:
            print(f"⚠️ HumanResources.{table} is empty. Skipping...")
            continue

        # Create table in PostgreSQL under the correct schema
        create_pg_table(PG_SCHEMA, table.lower(), df)

        # Load data into PostgreSQL with schema reference
        df.to_sql(table.lower(), pg_engine, schema=PG_SCHEMA, if_exists='replace', index=False, chunksize=5000)

        print(f"✅ HumanResources.{table} transferred successfully!")
    except Exception as e:
        print(f"❌ Error transferring HumanResources.{table}: {e}")

# Close SQL Server connection
sql_conn.close()
print("🎉 Data migration from 'HumanResources' schema completed successfully!")