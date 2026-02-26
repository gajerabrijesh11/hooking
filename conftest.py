import pytest
import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    print("\n Browser Launch Once (Session Start)")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        print("\n Browser Closing (Session End)")
        browser.close()

"""Using this pytest fixture function scope, when we run test fron test_function_scope.py, we can see new context will start for every test which is added
inside test file"""
@pytest.fixture(scope="function")
def page(browser):
    print("\n New Context Created")
    context = browser.new_context()
    page = context.new_page()
    yield page
    print("\n Context Closed")
    context.close()

""" If we remove this autouse hook and run then our test will fail because this hook will not redirect to site and not provide creads for login.
so, test fail """

"""@pytest.fixture(autouse=True)
def login(page):
    page.goto("https://www.saucedemo.com")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    yield
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link") """

""""Below fixture is without autouse. using this we can still make login, test and logout after every test but when we use this fixture
then we need to use def name in every test"""""

@pytest.fixture()
def login(page):
    page.goto("https://www.saucedemo.com")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    yield
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

@pytest.fixture(scope="class")
def auth_token():
    print("\n New Class Created")
    token = "my_generated_token"
    yield token
    print("Cleanup class auth token")



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")