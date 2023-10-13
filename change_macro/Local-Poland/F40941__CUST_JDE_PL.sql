{{
  config(
   alias='F40941' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F40941__CUR_JDE_PL')}}