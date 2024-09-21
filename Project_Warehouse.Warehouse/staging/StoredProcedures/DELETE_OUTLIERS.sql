CREATE PROCEDURE staging.DELETE_OUTLIERS
(@start_date DATETIME2,
@end_date DATETIME2)
AS
delete from staging.Yellow_Taxi_NYC WHERE tpep_pickup_datetime<@start_date or tpep_pickup_datetime>@end_date;