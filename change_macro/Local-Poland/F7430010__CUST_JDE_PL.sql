{{
  config(
   alias='F7430010' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F7430010__CUR_JDE_PL')}}