# PermitUserGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**perm** | **str** |  | 

## Example

```python
from gopad.models.permit_user_group_request import PermitUserGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermitUserGroupRequest from a JSON string
permit_user_group_request_instance = PermitUserGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PermitUserGroupRequest.to_json())

# convert the object into a dict
permit_user_group_request_dict = permit_user_group_request_instance.to_dict()
# create an instance of PermitUserGroupRequest from a dict
permit_user_group_request_from_dict = PermitUserGroupRequest.from_dict(permit_user_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


