CREATE TABLE [metadata].[process_log] (

	[pipeline_run_id] varchar(255) NULL, 
	[table_processed] varchar(255) NULL, 
	[rows_processed] int NULL, 
	[last_processed_pickup_date] datetime2(6) NULL, 
	[processed_tmstmp] datetime2(6) NULL
);

