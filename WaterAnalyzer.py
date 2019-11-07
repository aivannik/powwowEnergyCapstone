import numpy as np
import psycopg2
import os
from getpass import getpass
from dotenv import load_dotenv
from pathlib import Path  # python3 only
# Water Analyzer Module
# This contains functions to analyze the data and output areas of non uniformity or relatively high water use

def uniformity_analysis(eta_matrix):
    '''
        Input matrix is a 2D numpy array where each value is the ETa
        Return the coordinates where the ETa is relatively higher than the average
    '''

    nonuniform_coordinates = []
    mean = np.mean(eta_matrix)
    std_dev = np.std(eta_matrix)
    for row_idx, row in enumerate(eta_matrix):
        for col_idx, val in enumerate(row):
            if val > (mean + std_dev) or val < (mean - std_dev):
                nonuniform_coordinates.append( (row_idx, col_idx) )

    return nonuniform_coordinates


def get_eta_data():
    '''
        Query the database for the ETa values
        For now, the query is hardcoded and the data is 

        This function will eventually be replaced with an API that will be setup between the database and the backend
    '''

    eta_data = list()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    user = os.environ.get('USERNAME')
    host = os.environ.get('HOST')
    port = os.environ.get('PORT')
    password = os.environ.get('PASSWORD')
    database = os.environ.get('DATABASE')

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

        select_query = "SELECT * FROM eta_stub"
        cursor.execute(select_query)
        weather_records = cursor.fetchall()
        for row in weather_records:

            

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return eta_data


