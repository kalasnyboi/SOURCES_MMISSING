{{
  config(
   alias='F4602' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4602__CUR_JDE_PL') ) }}