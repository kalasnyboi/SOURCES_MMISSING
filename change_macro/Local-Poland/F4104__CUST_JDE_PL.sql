{{
  config(
   alias='F4104' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4104__CUR_JDE_PL') }}