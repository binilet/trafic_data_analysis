{{ config(materialized='table')}}

WITH split_data AS (
    SELECT 
        track_id,
        type,
        traveld_d,
        avg_speed,
        unnest(string_to_array(regexp_replace(data, '^[^;]+;[^;]+;[^;]+;[^;]+;', ''), ';')) AS location_data
    FROM
        {{ ref('stg_traffic-data') }}
)

SELECT
    track_id,
    type,
    traveled_d,
    avg_speed,
    split_part(location_data, ' ', 1) AS lat,
    split_part(location_data, ' ', 2) AS lon,
    split_part(location_data, ' ', 3) AS speed,
    split_part(location_data, ' ', 4) AS lon_acc,
    split_part(location_data, ' ', 5) AS lat_acc,
    split_part(location_data, ' ', 6) AS time
FROM
    split_data
WHERE
    track_id in (SELECT track_id FROM {{ ref('traffic_data_general') }})