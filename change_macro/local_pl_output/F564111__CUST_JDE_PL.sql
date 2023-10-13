{{
  config(
   alias='F564111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F564111__CUR_JDE_PL') ) }}