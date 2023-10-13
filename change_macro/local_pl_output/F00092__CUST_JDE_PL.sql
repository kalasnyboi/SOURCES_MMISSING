{{
  config(
   alias='F00092' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F00092__CUR_JDE_PL') )}}