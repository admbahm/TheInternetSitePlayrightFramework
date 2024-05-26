import pytest
from playwright.sync_api import sync_playwright
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def browser():
    logger.info("Starting browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        logger.info("Closing browser")
        browser.close()


def pytest_configure(config):
    config.option.htmlpath = "report.html"
