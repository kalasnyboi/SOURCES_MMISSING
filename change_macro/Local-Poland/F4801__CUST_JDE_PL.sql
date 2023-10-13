{{
  config(
   alias='F4801' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4801__CUR_JDE_PL')}}