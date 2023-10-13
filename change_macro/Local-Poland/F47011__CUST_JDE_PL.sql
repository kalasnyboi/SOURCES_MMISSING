{{
  config(
   alias='F47011' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F47011__CUR_JDE_PL') }}