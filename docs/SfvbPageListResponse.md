# SfvbPageListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** | The offset of the next window, omitted on the last one.  Only with detail&#x3D;true. | [optional] 
**pages** | [**[SfvbPageSummary]**](SfvbPageSummary.md) | Pages sorted by path, the root first.  Hidden pages are included. | [optional] 
**total** | **int** | How many pages the whole list has.  Only with detail&#x3D;true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


