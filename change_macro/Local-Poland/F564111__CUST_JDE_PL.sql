{{
  config(
   alias='F564111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F564111__CUR_JDE_PL') }}