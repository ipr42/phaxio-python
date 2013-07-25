import io
import requests
import urllib

from .utils import curry

class PhaxioApi(object):
    VERSION = 1
    BASE_URL = 'https://api.phaxio.com'
    __IMPLEMENTED = ('send', 'testReceive', 'attachPhaxCodeToPdf',
        'createPhaxCode', 'getHostedDocument'
    )

    api_key = None
    api_secret = None

    def __init__(self, key, secret):
        self.api_key = key
        self.api_secret = secret

    def _get(self, method, **kwargs):
        """ Builds the url for the specified method and arguments and returns
        the response as a dictionary.
        """

        payload = kwargs.copy()
        payload['api_key'] = self.api_key
        payload['api_secret'] = self.api_secret

        fns = payload.pop('filename', [])
        if isinstance(fns, basestring): fns = [fns]
        files = {}
        for fn_i, fn in enumerate(fns):
            files['filename'] = ('file.pdf', open(fn, 'rb'))

        url = '%s/v%d/%s' % (self.BASE_URL, self.VERSION, method)
        print(url)
        print(payload)
        print(files)
        #import ipdb; ipdb.set_trace()
        r = requests.get(url, params = payload, files = files)
        print('response: %s' % (r.content))
        return r.json()

    def __getattribute__(self, name):
        if name in PhaxioApi.__IMPLEMENTED:
            return curry(self._get, name)
        return super(PhaxioApi, self).__getattribute__(name)

