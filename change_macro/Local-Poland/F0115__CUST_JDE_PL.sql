{{
  config(
   alias='F0115' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0115__CUR_JDE_PL')}}