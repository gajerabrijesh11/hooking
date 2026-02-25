from .base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")