{{
  config(
   alias='F4960' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4960__CUR_JDE_PL') ) }}