{{
  config(
   alias='F03B11' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F03B11__CUR_JDE_PL') ) }}