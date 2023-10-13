{{
  config(
   alias='F3102' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F3102__CUR_JDE_PL') ) }}