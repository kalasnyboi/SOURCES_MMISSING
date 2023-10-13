{{
  config(
   alias='F3106' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F3106__CUR_JDE_PL') ) }}