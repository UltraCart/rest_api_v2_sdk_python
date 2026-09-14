# SfvbPageAttributeUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Attribute name.  Matched without regard to case against what the page already has, so you do not have to reproduce the exact casing.  A name nothing matches creates a new attribute. | [optional] 
**type** | **str** | Only consulted when creating an attribute no template declares.  For a declared attribute the template&#39;s type always wins, because the templates decide it and not the caller. | [optional] 
**value** | **str** | The value to store.  An empty string clears it.  For html the markup is stored as given and rendered as given.  For boolean send the text true or false. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


