class HomePage(object):

    def __init__(self, test):
        self.test = test


    def go_to_home_page(self):
        self.test.browser.get(self.test.server_url)
        self.test.wait_for(self.get_item_input)
        return self


    def get_item_input(self):
        return self.test.browser.find_element_by_id('id_text')


    def start_new_list(self, item_text):
        self.go_to_home_page()
        inputbox = self.get_item_input()
        inputbox.send_keys(item_text + '\n')
        list_page = ListPage(self.test)
        list_page.wait_for_new_item_in_list(item_text, 1)
        return list_page



class ListPage(object):

    def __init__(self, test):
        self.test = test

    def get_list_table_rows(self):
        return self.test.browser.find_elements_by_css_selector(
            '#id_list_table tr'
        )

    def wait_for_new_item_in_list(self, item_text, position):
        expected_row = '{}: {}'.format(position, item_text)
        self.test.wait_for(lambda: self.test.assertIn(
            expected_row,
            [row.text for row in self.get_list_table_rows()]
        ))

