{{
  config(
   alias='F4602' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4602__CUR_JDE_PL') }}