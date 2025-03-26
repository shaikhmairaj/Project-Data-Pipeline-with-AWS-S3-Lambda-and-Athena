-- Create a Table In data_pipeline_db--
...................................................
CREATE EXTERNAL TABLE hw_data_cleaned (
    height FLOAT,
    weight FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
LOCATION 's3://aws-data-bucket97/processed-data/';
................................................................
--Analyzing Data by using Queries--
SELECT * FROM hw_data_cleaned;
SELECT height FROM hw_data_cleaned;
SELECT height + 2 FROM hw_data_cleaned;