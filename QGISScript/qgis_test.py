# filename = "\\..\\..\\Users\\richa\\Documents\\GitHub\\powwowEnergyCapstone\\QGISScript\\qgis_test.py"
 # exec(open('C:/Users/richa/Documents/GitHub/powwowEnergyCapstone/QGISScript/qgis_test.py'.encode('utf-8')).read())
#reset with
# os.system('clear')
import gdal
import processing
QgsProject.instance().clear()


# Original unaltered Crop2014 dataset:
# Crop2014Path = "\\..\\..\\Users\\richa\\Documents\\PowWowData\\landiq\\ds2677.gdb"
# Original dataset with the z dimension removed and maybe buffered...:
# Crop2014Path = "\\..\\..\\Users\\richa\\Documents\\PowWowData\\landiq\\Crop2014\\Crop2014.shp"
# Original dataset withe z-dimension removed and only fields around .tif ETa data
# Crop2014Path = "\\..\\..\\Users\\richa\\Documents\\PowWowData\\landiq\\CropCrop2014\\CropCrop2014.shp"
# Just the features in Crop2014 that touch/intersect with the .tif file
Crop2014Path = "\\..\\..\\Users\\richa\\Documents\\PowWowData\\landiq\\ETaCrop2014\\ETaCrop2014.shp"
ETaPath = "\\..\\..\\Users\\richa\\Documents\\PowWowData\\2010_2018-sample\\ETa_2010001.tif"


# Open vector layer...
CropLayer = iface.addVectorLayer(Crop2014Path,"" ,"ogr")
if not CropLayer:
  print("Layer failed to load!")

#Add ETa layer
ETaLayer = iface.addRasterLayer(ETaPath, "ETa Layer")



PolyDictInput = {
'INPUT' : '/../../Users/richa/Documents/PowWowData/2010_2018-sample/ETa_2010001.tif',
'BAND' : 1,
'FIELD': 'VALUE',
'EIGHT_CONNECTEDNESS': -8,
'OUTPUT' : 'TEMPORARY_OUTPUT'
}
TifPoly = processing.run("gdal:polygonize", PolyDictInput)
iface.addVectorLayer(TifPoly['OUTPUT'],"ETaPolygonized" ,"ogr")





print("Script completed!")
