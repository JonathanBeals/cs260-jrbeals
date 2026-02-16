create table ph (
    x float,
    y float,
    id text,
    time_series_id text,
    monitoring_location_id text,
    parameter_code int,
    statistic_id int,
    time text,
    value float,
    unit_of_measure text,
    approval_status text,
    qualifier text,
    last_modified text
);

\COPY ph FROM continuous.csv (FORMAT CSV);
