{{
  config(
   alias='F03012' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F03012__CUR_JDE_PL') }}