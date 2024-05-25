from playwright.sync_api import Page


class SecurePage:
    def __init__(self, page: Page):
        self.page = page
        self.flash_message = page.locator("#flash")

    def get_flash_message(self) -> str:
        return self.flash_message.text_content()