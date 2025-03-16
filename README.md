# 🚀 Modern Data Architecture: Building a Data Warehouse from AdventureWorks OLTP  

## 📌 Project Overview  
This project aims to design and implement a **Modern Data Architecture** using the **medallion approach (Bronze, Silver, Gold)**. It serves as a **detailed, step-by-step guide for new learners**, covering all aspects of **data ingestion, transformation, modeling, scheduling, and visualization**.  

Instead of using the **pre-built AdventureWorks Data Warehouse**, we will **construct our own from scratch** using **AdventureWorks OLTP** as the raw data source.  

This hands-on approach provides a **deeper understanding of data warehousing concepts**, making it an **excellent portfolio project** for aspiring **Data Engineers** and **Analysts**.  

### 🏗 **Understanding AdventureWorks Data Models**  
- **OLTP Data** → Used for **online transaction processing workloads** (source data).  
- **Data Warehouse (DW)** → Optimized for **analytical workloads**.  
- **Lightweight (LT) Data** → A pared-down version of the OLTP sample.  

This project follows the **Bronze-Silver-Gold** architecture using:  
- **PostgreSQL** as the Data Warehouse  
- **dbt** for data transformations  
- **Apache Airflow** for orchestration and scheduling  

---

## 🏛 **Architecture of the Project**  

![image](https://github.com/user-attachments/assets/5f2dc4b6-26c5-4307-8568-758d0d405fd5)

### **1️⃣ Data Source (AdventureWorks OLTP - SQL Server)**  
- **Raw transactional data** is stored in **Microsoft SQL Server**.  

### **2️⃣ Ingestion (Python & Apache Airflow)**  
- **Python scripts** extract data from SQL Server and load it into PostgreSQL.  
- **Apache Airflow** orchestrates the ingestion, ensuring automation.  

### **3️⃣ Data Warehouse (PostgreSQL - Medallion Architecture)**  
- **🟤 Bronze Layer** → Raw ingested data from OLTP.  
- **⚪ Silver Layer** → Cleaned, standardized, and transformed data.  
- **🟡 Gold Layer** → Optimized data for reporting and analytics.  

### **4️⃣ Data Transformation (dbt & Git)**  
- **dbt (Data Build Tool)** transforms data from **Bronze → Silver → Gold**.  
- **Git** is integrated for version control and collaboration.  

### **5️⃣ Scheduling & Orchestration (Apache Airflow)**  
- Ensures **automated data refresh** and manages dependencies.  

### **6️⃣ Reporting & Visualization (Power BI)**  
- The **Gold Layer** serves as the final dataset for **Power BI dashboards**.  

---

## 🚀 **Key Features**  
✔ **End-to-End Data Pipeline** from SQL Server → PostgreSQL → Power BI.  
✔ **Automated Ingestion & Scheduling** with Apache Airflow.  
✔ **Medallion Architecture (Bronze-Silver-Gold)** for structured data processing.  
✔ **Data Transformations with dbt** to ensure data quality.  
✔ **Version Control with Git** for reproducibility.  
✔ **Scalable & Efficient PostgreSQL Warehouse** for analytics.  
✔ **Power BI Dashboards** for business insights.  

---

## 🏆 **Strengths of This Project**  

### ✅ **Hands-On Data Warehousing Experience**  
- Build a **real-world Data Warehouse** from **OLTP data**.  
- Learn **data modeling, ETL, and reporting** step by step.  

### ✅ **Best Practice: Bronze-Silver-Gold Architecture**  
- **Bronze Layer** → Raw, ingested data.  
- **Silver Layer** → Cleaned, standardized, and transformed data.  
- **Gold Layer** → Optimized data for reporting.  

### ✅ **Automated & Scalable Design**  
- **Apache Airflow** schedules and orchestrates the entire pipeline.  
- **PostgreSQL** efficiently handles analytical workloads.  

### ✅ **Industry-Standard Tools**  
- **dbt** for modular, scalable data transformations.  
- **Power BI** for **business intelligence** & reporting.  
- **Git** for version control & collaboration.  

---

## 🔧 **Future Improvements**  

### 📊 **Data Validation & Monitoring**  
- Implement **Great Expectations** for **data quality validation**.  
- Use **dbt tests** for **consistency checks**.  

### 📈 **Incremental Data Loads**  
- Implement **Change Data Capture (CDC)** for optimized refreshes.  
- Use **incremental dbt models** instead of full table refreshes.  

### ⚡ **Performance Optimization**  
- Optimize PostgreSQL with **indexing, partitioning, and query tuning**.  
- Use **materialized views** to improve Power BI performance.  

### 📡 **Logging & Alerting**  
- Add **detailed logging** in Python scripts.  
- Enable **Airflow alerts** for failure notifications.  

### ☁️ **Cloud Deployment (Optional)**  
- Deploy PostgreSQL on **AWS RDS** / **Azure PostgreSQL**.  
- Use **dbt Cloud** for managed transformations.  

---

## 📜 **Conclusion**  
This project is a **great portfolio piece** that showcases your skills in **Data Engineering, Automation, and Analytics**.  

By building a **Modern Data Warehouse** from **OLTP data**, you gain **practical experience** in:  
✅ **Data Extraction & Ingestion**  
✅ **ETL & Data Transformation**  
✅ **Automation & Orchestration**  
✅ **Data Modeling & Governance**  
✅ **BI & Data Visualization**  
