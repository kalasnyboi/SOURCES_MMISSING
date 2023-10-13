{{
  config(
   alias='F3111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F3111__CUR_JDE_PL') }}