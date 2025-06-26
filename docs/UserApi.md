# gopad.UserApi

All URIs are relative to *https://try.gopad.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_user_to_group**](UserApi.md#attach_user_to_group) | **POST** /users/{user_id}/groups | Attach a group to user
[**create_user**](UserApi.md#create_user) | **POST** /users | Create a new user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a specific user
[**delete_user_from_group**](UserApi.md#delete_user_from_group) | **DELETE** /users/{user_id}/groups | Unlink a group from user
[**list_user_groups**](UserApi.md#list_user_groups) | **GET** /users/{user_id}/groups | Fetch all groups attached to user
[**list_users**](UserApi.md#list_users) | **GET** /users | Fetch all available users
[**permit_user_group**](UserApi.md#permit_user_group) | **PUT** /users/{user_id}/groups | Update group perms for user
[**show_user**](UserApi.md#show_user) | **GET** /users/{user_id} | Fetch a specific user
[**update_user**](UserApi.md#update_user) | **PUT** /users/{user_id} | Update a specific user


# **attach_user_to_group**
> Notification attach_user_to_group(user_id, permit_user_group_request)

Attach a group to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.notification import Notification
from gopad.models.permit_user_group_request import PermitUserGroupRequest
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
    api_instance = gopad.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_user_group_request = gopad.PermitUserGroupRequest() # PermitUserGroupRequest | The user group data to permit

    try:
        # Attach a group to user
        api_response = api_instance.attach_user_to_group(user_id, permit_user_group_request)
        print("The response of UserApi->attach_user_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->attach_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_user_group_request** | [**PermitUserGroupRequest**](PermitUserGroupRequest.md)| The user group data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(create_user_request)

Create a new user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.create_user_request import CreateUserRequest
from gopad.models.user import User
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
    api_instance = gopad.UserApi(api_client)
    create_user_request = gopad.CreateUserRequest() # CreateUserRequest | The user data to create

    try:
        # Create a new user
        api_response = api_instance.create_user(create_user_request)
        print("The response of UserApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| The user data to create | 

### Return type

[**User**](User.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for an user |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Notification delete_user(user_id)

Delete a specific user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

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
    api_instance = gopad.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug

    try:
        # Delete a specific user
        api_response = api_instance.delete_user(user_id)
        print("The response of UserApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**400** | Failed to execute action for resource |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_group**
> Notification delete_user_from_group(user_id, delete_user_from_group_request)

Unlink a group from user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.delete_user_from_group_request import DeleteUserFromGroupRequest
from gopad.models.notification import Notification
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
    api_instance = gopad.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    delete_user_from_group_request = gopad.DeleteUserFromGroupRequest() # DeleteUserFromGroupRequest | The user group data to unlink

    try:
        # Unlink a group from user
        api_response = api_instance.delete_user_from_group(user_id, delete_user_from_group_request)
        print("The response of UserApi->delete_user_from_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **delete_user_from_group_request** | [**DeleteUserFromGroupRequest**](DeleteUserFromGroupRequest.md)| The user group data to unlink | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_groups**
> InlineObject4 list_user_groups(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all groups attached to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.inline_object4 import InlineObject4
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
    api_instance = gopad.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all groups attached to user
        api_response = api_instance.list_user_groups(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of UserApi->list_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**InlineObject4**](InlineObject4.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of user groups |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> InlineObject3 list_users(search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available users

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.inline_object3 import InlineObject3
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
    api_instance = gopad.UserApi(api_client)
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all available users
        api_response = api_instance.list_users(search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of UserApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**InlineObject3**](InlineObject3.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of users |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_group**
> Notification permit_user_group(user_id, permit_user_group_request)

Update group perms for user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.notification import Notification
from gopad.models.permit_user_group_request import PermitUserGroupRequest
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
    api_instance = gopad.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_user_group_request = gopad.PermitUserGroupRequest() # PermitUserGroupRequest | The user group data to permit

    try:
        # Update group perms for user
        api_response = api_instance.permit_user_group(user_id, permit_user_group_request)
        print("The response of UserApi->permit_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->permit_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_user_group_request** | [**PermitUserGroupRequest**](PermitUserGroupRequest.md)| The user group data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_user**
> User show_user(user_id)

Fetch a specific user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.user import User
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
    api_instance = gopad.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug

    try:
        # Fetch a specific user
        api_response = api_instance.show_user(user_id)
        print("The response of UserApi->show_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->show_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 

### Return type

[**User**](User.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for an user |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, update_user_request)

Update a specific user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.update_user_request import UpdateUserRequest
from gopad.models.user import User
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
    api_instance = gopad.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    update_user_request = gopad.UpdateUserRequest() # UpdateUserRequest | The user data to update

    try:
        # Update a specific user
        api_response = api_instance.update_user(user_id, update_user_request)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)| The user data to update | 

### Return type

[**User**](User.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for an user |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

