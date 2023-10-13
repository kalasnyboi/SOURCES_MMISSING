{{
  config(
   alias='F41003' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F41003__CUR_JDE_PL') }}