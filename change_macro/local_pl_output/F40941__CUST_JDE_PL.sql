{{
  config(
   alias='F40941' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F40941__CUR_JDE_PL') )}}