import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import json

import web_crawler.scraper_amazon as amazon
import web_crawler.scraper_walmart as walmart

step_size = 10

#with open('/libs/data.json') as f:
#    json_data = json.load(f)

products = pd.read_pickle("./data/products_pd.pickle")

products['price_dollar'] = np.nan

i=0

AsinList = []

for n, column in enumerate(products.iloc[i:i+step_size].iterrows()):
    keywords = " nestle Aguitas Manzana" #products.iloc[i+n].product_name
    dict_list = walmart.search(keywords=keywords)
    print(dict_list)

# json_data.update(extracted_data)

i = i+step_size

# Append to json file
f = open('data.json', 'w')
json.dump(dict_list, f, indent=4)




