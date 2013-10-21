import json
from unittest.mock import Mock, patch
from django.test import TestCase

from accounts.authentication import (
    PERSONA_VERIFY_URL, DOMAIN,
    PersonaAuthenticationBackend, User
)

mock_post = Mock()
@patch('accounts.authentication.requests.post', mock_post)
class AuthenticateTest(TestCase):

    def setUp(self):
        self.backend = PersonaAuthenticationBackend()
        self.mock_response = mock_post.return_value
        self.mock_response.ok = True
        self.mock_response.json.return_value = {
            'status': 'okay', 'email': 'a@b.com'
        }


    def tearDown(self):
        mock_post.reset_mock()


    def test_sends_assertion_to_mozilla_with_domain(self):
        self.backend.authenticate('an assertion')
        mock_post.assert_called_once_with(
            PERSONA_VERIFY_URL,
            data={'assertion': 'an assertion', 'audience': DOMAIN}
        )


    def test_return_none_if_response_errors(self):
        self.mock_response.ok = False
        user = self.backend.authenticate('an assertion')
        self.assertIsNone(user)


    def test_returns_none_if_status_not_okay(self):
        self.mock_response.json.return_value = {'status': 'not okay!'}
        user = self.backend.authenticate('an assertion')
        self.assertIsNone(user)


    def test_calls_get_user_with_email(self):
        self.backend.get_user = Mock()
        self.backend.authenticate('an assertion')
        self.backend.get_user.assert_called_once_with('a@b.com')


    def test_finds_existing_user_with_email(self):
        self.backend.get_user = Mock()
        mock_user = self.backend.get_user.return_value
        user = self.backend.authenticate('an assertion')
        self.assertEqual(user, mock_user)


    def test_creates_new_user_if_required(self):
        def raise_no_user_error(_):
            raise User.DoesNotExist()
        self.backend.get_user = raise_no_user_error
        user = self.backend.authenticate('an assertion')
        new_user = User.objects.all()[0]
        self.assertEqual(user, new_user)
        self.assertEqual(user.email, 'a@b.com')


    @patch('accounts.authentication.PersonaAuthenticationBackend.authenticate')
    def test_is_activated_in_settings(self, mock_our_authenticate):
        from django.contrib.auth import authenticate
        authenticate(email='foo')
        mock_our_authenticate.assert_called_once_with(email='foo')


class GetUserTest(TestCase):

    def test_get_user_gets_user_from_database(self):
        actual_user = User.objects.create(email='a@b.com')
        backend = PersonaAuthenticationBackend()
        found_user = backend.get_user('a@b.com')
        self.assertEqual(found_user, actual_user)


    def test_raises_if_no_user(self):
        backend = PersonaAuthenticationBackend()
        with self.assertRaises(User.DoesNotExist):
            backend.get_user('nosuch@email.com')

