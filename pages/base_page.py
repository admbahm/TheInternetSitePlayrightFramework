from playwright.sync_api import Page, TimeoutError


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        try:
            self.page.goto(url)
        except TimeoutError:
            raise Exception(f"Failed to load URL: {url}")
