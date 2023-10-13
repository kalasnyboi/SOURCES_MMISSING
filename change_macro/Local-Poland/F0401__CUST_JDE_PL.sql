{{
  config(
   alias='F0401' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0401__CUR_JDE_PL')}}