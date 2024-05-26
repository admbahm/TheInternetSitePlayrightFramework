import pytest
from playwright.sync_api import sync_playwright
from pages.checkboxes_page import CheckboxesPage


def test_checkboxes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        checkboxes_page = CheckboxesPage(page)

        # Navigate to the checkboxes page
        checkboxes_page.goto()

        # Ensure the first checkbox is checked
        checkboxes_page.check_first_checkbox()
        assert checkboxes_page.is_first_checkbox_checked() == True

        # Ensure the second checkbox is unchecked
        checkboxes_page.uncheck_second_checkbox()
        assert checkboxes_page.is_second_checkbox_checked() == False

        browser.close()

