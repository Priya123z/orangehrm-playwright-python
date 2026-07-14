from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.csv_reader import csvReader
import pytest

users = csvReader.read_csv("test_data/valid_login.csv")

@pytest.mark.parametrize(
    "user",
    users,
    ids=[f"{user}['username']_{index}" for user,index in users]
)
def test_valid_login(page, user):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.login(
        user["username"],
        user["password"]
    )

    dashboard_page.verify_dashboard_loaded()
