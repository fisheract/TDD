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

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')
        '''Check if header is give "To-Do" title'''
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #Insert list element
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        #Write in "Buy something
        input_box.send_keys('Buys some feather')

        #after pushing Enter page reload and have one to-do item "Buys ome feather"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(rows.text == '1: Buys some feather' for row in rows),
            "New element didn't appear in table"
        )
        # testing field still asking to add another element
        # make pillow from feather
        self.fail('End test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')