{{
  config(
   alias='A4072' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('A4072__CUR_JDE_PL') }}