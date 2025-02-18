# LoginAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from gopad.models.login_auth_request import LoginAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginAuthRequest from a JSON string
login_auth_request_instance = LoginAuthRequest.from_json(json)
# print the JSON string representation of the object
print(LoginAuthRequest.to_json())

# convert the object into a dict
login_auth_request_dict = login_auth_request_instance.to_dict()
# create an instance of LoginAuthRequest from a dict
login_auth_request_from_dict = LoginAuthRequest.from_dict(login_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


