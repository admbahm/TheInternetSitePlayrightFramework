import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from config import BASE_URL


@pytest.mark.parametrize("username, password, expected_message", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("invalid_user", "invalid_password", "Your username is invalid!")
])
def test_login(browser, username, password, expected_message):
    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)

    # Navigate to the login page
    login_page.goto(f"{BASE_URL}/login")

    # Perform login
    login_page.login(username, password)

    # Verify the expected message
    if username == "tomsmith":
        assert expected_message in secure_page.get_flash_message()
    else:
        assert expected_message in browser.locator("#flash").text_content()


def test_invalid_login(browser):
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.goto(f"{BASE_URL}/login")

    # Perform login with invalid credentials
    login_page.login("invalid_user", "invalid_password")

    # Verify unsuccessful login
    assert "Your username is invalid!" in browser.locator("#flash").text_content()