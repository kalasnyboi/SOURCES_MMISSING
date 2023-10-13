{{
  config(
   alias='F5730026' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F5730026__CUR_JDE_PL') ) }}