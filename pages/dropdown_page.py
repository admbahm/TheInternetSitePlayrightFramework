from playwright.sync_api import Page


class DropdownPage:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown = page.locator("#dropdown")

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")

    def select_option(self, value: str):
        self.dropdown.select_option(value)

    def get_selected_option(self) -> str:
        return self.dropdown.input_value()