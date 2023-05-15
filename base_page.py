from browser import Browser


class BasePage(Browser):

    def __init__(self):
        pass

    def check_error_message(self, locator, expected_result, mesaj_fail):
        actual_result = self.chrome.find_element(*locator).text
        assert actual_result == expected_result, mesaj_fail

    def check_link(self, link, fail_message):
        actual_result = self.chrome.current_url
        assert actual_result == link, fail_message
