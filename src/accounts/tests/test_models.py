from django.test import TestCase

from accounts.models import User


class UserModelTest(TestCase):
    def test_user_is_valid_with_email_only(self):
        user = User(email="a@b.com")
        user.full_clean()  # should not raise
