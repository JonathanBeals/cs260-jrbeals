create table river2025 
  (time text,turb float,ph float,doox float,cond float,discharge float,height float, temp float);

insert into river2025

select 
  turb.time as time,
  turb.value as turb,
  ph.value as ph, 
  diso.value as diso,
  cond.value as cond,
  discharge.value as discharge,
  height.value as height,
  temp.value as temp 
from 
  turb 
  join ph on turb.time=ph.time 
  join doox on doox.time=turb.time
  join cond on cond.time=turb.time
  join discharge on discharge.time=turb.time
  join height on height.time=turb.time
  join temp on temp.time=turb.time;
