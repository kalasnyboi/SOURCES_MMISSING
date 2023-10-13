{{
  config(
   alias='F00092' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F00092__CUR_JDE_PL')}}