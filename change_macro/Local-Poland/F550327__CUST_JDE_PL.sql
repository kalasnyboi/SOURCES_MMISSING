{{
  config(
   alias='F550327' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F550327__CUR_JDE_PL') }}