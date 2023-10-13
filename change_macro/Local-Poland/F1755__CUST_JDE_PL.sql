{{
  config(
   alias='F1755' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F1755__CUR_JDE_PL')}}