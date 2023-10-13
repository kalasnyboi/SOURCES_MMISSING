{{
  config(
   alias='F0014' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F0014__CUR_JDE_PL')}}