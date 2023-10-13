{{
  config(
   alias='F46024' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F46024__CUR_JDE_PL')}}