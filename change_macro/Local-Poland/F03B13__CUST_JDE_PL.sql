{{
  config(
   alias='F03B13' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F03B13__CUR_JDE_PL')}}