# swagger_client.DefaultApi

All URIs are relative to *https://api.phaxio.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_status_get**](DefaultApi.md#account_status_get) | **GET** /account/status | Get account status
[**faxes_fax_id_cancel_post**](DefaultApi.md#faxes_fax_id_cancel_post) | **POST** /faxes/{faxId}/cancel | Cancel a Fax
[**faxes_fax_id_delete**](DefaultApi.md#faxes_fax_id_delete) | **DELETE** /faxes/{faxId} | Delete a fax
[**faxes_fax_id_file_delete**](DefaultApi.md#faxes_fax_id_file_delete) | **DELETE** /faxes/{faxId}/file | Delete a fax file
[**faxes_fax_id_file_get**](DefaultApi.md#faxes_fax_id_file_get) | **GET** /faxes/{faxId}/file | Get fax content file or thumbnail
[**faxes_fax_id_get**](DefaultApi.md#faxes_fax_id_get) | **GET** /faxes/{faxId} | Get Fax
[**faxes_fax_id_resend_post**](DefaultApi.md#faxes_fax_id_resend_post) | **POST** /faxes/{faxId}/resend | Resend a Fax
[**faxes_get**](DefaultApi.md#faxes_get) | **GET** /faxes | List faxes in date range
[**faxes_post**](DefaultApi.md#faxes_post) | **POST** /faxes | Create and Send a Fax


# **account_status_get**
> AccountStatus account_status_get()

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
    api_response = api_instance.account_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->account_status_get: %s\n" % e)
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

# **faxes_fax_id_cancel_post**
> SendFaxResponse faxes_fax_id_cancel_post(fax_id)

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
    api_response = api_instance.faxes_fax_id_cancel_post(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_fax_id_cancel_post: %s\n" % e)
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

# **faxes_fax_id_delete**
> FailureResponse faxes_fax_id_delete(fax_id)

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
    api_response = api_instance.faxes_fax_id_delete(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_fax_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 

### Return type

[**FailureResponse**](FailureResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faxes_fax_id_file_delete**
> FailureResponse faxes_fax_id_file_delete(fax_id)

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
    api_response = api_instance.faxes_fax_id_file_delete(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_fax_id_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_id** | **int**| Fax ID | 

### Return type

[**FailureResponse**](FailureResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faxes_fax_id_file_get**
> file faxes_fax_id_file_get(fax_id, thumbnail=thumbnail)

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
    api_response = api_instance.faxes_fax_id_file_get(fax_id, thumbnail=thumbnail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_fax_id_file_get: %s\n" % e)
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

# **faxes_fax_id_get**
> GetFaxInfoResponse faxes_fax_id_get(fax_id)

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
    api_response = api_instance.faxes_fax_id_get(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_fax_id_get: %s\n" % e)
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

# **faxes_fax_id_resend_post**
> SendFaxResponse faxes_fax_id_resend_post(fax_id)

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
    api_response = api_instance.faxes_fax_id_resend_post(fax_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_fax_id_resend_post: %s\n" % e)
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

# **faxes_get**
> GetFaxesResponse faxes_get(created_before=created_before, created_after=created_after, direction=direction, status=status, phone_number=phone_number, per_page=per_page, page=page)

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
    api_response = api_instance.faxes_get(created_before=created_before, created_after=created_after, direction=direction, status=status, phone_number=phone_number, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_get: %s\n" % e)
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

# **faxes_post**
> SendFaxResponse faxes_post(to, direction=direction, file=file, content_url=content_url, header_text=header_text, batch_delay=batch_delay, batch_collision_avoidance=batch_collision_avoidance, callback_url=callback_url, cancel_timeout=cancel_timeout, tag=tag, caller_id=caller_id, test_fail=test_fail)

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
tag = 56 # int | Number of minutes to wait for successful send before cancelling fax (optional)
caller_id = 'caller_id_example' # str | Number to use for caller ID (optional)
test_fail = 'test_fail_example' # str | When sending a test fax, if this is set it will simulate the failure type specified (optional)

try: 
    # Create and Send a Fax
    api_response = api_instance.faxes_post(to, direction=direction, file=file, content_url=content_url, header_text=header_text, batch_delay=batch_delay, batch_collision_avoidance=batch_collision_avoidance, callback_url=callback_url, cancel_timeout=cancel_timeout, tag=tag, caller_id=caller_id, test_fail=test_fail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->faxes_post: %s\n" % e)
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
 **tag** | **int**| Number of minutes to wait for successful send before cancelling fax | [optional] 
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

