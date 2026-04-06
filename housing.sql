create table housing(
longitude numeric,
latitude float,
housing_median_age float,
total_rooms float,
total_bedrooms float,
population float,
households float,
median_income float,
median_house_value float,
ocean_proximity text);

\copy housing from 'housing.csv' with (FORMAT csv, HEADER true);