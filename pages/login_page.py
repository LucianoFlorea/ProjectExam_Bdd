from selenium.webdriver.common.by import By

import base_page


class Login_page(base_page.BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def open_login_page(self):
        self.chrome.get("https://www.saucedemo.com/")

    def insert_username(self, username):
        self.chrome.find_element(*self.USERNAME).send_keys(username)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def click_login_btn(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()

    def check_successful_login(self):
        self.check_link("https://www.saucedemo.com/inventory.html", "error: i was not logged in")

    def check_login_error_message(self, expected_result):
        error_message = "error: the failed login message is not displayed"
        self.check_error_message(self.ERROR_MSG, expected_result, error_message)




