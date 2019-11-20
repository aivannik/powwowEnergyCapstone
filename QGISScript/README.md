## Documentation and stuff...

- Crop2014 census has some errors that only show up when specific processes are run
- Thankfully stack exchange  exists
- Error : Invalid geometry
  - Occurred on an layer that had the bugged z-dimension removed
  - Solution: https://gis.stackexchange.com/questions/259256/qgis-invalid-geometry-even-after-using-validity-checker-and-v-clean
    - Run Vector-> Geometry Tools -> Check Validity
      - Select ds2677
      - I think I unchecked the "Ignore ring self intersection"
      - It produces two layers, a valid and an invalid one and provides a message on why
  - Solution: https://gis.stackexchange.com/questions/265661/fixing-polygon-self-intersection-in-qgis
    - Vector -> Geoprocessing Tools -> Buffer
      - Set the distance to 0 and run
    - Check that it worked, run "Check Validity" again, the invalid output layer show have zero features

#Main work flow:
- Goal: Get features from ds2677.gdb that have an intersection with the .tif raster file
  - Removed z dimension and created new shapefile called "Crop2014.shp"
    - The buffer function (See above) was also applied to this layer
  - Multiple guides online gave different suggestions on how to find overlapping sections
  - Next was to polygonize the .tif file to produce a vector layer
    - This was done with this command:
    - ```TifPoly = processing.run("gdal:polygonize", PolyDictInput)```
      - PolyDictInput was a dictionary of input parameters
  - To find the intersection Vector -> Research Tools -> Select by Location
   - Select from landiq vector layer and compare with polygonize .tif file
   - Checked the "touch" box
   - Picked "Selecting within current selection" ?
   - Running took a really long time since I assumed it was processing all of vectors throughout all of California so in the Crop2014 vector layer I selected all the features in large rectangular around the .tif area and created a new shapefile called CropCrop2014.shp
    - This actually helped a lot
  - The results of applying "Select by Location" on the polygonize .tif and the CropCrop2014 vector layer was simply a selection of all features that touch the .tif file
  - Those features were saved and copied to a new shape file called ETaCrop2014  


#Code stuff:
TO RUN SCRIPT ON QGIS:
```exec(open(PathToScript.encode('utf-8')).read())```

- ```QgsProject.instance().clear()```
  - Clears all layers that have been load on
- ``` iface.addVectorLayer(VectorPath,"" ,"ogr") ```
  - To add a vector layer, the path is just a string to a .shp to .gdb file
- ``` iface.addRasterLayer(RasterPath, "Layer Name")```
  - To add a raster file, the path should lead to a .tif file
-```#for alg in QgsApplication.processingRegistry().algorithms():
      print(alg.id(), "->", alg.displayName())
```
  - To print all algorithms that can be run
- ```processing.algorithmHelp("qgis:polygonize")```
  - To get a manual on specific algorithm
