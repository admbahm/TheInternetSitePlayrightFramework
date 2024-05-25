# The Internet Test Framework

This is a test framework for [The Internet](https://the-internet.herokuapp.com/) using Python, Playwright, Aqua IDE, and the Page Object Model (POM).

## Project Structure

```bash
├── pages/
│ ├── init.py
│ ├── login_page.py
│ ├── secure_page.py
├── tests/
│ ├── init.py
│ ├── test_login.py
├── .gitignore
├── README.md
├── requirements.txt
└── run_tests.py
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


