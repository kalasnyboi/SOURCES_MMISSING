{{
  config(
   alias='F3003' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F3003__CUR_JDE_PL')}}