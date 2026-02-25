This README for implementing hooks.
In this practice I implemented session, function and autouse hooks.
    - seesion hook use for open seesion for each run means when test start to run it will open chromium seesion for once and once all the test executed chromium session will down.
    - function hook use for open new context for each test means for every new test new incognito tab. So, test don't have any cookies, chache and ensure test isolation
    - autouse hook use for re-use repeatitive data like login creads.
For all above hooks are implemented in conftest.py.
then I created pages for all our tests.
then I created tests using pages.
then created vertual env for my testing using  python -m venv venv
then activated that env
then installed pytest-playwright and playwright using 
    -pip install pytest-playwright
    -playwright install
then run test using pytest or we can run using pytest .\tests\test_login.py if we want to run specifice test.

total 5 types of scope for pytest fixture:
    - function (default)
    - class
    - module
    - session
    - package

| Scope                  | How many time it will run        | When to use                 | Syntax Example                     |
| ---------------------- | -------------------------------- | --------------------------- | ---------------------------------- |
| **function (default)** | for every test                   |  if Isolation required      | `@pytest.fixture()`                |
| **class**              | Once for every class             | Class level setup           | `@pytest.fixture(scope="class")`   |
| **module**             | Once for every file              | Same file ma multiple tests | `@pytest.fixture(scope="module")`  |
| **package**            | Once for one package (folder)    | Large project structure     | `@pytest.fixture(scope="package")` |
| **session**            | Once for Full test run           | Browser launch, DB connect  | `@pytest.fixture(scope="session")` |
