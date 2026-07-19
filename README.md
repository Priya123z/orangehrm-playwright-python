# Playwright Python Automation Framework

A scalable, production-style UI automation framework built using **Playwright**, **Pytest**, and **Python** following software engineering best practices such as the **Page Object Model (POM)**, **Singleton Design Pattern**, **Factory Pattern**, and **Single Responsibility Principle (SRP)**.

The framework is designed to be maintainable, reusable, and easily extensible for enterprise-scale automation projects.

---

# Tech Stack

* Python 3.x
* Playwright
* Pytest
* Page Object Model (POM)
* Loguru
* python-dotenv
* pathlib
* JSON
* Git

---

# Framework Features

* Cross-browser execution (Chromium, Firefox, WebKit)
* Multi-environment configuration support
* Singleton-based Configuration Manager
* Browser Factory Pattern
* Environment-based configuration loading
* Authentication State Management
* Credential Management
* Artifact Management
* Automatic Screenshot Capture on Failure
* Playwright Tracing
* Video Recording
* Structured Logging
* Page Object Model
* BasePage abstraction
* Utility classes for reusable functionality
* Session-based authentication using Playwright Storage State

---

# Project Structure

```text
project/
│
├── auth/
│   ├── qa/
│   ├── uat/
│   └── prod/
│
├── config/
│   ├── qa.env
│   ├── uat.env
│   ├── prod.env
│   └── credentials.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/
│
├── utils/
│   ├── artifact_manager.py
│   ├── authentication_manager.py
│   ├── browser_factory.py
│   ├── config_manager.py
│   ├── credentials_manager.py
│   ├── file_utils.py
│   ├── logger.py
│   └── screenshot.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Framework Architecture

```text
Pytest
    │
    ▼
Fixtures (conftest.py)
    │
    ▼
BrowserFactory
    │
    ▼
Playwright Browser
    │
    ▼
Browser Context
    │
    ▼
Page
    │
    ▼
Page Objects
    │
    ▼
Business Methods
```

Supporting managers:

```text
ConfigManager
        │
        ▼
Environment Configuration

CredentialManager
        │
        ▼
Test Credentials

AuthManager
        │
        ▼
Playwright Storage State

ArtifactManager
        │
        ▼
Screenshots
Videos
Traces
```

---

# Authentication Flow

The framework supports Playwright Storage State Authentication.

```text
Test Starts
      │
      ▼
Storage State Exists?
      │
 ┌────┴─────┐
 │          │
Yes         No
 │          │
 │      Launch Temporary Browser
 │          │
 │      Perform Login
 │          │
 │      Save Storage State
 │          │
 └──────┬───┘
        │
Create Authenticated Context
        │
Create Page
        │
Execute Test
```

This significantly reduces execution time by avoiding repeated logins for business-flow tests.

---

# Environment Management

Environment-specific configuration is managed using dedicated `.env` files.

Example:

```text
config/
    qa.env
    uat.env
    prod.env
```

The framework loads the appropriate configuration at runtime using the `ConfigManager`.

---

# Credential Management

User credentials are maintained separately from the framework logic.

```text
credentials.json
```

The `CredentialManager`:

* Loads credentials once
* Caches them in memory
* Returns immutable credential objects
* Supports role-based authentication

---

# Artifact Management

The framework automatically generates:

* Screenshots on test failure
* Playwright trace files
* Video recordings
* Structured logs

Artifacts are organized for easier debugging and CI/CD reporting.

---

# Design Patterns Used

* Singleton Pattern
* Factory Pattern
* Page Object Model (POM)
* Single Responsibility Principle (SRP)
* Dependency Injection using Pytest Fixtures

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Install Playwright browsers.

```bash
playwright install
```

Playwright recommends installing the required browser binaries after installing the Python package.

---

# Running Tests

Run the complete suite.

```bash
pytest
```

Run a specific browser.

```bash
pytest --browser=chromium
```

```bash
pytest --browser=firefox
```

```bash
pytest --browser=webkit
```

Run a specific test.

```bash
pytest tests/test_login.py
```

Run a single test method.

```bash
pytest tests/test_login.py::test_valid_login
```

---

# Current Capabilities

* UI Automation
* Cross Browser Testing
* Authentication State Management
* Environment Management
* Automatic Failure Screenshots
* Playwright Trace Collection
* Video Recording
* Modular Framework Architecture

---

# Planned Enhancements

* Marker-based authentication
* Parallel execution with pytest-xdist
* API testing integration
* Retry mechanism
* Allure reporting
* GitHub Actions CI/CD
* Docker support
* Database validation utilities
* Data-driven testing utilities

---

# Version

Current Version: **v1.0**
