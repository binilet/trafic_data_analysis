{{config(materialized='view')}}

SELECT 
    data
FROM
    staging.traffic_data