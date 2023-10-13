{{
  config(
   alias='F4111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4111__CUR_JDE_PL')}}