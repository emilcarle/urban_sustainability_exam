#%% Libraries
from osgeo import gdal
from libpysal.weights import lat2W
from esda.moran import Moran
import numpy as np


# Raster Version
# DATA
#ds = gdal.Open(r'AllergenecityIndex.tif')
# print(AllergenecityIndex.RasterCount)

#myarray = np.array(ds.GetRasterBand(1).ReadAsArray())

#morans i = 1# myarray[np.isnan(myarray)] = 0
# not working#myarray = myarray[~np.isnan(myarray)]
#np.where(np.isfinite(myarray), myarray, 0)

# Create the matrix of weigthts 
#w = lat2W(myarray.shape[0], myarray.shape[1])
# indexError: tuple index out of range

# Create the pysal Moran object 
#mi = Moran(myarray, w)

# Verify Moran's I results 
#print(mi.I) 
#print(mi.p_norm)



# Gal Version
import pysal
import pandas as pd

# how
# f = pysal.open(pysal.examples.get_path("vector_wo_nas.txt"))
# y = np.array(f.by_col['DN'])

w = pd.read_table("vector_wo_nas.gal", encoding="iso-8859-1")
# Create the matrix of weigthts 

# Calculating mi
mi = pysal.Moran(y, w, two_tailed=False)

# printing Moran's I results 
#"%.3f"%mi.I
#"%.5f"%mi.p_norm





