{{
  config(
   alias='F580009' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F580009__CUR_JDE_PL')}}