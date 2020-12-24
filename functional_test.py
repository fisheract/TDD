from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        #установка
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #демонтаж
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        #conformation that strings are in lists
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')
        '''Check if header is give "To-Do" title'''
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #Insert first element
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
        #Write in "Buy something
        input_box.send_keys('Buy some feather')
        #after pushing Enter page reload and have one to-do item "Buys ome feather"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1. Buy some feather')

        # Insert second element
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
        # Write in "Make pillow from feather"
        input_box.send_keys('Make pillow from feather')
        # after pushing Enter page reload and have one to-do item "Buys ome feather"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('2. Make pillow from feather')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. Buy some feather', [row.text for row in rows])
        self.assertIn('2. Make pillow from feather', [row.text for row in rows])
        # testing field still asking to add another element
        # make pillow from feather
        self.fail('End test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')