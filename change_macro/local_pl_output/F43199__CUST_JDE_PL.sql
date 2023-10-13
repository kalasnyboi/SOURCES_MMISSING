{{
  config(
   alias='F43199' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F43199__CUR_JDE_PL') ) }}