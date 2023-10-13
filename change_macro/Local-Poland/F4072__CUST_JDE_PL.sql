{{
  config(
   alias='F4072' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4072__CUR_JDE_PL') }}