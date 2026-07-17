from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.dashboard_heading = page.get_by_role(
            "heading",
            name="Dashboard"
        )

    def verify_dashboard_loaded(self):
        self.wait_for_visibility(
            self.dashboard_heading,
            "Dashboard Heading"
        )

    def get_dashboard_title(self):
        return self.get_text(
            self.dashboard_heading,
            "Dashboard Heading"
        )