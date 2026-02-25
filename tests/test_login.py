def test_inventory_page_loaded(page, login):
    assert "inventory" in page.url