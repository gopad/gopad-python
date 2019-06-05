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
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
user_team = gopad.UserTeamParams() # UserTeamParams | The user team data to assign

try:
    # Assign a team to user
    api_response = api_instance.append_user_to_team(user_id, user_team)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(user)

Create a new user

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user = gopad.User() # User | The user data to create

try:
    # Create a new user
    api_response = api_instance.create_user(user)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> GeneralError delete_user(user_id)

Delete a specific user

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Delete a specific user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_team**
> GeneralError delete_user_from_team(user_id, user_team)

Remove a team from user

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
user_team = gopad.UserTeamParams() # UserTeamParams | The user team data to delete

try:
    # Remove a team from user
    api_response = api_instance.delete_user_from_team(user_id, user_team)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_teams**
> list[TeamUser] list_user_teams(user_id)

Fetch all teams assigned to user

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Fetch all teams assigned to user
    api_response = api_instance.list_user_teams(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 

### Return type

[**list[TeamUser]**](TeamUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list[User] list_users()

Fetch all available users

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()

try:
    # Fetch all available users
    api_response = api_instance.list_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_team**
> GeneralError permit_user_team(user_id, user_team)

Update team perms for user

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
user_team = gopad.UserTeamParams() # UserTeamParams | The user team data to update

try:
    # Update team perms for user
    api_response = api_instance.permit_user_team(user_id, user_team)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_user**
> User show_user(user_id)

Fetch a specific user

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Fetch a specific user
    api_response = api_instance.show_user(user_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, user)

Update a specific user

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
user = gopad.User() # User | The user data to update

try:
    # Update a specific user
    api_response = api_instance.update_user(user_id, user)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

