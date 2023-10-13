{{
  config(
   alias='F0015' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0015__CUR_JDE_PL')}}