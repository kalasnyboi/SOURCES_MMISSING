{{
  config(
   alias='F0030' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0030__CUR_JDE_PL')}}