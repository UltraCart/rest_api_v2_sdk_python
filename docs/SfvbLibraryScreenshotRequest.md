# SfvbLibraryScreenshotRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The staging key files/upload_url/png returned, after the PNG was PUT to its URL.  Redeemed once. | [optional] 
**sha256** | **str** | SHA-256 of the PNG bytes uploaded, lower case hex.  The upload is refused if it does not match. | [optional] 
**source** | **str** | Where the image came from.  own for a screenshot you took, licensed or stock otherwise.  Needed before the entry can be made public. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


