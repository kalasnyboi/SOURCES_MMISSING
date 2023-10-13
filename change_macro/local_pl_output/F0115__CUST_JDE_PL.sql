{{
  config(
   alias='F0115' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F0115__CUR_JDE_PL') )}}