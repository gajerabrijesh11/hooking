def test_title_index(page):
    page.goto("https://www.saucedemo.com")
    assert "Swag" in page.title()

def test_url_nav(page):
    page.goto("https://www.saucedemo.com")
    assert "https://www.saucedemo.com/" in page.url

