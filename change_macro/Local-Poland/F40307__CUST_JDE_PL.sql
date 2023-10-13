{{
  config(
   alias='F40307' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F40307__CUR_JDE_PL') }}