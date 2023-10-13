{{
  config(
   alias='F9201' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F9201__CUR_JDE_PL') ) }}