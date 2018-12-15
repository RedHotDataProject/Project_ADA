import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pylab
import copy 

from libs import exploring as explore

from sklearn import preprocessing

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

plots_folder = "./docs/Images/plots/"
save_plots_offline = False

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
    
    values_count = explore.count_values(df, column_key)

    # Convert to pandas df for plotting functionalities
    values_count_pdf = pd.DataFrame(list(values_count.items()), columns=['Value', 'Count'])

    # Plot stores counts
    values_count_pdf.set_index('Value').sort_values(by='Count', ascending=True)[-20:].plot(kind='barh', figsize=(10, 10))
    plt.title("{0}: Counts of top 20 distincive values".format(column_key.title()))
    plt.gca().xaxis.grid(True)
    plt.show()
    
    return values_count


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
    
    return values_count

def plot_grouped_counts(df, groupby_column='created_yyyy', count_columns=['nutrition_score_fr']):
    
    df_grouped = df[df['purchase_places']=='France'].groupby(groupby_column).count()
    
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    
    df_grouped['code'].plot(label='products total', ax=ax2)
    df_grouped[count_columns].plot(kind='bar', ax=ax)
    
    ax.set_title('Values counts grouped by '+ groupby_column)
    ax.set_ylabel('counts')
    plt.show()

def plot_occurences_on_map(df, column_key, save, save_title, show_distances=False, title=''):
    
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
            z = np.log10(values_count_pd['Count']),
            # name = values_count_pd['Country'],
            autocolorscale = False,
            reversescale = True,
            colorbar = dict(
                #lenmode='fraction', 
                len=0.7,
                #autotick = True,
                tick0= 1,
                tickmode= 'array',
                tickvals= [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
                ticktext = ['1','10<sup>1/2</sup>','10<sup>1</sup>', '10<sup>3/2</sup>', '10<sup>2</sup>', '10<sup>5/2</sup>', '10<sup>3</sup>','10<sup>3/2</sup>', '10<sup>4</sup>'],
                #ticks = 'outside',
                title = 'Counts'),
            colorscale='Viridis', 
            text = values_count_pd['Country'] + ' '+ values_count_pd['Count'].astype(str),
            hoverinfo= 'text'
          ) ]

    lines = []
    
    if show_distances:
        origin_latlng = countries.loc[countries['cca3'] == 'FRA']['latlng'].iloc[0]
        maximum = float(np.log10(values_count_pd['Count']).max())   
        for i, row in values_count_pd.iterrows():
            try:
                origin_latlng = countries.loc[countries['cca3'] == 'FRA']['latlng'].iloc[0]
                country_latlng = countries.loc[countries['cca3'] == row['cca3']]['latlng'].values[0]
                lines.append(
                    dict(
                        type = 'scattergeo',
                        lon = [ country_latlng[1], origin_latlng[1] ],
                        lat = [ country_latlng[0], origin_latlng[0] ],
                        mode = 'lines+markers',
                        name= '', 
                        text = row['Country'] + '<br>' + '# products: ' + str(row['Count']),
                        hoverinfo='text',
                        line = dict(
                            width = (np.log10(row['Count'])+0.1)*1.2,
                            color = 'red'
                        ),
                        opacity = min(float(np.log10(row['Count']))/maximum*1.2 + 0.1, 1)
                    )
                )
            except IndexError:
                continue
                
                
    if title == '':
        tile = column_key
                
    # Format map 
    layout = dict(
        geo = dict(
            projection = dict(
                type = 'equirectangular'
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
        yaxis = dict(fixedrange = True),
        margin=go.layout.Margin(
            l=50,
            r=100,
            b=0,
            t=0,
            pad=4
        )
    )

    figure = dict( data=worldmap + lines, layout=layout )
    
    # Plot interactive figure
    iplot(figure)
    
    # also save offline
    if save:
        plot(figure, filename= plots_folder + "map_" + save_title + ".html", auto_open=False)
    

def plot_cluster_by_tags(df, 
                         plot2D_features = ["carbon-footprint_100g", "energy_100g"], 
                         marker_text_column = "product_name",
                         cluster="labels"): 
    axis_title = copy.copy(plot2D_features)
    for i, column_str in enumerate(plot2D_features):
        if column_str == 'carbon-footprint_100g':
            axis_title[i] = 'Carbon footprint per 100g [g]'
        elif column_str == 'energy_100g':
            axis_title[i] = 'Energy per 100g [kj]'
        elif column_str == 'price_per_100g':
            axis_title[i] = 'Price per 100g [€]'
    
    figure = {
        'data': [
            {
                'x': df[df[cluster]==label][plot2D_features[0]],
                'y': df[df[cluster]==label][plot2D_features[1]],
                'text': df[df[cluster]==label][marker_text_column],
                'name': label,
                'mode': 'markers',
            } for label in df[cluster].value_counts().index.tolist()
        ],
        'layout': {
            'xaxis': {'title': axis_title[0]},
            'yaxis': {'title': axis_title[1]},
        }
    }
    
    # Plot interactive figure
    iplot(figure)
    
    # also save offline
    if save:
        plot(figure, filename= plots_folder + save_title + ".html", auto_open=False)    


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

    
def plot_column_composition(df, column_str, save, save_title, num_values=5):
    
    if isinstance(df[column_str].iloc[0], str):
        occurence = explore.count_tag_occurences(df, column_str)
    else:
        occurence = explore.count_tag_occurences_list(df, column_str)

    #the full dataframe
    counts_df = pd.DataFrame( data = {'key': list(occurence.keys()), 
                                      'value' : list(occurence.values())
                                     },
                            ).sort_values('value', ascending=False)

    # Move 'Unknown' and 'Others' column to end of df
    for values_str in ['Unknown', 'Others']:
        index = list(np.where(counts_df.key == values_str)[0])
        if index:
            idx = counts_df.index.tolist()
            popped = idx.pop(index[0])
            counts_df = counts_df.reindex(idx+[popped])
    
    # accumulate small values into others
    new_row = pd.DataFrame(data = {
        'key' : ['Others'],
        'value' : [counts_df['value'][num_values:].sum()]
    })

    # combining top 5 with others
    df2 = pd.concat([counts_df[:num_values].copy(), new_row])


    frames = []
    
    overall_count = 0
    # colors = ['#F4B5A6', '#F4EBA6',
    #      '#B2F4A6', '#A6E3F4',
    #      '#C4A6F4','#E0DBDD']
    colors = ['#90CB70', '#F0F472', '#B69C63','#D6D0C3', '#8CB5ED', '#F3AC6D', '#EC9BE2', '#7979CD', '#FCE2E4']

    # Load bar data
    traces = []
    i=0
    for n, row in df2.iterrows():
        trace = go.Bar(y = [0], 
                       x = [row.values[1]],
                       name=row.values[0],
                       orientation = 'h',
                       marker=dict(color=colors[i],
                                   # line=dict(color='rgb(248, 248,249)',width=1)
                                  ),
                      )
        i+=1
        overall_count += row.values[1]
        traces.append(trace);

    # Bar plot animation not supported yet
    # frames.append({'traces':traces})
    
    # set x-axis labels and their corresponding data values    
    frac = overall_count
    i = 0;
    while frac > 10:
        i = i+1;
        frac = frac/10
    tickvals = list(range(0,int(overall_count), 5*int(10**(i-1))))
    tickvals.append(overall_count)


    # Format layout
    layout = go.Layout(
                    showlegend=True, 
                    barmode="stack",
                    xaxis=dict(
                        tickvals=tickvals
                    ),
                    yaxis=dict(
                        showgrid=False,
                        showline=False,
                        showticklabels=False,
                        zeroline=False,
                    ),
                    width=800,
                    height=200,
                    margin=go.layout.Margin(
                        l=40,
                        r=40,
                        b=50,
                        t=15,
                        pad=4
                    )
    )
            

    figure = go.Figure(data=traces, layout=layout, frames=frames)

    # Plot interactive figure
    iplot(figure)
    
    # also save offline
    if save:
        plot(figure, filename= plots_folder + save_title + ".html", auto_open=False)    
    
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

    
def make_grade_stacked_bar(attempt, label_column, x_column, y_column, save, save_title):

    #colors = ["#008010", "#9ACD32","#FFD700", "#FF8C00", "#DB4832"]
    colors = ["#517C53", "#99EB9D","#E9F287", "#F2CE75", "#F68774"]
    # Load bar data
    traces = []
    i=0
    for num, grade in enumerate(attempt):

        years = [int(year) for year in attempt.year.unique()]
        grades = attempt.nutrition_grade.unique()

        traces = []
        for num, grade in enumerate(grades):

            trace = go.Bar(
                x=years,
                y=attempt[attempt.nutrition_grade == grade][y_column].values,
                name=grade,
                marker=dict(
                    color=colors[num],
                    line=dict(
                        color=colors[num],
                        width=2,
                    )
                )
            )

            traces.append(trace);

     # Format layout
    layout = go.Layout(
                    showlegend=True, 
                    barmode="stack",
                    margin=go.layout.Margin(
                        l=50,
                        r=50,
                        b=50,
                        t=15,
                        pad=4
                    )
    )
    
    figure = go.Figure(data=traces, layout=layout)

    # Plot interactive figure
    iplot(figure)
    
    # also save offline
    if save:
        plot(figure, filename= plots_folder + save_title + ".html", auto_open=False) 
    
def find_composition_list(df, column_str, cat_lis):
    if isinstance(df[column_str].iloc[0], str):
        occurence = explore.count_tag_occurences(df, column_str)
    else:
        occurence = explore.count_tag_occurences_list(df, column_str)

    #the full dataframe
    counts_df = pd.DataFrame( data = {'keys': list(occurence.keys()), 
                                      'value' : list(occurence.values())
                                     },
                            ).sort_values('value', ascending = False)
    
    counts_df_save = counts_df[counts_df['keys'].isin(cat_lis)]
    counts_df_dropped = counts_df[~counts_df['keys'].isin(cat_lis)]
    # others
    new_row = pd.DataFrame(data = {
        'keys' : ['Others'],
        'value' : [counts_df_dropped['value'][:].sum()]
    })

    #combining top 5 with others
    df2 = pd.concat([counts_df_save[:].copy(), new_row])
    return df2

    
    
def plot_grade_content(nutrition_over_time):
    index_list = ['B', 'C', 'D', 'E']
    cat_list = ['Plant-based', 'Carbs', 'Meats', 'Dairies', 'Seafood', 'Beverages', 'Sugary snacks','Others']
    categories = {"keys": cat_list}
    check = pd.DataFrame.from_dict(categories)
    
    nutrional_products = nutrition_over_time[nutrition_over_time["nutrition_grade"] == 'A']              
    table_content = find_composition_list(df=nutrional_products, column_str='main_category', cat_lis= cat_list)
    table_content['Percentage'] = table_content.value/table_content.value.sum()*100
    table_content = check.merge(table_content, how='outer', on= "keys").fillna(0)
    table_content['grade'] = 'A'
    
    for elem in index_list:
        nutrional_products = nutrition_over_time[nutrition_over_time["nutrition_grade"] == elem]
        add_content = find_composition_list(df=nutrional_products, column_str='main_category', cat_lis= cat_list)
        add_content['Percentage'] = add_content.value/add_content.value.sum()*100
        add_content = check.merge(add_content, how='outer', on= "keys").fillna(0)
        add_content['grade'] = elem
        table_content = table_content.append(add_content, ignore_index=True)
    return table_content

def make_content_stacked_bar(table, label_column, x_column, y_column, save, save_title):

    keys = table[label_column].drop_duplicates()
    data_stacked = []
    colors = ['#90CB70', '#F0F472', '#B69C63','#D6D0C3', '#8CB5ED', '#F3AC6D', '#EC9BE2', '#7979CD', '#FCE2E4']
    liste = ['A','B','C','D','E']
    for num, grade in enumerate(keys):
        values = list(table[table[label_column] == grade].loc[:, y_column])
        
        trace = go.Bar(
                x=liste,
                y=values,
                name=grade,
                #marker=dict(color=colors[num])
                marker = dict(color = colors[num]))

        layout = go.Layout(
            barmode='stack'
        )
        data_stacked.append(trace)

    fig = go.Figure(data=data_stacked,layout=layout)
    iplot(fig, filename='stacked-bar')
    
    # also save offline
    if save:
        plot(fig, filename= plots_folder + save_title  + ".html", auto_open=False) 

def palm_oil_overtime(df,df_absolute, save, save_title):   
    data = [go.Bar(x=df.index,
               y=df.values,
               #text=palm_oil_over_time,
               text = round(df, 2).astype(str) + '% <br>'+ df_absolute.astype(str),
               hoverinfo = 'text',
               marker=dict(color='#097B4E'))]


    layout = go.Layout(
        yaxis=dict(
            title='Percentage of products with palm oil [%]'
            ),
        margin=go.layout.Margin(
            l=50,
            r=50,
            b=40,
            t=15,
            pad=4
            )
        )

    figure = go.Figure(data=data, layout=layout)

    # Plot interactive figure
    iplot(figure)
    
    # also save offline
    if save:
        plot(figure, filename= plots_folder + save_title  + ".html", auto_open=False) 
