{{
  config(
   alias='F4311' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F4311__CUR_JDE_PL') )}}