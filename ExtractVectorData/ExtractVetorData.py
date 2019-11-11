import ogr, osr


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

for Feature in Layer:
    print(Feature.GetField("Crop2014"))
