
# Attempt at getting QGIS functions to work on a python script

- ~~pip3 install numpy~~
  - Won't work on my environment

- Need use to use GDAL to open .gdb files
## GDAL commands documentation can be installed to work on a shell thing
  - I installed it with cygwin on windows
  - orginfo is a command in the GDAL package
  - ogrinfo -al "ds2677.gdb"
    - Can also be used on the Anaconda3(see below) command prompt if GDAL has been installed
  - Prints ALL data in the dataset


## For python3:
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
