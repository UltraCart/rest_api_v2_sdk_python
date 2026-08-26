# SfvbContainerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_theme** | **bool** | True when this container lives in the theme currently serving live traffic.  Writing to it requires the sfvb_publish scope. | [optional] 
**cjson** | **str** | The container JSON.  Runtime state is stripped on the way out. | [optional] 
**container_id** | **str** | Container id as the compiler will derive it. | [optional] 
**container_name** | **str** | Container name. | [optional] 
**hash_sha256** | **str** | SHA-256 of the cjson.  Send back as If-Match when writing. | [optional] 
**last_modified** | **str** | When the container was last modified, where the store records it. | [optional] 
**owner_object_id** | **str** | Identifier of the owning object within its store. | [optional] 
**owner_type** | **str** | Where this container lives. | [optional] 
**path** | **str** | File path, for theme and page containers only. | [optional] 
**version** | **int** | File version, for theme and page containers only. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


