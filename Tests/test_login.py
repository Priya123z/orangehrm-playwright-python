from Pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


def test_valid_login(page):

    login = LoginPage(page)

    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/dashboard/index")

    assert "dashboard" in page.url.lower()