#%% IMPORTS
import geopandas as gp

#%% DATA
copenhagenTrees = gp.read_file('data_raw/copenhagen_trees.gpkg')
frederiksbergTrees = gp.read_file('data_raw/frederiksberg_trees.gpkg')

#%% CLEANING DATAFRAMES
copenhagenTrees["municipality"] = 'copenhagen'
copenhagenTrees = copenhagenTrees.filter(['kategori', 'municipality', 'traeart', 'planteaar', 'busk_trae', 'vejnavn', 'bydelsnavn', 'stammeomfang', 'omgivelse', 'geometry'])
copenhagenTrees.rename(columns = {
    'kategori':'category',
    'traeart':'species',
    'planteaar':'year',
    'busk_trae':'bush_tree',
    'vejnavn':'street',
    'bydelsnavn':'neighbourhood',
    'stammeomfang':'trunk_diameter',
    'omgivelse':'surroundings'}, 
    inplace=True)

frederiksbergTrees["municipality"] = 'frederiksberg'
frederiksbergTrees = frederiksbergTrees.filter(['art_sort', 'municipality', 'vejnavn', 'geometry'])
frederiksbergTrees.rename(columns = {
    'art_sort':'species',
    'vejnavn':'street'}, 
    inplace = True)

#%% MERGING GEODATAFRAMES AND STANDERDISING 'species' column
combinedTrees = copenhagenTrees.append(frederiksbergTrees)



#%% R
copenhagenTrees.drop(columns = ['id', 'saerligt_trae', 'type', ]
