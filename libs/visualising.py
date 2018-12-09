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
    
    values_count = count_values(df, column_key)

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

def plot_occurences_on_map(df, column_key, show_distances=False, title=''):
    
    countries_label = pd.read_csv("./data/country_lookup.csv")[['name', 'cca3']]     
    
    # Load the first sheet of the JSON file into a data frame
    countries = pd.read_json('./data/countries_latlon.json')
    
    values_count_pd = pd.DataFrame.from_dict(explore.count_values(df, column_key),
                                             orient='index',
                                             columns=['Count']).reset_index().\
                                            rename(index=str, columns={"index": "Country", "Count": "Count"})
    
    # Drop values that cannot be assigned to a geographic location
    values_count_pd = values_count_pd[values_count_pd.Country != "Unknown"]

    # Map country to cca3 code
    values_count_pd['cca3'] = values_count_pd.Country.apply(lambda l: search_cca3(l, countries_label))

    # Colour all countries based on their count
    worldmap = [ dict(
            type = 'choropleth',
            locations = values_count_pd['cca3'],
            z = np.log(values_count_pd['Count']),
            name = values_count_pd['Country'],
            autocolorscale = False,
            reversescale = True,
            colorbar = dict(
                autotick = True,
                title = 'Counts'),
          ) ]

    lines = []
    
    if show_distances:
        france_latlng = countries.loc[countries['cca3'] == 'FRA']['latlng'].iloc[0]
        for i, row in values_count_pd.iterrows():
            try:
                country_latlng = countries.loc[countries['cca3'] == row['cca3']]['latlng'].values[0]
                lines.append(
                    dict(
                        type = 'scattergeo',
                        lon = [ country_latlng[1], france_latlng[1] ],
                        lat = [ country_latlng[0], france_latlng[0] ],
                        mode = 'lines+marker',
                        name = row['Country'],
                        line = dict(
                            width = np.log(row['Count'])*0.5,
                            color = 'red',
                        ),
                    )
                )
            except IndexError:
                continue
                
                
    if title == '':
        tile = column_key
                
    # Format map
    layout = dict(
        title = title,
        geo = dict(
            projection = dict(
                type = 'Mercator'
            ),
            showframe = False,
            showcoastlines = True,
            showland = True,
            landcolor = "rgb(229, 229, 229)",
            countrycolor = "rgb(255, 255, 255)" ,
            coastlinecolor = "rgb(255, 255, 255)",
        ),
        showlegend=False,
        xaxis = dict(fixedrange = True),
        yaxis = dict(fixedrange = True)

    )

    fig = dict( data=worldmap + lines, layout=layout )
    iplot( fig, validate=False, filename='map'+column_key )

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
            'yaxis': {'title': "Price per 100g [g]"},
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

def find_composition(df, column_str):
    if isinstance(df[column_str].iloc[0], str):
        occurence = explore.count_tag_occurences(df, column_str)
    else:
        occurence = explore.count_tag_occurences_list(df, column_str)

    #the full dataframe
    counts_df = pd.DataFrame( data = {'keys': list(occurence.keys()), 
                                      'value' : list(occurence.values())
                                     },
                            ).sort_values('value', ascending = False)

    # others
    new_row = pd.DataFrame(data = {
        'keys' : ['Others'],
        'value' : [counts_df['value'][5:].sum()]
    })

    #combining top 5 with others
    df2 = pd.concat([counts_df[:5].copy(), new_row])
    return df2

def plot_column_composition_pie(df, column_str):
    
    fig = plt.figure(figsize=(8, 4))
    
    df2 = find_composition(df, column_str)

    ax = df2.plot.pie(y='value', labels=df2['keys'], autopct='%1.1f%%', startangle=45, cmap=plt.cm.tab20)

    #draw circle
    centre_circle = plt.Circle((0,0),0.75,fc='white')
    ax.add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')  
    plt.tight_layout()
    plt.title(column_str)
    ax.legend().set_visible(False)
    ax.set_ylabel(None).set_visible(False)
    plt.show()

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
                height=300)
            

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
    
    
# Matlab Parula colormap
colormap_rgb = [[0.2081, 0.1663, 0.5292], [0.2116238095, 0.1897809524, 0.5776761905], 
 [0.212252381, 0.2137714286, 0.6269714286], [0.2081, 0.2386, 0.6770857143], 
 [0.1959047619, 0.2644571429, 0.7279], [0.1707285714, 0.2919380952, 
  0.779247619], [0.1252714286, 0.3242428571, 0.8302714286], 
 [0.0591333333, 0.3598333333, 0.8683333333], [0.0116952381, 0.3875095238, 
  0.8819571429], [0.0059571429, 0.4086142857, 0.8828428571], 
 [0.0165142857, 0.4266, 0.8786333333], [0.032852381, 0.4430428571, 
  0.8719571429], [0.0498142857, 0.4585714286, 0.8640571429], 
 [0.0629333333, 0.4736904762, 0.8554380952], [0.0722666667, 0.4886666667, 
  0.8467], [0.0779428571, 0.5039857143, 0.8383714286], 
 [0.079347619, 0.5200238095, 0.8311809524], [0.0749428571, 0.5375428571, 
  0.8262714286], [0.0640571429, 0.5569857143, 0.8239571429], 
 [0.0487714286, 0.5772238095, 0.8228285714], [0.0343428571, 0.5965809524, 
  0.819852381], [0.0265, 0.6137, 0.8135], [0.0238904762, 0.6286619048, 
  0.8037619048], [0.0230904762, 0.6417857143, 0.7912666667], 
 [0.0227714286, 0.6534857143, 0.7767571429], [0.0266619048, 0.6641952381, 
  0.7607190476], [0.0383714286, 0.6742714286, 0.743552381], 
 [0.0589714286, 0.6837571429, 0.7253857143], 
 [0.0843, 0.6928333333, 0.7061666667], [0.1132952381, 0.7015, 0.6858571429], 
 [0.1452714286, 0.7097571429, 0.6646285714], [0.1801333333, 0.7176571429, 
  0.6424333333], [0.2178285714, 0.7250428571, 0.6192619048], 
 [0.2586428571, 0.7317142857, 0.5954285714], [0.3021714286, 0.7376047619, 
  0.5711857143], [0.3481666667, 0.7424333333, 0.5472666667], 
 [0.3952571429, 0.7459, 0.5244428571], [0.4420095238, 0.7480809524, 
  0.5033142857], [0.4871238095, 0.7490619048, 0.4839761905], 
 [0.5300285714, 0.7491142857, 0.4661142857], [0.5708571429, 0.7485190476, 
  0.4493904762], [0.609852381, 0.7473142857, 0.4336857143], 
 [0.6473, 0.7456, 0.4188], [0.6834190476, 0.7434761905, 0.4044333333], 
 [0.7184095238, 0.7411333333, 0.3904761905], 
 [0.7524857143, 0.7384, 0.3768142857], [0.7858428571, 0.7355666667, 
  0.3632714286], [0.8185047619, 0.7327333333, 0.3497904762], 
 [0.8506571429, 0.7299, 0.3360285714], [0.8824333333, 0.7274333333, 0.3217], 
 [0.9139333333, 0.7257857143, 0.3062761905], [0.9449571429, 0.7261142857, 
  0.2886428571], [0.9738952381, 0.7313952381, 0.266647619], 
 [0.9937714286, 0.7454571429, 0.240347619], [0.9990428571, 0.7653142857, 
  0.2164142857], [0.9955333333, 0.7860571429, 0.196652381], 
 [0.988, 0.8066, 0.1793666667], [0.9788571429, 0.8271428571, 0.1633142857], 
 [0.9697, 0.8481380952, 0.147452381], [0.9625857143, 0.8705142857, 0.1309], 
 [0.9588714286, 0.8949, 0.1132428571], [0.9598238095, 0.9218333333, 
  0.0948380952], [0.9661, 0.9514428571, 0.0755333333], 
 [0.9763, 0.9831, 0.0538]]
    
def make_grade_stacked_bar(attempt, label_column, x_column, y_column):
    fig, ax = plt.subplots(figsize=(10,7))  

    nutrition_grades = attempt[label_column].drop_duplicates()
    margin_bottom = np.zeros(len(attempt[x_column].drop_duplicates()))
    colors = ["#008010", "#9ACD32","#FFD700", "#FF8C00", "#DB4832"]

    for num, grade in enumerate(nutrition_grades):
        values = list(attempt[attempt[label_column] == grade].loc[:, y_column])

        attempt[attempt[label_column] == grade].plot.bar(x=x_column,y=y_column, ax=ax, stacked=True, 
                                        bottom = margin_bottom, color=colors[num], label=grade)
        margin_bottom += values
    ax.set_title("Products added in the dataset with a nutrition grade")
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    if(y_column == 'Percentage'):
        ax.set_ylabel('Percentage (%)')
        ax.set_title("Percentage of products added in the dataset with a certain nutrition grade")
    plt.show()
    
    
    
def plot_grade_content(nutrition_over_time):
    index_list = ['B', 'C', 'D', 'E']
    categories = {"keys": ['Plant-based', 'Carbs', 'Meats', 'Dairies', 'Frozen foods', 'Meals', 'Beverages', 'Sugary snacks','Others']}
    check = pd.DataFrame.from_dict(categories)
    
    nutrional_products = nutrition_over_time[nutrition_over_time["nutrition_grade"] == 'A']              
    table_content = find_composition(df=nutrional_products, column_str='main_category')
    table_content['Percentage'] = table_content.value/table_content.value.sum()*100
    table_content = check.merge(table_content, how='outer', on= "keys").fillna(0)
    table_content['grade'] = 'A'
    
    for elem in index_list:
        nutrional_products = nutrition_over_time[nutrition_over_time["nutrition_grade"] == elem]
        add_content = find_composition(df=nutrional_products, column_str='main_category')
        add_content['Percentage'] = add_content.value/add_content.value.sum()*100
        add_content = check.merge(add_content, how='outer', on= "keys").fillna(0)
        add_content['grade'] = elem
        table_content = table_content.append(add_content, ignore_index=True)
    return table_content

def make_content_stacked_bar(table, label_column, x_column, y_column):
    fig, ax = plt.subplots(figsize=(10,7))  

    keys = table[label_column].drop_duplicates()
    margin_bottom = np.zeros(len(table[x_column].drop_duplicates()))
    colors = ['#008010', '#ffe119', '#492424', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#285FB0', '#fabebe']
    
    for num, grade in enumerate(keys):
        values = list(table[table[label_column] == grade].loc[:, y_column])

        table[table[label_column] == grade].plot.bar(x=x_column,y=y_column, ax=ax, stacked=True, 
                                        bottom = margin_bottom, color=colors[num],label=grade)
        margin_bottom += values
    ax.set_title("Count of each categories per nutrition grade")
    ax.set_xlabel('Grade')
    ax.set_ylabel('Count')
    if(y_column == 'Percentage'):
        ax.set_ylabel('Percentage (%)')
        ax.set_title("Percentage of the five most important categories per nutrition grade [+others]")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()