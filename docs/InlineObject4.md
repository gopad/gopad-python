# InlineObject4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**user** | [**User**](User.md) |  | [optional] 
**groups** | [**List[UserGroup]**](UserGroup.md) |  | 

## Example

```python
from gopad.models.inline_object4 import InlineObject4

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject4 from a JSON string
inline_object4_instance = InlineObject4.from_json(json)
# print the JSON string representation of the object
print(InlineObject4.to_json())

# convert the object into a dict
inline_object4_dict = inline_object4_instance.to_dict()
# create an instance of InlineObject4 from a dict
inline_object4_from_dict = InlineObject4.from_dict(inline_object4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


