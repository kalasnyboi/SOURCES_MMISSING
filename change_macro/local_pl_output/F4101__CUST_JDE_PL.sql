{{
  config(
   alias='F4101' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4101__CUR_JDE_PL') ) }}