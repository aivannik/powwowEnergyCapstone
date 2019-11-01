'''
    The purpose of this script is to parse the ETa data from the .asc files

    To convert the .tif to an ascii from QGIS:
    1.  Open the file you wish to convert by selecting Layer >> Add Raster Layer.
    2.  Open the raster translator by selecting Raster >> Conversions >>Translate.
    3.  Set the input layer and in the Output file press the Select Button.
    4.  In the save dialogue, drop the file type down and select Arc/Info ASCII Grid (*.asc *.ASC).

    This describes the format of .asc files:
    https://en.wikipedia.org/wiki/Esri_grid
'''

def convert_ETa_data(pixelval):
    '''
    Each pixel represents ETa in volume (10000 Ac-ft). 
    The scaling factor 10,000 was used to convert the pixel values into interger. To retrieve ETa in Ac-ft (volume) simply divide by 10,000. 

    To convert pixel value into depth (inches):

    ETa (inches) = [ETa (10000 Ac ft) * 12 (ft to inches) ] /[ 10000 (scaling factor) 30 * 30 * 0.000247105 (pixel size meters, in acres) ]

    '''

    return pixelval * 12 / (10000 * 30 * 30 * 0.000247105)

# I am not sure what the units of xllcorner and yllcorner are. I'm going to assume that they are latitutde and longitude for now

file_in = "test.asc"
f = open(file_in, 'r')
num_cols = int(f.readline().split()[1])
num_rows = int(f.readline().split()[1])
xllcorner = float(f.readline().split()[1])
yllcorner = float(f.readline().split()[1])
cellsize = float(f.readline().split()[1])
nodata = f.readline().split()[1]

print("num cols:", num_cols)
print("num rows:", num_rows)
print("xllcorner:", xllcorner)
print("yllcorner:", yllcorner)
print("cellsize:", cellsize)
print("nodata:", nodata)

# For now, I will store the results of my algorithm within a list
# Each list element will have the following format: (latitude, longitude, ETa in inches)
results = list()

linenum = 0
for line in f:
    
    colnum = 0
    for pixelval in line.split():

        if pixelval != nodata:
            
        
            # One you find a value, its coordinates are:
            # x-coordinate: xllcorner + (num_rows - linenum - 1) * cellsize
            # y-coordinate: yllcorner + colnum  * cellsize

            x = xllcorner + ((num_rows - linenum - 1) * cellsize)
            y = yllcorner + (colnum * cellsize) 
            results.append((x, y, convert_ETa_data(float(pixelval))))

        colnum += 1

    linenum += 1

print(len(results))

f.close()