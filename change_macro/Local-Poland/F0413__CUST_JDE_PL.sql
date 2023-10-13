{{
  config(
   alias='F0413' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0413__CUR_JDE_PL')}}