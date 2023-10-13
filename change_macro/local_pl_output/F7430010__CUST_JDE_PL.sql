{{
  config(
   alias='F7430010' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F7430010__CUR_JDE_PL') )}}