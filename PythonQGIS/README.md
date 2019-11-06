
### Attempt at getting QGIS functions to work on a python script

- pip3 install numpy NOPE!

- Install Anaconda3
- conda install numpy
- conda install GDAL
  - enter y
  - some environment issues might occur but whatever
  - conda install -c conda-forge gdal
    - Maybe this one too?
  - Can now use GDAL commands on Anaconda terminal thingy
  - Also installed GDAL on cygwin but this might be redundant




# To run:
python PyQGIS.py
  - Its by default python3 if you installed Anaconda3
  - Actually ogrinfo -al "ds2677.gdb"
    - can be used from the command line to print the ENTIRE contents of the dataset
