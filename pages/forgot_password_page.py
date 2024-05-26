from playwright.sync_api import Page


class ForgotPasswordPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.retrieve_button = page.locator("#form_submit")

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/forgot_password")

    def retrieve_password(self, email: str):
        self.email_input.fill(email)
        self.retrieve_button.click()

    def get_confirmation_message(self) -> str:
        return self.page.locator("#content").text_content()
