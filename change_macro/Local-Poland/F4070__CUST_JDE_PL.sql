{{
  config(
   alias='F4070' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4070__CUR_JDE_PL') }}