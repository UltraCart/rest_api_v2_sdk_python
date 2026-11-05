# SfvbCommsProviderImportResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | True when nothing was imported. | [optional] 
**lists** | [**[SfvbCommsProviderList]**](SfvbCommsProviderList.md) | The lists imported, each into a new list of the same name. | [optional] 
**notes** | **[str]** | What the import does. | [optional] 
**provider** | **str** | The provider. | [optional] 
**queued** | **bool** | True when the import was started.  It runs in the background and emails the signed-in user when done. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


