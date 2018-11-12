import numpy as np
import pandas as pd

import findspark

findspark.init()

import pyspark.sql.functions as func


def count_not_null(c, nan_as_null=False):
    """Use conversion between boolean and integer
    - False -> 0
    - True ->  1
    """
    pred = func.col(c).isNotNull() & (~func.isnan(c) if nan_as_null else func.lit(True))
    return func.sum(pred.cast("integer")).alias(c)


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