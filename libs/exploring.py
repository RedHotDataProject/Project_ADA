import numpy as np
import pandas as pd


def extract_words(df, colonne = 'categories_en'):
    """
    Extract unique entries in the specified column of the data frame.
    :param df:
    :param colonne:
    :return:
    """
    list_words = set()
    for entry in df[colonne].astype('str'):
        if isinstance(entry, float): continue
        for word in entry.split(','):
            list_words.add(word)
    print("Nb of categories in '{}': {}".format(colonne, len(list_words)))
    return list(list_words)


def count_incomplete_columns(df, columns_list):
    """
    Count incomlete entries of listed columns in df.
    :param df:
    :param columns_list:
    :return: reduced dataframe containing only complete columns
    """
    reduced = df.select(columns_list)
    
    complete = reduced.na.drop()

    percentage = (1 - complete.count()/ reduced.count())*100
    print("Percentage of incomplete entries: " + str(percentage))

    return complete


def count_tag_occurences(df, column_name):
    count_keyword = dict()
    for index, col in df[column_name].iteritems():
        if isinstance(col, float): continue
        for s in col.split(','):
            if s in count_keyword.keys():
                count_keyword[s] += 1
            else:
                count_keyword[s] = 1

    return count_keyword
    
def count_tag_occurences_list(df, column_name):
    count_keyword = dict()
    for index, col in df[column_name].iteritems():
        if isinstance(col, float): continue
        for s in col:
            if s in count_keyword.keys():
                count_keyword[s] += 1
            else:
                count_keyword[s] = 1

    return count_keyword

def count_values(df, column_key):
    # Find all distinct countries
    values_set = set()
    for index, row in df.iterrows():
        for value in row[column_key].split(","):
            values_set.add(value)

    # Count the number of time each value appears in the column
    values_count = {}
    for value in list(values_set):
        values_count[value] = df[column_key].str.contains(value).sum()
        
    return values_count


def filter_france(name):
    res = []
    name = str(name)
    name = name.replace("'", "")
    list_name = name.strip("[]").split(", ")
    for name_part in list_name:
        if name_part == 'France':
            return 'France'
    return ''

def assign_score(entry):
    value = int(entry[0])

    if(entry[1] == "Beverages"): 
        if(value <= 1):
            return 'B'
        if(value >= 2  and value <=5):
            return 'C'
        if(value >= 6 and value <= 9):
            return 'D'
        if(value >= 10):
            return 'E'
    else:
        if(value <= -1):
            return 'A'
        if(value >= 0  and value <=2):
            return 'B'
        if(value >= 3  and value <=10):
            return 'C'
        if(value >= 11 and value <=18):
            return 'D'
        if(value >= 19):
            return 'E'     
        
def nutrition_grade(nutrition_over_time):
    nutrition_over_time['Count'] = 1
    nutrition_over_time["year"] = nutrition_over_time["created_datetime"].dt.year
    nutrition_over_time_reduced = nutrition_over_time[['year', 'nutrition_grade', 'Count']]
    nutrition_over_time_reduced = nutrition_over_time_reduced.groupby(['year', 'nutrition_grade']).count().reset_index()
    nutrition_over_time_reduced2 = nutrition_over_time_reduced[['year','nutrition_grade']]
    nutrition_over_time_reduced2['TotalPerYear'] = nutrition_over_time_reduced.Count
    nutrition_over_time_reduced2 = nutrition_over_time_reduced2.groupby('year').sum().reset_index()
    nutrition_over_time_reduced = pd.merge(nutrition_over_time_reduced, nutrition_over_time_reduced2, on=['year'])
    nutrition_over_time_reduced['Percentage'] = nutrition_over_time_reduced.Count / nutrition_over_time_reduced.TotalPerYear *100
    return nutrition_over_time_reduced.drop(columns = ['TotalPerYear'])


def proportion_palm_oil(food_facts_pd,palm_oil_pd):
    #extracting products with palm oil 
    palm_oil_over_time = palm_oil_pd['created_yyyy'].value_counts()
    food_facts_over_time = food_facts_pd['created_yyyy'].value_counts()
    proportions = palm_oil_over_time / food_facts_over_time *100
    return proportions,palm_oil_over_time
