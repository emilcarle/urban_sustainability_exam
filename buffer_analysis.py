#%% IMPORTS
import geopandas as gp
#from shapely import Point

#%% DATA
streetTrees = gp.read_file('data_created/street_trees.gpkg')

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