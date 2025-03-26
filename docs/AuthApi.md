# gopad.AuthApi

All URIs are relative to *https://try.gopad.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callback_provider**](AuthApi.md#callback_provider) | **GET** /auth/{provider}/callback | Callback to parse the defined provider
[**list_providers**](AuthApi.md#list_providers) | **GET** /auth/providers | Fetch the available auth providers
[**login_auth**](AuthApi.md#login_auth) | **POST** /auth/login | Authenticate an user by credentials
[**redirect_auth**](AuthApi.md#redirect_auth) | **POST** /auth/redirect | Retrieve real token after redirect
[**refresh_auth**](AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
[**request_provider**](AuthApi.md#request_provider) | **GET** /auth/{provider}/request | Request the redirect to defined provider
[**verify_auth**](AuthApi.md#verify_auth) | **GET** /auth/verify | Verify validity for an authentication token


# **callback_provider**
> callback_provider(provider, state=state, code=code)

Callback to parse the defined provider

### Example


```python
import gopad
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
        # Callback to parse the defined provider
        api_instance.callback_provider(provider, state=state, code=code)
    except Exception as e:
        print("Exception when calling AuthApi->callback_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| An identifier for the auth provider | 
 **state** | **str**| Auth state | [optional] 
 **code** | **str**| Auth code | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**308** | Generated expiring token |  -  |
**412** | Failed to initialize provider |  -  |
**404** | Provider not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ListProviders200Response list_providers()

Fetch the available auth providers

### Example


```python
import gopad
from gopad.models.list_providers200_response import ListProviders200Response
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

    try:
        # Fetch the available auth providers
        api_response = api_instance.list_providers()
        print("The response of AuthApi->list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->list_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListProviders200Response**](ListProviders200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of auth providers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_auth**
> AuthToken login_auth(login_auth_request)

Authenticate an user by credentials

### Example


```python
import gopad
from gopad.models.auth_token import AuthToken
from gopad.models.login_auth_request import LoginAuthRequest
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
    login_auth_request = gopad.LoginAuthRequest() # LoginAuthRequest | The credentials to authenticate

    try:
        # Authenticate an user by credentials
        api_response = api_instance.login_auth(login_auth_request)
        print("The response of AuthApi->login_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_auth_request** | [**LoginAuthRequest**](LoginAuthRequest.md)| The credentials to authenticate | 

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
**400** | Failed to parse request |  -  |
**401** | Unauthorized with wrong credentials |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_auth**
> AuthToken redirect_auth(redirect_auth_request)

Retrieve real token after redirect

### Example


```python
import gopad
from gopad.models.auth_token import AuthToken
from gopad.models.redirect_auth_request import RedirectAuthRequest
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
    redirect_auth_request = gopad.RedirectAuthRequest() # RedirectAuthRequest | The redirect token to authenticate

    try:
        # Retrieve real token after redirect
        api_response = api_instance.redirect_auth(redirect_auth_request)
        print("The response of AuthApi->redirect_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->redirect_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_auth_request** | [**RedirectAuthRequest**](RedirectAuthRequest.md)| The redirect token to authenticate | 

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
**200** | Generated token never expiring |  -  |
**400** | Failed to parse request |  -  |
**401** | Failed to generate or validate token |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_auth**
> AuthToken refresh_auth()

Refresh an auth token before it expires

### Example

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

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refreshed token with expire date |  -  |
**401** | Failed to generate or validate token |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_provider**
> request_provider(provider)

Request the redirect to defined provider

### Example


```python
import gopad
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

    try:
        # Request the redirect to defined provider
        api_instance.request_provider(provider)
    except Exception as e:
        print("Exception when calling AuthApi->request_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| An identifier for the auth provider | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**308** | Redirect to the provider |  -  |
**404** | Provider not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_auth**
> AuthVerify verify_auth()

Verify validity for an authentication token

### Example

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

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of the auth token |  -  |
**401** | Failed to generate or validate token |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

