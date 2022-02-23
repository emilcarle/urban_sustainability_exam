#%% IMPORTS
import geopandas as gp
import pandas as pd
from unidecode import unidecode

#%% DATA
copenhagenTrees = gp.read_file('data_raw/copenhagen_trees.gpkg')

frederiksbergStreetTrees = gp.read_file('data_raw/frederiksberg_trees.gpkg')

allergenicityIndex = pd.read_csv('approach/index_allergenetic_trees.csv', sep = ';')

#%% CLEANING AND MERGING DATAFRAMES
copenhagenStreetTrees = copenhagenTrees.loc[
    (copenhagenTrees['kategori'] == 'gadetræ') & (copenhagenTrees['busk_trae'] == 'Træ')].copy(deep = True)

copenhagenStreetTrees["municipality"] = 'copenhagen'

copenhagenStreetTrees = copenhagenStreetTrees.filter(['municipality', 'traeart', 'planteaar', 'vejnavn', 'bydelsnavn', 'stammeomfang', 'omgivelse', 'geometry'])

copenhagenStreetTrees.rename(columns = {
    'traeart':'genus',
    'planteaar':'year',
    'vejnavn':'street',
    'bydelsnavn':'neighbourhood',
    'stammeomfang':'trunk_diameter',
    'omgivelse':'surroundings'}, 
    inplace=True)

frederiksbergStreetTrees['municipality'] = 'frederiksberg'

frederiksbergStreetTrees = frederiksbergStreetTrees.filter(['art_sort', 'municipality', 'vejnavn', 'geometry'])

frederiksbergStreetTrees.rename(columns = {
    'art_sort':'genus',
    'vejnavn':'street'}, 
    inplace = True)

streetTrees = copenhagenStreetTrees.append(frederiksbergStreetTrees)

streetTrees['genus'] = streetTrees['genus'].fillna('not_registered')

#%% STANDARDISING/RENAMING IN 'genus' COLUMN
streetTrees = streetTrees.astype({'genus': str})

streetTrees['genus'] = streetTrees['genus'].apply(lambda x: unidecode(x, 'utf-8'))

for i, row in streetTrees.iterrows():
    if 'Tilia' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Tilia'
    elif 'Acer' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Acer'
    elif 'Alnus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Alnus'
    elif 'Betula' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Betula'
    elif 'Robinia' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Robinia'
    elif 'Ulmus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Ulmus'
    elif 'Sorbus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Sorbus'
    elif 'Fraxinus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Fraxinus'
    elif 'Malus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Malus'
    elif 'Quercus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Quercus'
    elif 'Carpinus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Carpinus'
    elif 'Pinus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Pinus'
    elif 'Platanus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Platanus'
    elif 'Crataegus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Crataegus'
    elif 'Pyrus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Pyrus'
    elif 'Prunus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Prunus'
    elif 'Corylus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Corylus'
    elif 'Larix' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Larix'
    elif 'Aesculus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Aesculus'
    elif 'Populus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Populus'
    elif 'Fagus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Fagus'
    elif 'Thuja' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Thuja'
    elif 'Ginkgo' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Ginkgo'
    elif 'Taxus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Taxus'
    elif 'Picea' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Picea'
    elif 'Juniperus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Juniperus'
    elif 'Castanea' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Castanea'
    elif 'Tsuga' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Tsuga'
    elif 'Ilex' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Ilex'
    elif 'Ailanthus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Ailanthus'
    elif 'Gleditsia' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Gleditsia'
    elif 'Laburnum' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Laburnum'
    elif 'Metasequoia' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Metasequoia'
    elif 'Liquidambar' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Liquidambar'
    elif 'Styphnolobium' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Styphnolobium'
    elif 'Liriodendron' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Liriodendron'
    elif 'Paulownia' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Paulownia'
    elif 'Koelreuteria' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Koelreuteria'
    elif 'Cedrus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Cedrus'
    elif 'Catalpa' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Catalpa'
    elif 'Eleagnus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Eleagnus'
    elif 'Taxodium' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Taxodium'
    elif 'Nothofagus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Nothofagus'
    elif 'Cercidiphyllum' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Cercidiphyllum'
    elif 'Salix' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Salix'
    elif 'Juglans' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Juglans'
    elif 'Pterocarya' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Pterocarya'
    elif 'Crataegus' in str(row['genus']) or 'Crateagus' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'Crataegus'
    elif 'Ikke registreret' in str(row['genus']):
        streetTrees.at[i, 'genus'] = 'not_registered'

#%% JOINING ALLERGENICITY INDEX WITH STREETTREES 
streetTrees = merge(streetTrees, )

streetTrees.merge(country_names, on = 'iso_a3')

#%% EXPORT TO FILE
streetTrees.to_file('data_created/street_trees.gpkg')

#%% ENDLESS ATTEMPTS AT BETTER RENAMING FUNCTION
def rename_genus(listOfgenus):
    global streetTrees
    for string in listOfgenus:
        if string in streetTrees['genus']:
            streetTrees['genus'] = string

def rename_genus(listOfgenus):
    global streetTrees
    for string in listOfgenus:
        streetTrees[streetTrees['genus'].str.contains(string)] = string

def rename_genus(listOfgenus):
    global streetTrees
    for string in listOfgenus:
        if streetTrees.loc[streetTrees['genus'].str.contains(string)]:
            streetTrees['genus'] = string

def rename_genus(listOfgenus):
    global streetTrees
    for string in listOfgenus:
        streetTrees.where(cond = streetTrees['genus'].str.contains(string), 
        other = string)

def rename_genus(listOfgenus):
    global streetTrees
    for string in listOfgenus:
        streetTrees.mask(cond = streetTrees['genus'].str.contains(string), 
        other = string)

rename_genus([
    'Tilia', 
    'Acer'
    'Alnus'
    'Betula',
    'Robinia',
    'Ulmus',
    'Sorbus',
    'Fraxinus',
    'Malus',
    'Quercus',
    'Carpinus',
    'Pinus',
    'Platanus',
    'Crataegus',
    'Pyrus',
    'Prunus',
    'Corylus'
    'Larix',
    'Aesculus',
    'Populus',
    'Fagus',
    'Thuja',
    'Ginkgo',
    'Taxus',
    'Picea',
    'Juniperus',
    'Castanea',
    'Tsuga',
    'Ilex',
    'Ailanthus',
    'Gleditsia',
    'Laburnum',
    'Metasequoia',
    'Liquidambar',
    'Styphnolobium',
    'Liriodendron',
    'Paulownia',
    'Koelreuteria',
    'Cedrus',
    'Catalpa',
    'Eleagnus',
    'Taxodium',
    'Nothofagus',
    'Cercidiphyllum',
    'Salix',
    'Juglans',
    'Pterocarya',
    'Crataegus'])