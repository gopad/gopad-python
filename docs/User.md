# User

Model to represent user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**admin** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**auths** | [**List[UserAuth]**](UserAuth.md) |  | [optional] [readonly] 
**teams** | [**List[UserTeam]**](UserTeam.md) |  | [optional] [readonly] 

## Example

```python
from gopad.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


