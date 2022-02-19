#%% IMPORTS
import geopandas as gp

#%% DATA
copenhagenTrees = gp.read_file('data_raw/copenhagen_trees.gpkg')

frederiksbergStreetTrees = gp.read_file('data_raw/frederiksberg_trees.gpkg')

#%% CLEANING DATAFRAMES
copenhagenStreetTrees = copenhagenTrees.loc[
    (copenhagenTrees['kategori'] == 'gadetræ') & (copenhagenTrees['busk_trae'] == 'Træ')].copy(deep=True)

copenhagenStreetTrees["municipality"] = 'copenhagen'

copenhagenStreetTrees = copenhagenStreetTrees.filter(['municipality', 'traeart', 'planteaar', 'vejnavn', 'bydelsnavn', 'stammeomfang', 'omgivelse', 'geometry'])

copenhagenStreetTrees.rename(columns = {
    'traeart':'species',
    'planteaar':'year',
    'vejnavn':'street',
    'bydelsnavn':'neighbourhood',
    'stammeomfang':'trunk_diameter',
    'omgivelse':'surroundings'}, 
    inplace=True)

frederiksbergStreetTrees["municipality"] = 'frederiksberg'

frederiksbergStreetTrees = frederiksbergStreetTrees.filter(['art_sort', 'municipality', 'vejnavn', 'geometry'])

frederiksbergStreetTrees.rename(columns = {
    'art_sort':'species',
    'vejnavn':'street'}, 
    inplace = True)

#%% MERGING GEODATAFRAMES
streetTrees = copenhagenStreetTrees.append(frederiksbergStreetTrees)

#%% STANDARDISING/RENAMING IN 'species' COLUMN
for i, row in streetTrees.iterrows():
    if 'Tilia' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Tilia'
    elif 'Acer' in str(row['species']) or 'Ácer' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Acer'
    elif 'Alnus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Alnus'
    elif 'Betula' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Betula'
    elif 'Robinia' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Robinia'
    elif 'Ulmus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Ulmus'
    elif 'Sorbus' in str(row['species']) or 'Sórbus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Sorbus'
    elif 'Fraxinus' in str(row['species']) or 'Fráxinus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Fraxinus'
    elif 'Malus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Malus'
    elif 'Quercus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Quercus'
    elif 'Carpinus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Carpinus'
    elif 'Pinus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Pinus'
    elif 'Platanus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Platanus'
    elif 'Crataegus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Crataegus'
    elif 'Pyrus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Pyrus'
    elif 'Prunus' in str(row['species']) or 'Prúnus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Prunus'
    elif 'Corylus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Corylus'
    elif 'Larix' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Larix'
    elif 'Aesculus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Aesculus'
    elif 'Populus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Populus'
    elif 'Fagus' in str(row['species']) or 'Fágus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Fagus'
    elif 'Thuja' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Thuja'
    elif 'Ginkgo' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Ginkgo'
    elif 'Taxus' in str(row['species']) or 'Táxus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Taxus'
    elif 'Picea' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Picea'
    elif 'Juniperus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Juniperus'
    elif 'Castanea' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Castanea'
    elif 'Tsuga' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Tsuga'
    elif 'Ilex' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Ilex'
    elif 'Ailanthus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Ailanthus'
    elif 'Gleditsia' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Gleditsia'
    elif 'Laburnum' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Laburnum'
    elif 'Metasequoia' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Metasequoia'
    elif 'Liquidambar' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Liquidambar'
    elif 'Styphnolobium' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Styphnolobium'
    elif 'Liriodendron' in str(row['species']) or 'Liriodéndron' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Liriodendron'
    elif 'Paulównia' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Paulownia'
    elif 'Koelreuteria' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Koelreuteria'
    elif 'Cedrús' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Cedrus'
    elif 'Catálpa' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Catalpa'
    elif 'Eleagnus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Eleagnus'
    elif 'Taxodium' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Taxodium'
    elif 'Nothofágus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Nothofagus'
    elif 'Cercidiphýllum' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Cercidiphyllum'
    elif 'Salix' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Salix'
    elif 'Juglans' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Juglans'
    elif 'Pterocárya' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Pterocarya'
    elif 'Crataegus' in str(row['species']) or 'Crateagus' in str(row['species']) or 'crataegus' in str(row['species']):
        streetTrees.at[i, 'species'] = 'Crataegus'
    elif 'Ikke registreret' in str(row['species']):
        streetTrees.at[i, 'species'] = 'not_registered'
    
print(streetTrees['species'].value_counts())

#%% Export to file
streetTrees.to_file('data_created/street_trees.gpkg')