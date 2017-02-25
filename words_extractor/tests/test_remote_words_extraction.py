import unittest
import logging
import sys

from words_extractor.extractor import return_words_from_remote_url_page



class TestParser(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(stream=sys.stdout)
        self.successful_example_url = 'http://www.tornadoweb.org/en/stable/web.html'


    def test_configuration_parser_SUCCESS(self):
        result = return_words_from_remote_url_page(self.successful_example_url)
        print(result)





if __name__ == '__main__':
    unittest.main()