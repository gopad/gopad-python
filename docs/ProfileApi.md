# gopad.ProfileApi

All URIs are relative to *http://http:/api/v1*

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
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.ProfileApi()

try:
    # Retrieve an unlimited auth token
    api_response = api_instance.show_profile()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_profile**
> AuthToken token_profile()

Retrieve an unlimited auth token

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.ProfileApi()

try:
    # Retrieve an unlimited auth token
    api_response = api_instance.token_profile()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> Profile update_profile(profile)

Retrieve an unlimited auth token

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.ProfileApi()
profile = gopad.Profile() # Profile | The profile data to update

try:
    # Retrieve an unlimited auth token
    api_response = api_instance.update_profile(profile)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

