{{
  config(
   alias='F59W0080' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F59W0080__CUR_JDE_PL') )}}