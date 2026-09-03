# SfvbContainerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | The container JSON.  Runtime state is stripped on the way out. | [optional] 
**container_name** | **str** | Container name. | [optional] 
**hash_sha256** | **str** | SHA-256 of the cjson.  Send back as If-Match when writing. | [optional] 
**last_modified** | **str** | When the container was last modified, in the store&#39;s own record of it.  Present for email, postcardfront and postcardback.  Absent for upsell and item, because those tables carry no modification timestamp at all - for those two, read created_dts on the current entry of container_versions, which records when this API last wrote the container.  Note that a postcard keeps one timestamp for both of its sides, so writing the front moves the value the back reports. | [optional] 
**owner_object_id** | **str** | Identifier of the owning object within its store. | [optional] 
**owner_type** | **str** | Where this container lives. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


