from selenium import webdriver
from bs4 import BeautifulSoup

import random

BASE_URL = "https://www.coop.ch/de/einkaufen.search.html#query="


class CoopScraper:

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
        self.driver.get(BASE_URL + query + '/' + query)

        # Find object on search results page
        python_button = self.driver.find_element_by_css_selector(
            '.mui-list-products-wide > li:nth-child(1) > a:nth-child(1)')  # First article in grid view
        python_button.click()  # click link

        # Hand the page source to Beautiful Soup
        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        # Extract requested data
        product = {}
        product['store_name'] = ''.join(soup.select_one('.sidebar-product-name').text).strip()
        product['store_price'] = soup.select_one('.current-price').text
        product['store_currency'] = 'CHF'
        product['store_quantity'] = ''.join(soup.select_one('span.right').text).strip()
        product['store_categories'] = soup.select_one('#breadcrumb').text.split()

        return product
