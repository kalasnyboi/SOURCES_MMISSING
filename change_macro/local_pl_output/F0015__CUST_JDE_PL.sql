{{
  config(
   alias='F0015' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0015__CUR_JDE_PL') )}}