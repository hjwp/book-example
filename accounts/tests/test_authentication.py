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
