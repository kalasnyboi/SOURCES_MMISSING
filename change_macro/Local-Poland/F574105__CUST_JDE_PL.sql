{{
  config(
   alias='F574105' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F574105__CUR_JDE_PL') }}