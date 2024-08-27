from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import wait


class ListPage:
    def __init__(self, test):
        self.test = test

    def get_table_rows(self):
        table = self.test.browser.find_element(By.ID, "id_list_table")
        return table.find_elements(By.TAG_NAME, "tr")

    @wait
    def wait_for_row_in_list_table(self, item_text, item_number):
        expected_row_text = f"{item_number}: {item_text}"
        rows = self.get_table_rows()
        self.test.assertIn(expected_row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.test.browser.find_element(By.ID, "id_text")

    def add_list_item(self, item_text):
        new_item_no = len(self.get_table_rows()) + 1
        self.get_item_input_box().send_keys(item_text)
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(item_text, new_item_no)
        return self
