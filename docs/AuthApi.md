# gopad.AuthApi

All URIs are relative to *http://try.gopad.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_user**](AuthApi.md#login_user) | **POST** /auth/login | Authenticate an user by credentials
[**refresh_auth**](AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
[**verify_auth**](AuthApi.md#verify_auth) | **GET** /auth/verify/{token} | Verify validity for an authentication token


# **login_user**
> AuthToken login_user(auth_login)

Authenticate an user by credentials

### Example


```python
import time
import gopad
from gopad.api import auth_api
from gopad.model.auth_login import AuthLogin
from gopad.model.auth_token import AuthToken
from gopad.model.general_error import GeneralError
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    auth_login = AuthLogin(
        username="username_example",
        password="password_example",
    ) # AuthLogin | The credentials to authenticate

    # example passing only required values which don't have defaults set
    try:
        # Authenticate an user by credentials
        api_response = api_instance.login_user(auth_login)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling AuthApi->login_user: %s\n" % e)
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
**200** | A generated token with expire |  -  |
**401** | Unauthorized if wrong credentials |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_auth**
> AuthToken refresh_auth()

Refresh an auth token before it expires

### Example


```python
import time
import gopad
from gopad.api import auth_api
from gopad.model.auth_token import AuthToken
from gopad.model.general_error import GeneralError
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Refresh an auth token before it expires
        api_response = api_instance.refresh_auth()
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling AuthApi->refresh_auth: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A refreshed token with expire |  -  |
**401** | Unauthorized if failed to generate |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_auth**
> AuthVerify verify_auth(token)

Verify validity for an authentication token

### Example


```python
import time
import gopad
from gopad.api import auth_api
from gopad.model.auth_verify import AuthVerify
from gopad.model.general_error import GeneralError
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    token = "token_example" # str | A token that have to be checked

    # example passing only required values which don't have defaults set
    try:
        # Verify validity for an authentication token
        api_response = api_instance.verify_auth(token)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling AuthApi->verify_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| A token that have to be checked |

### Return type

[**AuthVerify**](AuthVerify.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Meta data of the provided token |  -  |
**401** | Unauthorized if token is invalid |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

