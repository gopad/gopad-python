# gopad.GroupApi

All URIs are relative to *https://try.gopad.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_group_to_user**](GroupApi.md#attach_group_to_user) | **POST** /groups/{group_id}/users | Attach a user to group
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create a new group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /groups/{group_id} | Delete a specific group
[**delete_group_from_user**](GroupApi.md#delete_group_from_user) | **DELETE** /groups/{group_id}/users | Unlink a user from group
[**list_group_users**](GroupApi.md#list_group_users) | **GET** /groups/{group_id}/users | Fetch all users attached to group
[**list_groups**](GroupApi.md#list_groups) | **GET** /groups | Fetch all available groups
[**permit_group_user**](GroupApi.md#permit_group_user) | **PUT** /groups/{group_id}/users | Update user perms for group
[**show_group**](GroupApi.md#show_group) | **GET** /groups/{group_id} | Fetch a specific group
[**update_group**](GroupApi.md#update_group) | **PUT** /groups/{group_id} | Update a specific group


# **attach_group_to_user**
> Notification attach_group_to_user(group_id, permit_group_user_request)

Attach a user to group

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.notification import Notification
from gopad.models.permit_group_user_request import PermitGroupUserRequest
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
    api_instance = gopad.GroupApi(api_client)
    group_id = 'group_id_example' # str | A group identifier or slug
    permit_group_user_request = gopad.PermitGroupUserRequest() # PermitGroupUserRequest | The group user data to permit

    try:
        # Attach a user to group
        api_response = api_instance.attach_group_to_user(group_id, permit_group_user_request)
        print("The response of GroupApi->attach_group_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->attach_group_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A group identifier or slug | 
 **permit_group_user_request** | [**PermitGroupUserRequest**](PermitGroupUserRequest.md)| The group user data to permit | 

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

# **create_group**
> Group create_group(create_group_request)

Create a new group

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.create_group_request import CreateGroupRequest
from gopad.models.group import Group
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
    api_instance = gopad.GroupApi(api_client)
    create_group_request = gopad.CreateGroupRequest() # CreateGroupRequest | The group data to create

    try:
        # Create a new group
        api_response = api_instance.create_group(create_group_request)
        print("The response of GroupApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_request** | [**CreateGroupRequest**](CreateGroupRequest.md)| The group data to create | 

### Return type

[**Group**](Group.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for a group |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> Notification delete_group(group_id)

Delete a specific group

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
    api_instance = gopad.GroupApi(api_client)
    group_id = 'group_id_example' # str | A group identifier or slug

    try:
        # Delete a specific group
        api_response = api_instance.delete_group(group_id)
        print("The response of GroupApi->delete_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A group identifier or slug | 

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

# **delete_group_from_user**
> Notification delete_group_from_user(group_id, delete_group_from_user_request)

Unlink a user from group

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.delete_group_from_user_request import DeleteGroupFromUserRequest
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
    api_instance = gopad.GroupApi(api_client)
    group_id = 'group_id_example' # str | A group identifier or slug
    delete_group_from_user_request = gopad.DeleteGroupFromUserRequest() # DeleteGroupFromUserRequest | The group user data to unlink

    try:
        # Unlink a user from group
        api_response = api_instance.delete_group_from_user(group_id, delete_group_from_user_request)
        print("The response of GroupApi->delete_group_from_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A group identifier or slug | 
 **delete_group_from_user_request** | [**DeleteGroupFromUserRequest**](DeleteGroupFromUserRequest.md)| The group user data to unlink | 

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

# **list_group_users**
> InlineObject2 list_group_users(group_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all users attached to group

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.inline_object2 import InlineObject2
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
    api_instance = gopad.GroupApi(api_client)
    group_id = 'group_id_example' # str | A group identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all users attached to group
        api_response = api_instance.list_group_users(group_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of GroupApi->list_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_group_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A group identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**InlineObject2**](InlineObject2.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of group users |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> InlineObject1 list_groups(search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available groups

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.inline_object1 import InlineObject1
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
    api_instance = gopad.GroupApi(api_client)
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all available groups
        api_response = api_instance.list_groups(search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of GroupApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_groups: %s\n" % e)
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

[**InlineObject1**](InlineObject1.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of groups |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_group_user**
> Notification permit_group_user(group_id, permit_group_user_request)

Update user perms for group

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.notification import Notification
from gopad.models.permit_group_user_request import PermitGroupUserRequest
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
    api_instance = gopad.GroupApi(api_client)
    group_id = 'group_id_example' # str | A group identifier or slug
    permit_group_user_request = gopad.PermitGroupUserRequest() # PermitGroupUserRequest | The group user data to permit

    try:
        # Update user perms for group
        api_response = api_instance.permit_group_user(group_id, permit_group_user_request)
        print("The response of GroupApi->permit_group_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->permit_group_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A group identifier or slug | 
 **permit_group_user_request** | [**PermitGroupUserRequest**](PermitGroupUserRequest.md)| The group user data to permit | 

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

# **show_group**
> Group show_group(group_id)

Fetch a specific group

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.group import Group
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
    api_instance = gopad.GroupApi(api_client)
    group_id = 'group_id_example' # str | A group identifier or slug

    try:
        # Fetch a specific group
        api_response = api_instance.show_group(group_id)
        print("The response of GroupApi->show_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->show_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A group identifier or slug | 

### Return type

[**Group**](Group.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for a group |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(group_id, create_group_request)

Update a specific group

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import gopad
from gopad.models.create_group_request import CreateGroupRequest
from gopad.models.group import Group
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
    api_instance = gopad.GroupApi(api_client)
    group_id = 'group_id_example' # str | A group identifier or slug
    create_group_request = gopad.CreateGroupRequest() # CreateGroupRequest | The group data to update

    try:
        # Update a specific group
        api_response = api_instance.update_group(group_id, create_group_request)
        print("The response of GroupApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A group identifier or slug | 
 **create_group_request** | [**CreateGroupRequest**](CreateGroupRequest.md)| The group data to update | 

### Return type

[**Group**](Group.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for a group |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

