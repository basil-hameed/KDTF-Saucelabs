from pages.dashboard_page import DashboardPage

class DashboardKeywords:
    def __init__(self, driver):
        self.driver = driver
        self.dasboard_page = DashboardPage(driver)

    def verify_dashboard(self):
        return self.dasboard_page.get_dashboard_header() == "Swag Labs"
    