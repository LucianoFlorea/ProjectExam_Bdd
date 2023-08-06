from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    service = Service("C:\Program Files\Google\chromedriver")
    chrome = webdriver.Chrome(service=service)


    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.get("https://www.saucedemo.com/")

    def close(self):
        self.chrome.quit()


