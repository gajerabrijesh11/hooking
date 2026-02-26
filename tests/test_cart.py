from pages.inventory_page import InventoryPage

def test_add_to_cart(login, page):
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    assert "cart" in page.url