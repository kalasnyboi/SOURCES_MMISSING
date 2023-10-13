{{
  config(
   alias='F0150' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0150__CUR_JDE_PL') )}}