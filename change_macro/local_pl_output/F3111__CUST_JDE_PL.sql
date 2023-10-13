{{
  config(
   alias='F3111' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F3111__CUR_JDE_PL') ) }}