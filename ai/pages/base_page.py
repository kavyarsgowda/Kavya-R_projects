"""Base Page Object - Contains common methods for all pages"""

from playwright.sync_api import Page, expect
import time


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.demoblaze.com/index.html"
    
    def navigate(self):
        """Navigate to base URL"""
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        print(f"✅ Navigated to {self.base_url}")
    
    def wait_for_element(self, selector, timeout=5000):
        """Wait for element with multiple fallback selectors"""
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            print(f"✅ Element found: {selector}")
            return True
        except:
            print(f"⚠️ Element not found: {selector}")
            return False
    
    def click_element(self, selector):
        """Click on element"""
        self.page.click(selector)
        print(f"✅ Clicked: {selector}")
    
    def fill_text(self, selector, text):
        """Fill text in input field"""
        self.page.fill(selector, text)
        print(f"✅ Filled text in {selector}: {text}")
    
    def get_text(self, selector):
        """Get text content of element"""
        text = self.page.text_content(selector)
        print(f"✅ Text content: {text}")
        return text
    
    def is_visible(self, selector):
        """Check if element is visible"""
        visible = self.page.is_visible(selector)
        print(f"{'✅' if visible else '❌'} Element visible: {selector} = {visible}")
        return visible
    
    def wait(self, milliseconds):
        """Wait for specified milliseconds"""
        self.page.wait_for_timeout(milliseconds)

