{{
  config(
   alias='F3106' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F3106__CUR_JDE_PL') }}