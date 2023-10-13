{{
  config(
   alias='A4072' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('A4072__CUR_JDE_PL') ) }}