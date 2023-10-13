{{
  config(
   alias='F5730026' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F5730026__CUR_JDE_PL') }}