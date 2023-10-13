{{
  config(
   alias='F30008' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F30008__CUR_JDE_PL') }}