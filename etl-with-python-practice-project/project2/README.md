# Sales Data ETL Pipeline using Python and SQL

## 📌 Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline to process sales data and prepare it for analytics and reporting. The pipeline extracts raw sales data from an API source, cleans and transforms the data using Python, and loads the processed data into a SQL database.

The goal of this project is to demonstrate data engineering fundamentals such as data extraction, transformation, and database loading using a real-world dataset.

---

## 📊 Data Source
- Source: Kaggle (Sales Dataset)
- Data Type: Sales data
- Access Method: API request

---

## 🔄 ETL Workflow

### 1️⃣ Extract
- Extracted sales data using API requests
- Retrieved raw data in structured format

### 2️⃣ Transform
Performed data cleaning and transformation using Python:
- Removed null values
- Removed duplicate records
- Renamed columns for consistency
- Formatted date columns
- Prepared clean, analytics-ready data

### 3️⃣ Load
Loaded the transformed data into SQL Server using Python and SQLAlchemy.

```python
# Load the data into SQL Server using append option
df.to_sql(
    'df_orders',
    con=conn,
    index=False,
    if_exists='append'
).

## 📊 SQL Analysis & Insights

After loading the transformed data into SQL Server, multiple analytical queries were performed:

### 🔹 Top-Selling Products
- Identified top 10 products based on total sales using aggregation and sorting.

### 🔹 Regional Sales Analysis
- Identified top 5 highest-selling products in each region using window functions (`ROW_NUMBER`).

### 🔹 Year-over-Year Monthly Comparison
- Compared month-over-month sales between 2022 and 2023 to analyze growth trends.

### 🔹 Category Performance Analysis
- Determined the highest-selling month for each product category.

These queries demonstrate practical use of SQL aggregations, window functions, and time-based analysis on real-world sales data.

