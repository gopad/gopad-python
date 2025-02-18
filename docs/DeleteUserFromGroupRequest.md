# DeleteUserFromGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 

## Example

```python
from gopad.models.delete_user_from_group_request import DeleteUserFromGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserFromGroupRequest from a JSON string
delete_user_from_group_request_instance = DeleteUserFromGroupRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteUserFromGroupRequest.to_json())

# convert the object into a dict
delete_user_from_group_request_dict = delete_user_from_group_request_instance.to_dict()
# create an instance of DeleteUserFromGroupRequest from a dict
delete_user_from_group_request_from_dict = DeleteUserFromGroupRequest.from_dict(delete_user_from_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


