# SfvbContainerVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | The CJSON this version held.  Populated only when reading a single version, and null when the operation is create.  Listings omit it because container CJSON is large. | [optional] 
**comment** | **str** | Comment recorded with the write that replaced this version. | [optional] 
**container_history_oid** | **int** | History record oid.  Pass to the revert operation on the owning container.  Absent on the entry marked current, which holds the value stored right now, has no history row of its own, and so cannot be fetched or reverted to. | [optional] 
**container_name** | **str** | Container name, where the owner has more than one container. | [optional] 
**created_dts** | **str** | When this snapshot was taken. | [optional] 
**current** | **bool** | True for the value currently stored. | [optional] 
**edited_by** | **str** | Login of whoever caused this snapshot. | [optional] 
**hash_sha256** | **str** | SHA-256 of this version&#39;s CJSON. | [optional] 
**operation** | **str** | What the container was before the write this entry precedes.  create means it did not exist, so reverting to this entry removes it again; update means it held the cjson recorded here. | [optional] 
**owner_object_id** | **str** | Owner object identifier. | [optional] 
**owner_type** | **str** | Owner type. | [optional] 
**size** | **int** | Size of this version&#39;s CJSON in bytes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


