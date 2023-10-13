{{
  config(
   alias='F03B11' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F03B11__CUR_JDE_PL') }}