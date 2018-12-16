import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy

from libs import exploring as explore

from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

plots_folder = "./docs/Images/plots/"

        
def plot_occurrences_of_distinct_values_from_strings(df, column_key):
    """
    Count distinct tags in column and plot top 20 counts.
    :param df:
    :param column_key: column entries as comma separated strings
    :return dict: keys are tags, values their occurrences counts.
    """
    values_count = explore.count_values(df, column_key)

    # Convert to pandas df for plotting functionalities
    values_count_pdf = pd.DataFrame(list(values_count.items()), columns=['Value', 'Count'])

    # Plot stores counts
    values_count_pdf.set_index('Value').\
                     sort_values(by='Count', ascending=True)[-20:].\
                     plot(kind='barh', figsize=(10, 10))
    plt.title("{0}: Counts of top 20 distinctive values".format(column_key.title()))
    plt.gca().xaxis.grid(True)
    plt.show()

    return values_count


def plot_occurrences_of_distinct_values(df, column_key):
    """
    Count distinct tags in column and plot top 20 counts.
    :param df:
    :param column_key: column entries as lists
    :return dict: keys are tags, values their occurrences counts.
    """

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


def plot_occurrences_on_map(df, column_key,
                            show_distances=False,
                            save_offline=False,
                            save_offline_title='occurrences_on_map'):
    """
    Color countries outline corresponding to their occurrences in the column.
    :param df:
    :param column_key:
    :param show_distances:
    :param save:
    :param save_title:
    """
    countries_label = pd.read_csv("./data/country_lookup.csv")[['name', 'cca3']]

    # Load the first sheet of the JSON file into a data frame
    countries = pd.read_json('./data/countries_latlon.json')

    # Count occurences in the column
    values_count_pd = pd.DataFrame.from_dict(explore.count_values(df, column_key),
                                             orient='index',
                                             columns=['Count']).reset_index(). \
        rename(index=str, columns={"index": "Country", "Count": "Count"})

    # Drop values that cannot be assigned to a geographic location
    values_count_pd = values_count_pd[values_count_pd.Country != "Unknown"]

    # Map country to cca3 code
    values_count_pd['cca3'] = values_count_pd.Country.apply(lambda l: search_cca3(l, countries_label))

    # Colour all countries based on their count
    worldmap = [dict(
        type='choropleth',
        locations=values_count_pd['cca3'],
        z=np.log10(values_count_pd['Count']),
        # name = values_count_pd['Country'],
        autocolorscale=False,
        reversescale=True,
        colorbar=dict(
            len=0.7,
            tick0=1,
            tickmode='array',
            tickvals=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
            ticktext=['1', '10<sup>1/2</sup>', '10<sup>1</sup>', '10<sup>3/2</sup>', '10<sup>2</sup>',
                      '10<sup>5/2</sup>', '10<sup>3</sup>', '10<sup>3/2</sup>', '10<sup>4</sup>'],
            title='Counts'),
        colorscale='Viridis',
        text=values_count_pd['Country'] + ' ' + values_count_pd['Count'].astype(str),
        hoverinfo='text'
    )]

    lines = []
    if show_distances:
        maximum = float(np.log10(values_count_pd['Count']).max())
        for i, row in values_count_pd.iterrows():
            try:
                origin_latlng = countries.loc[countries['cca3'] == 'FRA']['latlng'].iloc[0]
                country_latlng = countries.loc[countries['cca3'] == row['cca3']]['latlng'].values[0]
                lines.append(
                    dict(
                        type='scattergeo',
                        lon=[country_latlng[1], origin_latlng[1]],
                        lat=[country_latlng[0], origin_latlng[0]],
                        mode='lines+markers',
                        name='',
                        text=row['Country'] + '<br>' + '# products: ' + str(row['Count']),
                        hoverinfo='text',
                        line=dict(
                            width=(np.log10(row['Count']) + 0.1) * 1.2,
                            color='red'
                        ),
                        opacity=min(float(np.log10(row['Count'])) / maximum * 1.2 + 0.1, 1) # make larger for visibility
                    )
                )
            except IndexError:
                continue

    # Format map
    layout = dict(
        geo=dict(
            projection=dict(
                type='equirectangular'
            ),
            showframe=False,
            showcoastlines=True,
            showland=True,
            landcolor="rgb(229, 229, 229)",
            countrycolor="rgb(255, 255, 255)",
            coastlinecolor="rgb(255, 255, 255)",
        ),
        showlegend=False,
        xaxis=dict(fixedrange=True),
        yaxis=dict(fixedrange=True),
        margin=go.layout.Margin(
            l=50,
            r=100,
            b=0,
            t=0,
            pad=4
        )
    )

    figure = dict(data=worldmap + lines, layout=layout)

    # Plot interactive figure
    iplot(figure)

    # also save offline
    if save_offline:
        plot(figure, filename=plots_folder + "map_" + save_offline_title + ".html", auto_open=False)
    

def plot_cluster_by_tags(df,
                         df_colors,
                         plot2D_features=["carbon-footprint_100g", "energy_100g"],
                         marker_text_column="product_name",
                         cluster="labels",
                         save_offline=False,
                         save_offline_title='scatter_plot'):

    # Personalized axes titles
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
                'x': df[df[cluster] == label][plot2D_features[0]],
                'y': df[df[cluster] == label][plot2D_features[1]],
                'text': df[df[cluster] == label][marker_text_column],
                'name': label,
                'mode': 'markers',
                'marker': {'color':df_colors[df_colors.category == label]['color'].values[0]}
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
    if save_offline:
        second_plot_url = plot(figure, filename=plots_folder + save_offline_title + ".html", auto_open=False)
        
        
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

    
def plot_column_composition(df,df_colors, column_str, num_values=5,
                            save_offline=False,
                            save_offline_title='column_composition_bar_plot'):
    """
    Plot vertical, stacked bar-plot of occurrences.
    :param df:
    :df_colors: default colour to be assigned
    :param column_str:
    :param num_values: number of most common distinct values that should shown in bar plot
    :param save_offline:
    :param save_offline_title:
    """
    occurrence = explore.count_tag_occurrences(df, column_str)

    # the full dataframe
    counts_df = pd.DataFrame(data={'key': list(occurrence.keys()),
                                   'value': list(occurrence.values())
                                   },
                             ).sort_values('value', ascending=False)

    # Move 'Unknown' and 'Others' column to end of df
    for values_str in ['Unknown', 'Other']:
        index = list(np.where(counts_df.key == values_str)[0])
        if index:
            idx = counts_df.index.tolist()
            popped = idx.pop(index[0])
            counts_df = counts_df.reindex(idx + [popped])

    # accumulate small values into others
    new_row = pd.DataFrame(data={
        'key': ['Others'],
        'value': [counts_df['value'][num_values:].sum()]
    })

    # combining top features with others
    df2 = pd.concat([counts_df[:num_values].copy(), new_row])

    frames = []

    overall_count = 0
    
    # Load bar data
    traces = []

    for n, row in df2.iterrows():
        
        if(df_colors[df_colors.category == str(row[0])]['color'].empty):
                color = '#7192C5'
        else :
            color = df_colors[df_colors.category == str(row[0])]['color'].values[0]
            
        trace = go.Bar(y=[0],
                       x=[row.values[1]],
                       name=row.values[0],
                       orientation='h',
                       marker=dict(color=color,
                                  
                                   ),
                       )

        overall_count += row.values[1]
        traces.append(trace);

    # Bar plot animation not supported yet
    # frames.append({'traces':traces})

    # set x-axis labels and their corresponding data values
    frac = overall_count
    i = 0;
    while frac > 10:
        i = i + 1;
        frac = frac / 10
    tickvals = list(range(0, int(overall_count), 5 * int(10 ** (i - 1))))
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
            b=25,
            t=25,
            pad=4
        )
    )

    figure = go.Figure(data=traces, layout=layout, frames=frames)

    # Plot interactive figure
    iplot(figure)

    # also save offline
    if save_offline:
        plot(figure, filename=plots_folder + save_offline_title + ".html", auto_open=False)

    
def search_cca3(name, countries):
    """
    Map country name to CCA3 code.
    :param name:
    :param countries:
    :return:
    """
    country_set_name = countries[countries.name.apply(lambda x: x.lower() == name.lower())]
    if not country_set_name.empty:
        return country_set_name.iloc[0, 1]
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

    
def make_grade_stacked_bar(attempt, label_column, x_column, y_column, save_offline=False, save_offline_title='make_grade_stacked_bar'):

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
    if y_column == 'Count':
        axis_y = 'Count'
    
    if y_column == 'Percentage':
        axis_y = 'Percentage of products [%]'
    layout = go.Layout(
                    showlegend=True, 
                    barmode="stack",
                    yaxis=dict(
                        title=axis_y
                        ),
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
    if save_offline:
        plot(figure, filename= plots_folder + save_offline_title + ".html", auto_open=False) 

        
def plot_grade_content(nutrition_over_time):
    index_list = ['B', 'C', 'D', 'E']
    cat_list = ['Plant-based', 'Carbs', 'Meats', 'Dairies', 'Seafood', 'Beverages', 'Sugary snacks','Others']
    categories = {"keys": cat_list}
    check = pd.DataFrame.from_dict(categories)
    
    nutrional_products = nutrition_over_time[nutrition_over_time["nutrition_grade"] == 'A']              
    table_content = explore.find_composition_list(df=nutrional_products, column_str='main_category', cat_lis= cat_list)
    table_content['Percentage'] = table_content.value/table_content.value.sum()*100
    table_content = check.merge(table_content, how='outer', on= "keys").fillna(0)
    table_content['grade'] = 'A'
    
    for elem in index_list:
        nutrional_products = nutrition_over_time[nutrition_over_time["nutrition_grade"] == elem]
        add_content = explore.find_composition_list(df=nutrional_products, column_str='main_category', cat_lis= cat_list)
        add_content['Percentage'] = add_content.value/add_content.value.sum()*100
        add_content = check.merge(add_content, how='outer', on= "keys").fillna(0)
        add_content['grade'] = elem
        table_content = table_content.append(add_content, ignore_index=True)
    return table_content

def make_content_stacked_bar(table, df_colors,label_column, x_column, y_column, save_offline=False, save_offline_title='content_stacked_bar'):

    keys = table[label_column].drop_duplicates()
    data_stacked = []
  
    liste = ['A','B','C','D','E']
    for num, grade in enumerate(keys):
        values = list(table[table[label_column] == grade].loc[:, y_column])
        
        if(grade=='Others'):
            color = '#7979CD'
        else:
            color = df_colors[df_colors.category == grade]['color'].values[0]
            
        trace = go.Bar(
                x=liste,
                y=values,
                name=grade,
                marker = dict(color =color))

        layout = go.Layout(
            barmode='stack',
            margin=go.layout.Margin(
                l=50,
                r=50,
                b=40,
                t=15,
                pad=4
            )
        )
        data_stacked.append(trace)

    fig = go.Figure(data=data_stacked,layout=layout)
    iplot(fig, filename='stacked-bar')
    
    # also save offline
    if save_offline:
        plot(fig, filename= plots_folder + save_offline_title  + ".html", auto_open=False) 

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
        
def create_colorbar_df(food_facts_pd):
    #creation of a dataframe with the colors for coherence in the story telling
    
    df_colors=pd.DataFrame()
    main_cat_colors = ['#90CB70','#7979CD','#D6D0C3','#B69C63','#EC9BE2','#F3AC6D','#8CB5ED','#F0F472','#FCE2E4']
    
    manuf_colors = ['#5f568b','#b6ddf0','#68a99e','#568967','#baba70','#e5daa3','#8d496b','#8d496b','#8d496b','#8d496b']
    
    stores_colors = ['#5f568b','#b6ddf0','#68a99e','#568967','#baba70','#e5daa3','#8d496b','#457B8E','#457B8E','#457B8E','#457B8E','#AE7CBB']


    list_items = list(food_facts_pd.main_category.value_counts().index) + list(food_facts_pd.manufacturing_places.value_counts().index)[:10] +list(food_facts_pd.stores.value_counts().index)[:12]
    
    df_colors['category'] = list_items
    df_colors['color'] = main_cat_colors + manuf_colors + stores_colors
    
    return df_colors
