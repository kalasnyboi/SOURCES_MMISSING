{{
  config(
   alias='F43199' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F43199__CUR_JDE_PL') }}