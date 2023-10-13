{{
  config(
   alias='F4105' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{remove_double_quotes_and_trim( ref('F4105__CUR_JDE_PL') )}}