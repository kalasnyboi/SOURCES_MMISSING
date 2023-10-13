{{
  config(
   alias='F4201' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4201__CUR_JDE_PL') }}