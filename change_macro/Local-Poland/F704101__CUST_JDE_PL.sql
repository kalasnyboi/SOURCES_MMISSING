{{
  config(
   alias='F704101' , 
   tags= ['PL', 'Local-Poland']
  )
}}

select * 
from {{ ref('F704101__CUR_JDE_PL') }}