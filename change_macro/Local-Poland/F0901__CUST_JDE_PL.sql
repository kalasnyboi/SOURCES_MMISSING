{{
  config(
   alias='F0901' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0901__CUR_JDE_PL')}}