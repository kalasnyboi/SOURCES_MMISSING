{{
  config(
   alias='F0411' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0411__CUR_JDE_PL')}}