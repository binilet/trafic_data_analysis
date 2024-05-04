{{ config(materialized='table')}}

WITH split_data AS (
    SELECT 
        split_part(data, ';', 1) AS track_id,
        unnest(string_to_array(regexp_replace(data, '^[^;]+;[^;]+;[^;]+;', ''), ';')) AS location_data
    FROM
        {{ ref('staging_traffic_data') }}
)

SELECT
    track_id,
    split_part(location_data, ' ', 1) AS lat,
    split_part(location_data, ' ', 2) AS lon,
    split_part(location_data, ' ', 3) AS speed,
    split_part(location_data, ' ', 4) AS lon_acc,
    split_part(location_data, ' ', 5) AS lat_acc,
    split_part(location_data, ' ', 6) AS time
FROM
    split_data