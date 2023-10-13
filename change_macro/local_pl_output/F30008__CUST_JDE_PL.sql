{{
  config(
   alias='F30008' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F30008__CUR_JDE_PL') ) }}