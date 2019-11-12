import ogr, osr
import json
import os
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
        return Connection
        # cur = Connection.cursor()

    except(Exception, psycopg2.DatabaseError) as error:
        print("Connection error:")
        print(error)









#Attept to open the .gdb file
PathName = "../../../PowWowData/landiq/ds2677.gdb"
driverName = "OpenFileGDB"
driver = ogr.GetDriverByName(driverName)
if driver is None:
    print( "%s driver not available." % driverName)
    exit()

DataSource = driver.Open(PathName, 0)
if DataSource is None:
    print ("Could not open dataset")
    exit()
Layer = DataSource.GetLayer()

#Filter the layer read from the dataset
print("Now filtering...")
# Layer.SetAttributeFilter("County = 'Santa Barbara' AND Acres < 0.05")
Layer.SetAttributeFilter("County = 'Santa Barbara'")


#Get the conversion from EPSG3310 to EPSG4326 (longitude and latitude)
inputEPSG = 3310
inSpatialRef = osr.SpatialReference()
inSpatialRef.ImportFromEPSG(inputEPSG)
outputEPSG = 4326 #For longitude and latitude
outSpatialRef = osr.SpatialReference()
outSpatialRef.ImportFromEPSG(outputEPSG)

CoorTrans = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

#Connect to psql server
Conn = ConnectToDatabaseServer()
cur = Conn.cursor()

print("Cycling through features...")
CurrentVector = 1;
for Feature in Layer:

    #Get Geometry/polygon data from the current feature
    Geometry = Feature.GetGeometryRef()
    #Transform to EPSG4326
    Geometry.Transform(CoorTrans)
    #Convert Geometry into a workabale json/dictionary
    GeometryJson = json.loads(Geometry.ExportToJson())
    #Remove z-axis and create a new json/dictionary
    Polygon = []
    for j in range(len(GeometryJson["coordinates"][0][0])):
        Point = { "lng" : GeometryJson["coordinates"][0][0][j][0], "lat" : GeometryJson["coordinates"][0][0][j][1]}
        Polygon.append(Point)
    CoorJson = {"coordinates": Polygon}
    #Insert to the psql database
    cur.execute("""INSERT INTO sbvectors ( coordinates ) VALUES ( '{0}' ) """.format(json.dumps(CoorJson)))

#Commit and close connections
cur.close()
Conn.commit()
Conn.close()
