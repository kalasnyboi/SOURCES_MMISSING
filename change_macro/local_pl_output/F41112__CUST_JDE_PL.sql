{{
  config(
   alias='F41112' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F41112__CUR_JDE_PL') )}}