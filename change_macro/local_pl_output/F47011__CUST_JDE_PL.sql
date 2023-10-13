{{
  config(
   alias='F47011' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F47011__CUR_JDE_PL') ) }}