{{
  config(
   alias='F0030' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0030__CUR_JDE_PL') )}}