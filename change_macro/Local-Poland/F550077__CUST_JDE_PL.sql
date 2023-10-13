{{
  config(
   alias='F550077' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F550077__CUR_JDE_PL')}}