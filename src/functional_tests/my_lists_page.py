from selenium.webdriver.common.by import By


class MyListsPage:
    def __init__(self, test):
        self.test = test

    def go_to_my_lists_page(self, email):
        self.test.browser.get(self.test.live_server_url)
        self.test.browser.find_element(By.LINK_TEXT, "My lists").click()
        self.test.wait_for(
            lambda: self.test.assertIn(
                email,
                self.test.browser.find_element(By.TAG_NAME, "h1").text,
            )
        )
        return self
