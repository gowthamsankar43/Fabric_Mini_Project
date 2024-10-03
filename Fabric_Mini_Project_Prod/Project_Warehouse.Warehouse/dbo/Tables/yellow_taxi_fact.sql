CREATE TABLE [dbo].[yellow_taxi_fact] (

	[vendor] varchar(50) NULL, 
	[tpep_pickup_datetime] date NULL, 
	[tpep_dropoff_datetime] date NULL, 
	[pu_borough] varchar(100) NULL, 
	[pu_zone] varchar(100) NULL, 
	[do_borough] varchar(100) NULL, 
	[do_zone] varchar(100) NULL, 
	[payment_method] varchar(50) NULL, 
	[passenger_count] int NULL, 
	[trip_distance] float NULL, 
	[total_amount] float NULL
);

