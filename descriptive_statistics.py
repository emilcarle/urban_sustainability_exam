#%% IMPORTS
import geopandas as gp
import plotly.express as px
import plotly.figure_factory as ff

#%% DATA
streetTrees = gp.read_file('data_created/street_trees.gpkg')

#%% CONSTRUCTION OF ADDITIONAL COLUMNS
#calculate frequency of genus
streetTrees['freq_genus'] = streetTrees.groupby('species')['species'].transform('count')

#renaming species summing those with small frequencies
streetTrees['species_large'] = streetTrees['species']
streetTrees.loc[streetTrees['freq_genus'] < 500, 'species_large'] = 'Other species'
streetTrees.loc[streetTrees['freq_genus'] < 100, 'species_large'] = 'Insignificant species'

#generating column for later use in frequency graphs
streetTrees['single_tree'] = 1

#%% PIE CHART: GENUS FREQUENCY
pieGenusFreq = px.pie(streetTrees, 
    values = 'single_tree', 
    names = 'species_large', 
    title = 'Distribution of Tree Genus')

pieGenusFreq.show()

#%% PIE CHART: FREQUENCY OF 'OTHER SPECIES' TREE GENUS
streetTreesOtherSpecies = streetTrees.loc[streetTrees['species_large'] == 'Other species']

pieOtherGenusFreq = px.pie(streetTreesOtherSpecies, 
    values = 'single_tree', 
    names = 'species', 
    title = '''Distribution of Tree Genus' within "Other Genus" category''')

pieOtherGenusFreq.show()
#%% BAR CHART OF TREE GENUS
barGenusFreq = px.bar(streetTrees, 
    x = 'species', 
    y = 'single_tree', 
    title = 'Distribution of Tree Genus',
    color = 'municipality')

barGenusFreq.show()

# %% CREATE BAR DIAGRAMS WITH BARS SORTED BY AMOUNT OF TREES
