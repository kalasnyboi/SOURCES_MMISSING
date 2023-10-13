{{
  config(
   alias='F3003' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F3003__CUR_JDE_PL') )}}