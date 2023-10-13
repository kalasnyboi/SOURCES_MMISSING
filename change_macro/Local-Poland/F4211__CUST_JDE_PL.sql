{{
  config(
   alias='F4211' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4211__CUR_JDE_PL') }}