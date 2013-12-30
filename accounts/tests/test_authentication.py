from unittest.mock import patch
from django.test import TestCase

from accounts.authentication import (
    PERSONA_VERIFY_URL, DOMAIN, PersonaAuthenticationBackend
)

class AuthenticateTest(TestCase):

    @patch('accounts.authentication.requests.post')
    def test_sends_assertion_to_mozilla_with_domain(self, mock_post):
        backend = PersonaAuthenticationBackend()
        backend.authenticate('an assertion')
        mock_post.assert_called_once_with(
            PERSONA_VERIFY_URL,
            data={'assertion': 'an assertion', 'audience': DOMAIN}
        )


    @patch('accounts.authentication.requests.post')
    def test_returns_none_if_response_errors(self, mock_post):
        mock_post.return_value.ok = False
        backend = PersonaAuthenticationBackend()

        user = backend.authenticate('an assertion')
        self.assertIsNone(user)

