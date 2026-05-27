"""Home Page Object"""

from playwright.sync_api import Page
from ai.pages.base_page import BasePage


class HomePage(BasePage):
    """Home page for demoblaze.com"""
    
    # Selectors - using self-healing with multiple alternatives
    LOGIN_LINK = "a[data-target='#logInModal']"
    WELCOME_MESSAGE = "a#nameofuser"  # Shows "Welcome [username]"
    LOGOUT_LINK_PRIMARY = "a[onclick='logOut()']"
    LOGOUT_LINK_ALT = "#logout2"  # Alternative selector
    LOGOUT_LINK_ALT2 = "a:has-text('Log out')"  # Text-based selector

    def __init__(self, page: Page):
        super().__init__(page)
    
    def click_login_link(self):
        """Click on Login link in navigation"""
        self.click_element(self.LOGIN_LINK)
        print("✅ Clicked Login link")
    
    def verify_logout_visible(self):
        """Verify that Logout link is visible - with fallback selectors"""
        # Try primary selector first
        selectors = [
            self.LOGOUT_LINK_PRIMARY,
            self.LOGOUT_LINK_ALT,
            self.LOGOUT_LINK_ALT2
        ]
        
        for selector in selectors:
            try:
                visible = self.is_visible(selector)
                if visible:
                    print(f"✅ Logout link found with selector: {selector}")
                    return True
            except:
                continue
        
        # If no selector worked, wait longer and try again
        print("⏳ Logout link not found, waiting and retrying...")
        self.wait(3000)
        visible = self.is_visible(self.LOGOUT_LINK_PRIMARY)
        assert visible, "Logout link not visible!"
        print("✅ Logout link verified - user is logged in")
        return visible
    
    def verify_welcome_message(self, username):
        """Verify welcome message with username"""
        self.wait(1000)  # Wait for message to appear
        welcome_text = self.get_text(self.WELCOME_MESSAGE)
        assert username in welcome_text, f"Welcome message doesn't contain {username}!"
        print(f"✅ Welcome message verified: {welcome_text}")
        return welcome_text
    
    def click_logout(self):
        """Click on Logout link - with self-healing"""
        selectors = [
            self.LOGOUT_LINK_PRIMARY,
            self.LOGOUT_LINK_ALT,
            self.LOGOUT_LINK_ALT2
        ]

        for selector in selectors:
            try:
                if self.page.is_visible(selector):
                    self.click_element(selector)
                    print(f"✅ Clicked Logout with selector: {selector}")
                    return
            except:
                continue

        raise Exception("Could not find and click logout link!")

    def verify_login_visible(self):
        """Verify that Login link is visible again after logout"""
        self.wait(2000)  # Wait for page to update
        visible = self.is_visible(self.LOGIN_LINK)
        assert visible, "Login link not visible after logout!"
        print("✅ Login link verified - user logged out successfully")
        return visible

