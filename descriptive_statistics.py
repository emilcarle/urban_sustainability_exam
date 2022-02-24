#%% IMPORTS
import geopandas as gp
import plotly.express as px
import kaleido

#%% DATA
streetTrees = gp.read_file('data_created/street_trees.gpkg')

#%% CONSTRUCTION OF ADDITIONAL COLUMNS
#calculate frequency of genus
streetTrees['freq_genus'] = streetTrees.groupby('genus')['genus'].transform('count')

#renaming genus summing those with small frequencies
streetTrees['genus_large'] = streetTrees['genus']
streetTrees.loc[streetTrees['freq_genus'] < 500, 'genus_large'] = 'Other genus'
streetTrees.loc[streetTrees['freq_genus'] < 100, 'genus_large'] = 'Insignificant genus'

#generating column for later use in frequency graphs
streetTrees['single_tree'] = 1

#%% PIE CHART: GENUS FREQUENCY
pieGenusFreq = px.pie(streetTrees, 
    values = 'single_tree', 
    names = 'genus_large', 
    title = 'Distribution of Tree Genus')

pieGenusFreq.show()

#%% PIE CHART: FREQUENCY OF 'OTHER genus' TREE GENUS
streetTreesOthergenus = streetTrees.loc[streetTrees['genus_large'] == 'Other genus']

pieOtherGenusFreq = px.pie(streetTreesOthergenus, 
    values = 'single_tree', 
    names = 'genus', 
    title = '''Distribution of Tree Genus' within "Other Genus" category''')

pieOtherGenusFreq.show()
#%% BAR CHART OF TREE GENUS
streetTreesGroupGenus = streetTrees.groupby('genus').sum()

barGenusFreq = px.bar(streetTreesGroupGenus, 
    orientation = 'h',
    y = 'single_tree', 
    title = 'Distribution of Tree Genus').update_xaxes(categoryorder = 'total descending')

barGenusFreq.show()

barGenusFreq.write_image('descriptive_statistics/barGenusFreq.png', engine = 'kaleido')

# %% CREATE BAR DIAGRAMS WITH BARS SORTED BY AMOUNT OF TREES
