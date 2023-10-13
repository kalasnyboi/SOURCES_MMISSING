{{
  config(
   alias='F41112' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F41112__CUR_JDE_PL')}}