{{
  config(
   alias='F4101D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4101D__CUR_JDE_PL') }}