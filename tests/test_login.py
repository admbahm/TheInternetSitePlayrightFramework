import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


# def test_valid_login():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         login_page = LoginPage(page)
#         secure_page = SecurePage(page)
#
#         # Navigate to the login page
#         login_page.goto()
#
#         # Perform login
#         login_page.login("tomsmith", "SuperSecretPassword!")
#
#         # Verify successful login
#         assert "You logged into a secure area!" in secure_page.get_flash_message()
#
#         browser.close()

def test_valid_login(setup_teardown):
    # Use the setup_teardown fixture to get a Playwright page object
    page = setup_teardown

    # Create an instance of the LoginPage page object
    login_page = LoginPage(page)

    # Create an instance of the SecurePage page object
    secure_page = SecurePage(page)

    # Navigate to the login page
    login_page.goto()

    # Perform login with valid credentials
    login_page.login("tomsmith", "SuperSecretPassword!")

    # Verify that the login was successful by checking the flash message
    assert "You logged into a secure area!" in secure_page.get_flash_message()


# Define a test function for an invalid login scenario
def test_invalid_login(setup_teardown):
    # Use the setup_teardown fixture to get a Playwright page object
    page = setup_teardown

    # Create an instance of the LoginPage page object
    login_page = LoginPage(page)

    # Navigate to the login page
    login_page.goto()

    # Perform login with invalid credentials
    login_page.login("invalid_user", "invalid_password")

    # Verify that the login was unsuccessful by checking the flash message
    assert "Your username is invalid!" in page.locator("#flash").text_content()