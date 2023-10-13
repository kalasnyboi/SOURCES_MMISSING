{{
  config(
   alias='F41002' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ remove_double_quotes_and_trim( ref('F41002__CUR_JDE_PL') ) }}