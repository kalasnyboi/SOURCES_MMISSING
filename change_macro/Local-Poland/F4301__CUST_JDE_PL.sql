{{
  config(
   alias='F4301' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4301__CUR_JDE_PL')}}