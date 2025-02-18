# PermitGroupUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**perm** | **str** |  | 

## Example

```python
from gopad.models.permit_group_user_request import PermitGroupUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermitGroupUserRequest from a JSON string
permit_group_user_request_instance = PermitGroupUserRequest.from_json(json)
# print the JSON string representation of the object
print(PermitGroupUserRequest.to_json())

# convert the object into a dict
permit_group_user_request_dict = permit_group_user_request_instance.to_dict()
# create an instance of PermitGroupUserRequest from a dict
permit_group_user_request_from_dict = PermitGroupUserRequest.from_dict(permit_group_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


