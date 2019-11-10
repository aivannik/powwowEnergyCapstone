import numpy
import os
import json
from osgeo import gdal
from osgeo import ogr
import ogr, osr

#Layer -> Feature -> Feature.GetGeometryRef().ExportToJson() -> Json_Geom
def ConvertJasonGeometry(Json_Geom):
    try:
        if(Json_Geom['type'] != 'MultiPolygon'):
            print("Error, invalid json passed")
            return
    except:
        print("Error, invalid json passed")
        return


    print("Success")
    return 1




#This will depend on your environment
PathName1 = r"../../../PowWowData/landiq/ds2677.gdb"
PathName2 = "../../../PowWowData/2010_2018-sample/ETa_2010001.tif"  #Use for opening raster files
PathName3 = "../../../PowWowData/Test.txt"


#To open .gdb file
driverName = "OpenFileGDB"
driver = ogr.GetDriverByName(driverName)
if driver is None:
    print( "%s driver not available." % driverName)
    exit()
else:
    print("%s driver IS available." % driverName)

DataSource = driver.Open(PathName1, 0)

if DataSource is None:
    print ("Could not open dataset")
    exit()


print("Dataset opened")
layer = DataSource.GetLayer()
featureCount = layer.GetFeatureCount()
print ("Number of features in %s: %d" % (os.path.basename(PathName1),featureCount))


#To sort by a specific feature, arguments can be sql querries ex Acres < 10
#Note: Most filters take a while to process
# layer.SetAttributeFilter("Crop2014 = 'Grapes'")
layer.SetAttributeFilter("Acres > 5000")



#Does not consider OBJECTID as a feature in the layers
# for feature in layer:
    # print(feature.GetField(0))


# Layer - > Feature - > Geometry

# OneFeature = layer[1]
# geom_Json = OneFeature.GetGeometryRef().ExportToJson()
# geom = json.loads(geom_Json)
# print(geom["coordinates"][0][0][0][0])

# ConvertJasonGeometry(geom["coordinates"])



for feature in layer:
    print(feature.GetField("Crop2014"))
    # geom = feature.GetGeometryRef()
    # huh = geom.Centroid().ExportToWkt()
    # print(huh)
    # print(geom.ExportToWkt())
    # print(geom.CoordinateDimension())

# layer.ResetReading()

# print(layer[1].GetFieldCount())
# print(layer[1].GetGeomFieldRef())












#This is used to open .tif files?
# dataset = gdal.Open(PathName1, gdal.GA_ReadOnly)
# if not dataset:
#     print("Error!")
# else:
#     print("Success!")
