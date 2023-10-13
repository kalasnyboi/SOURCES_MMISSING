{{
  config(
   alias='F4108' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4108__CUR_JDE_PL')}}