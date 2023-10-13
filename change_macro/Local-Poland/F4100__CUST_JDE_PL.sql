{{
  config(
   alias='F4100' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4100__CUR_JDE_PL')}}