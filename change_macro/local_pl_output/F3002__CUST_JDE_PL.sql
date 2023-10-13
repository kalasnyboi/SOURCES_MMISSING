{{
  config(
   alias='F3002' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F3002__CUR_JDE_PL') )}}