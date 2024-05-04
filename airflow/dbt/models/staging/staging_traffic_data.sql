{{config(materialized='table')}}

SELECT 
    data
FROM
    staging_traffic_data
LIMIT 5