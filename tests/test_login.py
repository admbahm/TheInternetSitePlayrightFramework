import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from config import BASE_URL


def test_valid_login(browser):
    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)

    # Navigate to the login page
    login_page.goto(f"{BASE_URL}/login")

    # Perform login
    login_page.login("tomsmith", "SuperSecretPassword!")

    # Verify successful login
    assert "You logged into a secure area!" in secure_page.get_flash_message()


def test_invalid_login(browser):
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.goto(f"{BASE_URL}/login")

    # Perform login with invalid credentials
    login_page.login("invalid_user", "invalid_password")

    # Verify unsuccessful login
    assert "Your username is invalid!" in browser.locator("#flash").text_content()