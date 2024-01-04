import unittest

from pages.reset_password import ResetPasswordPage


class TestResetPassword(unittest.TestCase):

    def test_reset_password(self):
        reset_page = ResetPasswordPage("https://create.kahoot.it/auth/login", "test@gmail.com")
        reset_page.reset_password()

if __name__ == "__main__":
    reset_page = ResetPasswordPage("https://google.com", "test@gmail.com")
    reset_page.reset_password()