{{
  config(
   alias='F4070' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4070__CUR_JDE_PL') ) }}