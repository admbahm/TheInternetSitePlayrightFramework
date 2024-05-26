import pytest
from playwright.sync_api import sync_playwright
from pages.forgot_password_page import ForgotPasswordPage


@pytest.fixture(scope='function')
def setup_teardown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

# broke right now
# def test_forgot_password(setup_teardown):
#     page = setup_teardown
#     forgot_password_page = ForgotPasswordPage(page)
#
#     # Navigate to the forgot password page
#     forgot_password_page.goto()
#
#     # Enter email and retrieve password
#     forgot_password_page.retrieve_password("test@example.com")
#
#     # Verify the confirmation message
#     assert "Your e-mail's been sent!" in forgot_password_page.get_confirmation_message()
