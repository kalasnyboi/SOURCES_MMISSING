{{
  config(
   alias='F0101' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F0101__CUR_JDE_PL') ) }}