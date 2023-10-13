{{
  config(
   alias='F41002' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F41002__CUR_JDE_PL') }}