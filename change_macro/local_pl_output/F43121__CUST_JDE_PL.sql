{{
  config(
   alias='F43121' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F43121__CUR_JDE_PL') )}}