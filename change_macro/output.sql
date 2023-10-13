{{
  config(
   alias='F580009' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{extra_de_patatas( ref('F580009__CUR_JDE_PL') )}} 


