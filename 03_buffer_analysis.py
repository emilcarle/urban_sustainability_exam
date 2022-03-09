
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

buffersAcer = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Acer']
buffersAilanthus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Ailanthus']
buffersAlnus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Alnus']
buffersBetula = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Betula']
buffersCarpinus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Carpinus']
buffersCastanea = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Castanea']
buffersCedrus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Cedrus']
buffersCorylus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Corylus']
buffersCrataegus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Crataegus']
buffersFagus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Fagus']
buffersFraxinus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Fraxinus']
buffersGleditsia = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Gleditsia']
buffersIlex = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Ilex']
buffersJuglans = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Juglans']
buffersJuniperus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Juniperus']
buffersLiquidambar = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Liquidambar']
buffersLiriodendron = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Liriodendron']
buffersMalus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Malus']
buffersPinus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Pinus']
buffersPlatanus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Platanus']
buffersPopulus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Populus']
buffersPrunus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Prunus']
buffersPterocarya = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Pterocarya']
buffersPyrus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Pyrus']
buffersQuercus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Quercus']
buffersRobinia = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Robinia']
buffersSalix = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Salix']
buffersSorbus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Sorbus']
buffersTilia = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Tilia']
buffersUlmus = treeBuffersGenusGroup.loc[treeBuffersGenusGroup['genus'] == 'Ulmus']

buffersAcer.to_file('data_created/buffersAcer.gpkg')
buffersAilanthus.to_file('data_created/buffersAilanthus.gpkg')
buffersAlnus.to_file('data_created/buffersAlnus.gpkg')
buffersBetula.to_file('data_created/buffersBetula.gpkg')
buffersCarpinus.to_file('data_created/buffersCarpinus.gpkg')
buffersCastanea.to_file('data_created/buffersCastanea.gpkg')
buffersCedrus.to_file('data_created/buffersCedrus.gpkg')
buffersCorylus.to_file('data_created/buffersCorylus.gpkg')
buffersCrataegus.to_file('data_created/buffersCrataegus.gpkg')
buffersFagus.to_file('data_created/buffersFagus.gpkg')
buffersFraxinus.to_file('data_created/buffersFraxinus.gpkg')
buffersGleditsia.to_file('data_created/buffersGleditsia.gpkg')
buffersIlex.to_file('data_created/buffersIlex.gpkg')
buffersJuglans.to_file('data_created/buffersJuglans.gpkg')
buffersJuniperus.to_file('data_created/buffersJuniperus.gpkg')
buffersLiquidambar.to_file('data_created/buffersLiquidambar.gpkg')
buffersLiriodendron.to_file('data_created/buffersLiriodendron.gpkg')
buffersMalus.to_file('data_created/buffersMalus.gpkg')
buffersPinus.to_file('data_created/buffersPinus.gpkg')
buffersPlatanus.to_file('data_created/buffersPlatanus.gpkg')
buffersPopulus.to_file('data_created/buffersPopulus.gpkg')
buffersPrunus.to_file('data_created/buffersPrunus.gpkg')
buffersPterocarya.to_file('data_created/buffersPterocarya.gpkg')
buffersPyrus.to_file('data_created/buffersPyrus.gpkg')
buffersQuercus.to_file('data_created/buffersQuercus.gpkg')
buffersRobinia.to_file('data_created/buffersRobinia.gpkg')
buffersSalix.to_file('data_created/buffersSalix.gpkg')
buffersSorbus.to_file('data_created/buffersSorbus.gpkg')
buffersTilia.to_file('data_created/buffersTilia.gpkg')
buffersUlmus.to_file('data_created/buffersUlmus.gpkg')

#rasterization and summing of all buffer rasters is performed in QGIS after running this script
#for further information refer to the the methods section of the final paper