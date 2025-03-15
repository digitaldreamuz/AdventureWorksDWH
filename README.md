# AdventureWorks_SQL_POSTGRE_Ingestion
The purpose of this project is to build a data warehouse in PostgreSQL using the AdventureWorks OLTP database. The raw OLTP data will be ingested into a staging layer and then transformed using the medallion architecture:

Bronze Layer – Stores raw ingested data.
Silver Layer – Cleansed and enriched data for analysis.
Gold Layer – Aggregated data optimized for reporting and business intelligence.
Python will be used to extract and load data from SQL Server into PostgreSQL, while dbt will handle data transformations and modeling. The goal is to maintain all data within PostgreSQL, enabling efficient analytics and reporting.