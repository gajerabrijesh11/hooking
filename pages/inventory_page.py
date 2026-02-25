from .base_page import BasePage

class InventoryPage(BasePage):

    def add_first_item_to_cart(self):
        self.page.click("(//button[text()='Add to cart'])[1]")

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")