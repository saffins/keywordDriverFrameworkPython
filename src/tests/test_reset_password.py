import unittest

from pages.reset_password import ResetPasswordPage


class TestResetPassword(unittest.TestCase):

    def test_reset_password(self):
        #enter any URL or emailid below as input to the test
        reset_page = ResetPasswordPage("https://create.kahoot.it/auth/login", "test@gmail.com")
        reset_page.reset_password()

