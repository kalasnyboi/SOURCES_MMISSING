{{
  config(
   alias='F40943' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F40943__CUR_JDE_PL') )}}