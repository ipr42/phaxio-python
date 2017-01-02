import os
import time
import unittest
import json

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

        # get fax metadata
        time.sleep(7)
        status_response = self.client.Fax.status(fax_id)
        self.logger.debug('status={}'.format(status_response))
        self.assertEqual(status_response.data.recipients[0].error_type, 'lineError')

        self.logger.debug('created_at type={}, val={}'.format(type(status_response.data.created_at), status_response.data.created_at))

        # try downloading the file
        time.sleep(2)
        response = self.client.Fax.get_file(fax_id, thumbnail='l')
        self.logger.debug('file download response={}'.format(response))

        # resend the fax
        time.sleep(2)
        resend_response = self.client.Fax.resend(fax_id)
        self.logger.debug('resend_response={}'.format(resend_response))
        self.assertTrue(resend_response.success)

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

    def _assert_paging_params(self, result, page, per_page):
        self.assertEqual(result.paging.page, page)
        self.assertEqual(result.paging.per_page, per_page)
        self.assertLessEqual(len(result.data), per_page)

    def test_get_countries(self):
        result = self.client.Countries.get_countries(page=1, per_page=10)
        self.logger.debug("countries result={}".format(result))

        self.assertTrue(result.success)
        self._assert_paging_params(result, 1, 10)

    def test_query_fax(self):
        result = self.client.Fax.query_faxes(direction='sent', status='success', per_page=20, page=1)
        self.logger.debug('query_result={}'.format(result))
        self.assertTrue(result.success)
        self._assert_paging_params(result, 1, 20)

    def test_area_codes(self):
        result = self.client.PhoneNumber.get_area_codes(page=3, per_page=10)
        self.logger.debug('area_codes_results={}'.format(result))
        self._assert_paging_params(result, 3, 10)

    def test_phax_codes(self):
        test_metadata = {'testkey': 'testval'}
        result = self.client.PhaxCode.create_json_phax_code(json.dumps(test_metadata))
        self.logger.debug('create_phax_code_result={}'.format(result))
        self.assertTrue(result.success)
        phax_id = result.data.identifier

        time.sleep(2)
        result = self.client.PhaxCode.get_phax_code(phax_code_id=phax_id)
        self.logger.debug('get_phax_code_result={}'.format(result))
        self.assertTrue(result.success)

        metadata_dict = json.loads(result.data.metadata)
        self.assertDictEqual(metadata_dict, test_metadata)
