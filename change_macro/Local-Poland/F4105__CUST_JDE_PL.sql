{{
  config(
   alias='F4105' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F4105__CUR_JDE_PL')}}