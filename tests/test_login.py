import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        secure_page = SecurePage(page)

        # Navigate to the login page
        login_page.goto()

        # Perform login
        login_page.login("tomsmith", "SuperSecretPassword!")

        # Verify successful login
        assert "You logged into a secure area!" in secure_page.get_flash_message()

        browser.close()
