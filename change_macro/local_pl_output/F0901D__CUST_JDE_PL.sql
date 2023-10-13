{{
  config(
   alias='F0901D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F0901D__CUR_JDE_PL') ) }}