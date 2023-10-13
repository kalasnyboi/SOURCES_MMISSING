{{
  config(
   alias='F704101' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F704101__CUR_JDE_PL') ) }}