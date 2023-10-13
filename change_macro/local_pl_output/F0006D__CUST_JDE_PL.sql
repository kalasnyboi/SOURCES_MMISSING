{{
  config(
   alias='F0006D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F0006D__CUR_JDE_PL') ) }}