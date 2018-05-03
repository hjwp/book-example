from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import NoAuthenticationBackend
User = get_user_model()


class AuthenticateTest(TestCase):

    def test_returns_new_user_with_email(self):
        email = 'edith@example.com'
        user = NoAuthenticationBackend().authenticate(email)
        new_user = User.objects.get(email=email)
        self.assertEqual(user, new_user)


    def test_returns_existing_user_with_email(self):
        email = 'edith@example.com'
        existing_user = User.objects.create(email=email)
        user = NoAuthenticationBackend().authenticate(email)
        self.assertEqual(user, existing_user)


class GetUserTest(TestCase):

    def test_gets_user_by_email(self):
        User.objects.create(email='another@example.com')
        desired_user = User.objects.create(email='edith@example.com')
        found_user = NoAuthenticationBackend().get_user(
            'edith@example.com'
        )
        self.assertEqual(found_user, desired_user)


    def test_returns_None_if_no_user_with_that_email(self):
        self.assertIsNone(
            NoAuthenticationBackend().get_user('edith@example.com')
        )

