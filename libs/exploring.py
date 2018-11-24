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
