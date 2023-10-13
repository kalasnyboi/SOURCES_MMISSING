{{
  config(
   alias='F4074' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4074__CUR_JDE_PL') }}