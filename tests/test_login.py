import time


class TestLogin:
    def test_click_login_btn(self, open_login):
        open_login.click_login_btn()
