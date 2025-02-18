# ListUserGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**user** | [**User**](User.md) |  | [optional] 
**groups** | [**List[UserGroup]**](UserGroup.md) |  | 

## Example

```python
from gopad.models.list_user_groups200_response import ListUserGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserGroups200Response from a JSON string
list_user_groups200_response_instance = ListUserGroups200Response.from_json(json)
# print the JSON string representation of the object
print(ListUserGroups200Response.to_json())

# convert the object into a dict
list_user_groups200_response_dict = list_user_groups200_response_instance.to_dict()
# create an instance of ListUserGroups200Response from a dict
list_user_groups200_response_from_dict = ListUserGroups200Response.from_dict(list_user_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


