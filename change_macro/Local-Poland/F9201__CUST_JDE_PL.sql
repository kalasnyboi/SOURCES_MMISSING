{{
  config(
   alias='F9201' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F9201__CUR_JDE_PL') }}