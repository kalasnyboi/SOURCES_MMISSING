{{
  config(
   alias='F0006' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F0006__CUR_JDE_PL') ) }}