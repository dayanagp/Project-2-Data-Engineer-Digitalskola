{{
  config(
    materialized='view'
  )
}}

SELECT
  *
FROM
  {{ source('dwh_dbt_project', 'dim_employees') }}