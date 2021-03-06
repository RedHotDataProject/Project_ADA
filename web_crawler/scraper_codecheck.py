from selenium import webdriver
from bs4 import BeautifulSoup
import random
import requests

BASE_URL = "https://www.codecheck.info/product.search?q="

class CodecheckScrapper:
    def __init__(self):
        # create a new Fiefox  session
        self.driver = webdriver.Firefox(executable_path='/Users/ninatubau/Desktop/geckodriver')
        self.driver.implicitly_wait(random.randint(1, 10))
    
    def search(query):
        """
        Navigates to article over search results page and extracts category if available.
        :param query: string comprising search terms
        :return: dict of product categorie 
        """
        r = requests.get(BASE_URL + str(query))
        page_body = r.text
        # Hand the page source to Beautiful Soup

        soup = BeautifulSoup(page_body, 'html.parser')
        
        product_item = soup.select('div.product-info-item')
        if(len(product_item)==0):
            product_item = soup.select('div.cat')
        #get the cateegory
        product_item = product_item[0]
        category = str(product_item.find_all('a'))
        category = category[category.find(">")+1:-5]
        
        url = str(soup.findAll('meta',property="og:url"))
        url_splitted = url.split('/')
        print(url)
        #parent_category = url_splitted[4]
        if(len(url)>20):
            parent_category = url_splitted[4]
        else:
            parent_category = None

          
        return category, parent_category
