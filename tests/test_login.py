from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import USERNAME, PASSWORD


def test_valid_login(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.login(USERNAME, PASSWORD)

    dashboard.verify_dashboard_loaded()