from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.CLASS_NAME, 'app_logo')

    def get_dashboard_header(self):
        return self.driver.find_element(*self.dashboard_header).text
    
