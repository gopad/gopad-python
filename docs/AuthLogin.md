# AuthLogin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from gopad.models.auth_login import AuthLogin

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLogin from a JSON string
auth_login_instance = AuthLogin.from_json(json)
# print the JSON string representation of the object
print(AuthLogin.to_json())

# convert the object into a dict
auth_login_dict = auth_login_instance.to_dict()
# create an instance of AuthLogin from a dict
auth_login_from_dict = AuthLogin.from_dict(auth_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


