{{
  config(
   alias='F46010' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F46010__CUR_JDE_PL')}}