{{
  config(
   alias='F0411' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0411__CUR_JDE_PL') )}}