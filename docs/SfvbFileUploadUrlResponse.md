# SfvbFileUploadUrlResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in_seconds** | **int** | Seconds until the upload URL stops working.  Ask for a new one rather than holding this across a long job. | [optional] 
**http_method** | **str** | HTTP method the upload URL expects. | [optional] 
**key** | **str** | Quote this back to the upload endpoint once the bytes are in place.  It identifies the uploaded object and is bound to your account. | [optional] 
**upload_url** | **str** | Send the raw bytes to this URL.  It is short lived and single use, and it is not part of this API - do not send an Authorization header with it. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


