{{
  config(
   alias='F0101' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F0101__CUR_JDE_PL') }}