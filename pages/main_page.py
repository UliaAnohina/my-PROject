from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url="http://selenium1py.pythonanywhere.com/"):
        self.browser.get(url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()