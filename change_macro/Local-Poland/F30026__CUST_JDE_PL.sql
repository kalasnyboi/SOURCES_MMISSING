{{
  config(
   alias='F30026' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F30026__CUR_JDE_PL')}}