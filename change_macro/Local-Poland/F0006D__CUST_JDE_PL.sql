{{
  config(
   alias='F0006D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F0006D__CUR_JDE_PL') }}