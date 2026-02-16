create table discharge (
    agency text, 
    site int, 
    datetime text, 
    tz text,
    value float,
    accepted text
    );

\COPY discharge FROM 'cleandischarge.csv' (FORMAT CSV, DELIMITER(E'\t'));