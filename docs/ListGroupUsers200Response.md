# ListGroupUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**group** | [**Group**](Group.md) |  | [optional] 
**users** | [**List[UserGroup]**](UserGroup.md) |  | 

## Example

```python
from gopad.models.list_group_users200_response import ListGroupUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListGroupUsers200Response from a JSON string
list_group_users200_response_instance = ListGroupUsers200Response.from_json(json)
# print the JSON string representation of the object
print(ListGroupUsers200Response.to_json())

# convert the object into a dict
list_group_users200_response_dict = list_group_users200_response_instance.to_dict()
# create an instance of ListGroupUsers200Response from a dict
list_group_users200_response_from_dict = ListGroupUsers200Response.from_dict(list_group_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


