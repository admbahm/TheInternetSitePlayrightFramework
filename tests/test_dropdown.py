import pytest
from playwright.sync_api import sync_playwright
from pages.dropdown_page import DropdownPage


def test_dropdown_selection():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        dropdown_page = DropdownPage(page)

        # Navigate to the dropdown page
        dropdown_page.goto()

        # Select the first option (value="1")
        dropdown_page.select_option("1")
        assert dropdown_page.get_selected_option() == "1"

        # Select the second option (value="2")
        dropdown_page.select_option("2")
        assert dropdown_page.get_selected_option() == "2"

        browser.close()