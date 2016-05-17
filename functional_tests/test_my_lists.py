from django.conf import settings
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session


class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_pre_authenticated_session(email)

        # to set a cookie we need to first visit the domain.
        # 404 pages load the quickest!
        self.browser.get(self.server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))


    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged-in user
        email = 'edith@example.com'
        self.create_pre_authenticated_session(email)

        # She goes to the home page and starts a list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('First list 1st item\n')
        self.get_item_input_box().send_keys('First list 2nd item\n')
        first_list_url = self.browser.current_url

        # She notices a "My lists" link, for the first time.
        self.browser.find_element_by_link_text('My lists').click()

        # When she clicks through to it, she sees the page's title
        # contains her email
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn(email, header.text)

        # She sees that her list is in there, named according to its
        # first list item
        self.browser.find_element_by_link_text('First list 1st item').click()

        # clicking on it takes her back to the first list page
        self.assertEqual(self.browser.current_url, first_list_url)


        # She decides to start another list, just to see
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Second list 1st item\n')
        second_list_url = self.browser.current_url

        # Under "my lists", her new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.browser.find_element_by_link_text('Second list 1st item').click()
        self.assertEqual(self.browser.current_url, second_list_url)

        # She logs out.  The "My lists" option disappears
        self.browser.find_element_by_id('id_logout').click()
        self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        )

