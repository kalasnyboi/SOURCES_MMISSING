{{
  config(
   alias='F0901' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0901__CUR_JDE_PL') )}}