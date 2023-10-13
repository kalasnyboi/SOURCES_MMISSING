{{
  config(
   alias='F4101' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4101__CUR_JDE_PL') }}