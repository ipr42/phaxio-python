import swagger_client
from swagger_client.apis.default_api import DefaultApi
#from v2.phaxio.exceptions import throw_if_not_authenticated


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

        # create objects to group related functions together
        self.Fax = _Fax(self.client)
        self.Account = _Account(self.client)
        self.PhoneNumber = _PhoneNumber(self.client)
        self.PhaxCode = _PhaxCode(self.client)
        self.Countries = _Countries(self.client)


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

    def cancel(self, fax_id):
        return self.client.cancel_fax(fax_id)

    def get_file(self, fax_id, thumbnail=None):
        opt_args = opt_args_to_dict(thumbnail=thumbnail)
        return self.client.get_fax_file(fax_id, **opt_args)

    def delete(self, fax_id):
        return self.client.delete_fax(fax_id)

    def delete_file(self, fax_id):
        return self.client.delete_fax_file(fax_id)

    def resend(self, fax_id):
        return self.client.resend_fax(fax_id)

    def query_faxes(self, created_before=None, created_after=None, direction=None, status=None, phone_number=None,
                    per_page=None, page=None):

        opt_args = opt_args_to_dict(created_before=created_before, created_after=created_after, direction=direction,
                                    status=status, phone_number=phone_number, per_page=per_page, page=page)
        return self.client.query_faxes(**opt_args)


class _Account(object):
    def __init__(self, client):
        self.client = client

    def get_status(self):
        return self.client.get_account_status()


class _PhoneNumber(object):
    def __init__(self, client):
        self.client = client

    def get_area_codes(self, page=None, per_page=None):
        opt_args = opt_args_to_dict(page=page, per_page=per_page)
        return self.client.get_area_codes(**opt_args)

    def get_phone_number_info(self, number):
        return self.client.get_phone_number(number)

    def release_phone_number(self, number):
        return self.client.release_phone_number(number)

    def provision_phone_number(self, country_code, area_code, callback_url=None):
        opt_args = opt_args_to_dict(callback_url=callback_url)
        return self.client.provision_phone_number(country_code, area_code, **opt_args)

    def query_phone_numbers(self, country_code=None, area_code=None, page=None, per_page=None):
        opt_args = opt_args_to_dict(country_code=country_code, area_code=area_code, page=page, per_page=per_page)
        return self.client.query_phone_numbers(**opt_args)


class _PhaxCode(object):
    def __init__(self, client):
        self.client = client

    def get_phax_code(self, phax_code_id=None):
        if not phax_code_id:
            return self.client.get_default_phax_code()

        return self.client.get_phax_code(phax_code_id)

    def create_json_phax_code(self, metadata):
        return self.client.create_phax_code_json(metadata=metadata)


class _Countries(object):
    def __init__(self, client):
        self.client = client

    def get_countries(self, page=None, per_page=None):
        opt_args = opt_args_to_dict(page=page, per_page=per_page)

        return self.client.get_countries(**opt_args)



