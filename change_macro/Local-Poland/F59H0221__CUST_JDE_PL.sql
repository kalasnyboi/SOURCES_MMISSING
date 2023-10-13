{{
  config(
   alias='F59H0221' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F59H0221__CUR_JDE_PL') }}