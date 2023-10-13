{{
  config(
   alias='F41003' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F41003__CUR_JDE_PL') ) }}