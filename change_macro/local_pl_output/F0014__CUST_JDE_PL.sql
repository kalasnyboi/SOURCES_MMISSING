{{
  config(
   alias='F0014' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0014__CUR_JDE_PL') )}}