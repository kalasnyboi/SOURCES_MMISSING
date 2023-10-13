{{
  config(
   alias='F0116' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F0116__CUR_JDE_PL') ) }}