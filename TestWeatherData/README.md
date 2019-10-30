- This folder and script was made to test inserting data into the psql database. 

- The python script to collects weather data from a specific weather station in
Santa Barbara, by lake Cachuma. 
- There are few api request parameters that will  need to be changed to get more data.
- It currently returns a year worth of weather data
- Running this script will produce a csv file


To run:
python3 api_test_weather.py


PSQL:
To input a cvs to a table that has already been set up:
\copy weatherdata FROM 'WeatherData.csv' WITH DELIMITER ',' CSV HEADER;

