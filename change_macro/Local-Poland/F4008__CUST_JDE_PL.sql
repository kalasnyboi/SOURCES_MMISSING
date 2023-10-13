{{
  config(
   alias='F4008' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F4008__CUR_JDE_PL') }}