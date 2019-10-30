import psycopg2
import getpass
from configparser import ConfigParser


#Taken from: http://www.postgresqltutorial.com/postgresql-python/connect/
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db #Returns a dictionary  with the config info for the psql database

def ConnectToDatabaseServer():
    try:
        #Read the info in the database.ini to connect to the server
        ConfigInfo = config()
        print("Attemping to connect...")
        Connection =psycopg2.connect(**ConfigInfo)
        print("Connection successful...")

        #Somthing cursor... its used to navigate the psql server
        cur = Connection.cursor()
        return cur

    except(Exception, psycopg2.DatabaseError) as error:
        print("Connection error:")
        print(error)


def CloseDatabaseConnection(cur):
    try:
        cur.close();
        print("Database connection now closed")
    except(Exception, psycopg2.DatabaseError) as error:
        print("Closing connection error:")
        print(error)




#Connect to psql server
cur = ConnectToDatabaseServer()


#Make a class for only rainy day entries
RainyDaysClass = [];

cur.execute("SELECT * FROM weatherdata WHERE prcp > 1") #Pick entries with rain

for record in cur:
    RainyDaysClass.append(record)

for j in RainyDaysClass:
    print("Rainy days:", j)

#Close connection
CloseDatabaseConnection(cur)
