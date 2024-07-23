import time
from pages.login_page import LoginPage

class LoginKeywords:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def perform_login(self, username, password):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        time.sleep(5)

    def verify_login_error(self):
        return self.login_page.get_login_error
    
