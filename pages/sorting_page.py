from selenium.webdriver.common.by import By
from base_page import BasePage
from decimal import Decimal
from selenium.webdriver.common.keys import Keys
from time import sleep


class Sorting_page(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    DROPDOWN_AZ_OPTION = (By.CSS_SELECTOR, "option[value='az']")
    DROPDOWN_ZA_OPTION = (By.CSS_SELECTOR, "option[value='za']")
    DROPDOWN_LO_HI_OPTION = (By.CSS_SELECTOR, "option[value='lohi']")
    DROPDOWN_HI_LO_OPTION = (By.CSS_SELECTOR, "option[value='hilo']")

    def sort_a_to_z(self):
        self.chrome.find_element(*self.SORT_DROPDOWN).click()
        self.chrome.find_element(*self.DROPDOWN_AZ_OPTION).click()

    def sort_z_to_a(self):
        self.chrome.find_element(*self.SORT_DROPDOWN).click()
        self.chrome.find_element(*self.DROPDOWN_ZA_OPTION).click()

    def sort_lo_to_hi(self):
        self.chrome.find_element(*self.SORT_DROPDOWN).click()
        self.chrome.find_element(*self.DROPDOWN_LO_HI_OPTION).click()

    def sort_hi_to_low(self):
        self.chrome.find_element(*self.SORT_DROPDOWN).click()
        self.chrome.find_element(*self.DROPDOWN_HI_LO_OPTION).click()

    def products_by_price(self, item_index=1):
        return self.chrome.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div["+ str(item_index) +"]/div[3]/div[1]")

    def verify_first_price_higher_than_second_price(self):
        first_price = Decimal(self.products_by_price(1).text[1:])
        second_price = Decimal(self.products_by_price(2).text[1:])
        assert first_price >= second_price, "Error: first price is not higher than second"

    def verify_first_price_lower_than_second_price(self):
        first_price = Decimal(self.products_by_price(1).text[1:])
        second_price = Decimal(self.products_by_price(2).text[1:])
        assert first_price <= second_price, "Error: first price is not lower than second"

    def products_by_name(self, item_index=1):
        return self.chrome.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div["+ str(item_index) +"]/div[2]/a[1]/div[1]")

    def verify_products_in_alphabetical_order(self):
        products_list = []
        first_product = self.products_by_name(1).text
        second_product = self.products_by_name(2).text
        products_list.append(first_product)
        products_list.append(second_product)
        products_list.sort()
        assert first_product == products_list[0], "Error: products are not alphabetical"
        assert second_product == products_list[1], "Error: products are not alphabetical"

    def verify_products_in_reverse_alphabetical_order(self):
        products_list = []
        first_product = self.products_by_name(1).text
        second_product = self.products_by_name(2).text
        products_list.append(first_product)
        products_list.append(second_product)
        products_list.sort()
        products_list.reverse()
        assert first_product == products_list[0], "Error: products are not reverse alphabetical"
        assert second_product == products_list[1], "Error: products are not reverse alphabetical"

