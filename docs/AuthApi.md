# gopad.AuthApi

All URIs are relative to *https://try.gopad.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_callback**](AuthApi.md#external_callback) | **GET** /auth/{provider}/callback | Callback for external authentication
[**external_initialize**](AuthApi.md#external_initialize) | **GET** /auth/{provider}/initialize | Initialize the external authentication


# **external_callback**
> Notification external_callback(provider, state=state, code=code)

Callback for external authentication

### Example


```python
import gopad
from gopad.models.notification import Notification
from gopad.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.gopad.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "https://try.gopad.eu/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gopad.AuthApi(api_client)
    provider = 'provider_example' # str | An identifier for the auth provider
    state = 'state_example' # str | Auth state (optional)
    code = 'code_example' # str | Auth code (optional)

    try:
        # Callback for external authentication
        api_response = api_instance.external_callback(provider, state=state, code=code)
        print("The response of AuthApi->external_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->external_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| An identifier for the auth provider | 
 **state** | **str**| Auth state | [optional] 
 **code** | **str**| Auth code | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**307** | Redirect to root of the application |  -  |
**404** | Provider identifier is unknown |  -  |
**412** | Failed to initialize provider |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_initialize**
> Notification external_initialize(provider, state=state)

Initialize the external authentication

### Example


```python
import gopad
from gopad.models.notification import Notification
from gopad.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.gopad.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "https://try.gopad.eu/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gopad.AuthApi(api_client)
    provider = 'provider_example' # str | An identifier for the auth provider
    state = 'state_example' # str | Auth state (optional)

    try:
        # Initialize the external authentication
        api_response = api_instance.external_initialize(provider, state=state)
        print("The response of AuthApi->external_initialize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->external_initialize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| An identifier for the auth provider | 
 **state** | **str**| Auth state | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**307** | Redirect to external auth provider |  -  |
**404** | Provider identifier is unknown |  -  |
**412** | Failed to initialze the provider |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

