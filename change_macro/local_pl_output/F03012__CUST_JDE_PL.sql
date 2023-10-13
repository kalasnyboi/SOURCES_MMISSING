{{
  config(
   alias='F03012' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F03012__CUR_JDE_PL') ) }}