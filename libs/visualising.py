import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import folium

from sklearn import preprocessing

def hist_all_features(df, column_keys):
    fig, ax = plt.subplots(9,3,figsize=(25,40))
    n = 0
    for feature in column_keys:
        sns.distplot(df[feature],
                     ax=ax[n,0])
        sns.distplot(df[df[feature]>0]["boxcox_" + feature],
                     ax=ax[n,1])
        sns.distplot(df["transformed_" + feature],
                     ax=ax[n,2])
        n+=1


def plot_cluster_by_tags(df, plot2D_features = ["carbon-footprint_100g", "energy_100g"], cluster="labels"):    
    plt.figure(figsize=(8, 8), dpi=80)
    
    first_tags = [tag[0] for tag in df[cluster].str.split(',')]
    
    le = preprocessing.LabelEncoder()
    le.fit(list(set(first_tags)))
    codes = le.transform(first_tags) 
    
    # define the colormap
    cmap = plt.cm.jet
    # extract all colors from cmap
    cmaplist = [cmap(i) for i in range(cmap.N)]
    # create the new map
    cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)

    label = le.inverse_transform(codes)

    N = len(list(set(label)))  # Number of labels

    # define the bins and normalize
    bounds = np.linspace(0, N, N + 1)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    limit = 10000

    ax = plt.scatter(x=df[plot2D_features[0]].values[0:limit],
                     y=df[plot2D_features[1]].values[0:limit],
                     c=codes,
                     marker='o',
                     cmap=cmap
            )

    # create the colorbar
    cb = plt.colorbar(ax, spacing='proportional', ticks=bounds)
    cb.set_ticklabels(list(set(label)))
    plt.show()


def plot_world_map(country_count):


    ## Country coordinates for plotting
    country_geo = '\libs\world-countries.json'

    map = folium.Map(location=[100, 0], zoom_start=1.5)

    # choropleth maps bind Pandas Data Frames and json geometries.
    map.choropleth(geo_data=country_geo,
                   data=country_count,
                   columns=['Country', 'Value'],
                   key_on='feature.id',
                   fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2,
                   )

