CREATE TABLE [staging].[Yellow_Taxi_NYC] (

	[VendorID] int NULL, 
	[tpep_pickup_datetime] datetime2(6) NULL, 
	[tpep_dropoff_datetime] datetime2(6) NULL, 
	[passenger_count] bigint NULL, 
	[trip_distance] float NULL, 
	[RatecodeID] bigint NULL, 
	[store_and_fwd_flag] varchar(8000) NULL, 
	[PULocationID] int NULL, 
	[DOLocationID] int NULL, 
	[payment_type] bigint NULL, 
	[fare_amount] float NULL, 
	[extra] float NULL, 
	[mta_tax] float NULL, 
	[tip_amount] float NULL, 
	[tolls_amount] float NULL, 
	[improvement_surcharge] float NULL, 
	[total_amount] float NULL, 
	[congestion_surcharge] float NULL, 
	[Airport_fee] float NULL
);

