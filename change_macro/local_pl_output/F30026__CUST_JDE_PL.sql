{{
  config(
   alias='F30026' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F30026__CUR_JDE_PL') )}}