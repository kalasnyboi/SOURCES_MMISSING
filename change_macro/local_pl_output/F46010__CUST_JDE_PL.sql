{{
  config(
   alias='F46010' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F46010__CUR_JDE_PL') )}}