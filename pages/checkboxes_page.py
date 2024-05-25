from playwright.sync_api import Page


class CheckboxesPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkbox1 = page.locator("input[type='checkbox']:nth-child(1)")
        self.checkbox2 = page.locator("input[type='checkbox']:nth-child(3)")

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def check_first_checkbox(self):
        if not self.checkbox1.is_checked():
            self.checkbox1.check()

    def uncheck_second_checkbox(self):
        if self.checkbox2.is_checked():
            self.checkbox2.uncheck()

    def is_first_checkbox_checked(self) -> bool:
        return self.checkbox1.is_checked()

    def is_second_checkbox_checked(self) -> bool:
        return self.checkbox2.is_checked()

