import swagger_client
#from v2.phaxio.exceptions import throw_if_not_authenticated


class PhaxioApiV2(object):

    def __init__(self, api_key="", api_secret=""):
        # default to "" instead of None because the swagger-generated code will try string ops on it
        swagger_client.configuration.username = api_key
        swagger_client.configuration.password = api_secret
        self.client = swagger_client.apis.default_api.DefaultApi()
        self.Fax = _Fax(self.client)


class _Fax(object):

    def __init__(self, client):
        self.client = client

    def send(self, to, files=None, content_urls=None, header_text=None, batch_delay=None,
             batch_collision_avoidance=None, callback_url=None, cancel_timeout=None, caller_id=None, test_fail=None):

        return self.client.faxes_post(to=to, file=files, content_url=content_urls, header_text=header_text,
                               batch_delay=batch_delay, batch_collision_avoidance=batch_collision_avoidance,
                               callback_url=callback_url, cancel_timeout=cancel_timeout, caller_id=caller_id,
                               test_fail=test_fail)
