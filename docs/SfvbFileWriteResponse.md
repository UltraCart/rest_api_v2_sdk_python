# SfvbFileWriteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compiled_path** | **str** | Path of the compiled output, when writing a .cjson under a theme triggered a compile. | [optional] 
**file** | [**SfvbFileEntry**](SfvbFileEntry.md) |  | [optional] 
**hash_sha256** | **str** | New SHA-256.  Use as the next If-Match value. | [optional] 
**validation** | [**SfvbValidationResponse**](SfvbValidationResponse.md) |  | [optional] 
**velocity_errors** | **str** | Velocity errors recorded by the store.  Present means the file was written but is not valid. | [optional] 
**version** | **int** | New version number. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


