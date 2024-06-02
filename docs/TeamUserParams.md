# TeamUserParams

Parameters to attach or remove team user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'user']

## Example

```python
from gopad.models.team_user_params import TeamUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of TeamUserParams from a JSON string
team_user_params_instance = TeamUserParams.from_json(json)
# print the JSON string representation of the object
print(TeamUserParams.to_json())

# convert the object into a dict
team_user_params_dict = team_user_params_instance.to_dict()
# create an instance of TeamUserParams from a dict
team_user_params_from_dict = TeamUserParams.from_dict(team_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


