#%% IMPORTS
import geopandas as gp
#from shapely import Point
from osgeo import gdal
from sklearn.decomposition import TruncatedSVD

#%% DATA
streetTrees = gp.read_file('data_created/street_trees.gpkg')

boundaries = gp.read_file('data_raw/municipal_boundaries.gpkg')

#%% CREATE BUFFERS
treeBuffers = streetTrees.to_crs(25832).buffer(500)

treeBuffers = gp.GeoDataFrame(treeBuffers)

treeBuffers.columns = ['geometry']

treeBuffers = treeBuffers.set_crs(25832)

#%% MERGE BUFFERS WITH TREE ATTRIBUTES
streetTrees = streetTrees.reset_index()

streetTrees = streetTrees.drop('geometry', axis = 1)

treeBuffers = treeBuffers.reset_index()

treeBuffers = treeBuffers.merge(streetTrees, on = 'index', how = 'left')

#%% EXPORT DATA
treeBuffers.to_file('data_created/tree_buffers.gpkg')

#%% CREATE AND EXPORT SEVERE VERSION OF TREE DATA
treeBuffersSevere = treeBuffers.loc[(treeBuffers['allergenecity_index'] != 0) & (treeBuffers['allergenecity_index'] != 1) & (treeBuffers['allergenecity_index'] != 2)]

treeBuffersSevere.to_file('data_created/tree_buffers_severe.gpkg')
#%%DISSOLVING TREE BUFFERS BY ALLERGENECITY INDEX
treeBuffersAllergyGroup = treeBuffers.dissolve(by = 'allergenecity_index')

treeBuffersAllergyGroup.to_file('data_created/tree_buffers_allergy_group.gpkg')
#%%DISSOLVING TREE BUFFERS BY ALLERGENECITY INDEX
treeBuffersGenusGroup = treeBuffers.loc[treeBuffers['allergenecity_index'] != 0]

treeBuffersGenusGroup = treeBuffersGenusGroup.dissolve(by = 'genus')

treeBuffersGenusGroup.to_file('data_created/tree_buffers_genus_group.gpkg')
# %%
