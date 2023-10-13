{{
  config(
   alias='F0911' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0911__CUR_JDE_PL')}}