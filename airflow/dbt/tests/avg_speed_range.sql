WITH validation AS (
    SELECT
        CASE
            WHEN avg_speed >= 0 AND avg_speed <= 200 THEN true
            ELSE false
        END AS result
    FROM {{ ref('traffic_data_general') }}
)

SELECT * FROM validation WHERE result = false
