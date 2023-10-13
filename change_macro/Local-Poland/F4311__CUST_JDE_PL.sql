{{
  config(
   alias='F4311' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4311__CUR_JDE_PL')}}