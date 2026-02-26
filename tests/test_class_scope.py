class TestAuth:
    def test_token_1(self, auth_token):
        assert auth_token.startswith("my_")

    def test_token_2(self, auth_token):
        assert "token" in auth_token