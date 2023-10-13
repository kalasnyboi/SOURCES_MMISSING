{{
  config(
   alias='F0005D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0005D__CUR_JDE_PL')}}