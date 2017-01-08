# swagger_client.DefaultApi

All URIs are relative to *https://api.phaxio.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_fax**](DefaultApi.md#cancel_fax) | **POST** /faxes/{faxId}/cancel | Cancel a Fax
[**create_phax_code_json**](DefaultApi.md#create_phax_code_json) | **POST** /phax_codes | 
[**create_phax_code_png**](DefaultApi.md#create_phax_code_png) | **POST** /phax_codes.png | 
[**delete_fax**](DefaultApi.md#delete_fax) | **DELETE** /faxes/{faxId} | Delete a fax
[**delete_fax_file**](DefaultApi.md#delete_fax_file) | **DELETE** /faxes/{faxId}/file | Delete a fax file
[**get_account_status**](DefaultApi.md#get_account_status) | **GET** /account/status | Get account status
[**get_area_codes**](DefaultApi.md#get_area_codes) | **GET** /public/area_codes | List area codes available for purchasing numbers
[**get_countries**](DefaultApi.md#get_countries) | **GET** /public/countries | Returns a list of supported countries for sending and receiving faxes
[**get_default_phax_code**](DefaultApi.md#get_default_phax_code) | **GET** /phax_code | 
[**get_default_phax_code_png**](DefaultApi.md#get_default_phax_code_png) | **GET** /phax_code.png | 
[**get_fax**](DefaultApi.md#get_fax) | **GET** /faxes/{faxId} | Get Fax
[**get_fax_file**](DefaultApi.md#get_fax_file) | **GET** /faxes/{faxId}/file | Get fax content file or thumbnail
[**get_phax_code**](DefaultApi.md#get_phax_code) | **GET** /phax_codes/{phax_code_id} | 
[**get_phax_code_png**](DefaultApi.md#get_phax_code_png) | **GET** /phax_codes/{phax_code_id}.png | 
[**get_phone_number**](DefaultApi.md#get_phone_number) | **GET** /phone_numbers/{number} | Get number info
[**provision_phone_number**](DefaultApi.md#provision_phone_number) | **POST** /phone_numbers | Provision a number
[**query_faxes**](DefaultApi.md#query_faxes) | **GET** /faxes | List faxes in date range
[**query_phone_numbers**](DefaultApi.md#query_phone_numbers) | **GET** /phone_numbers | List numbers
[**release_phone_number**](DefaultApi.md#release_phone_number) | **DELETE** /phone_numbers/{number} | Release a phone number you no longer need
[**resend_fax**](DefaultApi.md#resend_fax) | **POST** /faxes/{faxId}/resend | Resend a Fax
[**send_fax**](DefaultApi.md#send_fax) | **POST** /faxes | Create and Send a Fax


# **cancel_fax**
> SendFaxResponse cancel_fax(fax_id)

Cancel a Fax

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fax_id = 56 # int | Fax ID

try: 
    # Cancel a Fax
    api_response = api_instance.cancel_fax(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 

### Return type

[**SendFaxResponse**](SendFaxResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phax_code_json**
> GeneratePhaxCodeJsonResponse create_phax_code_json(metadata)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
metadata = 'metadata_example' # str | json file containing the phax code metadata

try: 
    api_response = api_instance.create_phax_code_json(metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_phax_code_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | **str**| json file containing the phax code metadata | 

### Return type

[**GeneratePhaxCodeJsonResponse**](GeneratePhaxCodeJsonResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phax_code_png**
> file create_phax_code_png(metadata)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
metadata = 'metadata_example' # str | json file containing the phax code metadata

try: 
    api_response = api_instance.create_phax_code_png(metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_phax_code_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | **str**| json file containing the phax code metadata | 

### Return type

[**file**](file.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fax**
> OperationStatus delete_fax(fax_id)

Delete a fax

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fax_id = 56 # int | Fax ID

try: 
    # Delete a fax
    api_response = api_instance.delete_fax(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fax_file**
> OperationStatus delete_fax_file(fax_id)

Delete a fax file

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fax_id = 56 # int | Fax ID

try: 
    # Delete a fax file
    api_response = api_instance.delete_fax_file(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_fax_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_status**
> AccountStatus get_account_status()

Get account status

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # Get account status
    api_response = api_instance.get_account_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_account_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountStatus**](AccountStatus.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_area_codes**
> GetAreaCodesResponse get_area_codes(toll_free=toll_free, country_code=country_code, country=country, state=state, per_page=per_page, page=page)

List area codes available for purchasing numbers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
toll_free = true # bool | If set to `true`, only toll free area codes will be returned. If specified and set to `false`, only non-toll free area codes will be returned. (optional)
country_code = 56 # int | A country code (E.164) you'd like to filter by (optional)
country = 'country_example' # str | A country code (E.164) you'd like to filter by (optional)
state = 'state_example' # str | A two character state or province abbreviation (ISO 3166; e.g. `IL` or `YT`) you'd like to filter by. When using this parameter, `country_code` or `country` must also be provided. (optional)
per_page = 56 # int | How many records to return per page (optional)
page = 56 # int | Page number to return (optional)

try: 
    # List area codes available for purchasing numbers
    api_response = api_instance.get_area_codes(toll_free=toll_free, country_code=country_code, country=country, state=state, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_area_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toll_free** | **bool**| If set to &#x60;true&#x60;, only toll free area codes will be returned. If specified and set to &#x60;false&#x60;, only non-toll free area codes will be returned. | [optional] 
 **country_code** | **int**| A country code (E.164) you&#39;d like to filter by | [optional] 
 **country** | **str**| A country code (E.164) you&#39;d like to filter by | [optional] 
 **state** | **str**| A two character state or province abbreviation (ISO 3166; e.g. &#x60;IL&#x60; or &#x60;YT&#x60;) you&#39;d like to filter by. When using this parameter, &#x60;country_code&#x60; or &#x60;country&#x60; must also be provided. | [optional] 
 **per_page** | **int**| How many records to return per page | [optional] 
 **page** | **int**| Page number to return | [optional] 

### Return type

[**GetAreaCodesResponse**](GetAreaCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> GetCountriesResponse get_countries(per_page=per_page, page=page)

Returns a list of supported countries for sending and receiving faxes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
per_page = 56 # int | How many records to return per page (optional)
page = 56 # int | Page number to return (optional)

try: 
    # Returns a list of supported countries for sending and receiving faxes
    api_response = api_instance.get_countries(per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| How many records to return per page | [optional] 
 **page** | **int**| Page number to return | [optional] 

### Return type

[**GetCountriesResponse**](GetCountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_phax_code**
> PhaxCode get_default_phax_code()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.get_default_phax_code()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_default_phax_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PhaxCode**](PhaxCode.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_phax_code_png**
> file get_default_phax_code_png()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.get_default_phax_code_png()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_default_phax_code_png: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fax**
> GetFaxInfoResponse get_fax(fax_id)

Get Fax

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fax_id = 56 # int | Fax ID

try: 
    # Get Fax
    api_response = api_instance.get_fax(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 

### Return type

[**GetFaxInfoResponse**](GetFaxInfoResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fax_file**
> file get_fax_file(fax_id, thumbnail=thumbnail)

Get fax content file or thumbnail

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fax_id = 56 # int | Fax ID
thumbnail = 'thumbnail_example' # str | if set, request a thumbnail only in specified size (optional)

try: 
    # Get fax content file or thumbnail
    api_response = api_instance.get_fax_file(fax_id, thumbnail=thumbnail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fax_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 
 **thumbnail** | **str**| if set, request a thumbnail only in specified size | [optional] 

### Return type

[**file**](file.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phax_code**
> PhaxCode get_phax_code(phax_code_id)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
phax_code_id = 'phax_code_id_example' # str | identifier for the phax code

try: 
    api_response = api_instance.get_phax_code(phax_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_phax_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phax_code_id** | **str**| identifier for the phax code | 

### Return type

[**PhaxCode**](PhaxCode.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phax_code_png**
> file get_phax_code_png(phax_code_id)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
phax_code_id = 'phax_code_id_example' # str | identifier for the phax code

try: 
    api_response = api_instance.get_phax_code_png(phax_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_phax_code_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phax_code_id** | **str**| identifier for the phax code | 

### Return type

[**file**](file.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_number**
> PhoneNumberResponse get_phone_number(number)

Get number info

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
number = 'number_example' # str | phone number

try: 
    # Get number info
    api_response = api_instance.get_phone_number(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| phone number | 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_phone_number**
> PhoneNumberResponse provision_phone_number(country_code, area_code, callback_url=callback_url)

Provision a number

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
country_code = 56 # int | The country code (E.164) of the number you'd like to provision
area_code = 56 # int | The area code of the number you'd like to provision
callback_url = 'callback_url_example' # str | A callback URL that we'll post to when a fax is received by this number (optional)

try: 
    # Provision a number
    api_response = api_instance.provision_phone_number(country_code, area_code, callback_url=callback_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->provision_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **int**| The country code (E.164) of the number you&#39;d like to provision | 
 **area_code** | **int**| The area code of the number you&#39;d like to provision | 
 **callback_url** | **str**| A callback URL that we&#39;ll post to when a fax is received by this number | [optional] 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_faxes**
> GetFaxesResponse query_faxes(created_before=created_before, created_after=created_after, direction=direction, status=status, phone_number=phone_number, per_page=per_page, page=page)

List faxes in date range

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
created_before = 'created_before_example' # str | End of the range (optional)
created_after = 'created_after_example' # str | Beginning of the range (optional)
direction = 'direction_example' # str | Limits results to faxes with the specified direction (optional)
status = 'status_example' # str | Limits results to faxes with the specified status (optional)
phone_number = 'phone_number_example' # str | A phone number in E.164 format that you want to use to filter results. (optional)
per_page = 56 # int | How many records to return per page (optional)
page = 56 # int | Page number to return (optional)

try: 
    # List faxes in date range
    api_response = api_instance.query_faxes(created_before=created_before, created_after=created_after, direction=direction, status=status, phone_number=phone_number, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->query_faxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_before** | **str**| End of the range | [optional] 
 **created_after** | **str**| Beginning of the range | [optional] 
 **direction** | **str**| Limits results to faxes with the specified direction | [optional] 
 **status** | **str**| Limits results to faxes with the specified status | [optional] 
 **phone_number** | **str**| A phone number in E.164 format that you want to use to filter results. | [optional] 
 **per_page** | **int**| How many records to return per page | [optional] 
 **page** | **int**| Page number to return | [optional] 

### Return type

[**GetFaxesResponse**](GetFaxesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_phone_numbers**
> ListPhoneNumbersResponse query_phone_numbers(country_code=country_code, area_code=area_code, per_page=per_page, page=page)

List numbers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
country_code = 56 # int | A country code you'd like to filter by (optional)
area_code = 56 # int | An area code you'd like to filter by (optional)
per_page = 56 # int | How many records to return per page (optional)
page = 56 # int | Page number to return (optional)

try: 
    # List numbers
    api_response = api_instance.query_phone_numbers(country_code=country_code, area_code=area_code, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->query_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **int**| A country code you&#39;d like to filter by | [optional] 
 **area_code** | **int**| An area code you&#39;d like to filter by | [optional] 
 **per_page** | **int**| How many records to return per page | [optional] 
 **page** | **int**| Page number to return | [optional] 

### Return type

[**ListPhoneNumbersResponse**](ListPhoneNumbersResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_phone_number**
> OperationStatus release_phone_number(number)

Release a phone number you no longer need

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
number = 'number_example' # str | phone number

try: 
    # Release a phone number you no longer need
    api_response = api_instance.release_phone_number(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->release_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| phone number | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_fax**
> SendFaxResponse resend_fax(fax_id)

Resend a Fax

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fax_id = 56 # int | Fax ID

try: 
    # Resend a Fax
    api_response = api_instance.resend_fax(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->resend_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 

### Return type

[**SendFaxResponse**](SendFaxResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_fax**
> SendFaxResponse send_fax(to, direction=direction, file=file, content_url=content_url, header_text=header_text, batch_delay=batch_delay, batch_collision_avoidance=batch_collision_avoidance, callback_url=callback_url, cancel_timeout=cancel_timeout, caller_id=caller_id, test_fail=test_fail)

Create and Send a Fax

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
to = 'to_example' # str | phone number
direction = 'direction_example' # str | Set to 'received' to receive test fax. (optional)
file = ['/path/to/file.txt'] # list[file] | file to send (optional)
content_url = ['content_url_example'] # list[str] | url of file to send (optional)
header_text = 'header_text_example' # str | Text that appears at the top of each page (optional)
batch_delay = 56 # int | Number of seconds to wait before sending batch (optional)
batch_collision_avoidance = true # bool | When batch_delay is set, fax will be blocked until the receiving machine is no longer busy (optional)
callback_url = 'callback_url_example' # str | Overrides global callback URL (optional)
cancel_timeout = 56 # int | Number of minutes to wait for successful send before cancelling fax (optional)
caller_id = 'caller_id_example' # str | Number to use for caller ID (optional)
test_fail = 'test_fail_example' # str | When sending a test fax, if this is set it will simulate the failure type specified (optional)

try: 
    # Create and Send a Fax
    api_response = api_instance.send_fax(to, direction=direction, file=file, content_url=content_url, header_text=header_text, batch_delay=batch_delay, batch_collision_avoidance=batch_collision_avoidance, callback_url=callback_url, cancel_timeout=cancel_timeout, caller_id=caller_id, test_fail=test_fail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->send_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| phone number | 
 **direction** | **str**| Set to &#39;received&#39; to receive test fax. | [optional] 
 **file** | **list[file]**| file to send | [optional] 
 **content_url** | [**list[str]**](str.md)| url of file to send | [optional] 
 **header_text** | **str**| Text that appears at the top of each page | [optional] 
 **batch_delay** | **int**| Number of seconds to wait before sending batch | [optional] 
 **batch_collision_avoidance** | **bool**| When batch_delay is set, fax will be blocked until the receiving machine is no longer busy | [optional] 
 **callback_url** | **str**| Overrides global callback URL | [optional] 
 **cancel_timeout** | **int**| Number of minutes to wait for successful send before cancelling fax | [optional] 
 **caller_id** | **str**| Number to use for caller ID | [optional] 
 **test_fail** | **str**| When sending a test fax, if this is set it will simulate the failure type specified | [optional] 

### Return type

[**SendFaxResponse**](SendFaxResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

