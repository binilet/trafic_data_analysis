
SELECT 
    split_part(data,';',1) as track_id,
    split_part(data,';',2) as type,
    split_part(data,';',3) as traveld_d,
    split_part(data,';',4) as avg_speed
FROM
    "postgres"."public"."stg_traffic_data"