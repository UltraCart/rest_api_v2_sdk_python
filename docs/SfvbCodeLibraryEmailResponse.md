# SfvbCodeLibraryEmailResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **bool** | On a save, true when this request made the item and false when an earlier save with the same uuid had, in which case nothing changed.  Absent on a read. | [optional] 
**email** | [**SfvbCodeLibraryEmailDetail**](SfvbCodeLibraryEmailDetail.md) |  | [optional] 
**files_skipped** | [**[SfvbCodeLibraryFileSkipped]**](SfvbCodeLibraryFileSkipped.md) | On a save, the files the body names that the item does not carry, each with the reason.  Absent on a read. | [optional] 
**notes** | **[str]** | Plain sentences about the save, for example executable elements or absolute file URLs in the body. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


