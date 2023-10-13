{{
  config(
   alias='F4960' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4960__CUR_JDE_PL') }}