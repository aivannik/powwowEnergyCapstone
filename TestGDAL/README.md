
# Attempt at getting QGIS functions to work on a python script
- Need use to use GDAL to open .gdb files

## GDAL has some command line packages and a python module 
  - I installed the GDAL package with cygwin on windows
  - orginfo is a command in the GDAL package
  - ```ogrinfo -al "ds2677.gdb" ```
    - Prints ALL data in the dataset
    - Can also be used on the Anaconda3(see below) command prompt if GDAL has been installed
  - ```orginfo --format```
    - Prints all formats that can be opened...
    -  OpenFileGDB -vector- (rov): ESRI FileGDB
      - This one is for .gdb

## GDAL for python3:
- Setting up environment:
  - ~~pip3 install numpy~~
    - Won't work on my environment, have to use Anaconda3
  - Install Anaconda3
  - On the anaconda3 command prompt:
    - ```conda install numpy```
    - ```conda install GDAL```
      - enter 'y'
      - some environment issues might occur but whatever
    - ```conda install -c conda-forge gdal```
      - Maybe this one too, idk?
- References:
  - https://pcjericks.github.io/py-gdalogr-cookbook/layers.html
  - https://gis.stackexchange.com/questions/32762/how-to-access-feature-classes-in-file-geodatabases-with-python-and-gdal
  - https://gdal.org/python/osgeo.ogr-module.html
- Pretty much use osgeo to read and process .gdb files and GDAL to process .tif?

## To run:
- ```python TestGDAL.py```
  - Should run on Anaconda3
  - Will need to change PathName1 to work properly
