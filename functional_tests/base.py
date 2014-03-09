from selenium import webdriver
import sys
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.common.exceptions import WebDriverException

DEFAULT_WAIT = 3


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(DEFAULT_WAIT)

    def tearDown(self):
        self.browser.quit()


    def wait_for(self, function_with_assertion, timeout=DEFAULT_WAIT):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                return function_with_assertion()
            except (AssertionError, WebDriverException):
                time.sleep(0.1)
        # one more try, which will raise any errors if they are outstanding
        return function_with_assertion()


    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

