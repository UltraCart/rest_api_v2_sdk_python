# SfvbFileContentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_compiled** | **bool** | True when this file is compiler output and must not be edited directly. | [optional] 
**content** | **str** | UTF-8 content.  Only text/* files can be read this way. | [optional] 
**fs_file_oid** | **int** | StoreFront file system file oid. | [optional] 
**hash_sha256** | **str** | SHA-256 of the content.  Also returned as the ETag header; send it back as If-Match when writing. | [optional] 
**mime_type** | **str** | Mime type. | [optional] 
**path** | **str** | Full path of the file. | [optional] 
**size** | **int** | Size in bytes. | [optional] 
**truncated** | **bool** | True when the content was cut short.  Never truncated silently. | [optional] 
**valid** | **bool** | False when the file failed Velocity validation on its last write. | [optional] 
**velocity_errors** | **str** | Velocity errors recorded on the last write.  Null when valid. | [optional] 
**version** | **int** | Version number of the content returned. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


