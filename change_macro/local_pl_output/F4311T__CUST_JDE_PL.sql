{{
  config(
   alias='F4311T' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4311T__CUR_JDE_PL') ) }}