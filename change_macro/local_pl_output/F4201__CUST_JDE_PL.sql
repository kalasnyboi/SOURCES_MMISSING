{{
  config(
   alias='F4201' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F4201__CUR_JDE_PL') ) }}