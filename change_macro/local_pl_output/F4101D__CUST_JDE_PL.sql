{{
  config(
   alias='F4101D' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4101D__CUR_JDE_PL') ) }}