{{
  config(
   alias='F03B13' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F03B13__CUR_JDE_PL') )}}