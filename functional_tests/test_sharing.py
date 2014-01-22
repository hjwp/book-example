from selenium import webdriver
from .base import FunctionalTest


def quit_if_possible(browser):
    try: browser.quit()
    except: pass


class SharingTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged-in user
        self.create_pre_authenticated_session('edith@example.com')
        edith_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(edith_browser))

        # Her friend Oniciferous is also hanging out on the lists site
        oni_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(oni_browser))
        self.browser = oni_browser
        self.create_pre_authenticated_session('oniciferous@example.com')

        # Edith goes to the home page and starts a list
        self.browser = edith_browser
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Get help\n')

        # She notices a "Share this list" option
        share_box = self.browser.find_element_by_css_selector('input[name=email]')
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
