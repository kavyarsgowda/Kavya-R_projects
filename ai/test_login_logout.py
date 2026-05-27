"""
Playwright Test: DemoBlaze Login/Logout
Build with Page Object Model (POM) design pattern

Test Scenario:
1. Open https://www.demoblaze.com/index.html
2. Click Login link
3. Enter username: pavanol
4. Enter password: test@123
5. Click Login button
6. Verify logout link visible
7. Verify "Welcome pavanol" message
8. Click logout
9. Verify login link visible again

Author: Kavya R
Date: 2026-05-03
"""

import pytest
from playwright.sync_api import Page
from ai.pages.home_page import HomePage
from ai.pages.login_page import LoginPage


class TestDemoBlazeLoginLogout:
    """Test suite for DemoBlaze login and logout functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup test - initialize page objects"""
        self.page = page
        self.home_page = HomePage(self.page)
        self.login_page = LoginPage(self.page)

    def test_login_logout_flow(self):
        """
        Complete test: Login and Logout flow with validations

        Steps:
        1. Navigate to DemoBlaze
        2. Click Login
        3. Enter credentials
        4. Verify login success
        5. Verify logout
        """

        print("\n" + "="*60)
        print("🚀 Starting DemoBlaze Login/Logout Test")
        print("="*60)

        # Step 1: Navigate to the application
        print("\n📍 STEP 1: Navigate to DemoBlaze")
        self.home_page.navigate()
        assert self.page.url == "https://www.demoblaze.com/index.html"
        print("✅ Successfully navigated to DemoBlaze")

        # Step 2: Click on Login link
        print("\n📍 STEP 2: Click on Login link")
        self.home_page.click_login_link()
        self.login_page.wait_for_login_modal()
        print("✅ Login modal is now open")

        # Step 3: Enter username
        print("\n📍 STEP 3: Enter username 'pavanol'")
        self.login_page.enter_username("pavanol")

        # Step 4: Enter password
        print("\n📍 STEP 4: Enter password 'test@123'")
        self.login_page.enter_password("test@123")

        # Step 5: Click Login button
        print("\n📍 STEP 5: Click Login button")
        self.login_page.click_login_button()

        # Step 6: Verify logout link is visible (indicates successful login)
        print("\n📍 STEP 6: Verify logout link is visible")
        self.home_page.verify_logout_visible()

        # Step 7: Verify welcome message
        print("\n📍 STEP 7: Verify 'Welcome pavanol' message")
        welcome_msg = self.home_page.verify_welcome_message("pavanol")
        assert "pavanol" in welcome_msg.lower()

        # Step 8: Click Logout link
        print("\n📍 STEP 8: Click Logout link")
        self.home_page.click_logout()

        # Step 9: Verify login link is visible again (indicates successful logout)
        print("\n📍 STEP 9: Verify Login link is visible again after logout")
        self.home_page.verify_login_visible()

        print("\n" + "="*60)
        print("✅✅✅ TEST PASSED: Complete Login/Logout Flow Successful")
        print("="*60 + "\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

