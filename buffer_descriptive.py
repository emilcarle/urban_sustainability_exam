#%% IMPORTS
import pandas as pd
import plotly.express as px
import rasterio as rio
import rioxarray

#%% DATA TO DATAFRAME
xarrayIndex = rioxarray.open_rasterio('data_created/AllergenecityIndex.tif')

xarrayIndex.name = 'allergenecity_index'

dfIndex = xarrayIndex.squeeze().to_dataframe().reset_index()

#%% FORMAT DATA
dfIndex = dfIndex[dfIndex['allergenecity_index'].notna()]

dfIndexGroup = dfIndex.groupby('allergenecity_index').count().reset_index()

dfIndexGroup = dfIndexGroup.drop(columns=['y', 'x', 'spatial_ref'])

dfIndexGroup['area_km2'] = (dfIndexGroup['band'] * 25) / 1000000

#%% BAR CHART OF AREA COVERAGE FOR ALLERGENECITY INDEX SCORES
grayScale = px.colors.sequential.gray[::-1]
grayScale = grayScale[2:]

barIndexArea = px.bar(dfIndexGroup, 
    x = 'allergenecity_index',
    y = 'area_km2', 
    labels = dict(allergenecity_index = 'Allergenecity pressure', area_km2 = 'Area [km²]'),
    color = 'allergenecity_index',
    color_continuous_scale = grayScale)
    
barIndexArea = barIndexArea.update_layout(showlegend = False, yaxis_range = [0, 5.5], plot_bgcolor = '#f0f0f0')

barIndexArea = barIndexArea.update_yaxes(tickvals=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])

barIndexArea = barIndexArea.update_xaxes(tickvals=[0, 5, 10, 15, 20, 25, 30, 35, 40])

barIndexArea.show()

barIndexArea.write_image('descriptive_statistics/barIndexArea.png', width = 1000, scale = 5)




