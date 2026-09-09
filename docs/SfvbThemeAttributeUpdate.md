# SfvbThemeAttributeUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font** | [**SfvbThemeFont**](SfvbThemeFont.md) |  | [optional] 
**name** | **str** | Slot name.  Matched without regard to case against what the theme already has, so you do not have to reproduce the exact casing.  A name nothing matches creates a new slot. | [optional] 
**type** | **str** | Only consulted when creating a slot the theme does not already have.  For a slot that exists the declared type always wins, because the templates decide it and not the caller. | [optional] 
**value** | **str** | The value to store.  An empty string clears the slot, which makes it fall back to the theme&#39;s default rather than removing it.  Ignored for a font when the font field is supplied. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


