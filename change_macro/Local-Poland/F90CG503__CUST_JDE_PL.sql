{{
  config(
   alias='F90CG503' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ref('F90CG503__CUR_JDE_PL')}}