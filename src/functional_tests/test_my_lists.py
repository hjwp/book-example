from django.conf import settings
from selenium.webdriver.common.by import By

from .base import FunctionalTest
from .management.commands.create_session import create_pre_authenticated_session
from .server_tools import create_session_on_server


class MyListsTest(FunctionalTest):
    def create_pre_authenticated_session(self, email):
        if self.test_server:
            session_key = create_session_on_server(self.test_server, email)
        else:
            session_key = create_pre_authenticated_session(email)

        ## to set a cookie we need to first visit the domain.
        ## 404 pages load the quickest!
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(
            dict(
                name=settings.SESSION_COOKIE_NAME,
                value=session_key,
                path="/",
            )
        )

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged-in user
        self.create_pre_authenticated_session("edith@example.com")

        # She goes to the home page and starts a list
        self.browser.get(self.live_server_url)
        self.add_list_item("Reticulate splines")
        self.add_list_item("Immanentize eschaton")
        first_list_url = self.browser.current_url

        # She notices a "My lists" link, for the first time.
        self.browser.find_element(By.LINK_TEXT, "My lists").click()

        # She sees that her list is in there, named according to its
        # first list item
        self.wait_for(
            lambda: self.browser.find_element(By.LINK_TEXT, "Reticulate splines")
        )
        self.browser.find_element(By.LINK_TEXT, "Reticulate splines").click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )
