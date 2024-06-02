# gopad.AuthApi

All URIs are relative to *https://try.gopad.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_callback**](AuthApi.md#external_callback) | **GET** /auth/{provider}/callback | Callback for external authentication
[**external_initialize**](AuthApi.md#external_initialize) | **GET** /auth/{provider}/initialize | Initialize the external authentication
[**login_auth**](AuthApi.md#login_auth) | **POST** /auth/login | Authenticate an user by credentials
[**refresh_auth**](AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
[**verify_auth**](AuthApi.md#verify_auth) | **GET** /auth/verify | Verify validity for an authentication token


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

# **login_auth**
> AuthToken login_auth(auth_login)

Authenticate an user by credentials

### Example


```python
import gopad
from gopad.models.auth_login import AuthLogin
from gopad.models.auth_token import AuthToken
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
    auth_login = gopad.AuthLogin() # AuthLogin | The credentials to authenticate

    try:
        # Authenticate an user by credentials
        api_response = api_instance.login_auth(auth_login)
        print("The response of AuthApi->login_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login** | [**AuthLogin**](AuthLogin.md)| The credentials to authenticate | 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated token with expire date |  -  |
**401** | Unauthorized with wrong credentials |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_auth**
> AuthToken refresh_auth()

Refresh an auth token before it expires

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.auth_token import AuthToken
from gopad.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.gopad.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "https://try.gopad.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = gopad.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = gopad.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gopad.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gopad.AuthApi(api_client)

    try:
        # Refresh an auth token before it expires
        api_response = api_instance.refresh_auth()
        print("The response of AuthApi->refresh_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_auth: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refreshed token with expire date |  -  |
**401** | Failed to generate valid token |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_auth**
> AuthVerify verify_auth()

Verify validity for an authentication token

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.auth_verify import AuthVerify
from gopad.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.gopad.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "https://try.gopad.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = gopad.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = gopad.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gopad.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gopad.AuthApi(api_client)

    try:
        # Verify validity for an authentication token
        api_response = api_instance.verify_auth()
        print("The response of AuthApi->verify_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->verify_auth: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthVerify**](AuthVerify.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of the auth token |  -  |
**401** | Unauthorized invalid token |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

