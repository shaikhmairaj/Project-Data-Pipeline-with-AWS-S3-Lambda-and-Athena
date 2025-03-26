# AWS Data Pipeline Project 🚀

## 📌 Project Overview
This project demonstrates a **serverless data pipeline** using **AWS S3, Lambda, Glue, and Athena** to process and query structured data.

## ⚙️ Technologies Used
- **AWS S3** – Stores raw and processed data.
- **AWS Lambda** – Processes raw data and stores results.
- **AWS Glue** – Catalogs processed data.
- **AWS Athena** – Queries the processed data using SQL.
- **GitHub** – Project version control and sharing.

## 📂 Folder Structure
AWS-Data-Pipeline/ │-- lambda_function.py # AWS Lambda function code │-- athena_queries.sql # SQL queries for Athena │-- glue_table_schema.txt # AWS Glue table schema │-- data/ # Raw & processed data files │ │-- raw-data.csv # Raw data from S3 │ │-- processed-data.csv # Processed data from S3 │-- architecture-diagram.png # AWS architecture diagram │-- README.md # Project documentation


## 🔹 AWS Workflow
1. **Raw Data Upload** – CSV files uploaded to **S3 (raw-data/)**.
2. **AWS Lambda Processing** – A Lambda function processes new data.
3. **Processed Data Storage** – Processed files saved in **S3 (processed-data/)**.
4. **AWS Glue Table** – A schema is created to query data in Athena.
5. **AWS Athena Queries** – SQL queries analyze the processed data.

## 🚀 How to Run the Project
1. Upload raw data to **S3 bucket (`aws-data-bucket97/raw-data/`)**.
2. AWS Lambda automatically processes the file and saves the output.
3. Run Athena queries to analyze processed data:
   '''sql'''
   SELECT * FROM processed_data LIMIT 10;

📊 Architecture Diagram

✨ **Future Improvements**
Integrate Amazon QuickSight for visualization.

Automate Glue crawlers for real-time schema updates.

