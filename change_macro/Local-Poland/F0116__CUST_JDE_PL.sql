{{
  config(
   alias='F0116' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F0116__CUR_JDE_PL') }}