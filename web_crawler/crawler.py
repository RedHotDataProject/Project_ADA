import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

from web_crawler.scraper import *

step_size = 10

#with open('/libs/data.json') as f:
#    json_data = json.load(f)

products = pd.read_pickle("./data/products_pd.pickle")

products['price_dollar'] = np.nan

i=0
while i < products.shape[0]-step_size-1:
    AsinList = []

    for n, column in enumerate(products.loc[i:i+step_size].iterrows()):
        query = products.loc[i+n].product_name.replace(' ', '+')
        AsinList.append(query)


    extracted_data = ReadAsin(AsinList)
    # json_data.update(extracted_data)

    i = i+step_size

    # Append to json file
    f = open('data.json', 'w')
    json.dump(extracted_data, f, indent=4)




