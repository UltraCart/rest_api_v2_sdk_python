# SfvbCodeLibraryEmailDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_cjson** | **str** | The item&#39;s body as stored.  Starting a new email from it gives its elements new ids. | [optional] 
**description** | **str** | The item&#39;s description. | [optional] 
**files** | [**[SfvbCodeLibraryFile]**](SfvbCodeLibraryFile.md) | The image files the item carries, without their contents. | [optional] 
**library_item_oid** | **int** | The item, to send as library_item_oid on the step insert. | [optional] 
**preview_text** | **str** | The preview text a new email takes from the item, or null when it has none. | [optional] 
**source** | **str** | owned (this account&#39;s own), shared (shared with this account) or public (published and approved by UltraCart). | [optional] 
**subject** | **str** | The subject a new email takes from the item, or null when it has none. | [optional] 
**title** | **str** | The item&#39;s title. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


