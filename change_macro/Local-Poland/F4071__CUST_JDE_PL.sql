{{
  config(
   alias='F4071' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4071__CUR_JDE_PL') }}