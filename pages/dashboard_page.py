from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_TITLE = "h6"

    def get_dashboard_title(self):
        return self.get_text(self.DASHBOARD_TITLE)
    def verify_dashboard_loaded(self):
        return self.get_dashboard_title()== "Dashboard"
