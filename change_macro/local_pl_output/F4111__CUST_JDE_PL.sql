{{
  config(
   alias='F4111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F4111__CUR_JDE_PL') )}}