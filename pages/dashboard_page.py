from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD = "h6"

    def verify_dashboard_loaded(self):
        return self.get_text(self.DASHBOARD)