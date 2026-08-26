# SfvbFileVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment recorded with the write. | [optional] 
**current** | **bool** | True for the version currently on disk. | [optional] 
**edited_by** | **str** | Login of whoever wrote this version. | [optional] 
**fs_file_history_oid** | **int** | History record oid. | [optional] 
**hash_sha256** | **str** | SHA-256 of this version&#39;s content. | [optional] 
**last_modified** | **str** | When this version was written. | [optional] 
**revertable** | **bool** | True when this version can be reverted to. | [optional] 
**size** | **int** | Size in bytes. | [optional] 
**version** | **int** | Version number.  Pass to files/content or files/revert. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


