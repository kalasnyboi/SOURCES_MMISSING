{{
  config(
   alias='F1755' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F1755__CUR_JDE_PL') )}}