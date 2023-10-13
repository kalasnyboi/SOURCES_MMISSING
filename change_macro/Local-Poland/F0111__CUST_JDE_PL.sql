{{
  config(
   alias='F0111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F0111__CUR_JDE_PL') }}