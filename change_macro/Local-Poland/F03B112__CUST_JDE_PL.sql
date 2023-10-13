{{
  config(
   alias='F03B112' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F03B112__CUR_JDE_PL')}}