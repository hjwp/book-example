import os
from datetime import datetime
import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from .server_tools import reset_database


SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_host = arg.split('=')[1]
                cls.server_url = 'http://' + cls.server_host
                cls.against_staging = True
                return
        super().setUpClass()
        cls.against_staging = False
        cls.server_url = cls.live_server_url


    @classmethod
    def tearDownClass(cls):
        if not cls.against_staging:
            super().tearDownClass()


    def setUp(self):
        if self.against_staging:
            reset_database(self.server_host)

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        if self._test_has_failed():
            if not os.path.exists(SCREEN_DUMP_LOCATION):
                os.makedirs(SCREEN_DUMP_LOCATION)
            for ix, handle in enumerate(self.browser.window_handles):
                self._windowid = ix
                self.browser.switch_to_window(handle)
                self.take_screenshot()
                self.dump_html()
        self.browser.quit()
        super().tearDown()


    def _test_has_failed(self):
        # slightly obscure but couldn't find a better way!
        return any(error for (method, error) in self._outcome.errors)


    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def assert_logged_in(self, email):
        self.browser.find_element_by_link_text('Log out')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)


    def assert_logged_out(self, email):
        self.browser.find_element_by_name('email')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)

