# SfvbFilesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**[SfvbFileEntry]**](SfvbFileEntry.md) | Directories first, then files, each sorted by name. | [optional] 
**fs_directory_oid** | **int** | Oid of the directory that was listed. | [optional] 
**omitted_count** | **int** | Number of entries omitted when truncated is true. | [optional] 
**parent_fs_directory_oid** | **int** | Oid of the parent directory, or zero at the root. | [optional] 
**path** | **str** | Path that was listed. | [optional] 
**truncated** | **bool** | True when the listing was capped.  Never truncated silently. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


