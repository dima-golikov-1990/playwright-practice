from conftest import base_url
from playwright.sync_api import Page, expect

class TestHomePage:
    def test_qa_practice_logo_is_visible(self, page: Page):
        page.goto(base_url)

        expect(page.locator("//img[@class='logo_image']")).to_be_visible()

    def test_home_page_link_is_visible(self, page: Page):
        page.goto(base_url)

        expect(page.get_by_text("Homepage")).to_be_visible()

    def test_ui_element_list_is_visible(self, page: Page):
        page.goto(base_url)

        expect(page.get_by_text("Single UI Elements")).to_be_visible()
        page.get_by_text("Single UI Elements").click()

        expect(page.locator("//a[text()='Inputs']")).to_be_visible()
        expect(page.locator("//a[text()='Buttons']")).to_be_visible()
        expect(page.locator("//a[text()='Checkbox']")).to_be_visible()
        expect(page.locator("//a[text()='Select']")).to_be_visible()
        expect(page.locator("//a[text()='New tab']")).to_be_visible()
        expect(page.locator("//a[text()='Text area']").first).to_be_visible()
        expect(page.locator("//a[text()='Alerts']")).to_be_visible()
        expect(page.locator("//a[text()='Drag and Drop']")).to_be_visible()
        expect(page.locator("//a[text()='Iframes']")).to_be_visible()
        expect(page.locator("//a[text()='Pop-Up']")).to_be_visible()