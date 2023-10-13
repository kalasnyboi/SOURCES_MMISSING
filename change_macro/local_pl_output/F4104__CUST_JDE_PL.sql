{{
  config(
   alias='F4104' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4104__CUR_JDE_PL') ) }}