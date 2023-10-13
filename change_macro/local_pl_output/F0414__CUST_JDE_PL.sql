{{
  config(
   alias='F0414' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0414__CUR_JDE_PL') )}}