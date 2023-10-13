{{
  config(
   alias='F0401' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0401__CUR_JDE_PL') )}}