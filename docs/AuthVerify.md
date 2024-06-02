# AuthVerify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from gopad.models.auth_verify import AuthVerify

# TODO update the JSON string below
json = "{}"
# create an instance of AuthVerify from a JSON string
auth_verify_instance = AuthVerify.from_json(json)
# print the JSON string representation of the object
print(AuthVerify.to_json())

# convert the object into a dict
auth_verify_dict = auth_verify_instance.to_dict()
# create an instance of AuthVerify from a dict
auth_verify_from_dict = AuthVerify.from_dict(auth_verify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


