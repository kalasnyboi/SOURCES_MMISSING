{{
  config(
   alias='F40942' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F40942__CUR_JDE_PL') )}}