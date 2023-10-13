{{
  config(
   alias='F0006' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F0006__CUR_JDE_PL') }}