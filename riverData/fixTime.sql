select 
  extract(JULIAN from to_timestamp(time,'YYYY-MM-DD HH24:MI:SS+'))-
  extract(JULIAN from to_timestamp('2025-01-01 00:00:00','YYYY-MM-DD HH24:MI:SS')) as t, ph 
from river2025 
    order by t;

update river2025 set t=extract(JULIAN from to_timestamp(time,'YYYY-MM-DD HH24:MI:SS+'))-
  extract(JULIAN from to_timestamp('2025-01-01 00:00:00','YYYY-MM-DD HH24:MI:SS'));
