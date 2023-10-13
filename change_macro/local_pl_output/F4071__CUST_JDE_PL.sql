{{
  config(
   alias='F4071' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4071__CUR_JDE_PL') ) }}