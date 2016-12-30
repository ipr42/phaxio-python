import os
import time
import unittest

from api import PhaxioApiV2
from swagger_client.models import error

import sys
import unittest
import logging


class TestV2Api(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logger.level = logging.DEBUG

    handler = logging.FileHandler('test.log')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(handler)

    test_number = '4145556984'

    def setUp(self):

        api_key = os.getenv('API_KEY')
        api_secret = os.getenv('API_SECRET')

        file_download_path = './'
        self.client = PhaxioApiV2(api_key, api_secret, file_download_path=file_download_path)

    def tearDown(self):
        #self.logger.removeHandler(self.stream_handler)
        # needed to prevent rate-limiting
        time.sleep(1)

    def test_send_fax(self):
        response = self.client.Fax.send(self.test_number, files=['/mnt/d/src/pyphaxio/v2/phaxio/requirements.txt'],
                        content_urls=['http://www.google.com', 'http://www.bing.com'])
        self.logger.info('response={}'.format(response))
        self.assertTrue(response.success)

    def test_send_fax_with_test_failure(self):
        # send fax with test_fail set, get its status, delete the file then delete the fax, verify each
        response = self.client.Fax.send(self.test_number, content_urls='http://www.google.com', test_fail='lineError')
        self.logger.debug('response={}'.format(response))
        self.assertTrue(response.success)
        fax_id = response.data.id
        time.sleep(7)
        status_response = self.client.Fax.status(fax_id)
        self.logger.debug('status={}'.format(status_response))
        self.assertEqual(status_response.data.recipients[0].error_type, 'lineError')

        # try downloading the file
        time.sleep(2)
        response = self.client.Fax.get_file(fax_id)
        self.logger.debug('file download response={}'.format(response))

        time.sleep(2)
        # now verify delete, file first
        delete_response = self.client.Fax.delete_file(fax_id)
        self.assertTrue(delete_response.success)
        self.logger.debug('delete_file_response={}'.format(delete_response))

        # now delete the fax itself
        time.sleep(2)
        delete_response = self.client.Fax.delete(fax_id)
        self.assertTrue(delete_response.success)
        self.logger.debug('delete_response={}'.format(delete_response))

