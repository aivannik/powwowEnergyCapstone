
# Attempt at getting QGIS functions to work on a python script

- ~~pip3 install numpy~~
  - Won't work on my environment

- Need use GDAL
## For python3:
- Install Anaconda3
- On the anaconda3 command prompt:
  - conda install numpy
  - conda install GDAL
    - enter 'y'
    - some environment issues might occur but whatever
  - conda install -c conda-forge gdal
    - Maybe this one too?
## GDAL commands documentation can be installed to work on a shell thing
  - I installed it with cygwin on windows

## To run:
- ~~python PyQGIS.py
  - Not working
- ogrinfo -al "ds2677.gdb"
  - Can be used from your shell/terminal or the Anaconda3 command prompt if GDAL has been installed
  - Prints ALL data in the dataset
