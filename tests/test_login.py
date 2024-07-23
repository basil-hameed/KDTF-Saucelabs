import pytest
from selenium import webdriver
from keywords.login_keywords import LoginKeywords
from keywords.dashboard_keywords import DashboardKeywords

class TestLogin:

    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.saucedemo.com/')
        yield
        self.driver.quit()

    
    def test_login(self, setup):
        LoginKeywords(self.driver).perform_login('standard_user', 'secret_sauce')
        assert DashboardKeywords(self.driver).verify_dashboard()

    def test_invalid_login(self, setup):
        LoginKeywords(self.driver).perform_login('standard_user', 'secret_password')
        assert LoginKeywords(self.driver).verify_login_error()