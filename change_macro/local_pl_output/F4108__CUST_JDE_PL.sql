{{
  config(
   alias='F4108' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F4108__CUR_JDE_PL') )}}