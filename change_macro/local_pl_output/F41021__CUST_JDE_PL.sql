{{
  config(
   alias='F41021' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F41021__CUR_JDE_PL') )}}