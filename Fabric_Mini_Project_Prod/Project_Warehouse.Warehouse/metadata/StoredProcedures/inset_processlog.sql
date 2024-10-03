create PROCEDURE metadata.inset_processlog
@pipeline_run_id varchar(255),
@table_name varchar(255),
@processed_date DATETIME2
AS
INSERT into metadata.process_log(pipeline_run_id,table_processed,rows_processed,last_processed_pickup_date,processed_tmstmp)
SELECT
@pipeline_run_id as pipeline_run_id,
@table_name as table_processed,
count(*) as rows_processed,
max(tpep_pickup_datetime) as last_processed_pickup_date,
@processed_date as processed_tmstmp
from [Project_Warehouse].[staging].[Yellow_Taxi_NYC]