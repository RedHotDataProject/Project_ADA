import pandas as pd


def extract_words(df, column_str='categories_en'):
    """
    Extract unique entries in the specified column of the data frame.
    :param df:
    :param column_str:
    :return:
    """
    list_words = set()
    for entry in df[column_str].astype('str'):
        if isinstance(entry, float): continue
        for word in entry.split(','):
            list_words.add(word)
    print("Nb of categories in '{}': {}".format(column_str, len(list_words)))
    return list(list_words)



def count_incomplete_columns(df, columns_list):
    """
    Count incomplete entries of listed columns in df.
    :param df:
    :param columns_list:
    :return: reduced df containing only complete columns
    """
    reduced = df.select(columns_list)
    
    complete = reduced.na.drop()

    percentage = (1 - complete.count()/ reduced.count())*100
    print("Percentage of incomplete entries: " + str(percentage))

    return complete


def count_tag_occurrences(df, column_str):
    """
    Count how often a tag occurs in a column.
    :param df:
    :param column_str:
    :return: dict: tag as keywords to occurrence count
    """
    count_keyword = dict()

    for index, col in df[column_str].iteritems():
        # Escape from NaN values
        if isinstance(col, float):
            continue

        for s in col.split(','):
            if s in count_keyword.keys():
                count_keyword[s] += 1
            else:
                count_keyword[s] = 1

    return count_keyword
    

def count_values(df, column_str):
    """
    Count occurrences for all distinctive values in a column.
    :param df:
    :param column_str:
    :return:
    """

    # Find all distinct values
    values_set = set()
    for index, row in df.iterrows():
        for value in row[column_str].split(","):
            values_set.add(value)

    # Count the number of time each value appears in the column
    values_count = {}
    for value in list(values_set):
        values_count[value] = df[column_str].str.contains(value).sum()
        
    return values_count


def filter_france(name):
    """
    Extract all rows that indicate the country France.
    :param name:
    :return: name of set {'', 'France'}
    """
    name = str(name)
    name = name.replace("'", "")
    list_name = name.strip("[]").split(", ")
    for name_part in list_name:
        if name_part == 'France':
            return 'France'
    return ''


def assign_score(nutrition_score):
    """
    Map nutrition score to corresponding grade
    :param nutrition_score
    :return: nutrition grade
    """
    value = int(nutrition_score[0])

    if nutrition_score[1] == "Beverages":
        # Beverage item grading
        if value <= 1:
            return 'B'
        if 2 <= value <= 5:
            return 'C'
        if 6 <= value <= 9:
            return 'D'
        if value >= 10:
            return 'E'
    else:
        # Food item grading
        if value <= -1:
            return 'A'
        if 0 <= value <= 2:
            return 'B'
        if 3 <= value <= 10:
            return 'C'
        if 11 <= value <= 18:
            return 'D'
        if value >= 19:
            return 'E'      
        
def count_nutrition_grade(food_facts_df):
    """
    Count grades based on year and grade.
    :param food_facts_df:
    :return: food_facts_df_counted
    """
    # Initialize year and count
    food_facts_df['Count'] = 1
    food_facts_df["year"] = food_facts_df["created_datetime"].dt.year

    # Group by year and grade
    nutrition_over_time_reduced = food_facts_df[['year', 'nutrition_grade', 'Count']]
    nutrition_over_time_reduced = nutrition_over_time_reduced.\
        groupby(['year', 'nutrition_grade']).\
        count().\
        reset_index()

    # Compute count percentages
    nutrition_over_time_reduced2 = nutrition_over_time_reduced[['year','nutrition_grade']]
    nutrition_over_time_reduced2['TotalPerYear'] = nutrition_over_time_reduced.Count
    nutrition_over_time_reduced2 = nutrition_over_time_reduced2.groupby('year').sum().reset_index()
    nutrition_over_time_reduced = pd.merge(nutrition_over_time_reduced, nutrition_over_time_reduced2, on=['year'])
    nutrition_over_time_reduced['Percentage'] = nutrition_over_time_reduced.Count\
                                                / nutrition_over_time_reduced.TotalPerYear * 100

    return nutrition_over_time_reduced.drop(columns = ['TotalPerYear'])


def proportion_palm_oil(food_facts_pd):
    #extracting products with palm oil 
    palm_oil_pd = food_facts_pd[food_facts_pd.ingredients_text.str.contains("palm").fillna(value=False)]
    palm_oil_over_time = palm_oil_pd['created_yyyy'].value_counts()
    food_facts_over_time = food_facts_pd['created_yyyy'].value_counts()
    proportions = palm_oil_over_time / food_facts_over_time *100
    return proportions,palm_oil_over_time

def find_composition_list(df, column_str, cat_lis):
    occurence = count_tag_occurrences(df, column_str)

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
