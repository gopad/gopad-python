# RedirectAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from gopad.models.redirect_auth_request import RedirectAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectAuthRequest from a JSON string
redirect_auth_request_instance = RedirectAuthRequest.from_json(json)
# print the JSON string representation of the object
print(RedirectAuthRequest.to_json())

# convert the object into a dict
redirect_auth_request_dict = redirect_auth_request_instance.to_dict()
# create an instance of RedirectAuthRequest from a dict
redirect_auth_request_from_dict = RedirectAuthRequest.from_dict(redirect_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


