{{
  config(
   alias='F574105' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F574105__CUR_JDE_PL') ) }}