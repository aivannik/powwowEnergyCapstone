
# Attempt at getting QGIS functions to work on a python script
- Need use to use GDAL to open .gdb files

## GDAL has some command line commands
  - I installed it with cygwin on windows
  - orginfo is a command in the GDAL package
  - ogrinfo -al "ds2677.gdb"
    - Prints ALL data in the dataset
    - Can also be used on the Anaconda3(see below) command prompt if GDAL has been installed

## GDAL for python3:
- ~~pip3 install numpy~~
  - Won't work on my environment
- Install Anaconda3
- On the anaconda3 command prompt:
  - conda install numpy
  - conda install GDAL
    - enter 'y'
    - some environment issues might occur but whatever
  - conda install -c conda-forge gdal
    - Maybe this one too?
## To run:
- ~~python PyQGIS.py~~~
  - Not working
