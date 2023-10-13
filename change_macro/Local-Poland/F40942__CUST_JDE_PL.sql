{{
  config(
   alias='F40942' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F40942__CUR_JDE_PL')}}