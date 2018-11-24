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
        
def plot_occurences_of_distinct_values(df, column_key):
    # Find all distinct countries
    values_set = set()
    for index, row in df.iterrows():
        for value in row[column_key]:
            values_set.add(value)

    # Count the number of time each value appears in the column
    values_count = {}
    for value in list(values_set):
        values_count[value] = df[column_key].apply({value}.issubset).sum()

    # Convert to pandas df for plotting functionalities
    values_count_pdf = pd.DataFrame(list(values_count.items()), columns=['Value', 'Count'])

    # Plot stores counts
    values_count_pdf.set_index('Value').sort_values(by='Count', ascending=False)[:50].plot(kind='barh', figsize=(10, 20))
    plt.title("{0}: Count of distincive values".format(column_key.title()))
    plt.show()
    
    # return values_set, values_count


def plot_cluster_by_tags(df, plot2D_features = ["carbon-footprint_100g", "energy_100g"], cluster="labels"):    
    plt.figure(figsize=(8, 8), dpi=80)
    
    first_tags = [tag[0] for tag in df[cluster]]
    
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

    ax = plt.scatter(x=df[plot2D_features[0]].iloc[:limit].values,
                     y=df[plot2D_features[1]].iloc[:limit].values,
                     c=codes[:limit],
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

