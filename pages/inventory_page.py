from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import Login_page


class Inventory_page(Login_page):
    username = "standard_user"
    password = "secret_sauce"
    items = ["sauce-labs-bike-light", "sauce-labs-bolt-t-shirt", "sauce-labs-backpack", "sauce-labs-fleece-jacket",
             "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)"]
    items2 = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
              "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    PRODUCT_NAMES_LOCATOR = (By.CLASS_NAME, 'inventory_item_name')
    PRODUCT_PRICES_LOCATOR = (By.CLASS_NAME, 'inventory_item_price')

    def login(self):
        self.open_login_page()
        self.insert_username(self.username)
        self.insert_password(self.password)
        self.click_login_btn()

    def getAddCartLocator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='add-to-cart-{item}']")

    def getRemoveLocator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='remove-{item}']")

    def press_add_cart_item(self, item):
        for i in self.items:
            if i == item:
                self.getAddCartLocator(i).click()

    def check_remove_button_is_present(self, item):
        for i in self.items:
            if i == item:
                assert EC.visibility_of_element_located(self.getRemoveLocator(i))

    # ------------------------------------------------------------------------------------

    def check_basket_page(self):
        basket_button_locator = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.chrome.find_element(*basket_button_locator).click()
        basket_url = "https://www.saucedemo.com/cart.html"
        assert self.chrome.current_url == basket_url, "Error: The current page is not the basket page"

    def check_item_in_basket(self, item):
        # item_locator = (By.XPATH, f"//div[@class='inventory_item_name' and text()='{item}']")
        # assert self.chrome.find_element(*item_locator).is_displayed(), f"error:'{item}' is not displayed in the basket."
        remove_btn_locator = (By.XPATH, f"//button[@id='remove-{item}']")
        assert self.chrome.find_element(*remove_btn_locator).is_displayed(), f"error:'{item}' is not displayed in the basket."


    def remove_item_from_cart(self, item):
        remove_btn_locator = (By.XPATH, f"//button[@id='remove-{item}']")
        self.chrome.find_element(*remove_btn_locator).click()

    def go_back_to_shopping_list(self):
        self.chrome.back()

    def check_add_to_cart_btn_present(self, item):
        add_to_cart_locator = (By.XPATH, f"//button[@id='add-to-cart-{item}']")
        assert self.chrome.find_element(*add_to_cart_locator).is_displayed(), f"error: Add cart btn isn't displayed for {item}"

#---------------------------------------------------------

    def check_inventory_page(self):
        # Wait for the inventory items to be visible on the page
        WebDriverWait(self.chrome, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def go_to_product_page(self, item2):
        product_link_locator = (By.XPATH, f"//div[normalize-space()='{item2}']")
        self.chrome.find_element(*product_link_locator).click()

    def get_product_price(self):
        product_price_locator = (By.CLASS_NAME,'inventory_details_price')
        product_price_element = self.chrome.find_element(*product_price_locator)
        return product_price_element.text

    def get_product_names_and_prices(self):
        product_names = self.driver.find_elements(*self.PRODUCT_NAMES_LOCATOR)
        product_prices = self.driver.find_elements(*self.PRODUCT_PRICES_LOCATOR)

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
