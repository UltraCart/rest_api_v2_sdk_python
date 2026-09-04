# SfvbContainerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | The container JSON.  Runtime state is stripped on the way out. | [optional] 
**container_name** | **str** | Container name. | [optional] 
**hash_sha256** | **str** | SHA-256 of the cjson.  Send back as If-Match when writing. | [optional] 
**last_modified** | **str** | When the container was last modified, in the store&#39;s own record of it.  Every owner type reports this.  It is absent only when the container has never been written since the store began recording it, so treat an absent value as unknown rather than as never modified.  Two behaviours worth knowing.  A postcard keeps one timestamp for both of its sides, so writing the front moves the value the back reports.  An upsell container that is rewritten with byte identical content keeps its original date rather than moving to now, because the timestamp tracks changes to the container and not writes to the offer. | [optional] 
**owner_object_id** | **str** | Identifier of the owning object within its store. | [optional] 
**owner_type** | **str** | Where this container lives. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


