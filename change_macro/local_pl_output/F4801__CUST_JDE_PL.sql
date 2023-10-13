{{
  config(
   alias='F4801' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F4801__CUR_JDE_PL') )}}