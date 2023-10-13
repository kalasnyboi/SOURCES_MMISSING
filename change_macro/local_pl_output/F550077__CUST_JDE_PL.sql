{{
  config(
   alias='F550077' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F550077__CUR_JDE_PL') )}}