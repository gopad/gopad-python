# Profile

Model to represent profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**admin** | **bool** |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**auths** | [**List[UserAuth]**](UserAuth.md) |  | [optional] [readonly] 
**groups** | [**List[UserGroup]**](UserGroup.md) |  | [optional] [readonly] 

## Example

```python
from gopad.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


