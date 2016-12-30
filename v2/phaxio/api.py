import swagger_client
from swagger_client.apis.default_api import DefaultApi
#from v2.phaxio.exceptions import throw_if_not_authenticated

"""
    def cancel_fax(self, fax_id, **kwargs):
    def create_phax_code_json(self, metadata, **kwargs):
    def delete_fax(self, fax_id, **kwargs):
    def delete_fax_file(self, fax_id, **kwargs):
    def get_account_status(self, **kwargs):
    def get_area_codes(self, **kwargs):
    def get_countries(self, **kwargs):
    def get_default_phax_code(self, **kwargs):
    def get_fax(self, fax_id, **kwargs):
    def get_fax_file(self, fax_id, **kwargs):
    def get_phax_code(self, phax_code_id, **kwargs):
    def get_phone_number(self, number, **kwargs):
    def provision_phone_number(self, country_code, area_code, **kwargs):
    def query_faxes(self, **kwargs):
    def query_phone_numbers(self, **kwargs):
    def release_phone_number(self, number, **kwargs):
    def resend_fax(self, fax_id, **kwargs):
    def send_fax(self, to, **kwargs):


"""

def opt_args_to_dict(**kwargs):
    # return kwargs as a dictionary that excludes parameters that are set to None. It's handy because some APIs don't
    # like having optional params set to null when None was passed in, so we return the kwargs without the nulls
    ret = {}
    for k, v in kwargs.iteritems():
        if v is not None:
            ret[k] = v
    return ret

class PhaxioApiV2(object):

    def __init__(self, api_key="", api_secret="", file_download_path=None):
        # default to "" instead of None because the swagger-generated code will try string ops on it
        swagger_client.configuration.username = api_key
        swagger_client.configuration.password = api_secret
        if file_download_path:
            swagger_client.configuration.temp_folder_path = file_download_path
        self.client = DefaultApi()

        # create objects through which clients will call the APIs
        self.Fax = _Fax(self.client)

class _Fax(object):

    def __init__(self, client):
        self.client = client

    def send(self, to, files=None, content_urls=None, header_text=None, batch_delay=None,
             batch_collision_avoidance=None, callback_url=None, cancel_timeout=None, caller_id=None, test_fail=None):
        # make sure files and content_urls are lists
        if isinstance(files, basestring):
            files = [files]
        if isinstance(content_urls, basestring):
            content_urls = [content_urls]

        opt_args = opt_args_to_dict(file=files, content_url=content_urls, header_text=header_text,
                                    batch_delay=batch_delay, batch_collision_avoidance=batch_collision_avoidance,
                                    callback_url=callback_url, cancel_timeout=cancel_timeout,
                                    caller_id=caller_id, test_fail=test_fail)

        return self.client.send_fax(to=to, **opt_args)

    def status(self, fax_id):
        return self.client.get_fax(fax_id)

    def get_file(self, fax_id, thumbnail=None):
        opt_args = opt_args_to_dict(thumbnail=thumbnail)
        return self.client.get_fax_file(fax_id, **opt_args)

    def delete(self, fax_id):
        return self.client.delete_fax(fax_id)

    def delete_file(self, fax_id):
        return self.client.delete_fax_file(fax_id)


