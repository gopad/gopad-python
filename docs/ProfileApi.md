# gopad.ProfileApi

All URIs are relative to *http://try.gopad.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_profile**](ProfileApi.md#show_profile) | **GET** /profile/self | Retrieve an unlimited auth token
[**token_profile**](ProfileApi.md#token_profile) | **GET** /profile/token | Retrieve an unlimited auth token
[**update_profile**](ProfileApi.md#update_profile) | **PUT** /profile/self | Retrieve an unlimited auth token


# **show_profile**
> Profile show_profile()

Retrieve an unlimited auth token

### Example


```python
import time
import gopad
from gopad.api import profile_api
from gopad.model.general_error import GeneralError
from gopad.model.profile import Profile
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = profile_api.ProfileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve an unlimited auth token
        api_response = api_instance.show_profile()
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling ProfileApi->show_profile: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current profile data |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_profile**
> AuthToken token_profile()

Retrieve an unlimited auth token

### Example


```python
import time
import gopad
from gopad.api import profile_api
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
    api_instance = profile_api.ProfileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve an unlimited auth token
        api_response = api_instance.token_profile()
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling ProfileApi->token_profile: %s\n" % e)
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
**200** | The unlimited auth token |  -  |
**403** | User is not authorized |  -  |
**500** | Failed to generate a token |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> Profile update_profile(profile)

Retrieve an unlimited auth token

### Example


```python
import time
import gopad
from gopad.api import profile_api
from gopad.model.validation_error import ValidationError
from gopad.model.general_error import GeneralError
from gopad.model.profile import Profile
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = profile_api.ProfileApi(api_client)
    profile = Profile(
        slug="slug_example",
        username="username_example",
        password="password_example",
        email="email_example",
        admin=True,
        active=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Profile | The profile data to update

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an unlimited auth token
        api_response = api_instance.update_profile(profile)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling ProfileApi->update_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**Profile**](Profile.md)| The profile data to update |

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated profile data |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

