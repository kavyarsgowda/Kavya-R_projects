"""Pytest configuration for AI tests"""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    """Fixture to provide Playwright page object"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headed mode - browser visible
        page = browser.new_page()
        yield page
        browser.close()

