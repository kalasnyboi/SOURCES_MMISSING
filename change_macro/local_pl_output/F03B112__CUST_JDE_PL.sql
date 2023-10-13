{{
  config(
   alias='F03B112' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F03B112__CUR_JDE_PL') )}}