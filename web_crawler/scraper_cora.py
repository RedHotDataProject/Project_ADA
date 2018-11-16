from selenium import webdriver
from bs4 import BeautifulSoup

import random

BASE_URL = "https://www.coradrive.fr/colmar/rechercher.html?searchquery="


class CoraScraper:

    def __init__(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(executable_path='/home/kingkolibri/Programs/geckodriver')
        self.driver.implicitly_wait(random.randint(1, 10))

    def search(self, query):
        """
        Navigates to article over search results page and extracts article name, price, quantity and category if available.
        :param query: string comprising search terms
        :return: dict of product properties on store website
        """
        self.driver.get(BASE_URL + query.replace(" ", "+"))

        # Find object on search results page
        python_button = self.driver.find_element_by_css_selector(
            '.row > div:nth-child(1)')  # First article in grid view
        python_button.click()  # click link

        # Hand the page source to Beautiful Soup
        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        # Extract requested data
        product = {}
        product['store_name'] = self.driver.current_url.split('/')[-1].split('.')[0]
        product['store_price'] = soup.select_one('.ok').text.split()[0:1]
        product['store_currency'] = 'EURO'
        product['store_quantity'] = ''.join(soup.select_one('.note').text).strip()
        product['store_categories'] = [i.text for i in soup.select_one('#title').findAll('span')[:-2]]

        return product
