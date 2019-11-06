import numpy
import os
from osgeo import gdal
from osgeo import ogr


#This will depend on your environment
PathName1 = r"../../../PowWowData/landiq/ds2677.gdb"
PathName2 = "../../../PowWowData/2010_2018-sample/ETa_2010001.tif"
PathName3 = "../../../PowWowData/Test.txt"

driverName = "OpenFileGDB"
driver = ogr.GetDriverByName(driverName)
if driver is None:
    print( "%s driver not available.\n" % driverName)
else:
    print("%s driver IS available.\n" % driverName)

# DataSource = driver.Open(r"C:\temp\buildings.gdb", 0)
DataSource = driver.Open(PathName1, 0)


if DataSource is None:
    print ("Could not open")
else:
    print ("Opened filed :)")
    layer = DataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print ("Number of features in %s: %d" % (os.path.basename(PathName1),featureCount))


#This gave a permission error...
# dataset = gdal.Open(PathName1, gdal.GA_ReadOnly)
# if not dataset:
#     print("Error!")
# else:
#     print("Success!")
