#%% IMPORTS
import geopandas as gp
import plotly.express as px
import numpy as np
import os

if not os.path.exists('descriptive_statistics'):
    os.mkdir('descriptive_statistics')
#%% DATA
streetTrees = gp.read_file('data_created/street_trees.gpkg')

#%% CONSTRUCTION OF ADDITIONAL COLUMNS
#calculate frequency of genus
streetTrees['freq_genus'] = streetTrees.groupby('genus')['genus'].transform('count')
#renaming genus summing those with small frequencies
streetTrees['genus_large'] = streetTrees['genus']
streetTrees.loc[streetTrees['freq_genus'] < 100, 'genus_large'] = 'Other genera'
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
    names = 'genus')

pieOtherGenusFreq.show()

#%% BAR CHART OF TREE GENUS
streetTreesGroupInsignificantGenus = streetTrees.groupby('genus_large').sum().reset_index()

streetTreesGroupInsignificantGenus['is_aggregated'] = np.where(streetTreesGroupInsignificantGenus['genus_large'] == 'Other genera', 'aggregated', 'raw')

streetTreesGroupInsignificantGenus = streetTreesGroupInsignificantGenus.sort_values(by = 'single_tree', ascending = False)

barGenusFreq = px.bar(streetTreesGroupInsignificantGenus, 
    x = 'genus_large',
    y = 'single_tree', 
    color = 'is_aggregated',
    labels = dict(genus_large = 'Tree genera', single_tree = 'Number of trees'),
    color_discrete_sequence = ['grey', 'darkgrey'])
    
barGenusFreq = barGenusFreq.update_xaxes(categoryorder = 'array', categoryarray = ['Other genera'], type = 'category')

barGenusFreq = barGenusFreq.update_layout(showlegend = False, yaxis_range = [0, 8000], plot_bgcolor = '#f0f0f0')

barGenusFreq = barGenusFreq.update_yaxes(tickvals=[0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000])

barGenusFreq.show()

barGenusFreq.write_image('descriptive_statistics/barGenusFreq.png', scale = 5)
#%% CREATE BAR CHART OF ALLERGENECITY
streetTreesAllergenecity = streetTrees.groupby('allergenecity_index').sum().reset_index()

barAllergenecityFreq = px.bar(streetTreesAllergenecity, 
    x = 'allergenecity_index',
    y = 'single_tree',
    color = 'allergenecity_index',
    labels = dict(allergenecity_index = 'Allergenecity Index', single_tree = 'Number of trees'),
    color_discrete_sequence = px.colors.qualitative.Set3)
    
barAllergenecityFreq = barAllergenecityFreq.update_layout(showlegend = False, yaxis_range = [0, 20000], plot_bgcolor = '#f0f0f0')

barAllergenecityFreq = barAllergenecityFreq.update_yaxes(tickvals = [0, 500, 1000, 1500, 2000, 4000, 6000, 8000, 10000, 15000, 20000])

barAllergenecityFreq.show()

barAllergenecityFreq.write_image('descriptive_statistics/barAllergenecityFreq.png', scale = 5)

#%% ALLERGENECITY .CSV
streetTreesAllergenecity = streetTrees.groupby('allergenecity_index').sum().reset_index()

streetTreesAllergenecity = streetTreesAllergenecity.drop('freq_genus', axis = 1).rename(columns = {'single_tree':'count'})

streetTreesAllergenecity.to_csv('descriptive_statistics/allergenecity_tree_count.csv')