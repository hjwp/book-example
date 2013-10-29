from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import TestCase
from unittest.mock import patch

User = get_user_model()

from accounts.views import login
from lists.models import List, Item


class LoginViewTest(TestCase):

    @patch('accounts.views.authenticate')
    def test_calls_authenticate_with_assertion_from_post(
        self, mock_authenticate
    ):
        mock_authenticate.return_value = None
        self.client.post('/accounts/login', {'assertion': 'assert this'})
        mock_authenticate.assert_called_once_with(assertion='assert this')


    @patch('accounts.views.authenticate')
    def test_returns_OK_when_user_found(
        self, mock_authenticate
    ):
        user = User.objects.create(email='a@b.com')
        user.backend = '' # required for auth_login to work
        mock_authenticate.return_value = user
        response = self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertEqual(response.content.decode(), 'OK')


    @patch('accounts.views.auth_login')
    @patch('accounts.views.authenticate')
    def test_calls_auth_login_if_authenticate_returns_a_user(
        self, mock_authenticate, mock_auth_login
    ):
        request = HttpRequest()
        request.POST['assertion'] = 'asserted'
        mock_user = mock_authenticate.return_value
        login(request)
        mock_auth_login.assert_called_once_with(request, mock_user)


    @patch('accounts.views.auth_login')
    @patch('accounts.views.authenticate')
    def test_does_not_call_auth_login_if_authenticate_returns_None(
        self, mock_authenticate, mock_auth_login
    ):
        request = HttpRequest()
        request.POST['assertion'] = 'asserted'
        mock_authenticate.return_value = None
        login(request)
        self.assertFalse(mock_auth_login.called)


class MyListsViewTest(TestCase):

    def test_uses_my_lists_template(self):
        user = User.objects.create(email='list@user.com')
        response = self.client.get('/accounts/list@user.com/')
        self.assertTemplateUsed(response, 'my_lists.html')


    def test_passes_user_in_context(self):
        wrong_user = User.objects.create(email='not@me.com')
        user = User.objects.create(email='list@user.com')
        response = self.client.get('/accounts/list@user.com/')
        self.assertEqual(response.context['owner'], user)


    def test_template_displays_lists_using_first_item_text(self):
        user = User.objects.create(email='list@user.com')
        list1 = List.objects.create(owner=user)
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='i2')
        list2 = List.objects.create(owner=user)
        item3 = Item.objects.create(list=list2, text='i3')
        item4 = Item.objects.create(list=list2, text='i4')

        response = self.client.get('/accounts/list@user.com/')
        self.assertContains(response, 'i1')
        self.assertContains(response, 'i3')
