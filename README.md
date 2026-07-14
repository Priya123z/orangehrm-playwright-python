# OrangeHRM Playwright Python Automation Framework

## Overview

This project is a UI automation framework built using:

- Playwright (Python)
- Pytest
- Page Object Model (POM)
- Python Dotenv
- Loguru (Coming Soon)
- Allure Reports (Coming Soon)
- GitHub Actions (Coming Soon)

## Project Structure

```
orangehrm-playwright-python/
│
├── pages/
├── tests/
├── utils/
├── reports/
├── screenshots/
├── logs/
├── test_data/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repository-url>
cd orangehrm-playwright-python

python -m venv .venv

source .venv/bin/activate        # Linux/macOS
# OR
.venv\Scripts\activate           # Windows

pip install -r requirements.txt
playwright install
```

## Execute Tests

```bash
pytest
```

## Current Features

- ✅ Framework Setup
- ✅ Environment Configuration
- ✅ Page Object Model
- ✅ Login Automation
- ⏳ Dashboard Automation
- ⏳ Allure Reports
- ⏳ CI/CD Pipeline