select 
    ph.value as ph, 
    discharge.value as discharge, 
    datetime 
from ph join discharge 
on left(time,16)=datetime 
order by datetime asc limit 5;


select
    corr(ph.value, discharge.value)
  from ph join discharge
    on left(time,16)=datetime;