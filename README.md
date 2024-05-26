# The Internet Test Framework

This is a test framework for [The Internet](https://the-internet.herokuapp.com/) using Python, Playwright, Aqua IDE, and the Page Object Model (POM).

## Project Structure

```bash
├── pages/
│ ├── init.py
│ ├── base_page.py
│ ├── login_page.py
│ ├── secure_page.py
│ ├── checkboxes_page.py
│ ├── dropdown_page.py
│ ├── forgot_password_page.py
├── tests/
│ ├── init.py
│ ├── test_login.py
│ ├── test_checkboxes.py
│ ├── test_dropdown.py
│ ├── test_forgot_password.py
├── .github/
│ ├── workflows/
│ ├── main.yml
├── .gitignore
├── README.md
├── conftest.py
├── requirements.txt
├── run_tests.py
└── config.py
```
## Setup

1. Clone the repository and navigate into the project directory:

    ```bash
    git clone https://github.com/yourusername/the-internet-test-framework.git
    cd the-internet-test-framework
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Running Tests

To run the tests, use the following command:

```bash
python run_tests.py
```
This will execute all tests in the tests directory

An Extremely good tool for element definitions can be launched with:

`npx playwright codegen https://the-internet.herokuapp.com/checkboxes
`
Where the url is whatever page you're testing.

