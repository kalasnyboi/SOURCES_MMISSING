{{
  config(
   alias='F3102' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F3102__CUR_JDE_PL') }}