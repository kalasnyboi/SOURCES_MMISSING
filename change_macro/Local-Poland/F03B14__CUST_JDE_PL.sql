{{
  config(
   alias='F03B14' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F03B14__CUR_JDE_PL')}}