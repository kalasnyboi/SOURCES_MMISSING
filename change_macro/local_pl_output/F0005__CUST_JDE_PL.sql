{{
  config(
   alias='F0005' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F0005__CUR_JDE_PL') ) }}