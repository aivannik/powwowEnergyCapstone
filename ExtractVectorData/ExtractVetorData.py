import ogr, osr
import json
import os
import psycopg2
from psycopg2 import sql
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






# Start here

#PSQL preparation:
# Make sure you have a "database.ini" file in you working directory
# Also make sure your table as been set up in this format
# ```CREATE TABLE sbvectors2 (id INT, crop VARCHAR(100), acres FLOAT, coordinates JSON);```

#**********IMPORTANT**********
#**********IMPORTANT**********
#**********IMPORTANT**********
#MAKE SURE THE cur.execute IS INSERTING TO THE CORRECT TABLE!!!!!!



# Enter filepath to .shp or .gdb
PathName = "../../../PowWowData/landiq/ETaCrop2014/ETaCrop2014.shp"
# PathName = "../../../PowWowData/landiq/ds2677.gdb"

#Enter any filtering as an SQL command, ex "County = 'Santa Barbara' AND Acres < 0.05"
Filter = ""
# Filter = "Acres < 0.9"
# Filter = "County = 'Santa Barbara' AND Acres < 0.05"
# Filter = "County = 'Fresno'"


#Specify which file format
SHP = False
GDB = False
SHP = True
# GDB = True













if(SHP == GDB):
    print("Specify file format")
    exit()

driverName = ""
if(SHP == True):
    driverName = "ESRI Shapefile"
elif(GDB == True):
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
print("Dataset opened")

#Filter the layer read from the dataset
print("Applying filtering...")
# Layer.SetAttributeFilter("County = 'Santa Barbara' AND Acres < 0.05")
Layer.SetAttributeFilter(Filter)
# Layer.SetAttributeFilter("County = 'Santa Barbara'")


#Get the conversion from EPSG3310 to EPSG4326 (longitude and latitude)
inputEPSG = 3310
inSpatialRef = osr.SpatialReference()
inSpatialRef.ImportFromEPSG(inputEPSG)
outputEPSG = 4326 #For longitude and latitude
outSpatialRef = osr.SpatialReference()
outSpatialRef.ImportFromEPSG(outputEPSG)
CoorTrans = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)


# Connect to psql server
Conn = ConnectToDatabaseServer()
cur = Conn.cursor()

IndexNumber = 0
Acres = 0.0
Crop = ""


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


    if(SHP == True):
        #NOTE: in later shapefiles, I removed the z dimension and the Geometry has changed!!!
        if(len(GeometryJson["coordinates"][0][0]) != 2):
            print("Error in geometry... Adding anyways, multiple polygons at OBJECTID: ", int(Feature.GetField("OBJECTID")))
            print("Likely a vector entry with multiple polygons")

        Polygon = []
        for j in range(len(GeometryJson["coordinates"][0])):
            Point = { "lng" : GeometryJson["coordinates"][0][j][0], "lat" : GeometryJson["coordinates"][0][j][1]}
            Polygon.append(Point)
            CoorJson = {"coordinates": Polygon}

    else:
        if(len(GeometryJson["coordinates"][0][0][0]) != 3):
            print("Potential error in geometry... Adding anyways, multiple polygons at OBJECTID: ", Feature.GetFID())

        Polygon = []
        for j in range(len(GeometryJson["coordinates"][0][0])):
            Point = { "lng" : GeometryJson["coordinates"][0][0][j][0], "lat" : GeometryJson["coordinates"][0][0][j][1]}
            Polygon.append(Point)
        CoorJson = {"coordinates": Polygon}



    #Add in some extra info
    IndexNumber = 0;
    if(SHP == True):
        IndexNumber = int(Feature.GetField("OBJECTID"))
    else:
        IndexNumber = Feature.GetFID()
    Crop = Feature.GetField("Crop2014")
    Acres = Feature.GetField("Acres")


    #Insert to the psql database
    #IMPORTANT!
    #MAKE SURE YOU'RE WRITING TO THE CORRECT TABLE
    cur.execute("""INSERT INTO huron_delano_vectors ( id, crop, acres, coordinates ) VALUES (%s, %s, %s, %s) """, (IndexNumber, Crop, Acres, json.dumps(CoorJson)))
    # cur.execute("""INSERT INTO sbvectors3 ( id, crop, acres, coordinates ) VALUES (%s, %s, %s, %s) """, (IndexNumber, Crop, Acres, json.dumps(CoorJson)))




#Commit and close connections
print("Script completed and entries placed in PSQL table")
cur.close()
Conn.commit()
Conn.close()
