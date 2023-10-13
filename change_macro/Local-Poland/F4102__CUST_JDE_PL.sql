{{
  config(
   alias='F4102' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4102__CUR_JDE_PL')}}