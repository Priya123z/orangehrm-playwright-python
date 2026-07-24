from pathlib import Path

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest

from utils.test_data import TestData

filepath = Path(__file__).parent.parent.resolve()

@pytest.mark.parametrize(
    "user",
    TestData.load(
        filepath/"test_data"/"valid_login.csv",
        filters={
            "Execute": "Yes"
        },
        id_field="username"
    )
)
def test_valid_login(page, user):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login(
        user["username"],
        user["password"]
    )
    dashboard_page.verify_dashboard_loaded()
