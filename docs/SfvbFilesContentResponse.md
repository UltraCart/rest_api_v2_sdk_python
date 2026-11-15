# SfvbFilesContentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**[SfvbFileContentResult]**](SfvbFileContentResult.md) | One entry per path read, in the order asked. | [optional] 
**remaining_paths** | **[str]** | Paths not read because the response reached its size limit, in the order asked.  Send them again to read them.  Omitted when every path was read. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


