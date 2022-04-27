# gopad.UserApi

All URIs are relative to *http://try.gopad.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_user_to_team**](UserApi.md#append_user_to_team) | **POST** /users/{user_id}/teams | Assign a team to user
[**create_user**](UserApi.md#create_user) | **POST** /users | Create a new user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a specific user
[**delete_user_from_team**](UserApi.md#delete_user_from_team) | **DELETE** /users/{user_id}/teams | Remove a team from user
[**list_user_teams**](UserApi.md#list_user_teams) | **GET** /users/{user_id}/teams | Fetch all teams assigned to user
[**list_users**](UserApi.md#list_users) | **GET** /users | Fetch all available users
[**permit_user_team**](UserApi.md#permit_user_team) | **PUT** /users/{user_id}/teams | Update team perms for user
[**show_user**](UserApi.md#show_user) | **GET** /users/{user_id} | Fetch a specific user
[**update_user**](UserApi.md#update_user) | **PUT** /users/{user_id} | Update a specific user


# **append_user_to_team**
> GeneralError append_user_to_team(user_id, user_team)

Assign a team to user

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.user_team_params import UserTeamParams
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
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | A user UUID or slug
    user_team = UserTeamParams(
        team="team_example",
        perm="user",
    ) # UserTeamParams | The user team data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a team to user
        api_response = api_instance.append_user_to_team(user_id, user_team)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->append_user_to_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug |
 **user_team** | [**UserTeamParams**](UserTeamParams.md)| The user team data to assign |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Team is already assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(user)

Create a new user

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.validation_error import ValidationError
from gopad.model.general_error import GeneralError
from gopad.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user = User(
        slug="slug_example",
        username="username_example",
        password="password_example",
        email="email_example",
        admin=True,
        active=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # User | The user data to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new user
        api_response = api_instance.create_user(user)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| The user data to create |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created user data |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> GeneralError delete_user(user_id)

Delete a specific user

### Example


```python
import time
import gopad
from gopad.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | A user UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific user
        api_response = api_instance.delete_user(user_id)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to delete the user |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_team**
> GeneralError delete_user_from_team(user_id, user_team)

Remove a team from user

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.user_team_params import UserTeamParams
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
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | A user UUID or slug
    user_team = UserTeamParams(
        team="team_example",
        perm="user",
    ) # UserTeamParams | The user team data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a team from user
        api_response = api_instance.delete_user_from_team(user_id, user_team)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->delete_user_from_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug |
 **user_team** | [**UserTeamParams**](UserTeamParams.md)| The user team data to delete |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Team is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_teams**
> [TeamUser] list_user_teams(user_id)

Fetch all teams assigned to user

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.general_error import GeneralError
from gopad.model.team_user import TeamUser
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | A user UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all teams assigned to user
        api_response = api_instance.list_user_teams(user_id)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->list_user_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug |

### Return type

[**[TeamUser]**](TeamUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of user teams |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> [User] list_users()

Fetch all available users

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.general_error import GeneralError
from gopad.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all available users
        api_response = api_instance.list_users()
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of users |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_team**
> GeneralError permit_user_team(user_id, user_team)

Update team perms for user

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.user_team_params import UserTeamParams
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
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | A user UUID or slug
    user_team = UserTeamParams(
        team="team_example",
        perm="user",
    ) # UserTeamParams | The user team data to update

    # example passing only required values which don't have defaults set
    try:
        # Update team perms for user
        api_response = api_instance.permit_user_team(user_id, user_team)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->permit_user_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug |
 **user_team** | [**UserTeamParams**](UserTeamParams.md)| The user team data to update |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Team is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_user**
> User show_user(user_id)

Fetch a specific user

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.general_error import GeneralError
from gopad.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | A user UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch a specific user
        api_response = api_instance.show_user(user_id)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->show_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched user details |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, user)

Update a specific user

### Example


```python
import time
import gopad
from gopad.api import user_api
from gopad.model.validation_error import ValidationError
from gopad.model.general_error import GeneralError
from gopad.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to http://try.gopad.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gopad.Configuration(
    host = "http://try.gopad.tech/api/v1"
)


# Enter a context with an instance of the API client
with gopad.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | A user UUID or slug
    user = User(
        slug="slug_example",
        username="username_example",
        password="password_example",
        email="email_example",
        admin=True,
        active=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # User | The user data to update

    # example passing only required values which don't have defaults set
    try:
        # Update a specific user
        api_response = api_instance.update_user(user_id, user)
        pprint(api_response)
    except gopad.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug |
 **user** | [**User**](User.md)| The user data to update |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated user details |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

