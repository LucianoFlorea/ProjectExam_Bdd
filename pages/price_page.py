from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import Login_page
from pages.inventory_page import Inventory_page

class Price_page(BasePage):

    items2 = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
              "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    PRODUCT_NAMES_LOCATOR = (By.CLASS_NAME, 'inventory_item_name')
    PRODUCT_PRICES_LOCATOR = (By.CLASS_NAME, 'inventory_item_price')
    def check_inventory_page(self):
        # Wait for the inventory items to be visible on the page
        WebDriverWait(self.chrome, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )


    def go_to_product_page(self, item2):
        product_link_locator = (By.XPATH, f"//div[normalize-space()='{item2}']")
        self.chrome.find_element(*product_link_locator).click()


    def get_product_price(self):
        product_price_locator = (By.CLASS_NAME, 'inventory_details_price')
        product_price_element = self.chrome.find_element(*product_price_locator)
        return product_price_element.text


    def get_product_names_and_prices(self):
        product_names = self.chrome.find_elements(*self.PRODUCT_NAMES_LOCATOR)
        product_prices = self.chrome.find_elements(*self.PRODUCT_PRICES_LOCATOR)

        products = {}
        for name_element, price_element in zip(product_names, product_prices):
            product_name = name_element.text
            product_price = price_element.text
            products[product_name] = product_price

        return products


    def get_expected_price_by_product_name(self, product_name):
        # Define the expected prices based on the product name
        expected_prices = {
            'Sauce Labs Backpack': '$29.99',
            'Sauce Labs Bike Light': '$9.99',
            'Sauce Labs Bolt T-Shirt': '$15.99',
            'Sauce Labs Fleece Jacket': '$49.99',
            'Sauce Labs Onesie': '$7.99',
            'Test.allTheThings() T-Shirt (Red)': '$15.99',
            # Add other product names and their expected prices here
        }

        # Return the expected price for the given product name
        return expected_prices.get(product_name,
                                   'Unknown')  # Return 'Unknown' if the product name is not found in the dictionary


