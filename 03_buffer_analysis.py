
#script to generate 500m buffers around street trees by genera
#%% IMPORTS
import geopandas as gp

#%% DATA
streetTrees = gp.read_file('data_created/street_trees.gpkg')

boundaries = gp.read_file('data_raw/municipal_boundaries_2.gpkg')

#%% CREATE BUFFERS
treeBuffers = streetTrees.to_crs(25832).buffer(500, resolution=2)

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

#%%DISSOLVING TREE BUFFERS BY ALLERGENECITY INDEX
treeBuffersGenusGroup = treeBuffers.loc[treeBuffers['allergenecity_index'] != 0]

treeBuffersGenusGroup = treeBuffersGenusGroup.dissolve(by = 'genus')

treeBuffersGenusGroup.to_file('data_created/tree_buffers_genus_group.gpkg')

#%% SEPERATE GEODATAFRAME AND EXPORTED GEOPACKAGE FOR EACH GENUS
treeBuffersGenusGroup = treeBuffersGenusGroup.reset_index()

treeBuffersGenusGroup = treeBuffersGenusGroup.drop(columns=['index'])

treeBuffersGenusGroup = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['allergenecity_index'] != 0]

for genus in treeBuffersGenusGroup['genus']:
    layer = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == genus]
    layer.to_file(f'data_created/buffers{genus}.gpkg')

#rasterization and summing of all buffer rasters is performed in QGIS after running this script
#for further information refer to the the methods section of the final paper