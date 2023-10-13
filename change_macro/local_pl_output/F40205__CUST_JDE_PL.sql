{{
  config(
   alias='F40205' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F40205__CUR_JDE_PL') ) }}