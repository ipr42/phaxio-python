# swagger_client.DefaultApi

All URIs are relative to *https://api.phaxio.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_status_get**](DefaultApi.md#account_status_get) | **GET** /account/status | Get account status
[**faxes_fax_id_cancel_post**](DefaultApi.md#faxes_fax_id_cancel_post) | **POST** /faxes/{faxId}/cancel | Cancel a Fax
[**faxes_fax_id_get**](DefaultApi.md#faxes_fax_id_get) | **GET** /faxes/{faxId} | Get Fax
[**faxes_fax_id_resend_post**](DefaultApi.md#faxes_fax_id_resend_post) | **POST** /faxes/{faxId}/resend | Resend a Fax
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

# **faxes_fax_id_get**
> FaxInfo faxes_fax_id_get(fax_id)

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

[**FaxInfo**](FaxInfo.md)

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

