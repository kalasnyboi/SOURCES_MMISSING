{{
  config(
   alias='F40943' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F40943__CUR_JDE_PL')}}