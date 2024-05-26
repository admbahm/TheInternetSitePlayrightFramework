from pages.base_page import BasePage
from playwright.sync_api import Page


class SecurePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.flash_message = page.locator("#flash")

    def get_flash_message(self) -> str:
        return self.flash_message.text_content()