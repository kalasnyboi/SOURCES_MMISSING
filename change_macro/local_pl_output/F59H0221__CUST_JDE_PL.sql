{{
  config(
   alias='F59H0221' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F59H0221__CUR_JDE_PL') ) }}