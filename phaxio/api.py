import swagger_client
from swagger_client.apis.default_api import DefaultApi


def _opt_args_to_dict(**kwargs):
    # return kwargs as a dictionary that excludes parameters that are set to None. It's handy because some APIs don't
    # like having optional params set to null when None was passed in, so we return the kwargs without the nulls
    ret = {}
    for k, v in kwargs.iteritems():
        if v is not None:
            ret[k] = v
    return ret


class PhaxioApi(object):

    def __init__(self, api_key="", api_secret="", file_download_path=None):
        # default to "" instead of None because the swagger-generated code will try string ops on it
        swagger_client.configuration.username = api_key
        swagger_client.configuration.password = api_secret
        if file_download_path:
            swagger_client.configuration.temp_folder_path = file_download_path
        self._client = DefaultApi()

        # create objects to group related functions together
        self.Fax = _Fax(self._client)
        self.Account = _Account(self._client)
        self.PhoneNumber = _PhoneNumber(self._client)
        self.PhaxCode = _PhaxCode(self._client)
        self.Countries = _Countries(self._client)


class _Fax(object):

    def __init__(self, client):
        self._client = client

    def send(self, to, files=None, content_urls=None, header_text=None, batch_delay=None,
             batch_collision_avoidance=None, callback_url=None, cancel_timeout=None, caller_id=None, test_fail=None):
        """

        :param to:
        :param files:
        :param content_urls:
        :param header_text:
        :param batch_delay:
        :param batch_collision_avoidance:
        :param callback_url:
        :param cancel_timeout:
        :param caller_id:
        :param test_fail:
        :return: Fax
        """
        # make sure files and content_urls are lists
        if isinstance(files, basestring):
            files = [files]
        if isinstance(content_urls, basestring):
            content_urls = [content_urls]

        opt_args = _opt_args_to_dict(file=files, content_url=content_urls, header_text=header_text,
                                     batch_delay=batch_delay, batch_collision_avoidance=batch_collision_avoidance,
                                     callback_url=callback_url, cancel_timeout=cancel_timeout,
                                     caller_id=caller_id, test_fail=test_fail)

        return self._client.send_fax(to=to, **opt_args)

    def status(self, fax_id):
        """

        :param fax_id:
        :return: FaxInfo
        """
        return self._client.get_fax(fax_id)

    def cancel(self, fax_id):
        """

        :param fax_id:
        :return:
        """
        return self._client.cancel_fax(fax_id)

    def get_file(self, fax_id, thumbnail=None):
        """

        :param fax_id:
        :param thumbnail:
        :return:
        """
        opt_args = _opt_args_to_dict(thumbnail=thumbnail)
        return self._client.get_fax_file(fax_id, **opt_args)

    def delete(self, fax_id):
        """

        :param fax_id:
        :return:
        """
        return self._client.delete_fax(fax_id)

    def delete_file(self, fax_id):
        """

        :param fax_id:
        :return:
        """
        return self._client.delete_fax_file(fax_id)

    def resend(self, fax_id):
        """

        :param fax_id:
        :return:
        """
        return self._client.resend_fax(fax_id)

    def query_faxes(self, created_before=None, created_after=None, direction=None, status=None, phone_number=None,
                    per_page=None, page=None):
        """

        :param created_before: timestamp in ISO-3339 format or datetime object
        :param created_after: timestamp in ISO-3339 format or datetime object
        :param direction:
        :param status:
        :param phone_number:
        :param per_page:
        :param page:
        :return:
        """

        opt_args = _opt_args_to_dict(created_before=created_before, created_after=created_after, direction=direction,
                                     status=status, phone_number=phone_number, per_page=per_page, page=page)
        return self._client.query_faxes(**opt_args)


class _Account(object):
    def __init__(self, client):
        self._client = client

    def get_status(self):
        """

        :return:
        """
        return self._client.get_account_status()


class _PhoneNumber(object):
    def __init__(self, client):
        self._client = client

    def get_area_codes(self, page=None, per_page=None):
        """

        :param page:
        :param per_page:
        :return:
        """
        opt_args = _opt_args_to_dict(page=page, per_page=per_page)
        return self._client.get_area_codes(**opt_args)

    def get_phone_number_info(self, number):
        """

        :param number:
        :return:
        """
        return self._client.get_phone_number(number)

    def release_phone_number(self, number):
        """

        :param number:
        :return:
        """
        return self._client.release_phone_number(number)

    def provision_phone_number(self, country_code, area_code, callback_url=None):
        """

        :param country_code:
        :param area_code:
        :param callback_url:
        :return:
        """
        opt_args = _opt_args_to_dict(callback_url=callback_url)
        return self._client.provision_phone_number(country_code, area_code, **opt_args)

    def query_phone_numbers(self, country_code=None, area_code=None, page=None, per_page=None):
        """

        :param country_code:
        :param area_code:
        :param page:
        :param per_page:
        :return:
        """
        opt_args = _opt_args_to_dict(country_code=country_code, area_code=area_code, page=page, per_page=per_page)
        return self._client.query_phone_numbers(**opt_args)


class _PhaxCode(object):
    def __init__(self, client):
        self._client = client

    def get_phax_code(self, phax_code_id=None):
        """

        :param phax_code_id:
        :return:
        """
        if not phax_code_id:
            return self._client.get_default_phax_code()

        return self._client.get_phax_code(phax_code_id)

    def create_json_phax_code(self, metadata):
        """

        :param metadata:
        :return:
        """
        return self._client.create_phax_code_json(metadata=metadata)


class _Countries(object):
    def __init__(self, client):
        self._client = client

    def get_countries(self, page=None, per_page=None):
        """

        :param page:
        :param per_page:
        :return:
        """
        opt_args = _opt_args_to_dict(page=page, per_page=per_page)

        return self._client.get_countries(**opt_args)



