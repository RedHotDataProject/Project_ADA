import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

products = pd.read_pickle("./data/products_pd.pickle")

products['price_dollar'] = np.nan


url_to_scrape = "https://www.amazon.com/s/ref=nb_sb_ss_i_1_18?url=search-alias%3Damazonfresh&field-keywords=flat+leaf+parsley"
r = requests.get(url_to_scrape)

soup = BeautifulSoup(r.text)

print(soup.get('a-offscreen'))


