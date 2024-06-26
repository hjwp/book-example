from django.contrib import auth
from django.test import TestCase

from accounts.models import Token, User


class UserModelTest(TestCase):
    def test_model_is_configured_for_django_auth(self):
        self.assertEqual(auth.get_user_model(), User)

    def test_user_is_valid_with_email_only(self):
        user = User(email="a@b.com")
        user.full_clean()  # should not raise

    def test_email_is_primary_key(self):
        user = User(email="a@b.com")
        self.assertEqual(user.pk, "a@b.com")


class TokenModelTest(TestCase):
    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email="a@b.com")
        token2 = Token.objects.create(email="a@b.com")
        self.assertNotEqual(token1.uid, token2.uid)
