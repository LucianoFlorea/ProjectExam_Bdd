from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page


class Inventory_page(Login_page):
    username = "standard_user"
    password = "secret_sauce"
    items = ["sauce-labs-bike-light", "sauce-labs-bolt-t-shirt", "sauce-labs-backpack", "sauce-labs-fleece-jacket",
             "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)"]

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