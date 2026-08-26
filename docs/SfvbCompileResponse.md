# SfvbCompileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | Container id the document compiled under. | [optional] 
**directives** | **[str]** | Velocity directives the compiled output declares. | [optional] 
**success** | **bool** | True when compilation produced output. | [optional] 
**used_elements** | **[str]** | Element types used, sorted. | [optional] 
**validation** | [**SfvbValidationResponse**](SfvbValidationResponse.md) |  | [optional] 
**velocity** | **str** | The compiled Velocity.  This is the body only; the cache wrapper a stored .cjson gets is not included. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


