# PytestPython Test Automation Framework

A comprehensive **Pytest + Playwright** test automation framework using the **Page Object Model (POM)** design pattern for end-to-end testing of web applications.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Test Examples](#test-examples)
- [Page Objects](#page-objects)
- [API Utilities](#api-utilities)
- [Contributing](#contributing)

---

## 🎯 Project Overview

This framework automates end-to-end testing for an e-commerce web application. It combines:
- **Playwright** for cross-browser UI automation (Chrome, Firefox, WebKit)
- **Pytest** for test execution and reporting
- **API testing** with Playwright request context
- **Page Object Model** for maintainable test code

### Key Features

✅ Multi-browser support (Chrome, Firefox, WebKit)  
✅ Page Object Model architecture  
✅ API + UI hybrid testing  
✅ Parameterized test execution with multiple user credentials  
✅ HTML report generation  
✅ Parallel test execution with pytest-xdist  
✅ BDD support with pytest-bdd

---

## 🛠️ Tech Stack

- **Python 3.14+**
- **Pytest 9.0+** - Test framework
- **Playwright 1.60+** - Browser automation
- **pytest-html** - HTML report generation
- **pytest-xdist** - Parallel test execution
- **pytest-playwright** - Pytest + Playwright integration
- **pytest-bdd** - BDD testing support
- **requests** - HTTP client library

---

## 📦 Prerequisites

- **Python 3.14+** installed
- **pip** package manager
- **Windows/Mac/Linux** OS

---

## 🚀 Installation

### 1. Clone or Navigate to Project

```bash
cd "C:\Users\Kavya\PytestPython (1)"
```

### 2. Create Virtual Environment

```powershell
# For Windows PowerShell
py -3 -m venv .venv
```

### 3. Activate Virtual Environment

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat

# Mac/Linux
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```bash
python -m playwright install
```

Or install specific browser:
```bash
python -m playwright install chromium
```

---

## 📁 Project Structure

```
PytestPython/
├── playwright/
│   ├── conftest.py                    # Pytest fixtures & configuration
│   ├── data/
│   │   └── credentials.json           # Test user credentials
│   ├── pageObjects/                   # Page Object Model classes
│   │   ├── login.py                   # Login page object
│   │   ├── dashboard.py               # Dashboard page object
│   │   ├── orderDetails.py            # Order details page object
│   │   ├── ordersHistory.py           # Orders history page object
│   ├── utils/
│   │   ├── apiBaseFramework.py        # API utility functions
│   │  
│   ├── features/                      # BDD feature files
│   │   └── orderTransaction.feature   # Feature scenarios
│   ├── test_framework_web_api.py      # Main E2E test file
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

---

## ⚙️ Configuration

### credentials.json

Update user credentials in `playwright/data/credentials.json`:

```json
{
  "user_credentials": [
    {
      "userEmail": "your-email@example.com",
      "userPassword": "your-password"
    },
    {
      "userEmail": "another-email@example.com",
      "userPassword": "another-password"
    }
  ]
}
```

### conftest.py

Customize fixtures in `playwright/conftest.py`:

```python
@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    # ... browser setup logic
```

**Available Options:**
- `--browser_name`: Select browser (chrome, firefox, webkit) - Default: chrome
- `--url_name`: Application URL - Default: https://rahulshettyacademy.com/client

---

## 🧪 Running Tests

### Run All Tests

```bash
pytest -q
```

### Run Specific Test File

```bash
pytest playwright/test_framework_web_api.py -v
```

### Run Specific Test

```bash
pytest playwright/test_framework_web_api.py::test_e2e_web_api -v
```

### Run Tests with Specific Browser

```bash
pytest --browser_name firefox -q
```

### Run Tests with Multiple Browsers

```bash
pytest --browser_name chrome -q
pytest --browser_name firefox -q
```

### Run Tests with HTML Report

```bash
pytest --html=report.html -q
```

### Run Tests in Parallel (3 workers)

```bash
pytest -n 3 -q
```

### Run Tests with Tracing

```bash
pytest --tracing on -q
```

### Combined Command (as per original code comments)

```bash
pytest --browser_name chrome -m smoke -n 3 --tracing on --html=report.html -q
```

### Run Tests with Specific Marks

```bash
pytest -m smoke -q
```

### Run BDD Tests

```bash
pytest playwright/test_pytest-bddTest.py -q
```

---

## 🎬 Test Examples

### Example 1: E2E Web + API Test

```python
@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials):
    """
    End-to-end test that:
    1. Creates order via API
    2. Logs in via UI
    3. Verifies order in dashboard
    """
    
    # API: Create Order
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    
    # UI: Login
    userName = user_credentials["userEmail"]
    password = user_credentials["userPassword"]
    
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, password)
    
    # UI: Verify Order
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    ordersDetailsPage = orderHistoryPage.selectOrder(orderId)
    ordersDetailsPage.verifyOrderMessage()
```

---

## 📄 Page Objects

### LoginPage

```python
from pageObjects.login import LoginPage

login_page = LoginPage(page)
login_page.navigate()  # Navigate to login URL
dashboard = login_page.login(email, password)  # Perform login
```

### DashboardPage

```python
from pageObjects.dashboard import DashboardPage

dashboard = DashboardPage(page)
orders_page = dashboard.selectOrdersNavLink()  # Navigate to orders
```

### OrdersHistoryPage

```python
orders_page = OrdersHistoryPage(page)
order_detail = orders_page.selectOrder(order_id)  # Select specific order
```

### OrderDetailsPage

```python
order_detail = OrderDetailsPage(page)
order_detail.verifyOrderMessage()  # Verify order details
```

---

## 🔌 API Utilities

### APIUtils Class

```python
from utils.apiBaseFramework import APIUtils

api_utils = APIUtils()

# Get Authentication Token
token = api_utils.getToken(playwright, user_credentials)

# Create Order
order_id = api_utils.createOrder(playwright, user_credentials)
```

**Base URL:** `https://rahulshettyacademy.com`

**Endpoints:**
- `POST /api/ecom/auth/login` - User authentication
- `POST /api/ecom/order/create-order` - Create order

---

## 📊 Reports

### HTML Reports

After running tests with `--html` flag:

```bash
pytest --html=report.html -q
```

Open `report.html` in browser to view detailed test results.

### Console Output

```bash
# Quiet mode
pytest -q

# Verbose mode
pytest -v

# Show print statements
pytest -s
```

---

## 🐛 Debugging

### Enable Playwright Inspector

```bash
PWDEBUG=1 pytest test_file.py
```

### Take Screenshots

```python
browserInstance.screenshot(path="screenshot.png")
```

### Enable Trace

```bash
pytest --tracing on
```

Trace file will be saved and can be viewed with Playwright Trace Viewer.

---

## ✅ Troubleshooting

### Issue: FileNotFoundError for credentials.json

**Solution:** Ensure `playwright/data/credentials.json` exists with valid JSON content.

### Issue: Browser not launching

**Solution:** Reinstall Playwright browsers:
```bash
python -m playwright install
```

### Issue: Tests not collecting

**Solution:** Verify imports and pytest configuration:
```bash
pytest --collect-only
```

### Issue: Module not found errors

**Solution:** Ensure virtual environment is activated:
```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 📝 Best Practices

1. **Page Object Model**: Keep page locators in POM classes, not in tests
2. **Credentials**: Never hardcode credentials; use `credentials.json`
3. **Assertions**: Use explicit assertions; avoid implicit waits
4. **Fixtures**: Leverage pytest fixtures for setup/teardown
5. **Marks**: Use pytest marks for test categorization (smoke, regression, etc.)
6. **Reports**: Always generate HTML reports for CI/CD integration

---

## 🤝 Contributing

1. Create feature branches for new tests
2. Follow Page Object Model pattern
3. Add descriptive test names and docstrings
4. Update credentials.json for new test users
5. Run full test suite before committing:
   ```bash
   pytest -q
   ```

---

## 📚 Useful Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Python Docs](https://playwright.dev/python/)
- [Page Object Model Pattern](https://www.sauceLabs.com/resources/articles/page-object-model)

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review test logs and HTML reports
3. Enable trace mode for debugging

---

**Last Updated:** May 26, 2026  
**Python Version:** 3.14+  
**Playwright Version:** 1.60+

