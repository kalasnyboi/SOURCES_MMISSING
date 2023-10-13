{{
  config(
   alias='F0150' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0150__CUR_JDE_PL')}}