{{
  config(
   alias='F59W0080' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F59W0080__CUR_JDE_PL')}}