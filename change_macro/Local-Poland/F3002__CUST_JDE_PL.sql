{{
  config(
   alias='F3002' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F3002__CUR_JDE_PL')}}