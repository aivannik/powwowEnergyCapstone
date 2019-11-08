import psycopg2
import os
from getpass import getpass
from dotenv import load_dotenv
from pathlib import Path  # python3 only
# https://pynative.com/python-postgresql-tutorial/

'''
    I ran into issues installing psycopg2
    Fix: https://stackoverflow.com/questions/20170895/mac-virtualenv-pip-postgresql-error-pg-config-executable-not-found
'''


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
    
user = os.environ.get('POWWOW_PG_USER')
host = os.environ.get('POWWOW_PG_HOST')
port = os.environ.get('POWWOW_PG_PORT')
password = os.environ.get('POWWOW_PG_PASS')
database = os.environ.get('POWWOW_PG_DB')

try:
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)
    print("Success")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    weatherdata_select_query = "SELECT * FROM weatherdata LIMIT 5;"
    cursor.execute(weatherdata_select_query)
    weather_records = cursor.fetchall()
    for row in weather_records:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
