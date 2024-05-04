
  
    

  create  table "postgres"."public"."stg_traffic_data__dbt_tmp"
  
  
    as
  
  (
    

SELECT 
    data
FROM
    staging_traffic_data
  );
  