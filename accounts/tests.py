"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from mock import patch
from django.test import TestCase

from accounts.models import ListUser

class SimpleTest(TestCase):

    @patch('accounts.authentication.PersonaAuthenticationBackend.authenticate')
    def test_login_view(self, mock_authenticate):
        user = ListUser.objects.create(email='a@b.com')
        mock_authenticate.return_value = user
        response = self.client.post('/accounts/login', data=dict(assertion='bla'))
        self.assertRedirects(response, '/')
        self.fail(self.client.session['_auth_user_id'])
        self.assertEqual(response.context['user'], user)

