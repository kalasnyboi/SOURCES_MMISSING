{{
  config(
   alias='F4211' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4211__CUR_JDE_PL') ) }}