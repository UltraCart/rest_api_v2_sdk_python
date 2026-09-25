# SfvbTemplateResolvePath


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidates** | [**[SfvbTemplateResolveCandidate]**](SfvbTemplateResolveCandidate.md) | Every file of that name below this path, in the order the storefront searches. | [optional] 
**directory_found** | **bool** | False when the theme has no such directory, so the storefront skips this path. | [optional] 
**match** | **str** | The candidate this path supplies, relative to the theme root, or null.  It is the first candidate that is not skipped. | [optional] 
**_resource_path** | **str** | The resource path, relative to the theme root.  / is the theme root itself. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


