from django.test import TestCase
from unittest.mock import patch, call


@patch('accounts.views.auth')
class LoginViewTest(TestCase):

    def test_redirects_to_home_page(self, mock_auth):
        response = self.client.post('/accounts/login', {'email': 'a@b.com'})
        self.assertRedirects(response, '/')


    def test_calls_authenticate_with_email(self, mock_auth):
        self.client.post('/accounts/login', {'email': 'a@b.com'})
        self.assertEqual(
            mock_auth.authenticate.call_args,
            call(email='a@b.com')
        )


    def test_calls_auth_login_with_user_if_there_is_one(self, mock_auth):
        response = self.client.post('/accounts/login', {'email': 'a@b.com'})
        self.assertEqual(
            mock_auth.login.call_args,
            call(response.wsgi_request, mock_auth.authenticate.return_value)
        )


    def test_does_not_login_if_user_is_not_authenticated(self, mock_auth):
        mock_auth.authenticate.return_value = None
        self.client.post('/accounts/login', {'email': 'a@b.com'})
        self.assertEqual(mock_auth.login.called, False)

