{{
  config(
   alias='F03B14' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F03B14__CUR_JDE_PL') )}}