{{
  config(
   alias='F4311T' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4311T__CUR_JDE_PL') }}