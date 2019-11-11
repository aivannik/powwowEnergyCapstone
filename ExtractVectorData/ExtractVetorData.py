import ogr, osr
import json
import os



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

Layer.SetAttributeFilter("County = 'Santa Barbara'")

#Convert from EPSG4326 to EPSG3310 (longitude and latitude)
inputEPSG = 3310
inSpatialRef = osr.SpatialReference()
inSpatialRef.ImportFromEPSG(inputEPSG)
outputEPSG = 4326 #For longitude and latitude
outSpatialRef = osr.SpatialReference()
outSpatialRef.ImportFromEPSG(outputEPSG)

CoorTrans = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

#Write a .json to folder for every vector and
CurrentVector = 1;
for Feature in Layer:
    Geometry = Feature.GetGeometryRef()
    Geometry.Transform(CoorTrans)
    GeometryJson = json.loads(Geometry.ExportToJson())
    Polygon = json.dumps(GeometryJson)

    OutFileName = "SantaBarbaraVectors/Polygon" + str(CurrentVector) + ".json"
    CurrentVector = CurrentVector + 1

    os.makedirs(os.path.dirname(OutFileName), exist_ok=True)
    with open(OutFileName, 'w') as f:
        json.dump(Polygon, f)
