# UserAuth

Model to represent user auth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from gopad.models.user_auth import UserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of UserAuth from a JSON string
user_auth_instance = UserAuth.from_json(json)
# print the JSON string representation of the object
print(UserAuth.to_json())

# convert the object into a dict
user_auth_dict = user_auth_instance.to_dict()
# create an instance of UserAuth from a dict
user_auth_from_dict = UserAuth.from_dict(user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


