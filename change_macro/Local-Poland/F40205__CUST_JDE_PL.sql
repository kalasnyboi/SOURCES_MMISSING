{{
  config(
   alias='F40205' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F40205__CUR_JDE_PL') }}