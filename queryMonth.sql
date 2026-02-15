select avg(value),stddev(value),min(value),max(value)
    from discharge
    where datetime like '2025-07-%';