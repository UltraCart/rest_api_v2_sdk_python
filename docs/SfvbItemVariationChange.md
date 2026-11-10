# SfvbItemVariationChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axis** | **str** | The axis the change is about. | [optional] 
**before** | **str** | add_option puts the new option before this one.  Otherwise it goes last. | [optional] 
**child** | **str** | set_combination - the child item id, or null to clear the combination. | [optional] 
**default** | **bool** | add_option and add_axis make the option the default. | [optional] 
**default_text** | **str** | The prompt, for add_axis and set_default_text.  Null clears it. | [optional] 
**multimedia_oid** | **int** | An image of the parent item.  For set_option_multimedia null clears it; for set_combination null keeps the current one. | [optional] 
**op** | **str** | add_axis, remove_axis, rename_axis, add_option, remove_option, rename_option, reorder_options, set_default, set_default_text, set_option_multimedia or set_combination. | [optional] 
**quantity** | **int** | set_combination - how many of the child the combination adds.  Defaults to 1. | [optional] 
**to** | **str** | The new name, for rename_axis and rename_option. | [optional] 
**value** | **str** | The option the change is about. | [optional] 
**values** | **[str]** | add_axis options in order, or every option in its new order for reorder_options. | [optional] 
**variation_values** | [**[SfvbItemVariationValue]**](SfvbItemVariationValue.md) | set_combination - one axis and option per axis. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


