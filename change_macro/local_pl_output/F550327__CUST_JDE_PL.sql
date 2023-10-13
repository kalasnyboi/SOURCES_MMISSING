{{
  config(
   alias='F550327' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F550327__CUR_JDE_PL') ) }}