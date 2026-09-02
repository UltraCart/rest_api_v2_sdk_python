# SfvbFileWriteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compiled_path** | **str** | Path of the compiled output, when writing a .cjson under a theme triggered a compile. | [optional] 
**file** | [**SfvbFileEntry**](SfvbFileEntry.md) |  | [optional] 
**hash_sha256** | **str** | New SHA-256.  Use as the next If-Match value. | [optional] 
**public_url** | **str** | Where a shopper&#39;s browser will fetch this file, for use in an img src or a background image.  Present only for a path outside /themes/, which is served straight off the storefront root.  A file inside a theme is absent here because its public URL depends on which theme is active, and guessing it would be worse than omitting it. | [optional] 
**validation** | [**SfvbValidationResponse**](SfvbValidationResponse.md) |  | [optional] 
**velocity_errors** | **str** | Velocity errors recorded by the store.  Present means the file was written but is not valid. | [optional] 
**version** | **int** | New version number. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


