# SfvbCodeLibraryEmailCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_cjson** | **str** | The email body, a container that passes the email container rules. | [optional] 
**description** | **str** | Up to 1000 characters on one line, or empty. | [optional] 
**preview_text** | **str** | The preview text a new email started from the item takes, 5 to 150 characters on one line. | [optional] 
**subject** | **str** | The subject a new email started from the item takes, 5 to 150 characters on one line. | [optional] 
**title** | **str** | The title the new-email picker shows, 4 to 100 characters on one line. | [optional] 
**uuid** | **str** | A UUID the caller makes for this save.  Sending the same uuid again returns the item it saved, unchanged, so a retry after an uncertain response never makes a second item. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


