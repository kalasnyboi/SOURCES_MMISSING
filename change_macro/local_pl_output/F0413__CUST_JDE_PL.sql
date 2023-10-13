{{
  config(
   alias='F0413' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0413__CUR_JDE_PL') )}}