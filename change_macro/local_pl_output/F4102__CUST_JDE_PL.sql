{{
  config(
   alias='F4102' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F4102__CUR_JDE_PL') )}}