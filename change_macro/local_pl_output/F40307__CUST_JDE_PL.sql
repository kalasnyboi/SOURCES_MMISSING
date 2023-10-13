{{
  config(
   alias='F40307' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F40307__CUR_JDE_PL') ) }}