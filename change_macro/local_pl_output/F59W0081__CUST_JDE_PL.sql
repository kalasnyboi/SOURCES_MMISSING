{{
  config(
   alias='F59W0081' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F59W0081__CUR_JDE_PL') )}}