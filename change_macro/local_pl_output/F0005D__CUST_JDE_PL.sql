{{
  config(
   alias='F0005D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0005D__CUR_JDE_PL') )}}