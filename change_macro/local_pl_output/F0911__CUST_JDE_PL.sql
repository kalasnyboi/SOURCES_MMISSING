{{
  config(
   alias='F0911' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0911__CUR_JDE_PL') )}}