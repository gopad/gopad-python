# gopad.AuthApi

All URIs are relative to *http://try.gopad.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_user**](AuthApi.md#login_user) | **POST** /auth/login | Authenticate an user by credentials
[**refresh_auth**](AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
[**verify_auth**](AuthApi.md#verify_auth) | **GET** /auth/verify/{token} | Verify validity for an authentication token


# **login_user**
> AuthToken login_user(params)

Authenticate an user by credentials

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.AuthApi()
params = gopad.AuthLogin() # AuthLogin | The credentials to authenticate

try:
    # Authenticate an user by credentials
    api_response = api_instance.login_user(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**AuthLogin**](AuthLogin.md)| The credentials to authenticate | 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_auth**
> AuthToken refresh_auth()

Refresh an auth token before it expires

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.AuthApi()

try:
    # Refresh an auth token before it expires
    api_response = api_instance.refresh_auth()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_auth**
> AuthVerify verify_auth(token)

Verify validity for an authentication token

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.AuthApi()
token = 'token_example' # str | A token that have to be checked

try:
    # Verify validity for an authentication token
    api_response = api_instance.verify_auth(token)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

