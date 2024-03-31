from conftest import base_url
from playwright.sync_api import Page, expect

class TestHomePage:
    def test_qa_practice_logo_is_visible(self, page: Page):
        page.goto(base_url)

        expect(page.locator("xpath=//img[@class='logo_image']")).to_be_visible()