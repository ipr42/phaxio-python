import unittest
import os
import re
import logging
import requests
import json
import urllib3
import urllib
from urllib3_mock import Responses

from phaxio import PhaxioApi
from phaxio.swagger_client.models.phone_number_response import PhoneNumberResponse
from phaxio.swagger_client.models.phone_number import PhoneNumber
from phaxio.swagger_client.api_client import ApiException

# need to set up mocks for both urllib3-based requests (used for most everything) and requests-based ones (used for some posts)
responses_requests = Responses('requests.packages.urllib3')
responses_urllib = Responses()


class PhaxioApiUnitTests(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logger.level = logging.DEBUG

    handler = logging.FileHandler('test.log')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(handler)

    def setUp(self):
        self.client = PhaxioApi()
        self.request = None

        # this will cause all API requests to get routed to request_callback, which just returns empty reponses
        # and saves the request in self.request so it can be validated
        url_re = re.compile(r'/v2/.*')
        responses_urllib.add_callback('GET', url_re, callback=self.request_callback)
        responses_urllib.add_callback('POST', url_re, callback=self.request_callback)
        responses_requests.add_callback('POST', url_re, callback=self.request_callback)
        responses_urllib.add_callback('DELETE', url_re, callback=self.request_callback)

    def request_callback(self, r):
        self.request = r
        self.logger.debug('request={}'.format(r))
        return 200, {}, ''

    def assert_request_is_correct(self, method, url, headers_dict=None, body=None):
        self.assertEqual(self.request.method, method)
        self.assertEqual(self.request.url, url)
        if headers_dict:
            self.assertDictContainsSubset(headers_dict, self.request.headers)
        if body:
            self.assertEqual(body, self.request.body)

    @responses_urllib.activate
    @responses_requests.activate
    def test_phone_numbers_api(self):
        self.client.PhoneNumber.get_phone_number_info('4132343233')
        self.assert_request_is_correct('GET', '/v2/phone_numbers/4132343233')

        self.client.PhoneNumber.get_area_codes(page=3, per_page=49)
        self.assert_request_is_correct('GET', '/v2/public/area_codes?per_page=49&page=3')
        # auth not required for this api
        self.assertNotIn('Authorization', self.request.headers)

        # some apis don't like the empty return, so catch the exception
        try:
            self.client.PhoneNumber.provision_phone_number('1', '206', 'http://fake/callback')
        except Exception as e:
            pass

        self.assert_request_is_correct('POST', '/v2/phone_numbers', {'Content-Type': 'application/x-www-form-urlencoded'},
                                       body='country_code=1&area_code=206&callback_url=http%3A%2F%2Ffake%2Fcallback')

        self.client.PhoneNumber.query_phone_numbers(country_code=1, area_code=206, page=4, per_page=12)
        self.assert_request_is_correct('GET', '/v2/phone_numbers?per_page=12&area_code=206&page=4&country_code=1')

        self.client.PhoneNumber.release_phone_number('2065551234')
        self.assert_request_is_correct('DELETE', '/v2/phone_numbers/2065551234')

    @responses_urllib.activate
    @responses_requests.activate
    def test_account_info_api(self):
        self.client.Account.get_status()
        self.assert_request_is_correct('GET', '/v2/account/status')

    @responses_urllib.activate
    @responses_requests.activate
    def test_phax_code_api(self):
        try:
            self.client.PhaxCode.create_json_phax_code('{"test_key": "test_val"}')
        except Exception as e:
            pass

        self.assert_request_is_correct('POST', '/v2/phax_codes',
                                       headers_dict={'Content-Type': 'application/x-www-form-urlencoded'},
                                       body='metadata=%7B%22test_key%22%3A+%22test_val%22%7D')
        self.client.PhaxCode.get_phax_code('phax_code_id')
        self.assert_request_is_correct('GET', '/v2/phax_codes/phax_code_id')

    @responses_urllib.activate
    @responses_requests.activate
    def test_countries_api(self):
        self.client.Countries.get_countries()
        self.assert_request_is_correct('GET', '/v2/public/countries')
        self.client.Countries.get_countries(page=4)
        self.assert_request_is_correct('GET', '/v2/public/countries?page=4')

    @responses_urllib.activate
    @responses_requests.activate
    def test_fax_api(self):
        pass









