# ListProviders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**providers** | [**List[Provider]**](Provider.md) |  | 

## Example

```python
from gopad.models.list_providers200_response import ListProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListProviders200Response from a JSON string
list_providers200_response_instance = ListProviders200Response.from_json(json)
# print the JSON string representation of the object
print(ListProviders200Response.to_json())

# convert the object into a dict
list_providers200_response_dict = list_providers200_response_instance.to_dict()
# create an instance of ListProviders200Response from a dict
list_providers200_response_from_dict = ListProviders200Response.from_dict(list_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


