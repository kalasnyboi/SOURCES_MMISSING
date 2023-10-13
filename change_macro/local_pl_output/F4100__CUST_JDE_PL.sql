{{
  config(
   alias='F4100' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F4100__CUR_JDE_PL') )}}