{{
  config(
   alias='F41021' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F41021__CUR_JDE_PL')}}