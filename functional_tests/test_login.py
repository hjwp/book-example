from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


SUBJECT = 'Your login link for Superlists'


class LoginTest(FunctionalTest):

    def test_can_use_email_to_login(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        test_email = 'edith@example.com'
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(test_email)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # she is logged in!
        self.wait_to_be_logged_in(email=test_email)

        # Now she logs out
        self.browser.find_element_by_link_text('Log out').click()

        # She is logged out
        self.wait_to_be_logged_out(email=test_email)

