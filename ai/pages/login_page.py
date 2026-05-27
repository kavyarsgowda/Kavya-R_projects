"""Login Page Object"""

from playwright.sync_api import Page
from ai.pages.base_page import BasePage


class LoginPage(BasePage):
    """Login modal for demoblaze.com"""
    
    # Selectors for login modal
    LOGIN_MODAL = "#logInModal"
    USERNAME_INPUT = "#loginusername"
    PASSWORD_INPUT = "#loginpassword"
    LOGIN_BUTTON = "button[onclick='logIn()']"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def wait_for_login_modal(self, timeout=5000):
        """Wait for login modal to appear"""
        self.page.wait_for_selector(self.LOGIN_MODAL, timeout=timeout, state="visible")
        print("✅ Login modal appeared")
    
    def enter_username(self, username):
        """Enter username in login form"""
        self.fill_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password in login form"""
        self.fill_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click on Login button in modal"""
        self.click_element(self.LOGIN_BUTTON)
        print("✅ Clicked Login button")
    
    def login(self, username, password):
        """Complete login flow"""
        print(f"\n--- Logging in with username: {username} ---")
        self.wait_for_login_modal()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait(2000)  # Wait for login to complete
        print("✅ Login process completed")

