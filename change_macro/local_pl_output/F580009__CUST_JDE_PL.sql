{{
  config(
   alias='F580009' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F580009__CUR_JDE_PL') )}}