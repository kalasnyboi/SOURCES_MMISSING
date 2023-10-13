{{
  config(
   alias='F43121' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F43121__CUR_JDE_PL')}}