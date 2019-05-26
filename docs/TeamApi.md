# gopad.TeamApi

All URIs are relative to *http://http:/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_team_to_user**](TeamApi.md#append_team_to_user) | **POST** /teams/{team_id}/users | Assign a user to team
[**create_team**](TeamApi.md#create_team) | **POST** /teams | Create a new team
[**delete_team**](TeamApi.md#delete_team) | **DELETE** /teams/{team_id} | Delete a specific team
[**delte_team_from_user**](TeamApi.md#delte_team_from_user) | **DELETE** /teams/{team_id}/users | Remove a user from team
[**list_team_users**](TeamApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all users assigned to team
[**list_teams**](TeamApi.md#list_teams) | **GET** /teams | Fetch all available teams
[**permit_team_user**](TeamApi.md#permit_team_user) | **PUT** /teams/{team_id}/users | Update user perms for team
[**show_team**](TeamApi.md#show_team) | **GET** /teams/{team_id} | Fetch a specific team
[**update_team**](TeamApi.md#update_team) | **PUT** /teams/{team_id} | Update a specific team


# **append_team_to_user**
> object append_team_to_user(team_id, team_user)

Assign a user to team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
team_user = gopad.TeamUserParams() # TeamUserParams | The team user data to assign

try:
    # Assign a user to team
    api_response = api_instance.append_team_to_user(team_id, team_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->append_team_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **team_user** | [**TeamUserParams**](TeamUserParams.md)| The team user data to assign | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> Team create_team(team)

Create a new team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team = gopad.Team() # Team | The team data to create

try:
    # Create a new team
    api_response = api_instance.create_team(team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)| The team data to create | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> object delete_team(team_id)

Delete a specific team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Delete a specific team
    api_response = api_instance.delete_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delte_team_from_user**
> object delte_team_from_user(team_id, team_user)

Remove a user from team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
team_user = gopad.TeamUserParams() # TeamUserParams | The team user data to delete

try:
    # Remove a user from team
    api_response = api_instance.delte_team_from_user(team_id, team_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delte_team_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **team_user** | [**TeamUserParams**](TeamUserParams.md)| The team user data to delete | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_users**
> list[TeamUser] list_team_users(team_id)

Fetch all users assigned to team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Fetch all users assigned to team
    api_response = api_instance.list_team_users(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_team_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

[**list[TeamUser]**](TeamUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> list[Team] list_teams()

Fetch all available teams

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()

try:
    # Fetch all available teams
    api_response = api_instance.list_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_user**
> object permit_team_user(team_id, team_user)

Update user perms for team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
team_user = gopad.TeamUserParams() # TeamUserParams | The team user data to update

try:
    # Update user perms for team
    api_response = api_instance.permit_team_user(team_id, team_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->permit_team_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **team_user** | [**TeamUserParams**](TeamUserParams.md)| The team user data to update | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_team**
> Team show_team(team_id)

Fetch a specific team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Fetch a specific team
    api_response = api_instance.show_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->show_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(team_id, team)

Update a specific team

### Example

```python
from __future__ import print_function
import time
import gopad
from gopad.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gopad.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
team = gopad.Team() # Team | The team data to update

try:
    # Update a specific team
    api_response = api_instance.update_team(team_id, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **team** | [**Team**](Team.md)| The team data to update | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

