import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import folium

from libs import exploring as explore

from sklearn import preprocessing

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

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
        
def plot_occurences_of_distinct_values_from_strings(df, column_key):
    # Find all distinct values
    values_set = set()

    for index, row in df.iterrows():
        for value in row[column_key].split(','):
            values_set.add(value)

    # Count the number of time each value appears in the column
    values_count = {}
    for value in list(values_set):
        values_count[value] = df[column_key].str.replace('(', '\(')\
                                            .str.replace(')', '\)')\
                                            .str.contains(value).sum()

    # Convert to pandas df for plotting functionalities
    values_count_pdf = pd.DataFrame(list(values_count.items()), columns=['Value', 'Count'])

    # Plot stores counts
    values_count_pdf.set_index('Value').sort_values(by='Count', ascending=True)[-20:].plot(kind='barh', figsize=(10, 10))
    plt.title("{0}: Counts of top 20 distincive values".format(column_key.title()))
    plt.gca().xaxis.grid(True)
    plt.show()
    
    return values_set, values_count

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
    values_count_pdf.set_index('Value').sort_values(by='Count', ascending=True)[-20:].plot(kind='barh', figsize=(10, 10))
    plt.title("{0}: Count of top 20 distincive values".format(column_key.title()))
    plt.show()
    
    return values_set, values_count


def plot_cluster_by_tags(df, plot2D_features = ["carbon-footprint_100g", "energy_100g"], cluster="labels"): 
    
    
    plt.rc('font', size=10)          # controls default text sizes
    plt.rc('axes', titlesize=10)     # fontsize of the axes title
    plt.rc('axes', labelsize=10)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=8)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=8)    # fontsize of the tick labels
    plt.rc('legend', fontsize=8)    # legend fontsize
    plt.rc('figure', titlesize=12)  # fontsize of the figure title
    
    plt.figure(figsize=(12, 6), dpi=100)

    first_tags = [tag[0][:60] for tag in df[cluster].str.split(',')]

    le = preprocessing.LabelEncoder()
    le.fit(list(set(first_tags)))
    codes = le.transform(first_tags) 

    # define the colormap
    cmap = plt.cm.tab20b
        
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
    plt.xlabel(plot2D_features[0]+ ' [g]')
    plt.ylabel(plot2D_features[1]+ ' [€]')
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

def plot_column_composition(df, columns):
    
    fig = plt.figure(figsize=(8, 4))
    
    for i, column_str in enumerate(columns):
        if isinstance(df[column_str].iloc[0], str):
            occurence = explore.count_tag_occurences(df, column_str)
        else:
            occurence = explore.count_tag_occurences_list(df, column_str)

        #the full dataframe
        counts_df = pd.DataFrame( data = {'keys': list(occurence.keys()), 
                                          'value' : list(occurence.values())
                                         },
                                ).sort_values('value', ascending = False)

        n_cols = 2
        n_rows = int(np.ceil(len(columns)/n_cols))
        
        ax = fig.add_subplot(n_rows, n_cols, i+1)
        
        # others
        new_row = pd.DataFrame(data = {
            'keys' : ['Others'],
            'value' : [counts_df['value'][5:].sum()]
        })

        #combining top 5 with others
        df2 = pd.concat([counts_df[:5].copy(), new_row])

        df2.plot.pie(y='value', labels=df2['keys'], autopct='%1.1f%%', startangle=45, ax=ax, cmap=plt.cm.tab20)

        #draw circle
        centre_circle = plt.Circle((0,0),0.75,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')  
        plt.tight_layout()
        plt.title(column_str)
        ax.legend().set_visible(False)
        ax.set_ylabel(None).set_visible(False)
    plt.show()

def search_cca3(name, countries):
    country_set_name = countries[countries.name.apply(lambda x: x.lower()  == name.lower())]
    if(not country_set_name.empty):
        return country_set_name.iloc[0,1]
    return " "

def make_plot(title, hist, edges):
    p = figure(title=title, tools='', background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5)
    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 't (year)'
    p.yaxis.axis_label = '% of palm oil products '
    p.grid.grid_line_color="white"
    return p

def hist(column):
    bins = column.max() - column.min()
    hist, edges = np.histogram(column, density=True, bins=bins)
    p1 = make_plot("Distribution of palm oil products", hist, edges)
    show(p1)