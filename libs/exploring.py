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
    value = int(entry)

    if(0): 
        """ 
        #need to be adapted
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
        """
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
    