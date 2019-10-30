### API test to get weather data
- The python script to collects weather data from a specific weather station in
Santa Barbara, by lake Cachuma. 
- There are few api request parameters that can be changed to get more data.
- It currently returns a year worth of weather data
- Running this script will produce a csv file


## To run:
`python3 api_test_weather.py`


## PSQL:
- A table called "weatherdata" in db1 has been setup
- To input the cvs to a table:
`\copy weatherdata FROM 'WeatherData.csv' WITH DELIMITER ',' CSV HEADER;`

