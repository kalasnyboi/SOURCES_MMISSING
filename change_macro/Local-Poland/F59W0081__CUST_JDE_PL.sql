{{
  config(
   alias='F59W0081' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F59W0081__CUR_JDE_PL')}}