import os
import unittest

from api import PhaxioApiV2


class TestV2Api(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('API_KEY')
        api_secret = os.getenv('API_SECRET')

        self.client = PhaxioApiV2(api_key, api_secret)

    def test_send_fax(self):
        response = self.client.Fax.send('4145556984', files=['/mnt/d/src/pyphaxio/v2/phaxio/requirements.txt'],
                        content_urls=['http://www.google.com', 'http://www.bing.com'])
        self.assertTrue(response.success)