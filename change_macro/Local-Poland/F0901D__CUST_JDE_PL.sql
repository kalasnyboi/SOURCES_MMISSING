{{
  config(
   alias='F0901D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F0901D__CUR_JDE_PL') }}