/* DO $$
DECLARE
    item TEXT;
    my_list TEXT[] := ARRAY['cond', 'discharge'];
BEGIN
    FOREACH item IN ARRAY my_list
    LOOP */
        create table pHb (
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

        \COPY pHb FROM pHb_primary-time-series.csv (HEADER, FORMAT CSV );
/*
    END LOOP;
END $$;
*/
