from selenium import webdriver
from bs4 import BeautifulSoup

import random

BASE_URL = "https://www.kaufland.de/suche.assortmentSearch.html?q="


class KauflandScraper:

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
        self.driver.get(BASE_URL + query)

        # Find object on search results page
        python_button = self.driver.find_element_by_css_selector(
            'div.t-search-result__list-item:nth-child(1) > div:nth-child(1) > a:nth-child(1)')  # First article in grid view
        try:
            python_button.click()  # click link
        except Exception:
            print(Exception.with_traceback)
            # Accept the cookies
            python_button = self.driver.find_element_by_css_selector(
            '.a-button--outlined > button:nth-child(1)')  # First article in grid view
            python_button.click()  # click link

            # Retry element
            python_button = self.driver.find_element_by_css_selector(
            'div.t-search-result__list-item:nth-child(1) > div:nth-child(1) > a:nth-child(1)')  # First article in grid view
            python_button.click()  # click link

        # Hand the page source to Beautiful Soup
        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        # Extract requested data
        product = {}
        product['store_name'] = ''.join(soup.select_one('.t-assortment-detail__title').text).strip()
        product['store_price'] = soup.select_one('.a-pricetag__price').text
        product['store_currency'] = 'EURO'
        product['store_quantity'] = ''.join(soup.select_one('.t-assortment-detail__basic-price').text).strip()
        product['store_categories'] = soup.select_one('.m-offer-categories__title').text.split()

        return product
