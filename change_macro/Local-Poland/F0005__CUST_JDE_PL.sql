{{
  config(
   alias='F0005' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F0005__CUR_JDE_PL') }}