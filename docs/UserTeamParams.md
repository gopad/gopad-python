# UserTeamParams

Parameters to attach or unlink user team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'user']

## Example

```python
from gopad.models.user_team_params import UserTeamParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserTeamParams from a JSON string
user_team_params_instance = UserTeamParams.from_json(json)
# print the JSON string representation of the object
print(UserTeamParams.to_json())

# convert the object into a dict
user_team_params_dict = user_team_params_instance.to_dict()
# create an instance of UserTeamParams from a dict
user_team_params_from_dict = UserTeamParams.from_dict(user_team_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


