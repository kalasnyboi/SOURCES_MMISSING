{{
  config(
   alias='F5810' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F5810__CUR_JDE_PL')}}