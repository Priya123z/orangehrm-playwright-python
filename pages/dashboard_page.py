from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_TITLE = "h6"

    def get_dashboard_title(self):
        return self.get_text(self.DASHBOARD_TITLE)
    def verify_dashboard_loaded(self):
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()