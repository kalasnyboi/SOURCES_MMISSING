{{
  config(
   alias='F0111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F0111__CUR_JDE_PL') ) }}