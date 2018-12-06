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

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

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
    
    fig = {
        'data': [
            {
                'x': df[df['main_category']==category]['carbon-footprint_100g'],
                'y': df[df['main_category']==category]['price_per_100g'],
                'text': df[df['main_category']==category]['product_name'],
                'name': category,
                'mode': 'markers',
            } for category in df['main_category'].value_counts().index.tolist()
        ],
        'layout': {
            'xaxis': {'title': 'Carbon footprint per 100g [g]'},
            'yaxis': {'title': "Price per 100g [g]"}
        }
    }

    iplot(fig, filename='Carbon footprints clusters')


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

def plot_column_composition_circle(df, columns):
    
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

    
def plot_column_composition(df, column_str):
    if isinstance(df[column_str].iloc[0], str):
        occurence = explore.count_tag_occurences(df, column_str)
    else:
        occurence = explore.count_tag_occurences_list(df, column_str)

    #the full dataframe
    counts_df = pd.DataFrame( data = {'key': list(occurence.keys()), 
                                      'value' : list(occurence.values())
                                     },
                            ).sort_values('value', ascending = False)

    # accumulate small values into others
    new_row = pd.DataFrame(data = {
        'key' : ['Others'],
        'value' : [counts_df['value'][5:].sum()]
    })

    # combining top 5 with others
    df2 = pd.concat([counts_df[:5].copy(), new_row])


    frames = []

    # Load bar data
    traces = []
    for n, row in df2.iterrows():
        trace = go.Bar(y = [0], 
                       x = [row.values[1]],
                       name=row.values[0],
                       orientation = 'h')
        traces.append(trace);

    # Bar plot animation not supported yet
    # frames.append({'traces':traces})

    # Format layout
    layout = go.Layout(
                  title=column_str, 
                  showlegend=True, 
                  barmode="stack",
                  xaxis=dict(
                    showgrid=False,
                    showticklabels=True,
                ),
                yaxis=dict(
                    showgrid=False,
                    showline=False,
                    showticklabels=False,
                    zeroline=False,
                ),
                width=800,
                height=300,
            )

    figure = go.Figure(data=traces, layout=layout, frames=frames)

    iplot(figure)
    
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