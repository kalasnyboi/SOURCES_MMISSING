{{
  config(
   alias='F46011' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F46011__CUR_JDE_PL') )}}