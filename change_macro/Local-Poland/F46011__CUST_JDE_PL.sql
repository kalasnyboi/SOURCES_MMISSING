{{
  config(
   alias='F46011' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F46011__CUR_JDE_PL')}}