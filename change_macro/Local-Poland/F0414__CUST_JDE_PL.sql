{{
  config(
   alias='F0414' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0414__CUR_JDE_PL')}}