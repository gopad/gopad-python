# ListUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**users** | [**List[User]**](User.md) |  | 

## Example

```python
from gopad.models.list_users200_response import ListUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsers200Response from a JSON string
list_users200_response_instance = ListUsers200Response.from_json(json)
# print the JSON string representation of the object
print(ListUsers200Response.to_json())

# convert the object into a dict
list_users200_response_dict = list_users200_response_instance.to_dict()
# create an instance of ListUsers200Response from a dict
list_users200_response_from_dict = ListUsers200Response.from_dict(list_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


