from selenium import webdriver


class Browser:
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.get("https://www.saucedemo.com/")

    def close(self):
        self.chrome.quit()