{{
  config(
   alias='F4074' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4074__CUR_JDE_PL') ) }}