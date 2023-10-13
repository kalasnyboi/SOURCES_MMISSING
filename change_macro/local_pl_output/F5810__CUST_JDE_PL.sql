{{
  config(
   alias='F5810' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F5810__CUR_JDE_PL') )}}