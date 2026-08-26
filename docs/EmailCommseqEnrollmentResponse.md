# EmailCommseqEnrollmentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**already_enrolled** | **bool** | True if the customer was already enrolled and therefore not enrolled again | [optional] 
**enrolled** | **bool** | True if the customer was newly enrolled into the sequence | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**esp_customer_uuid** | **str** | The resolved ESP customer UUID for the enrolled email | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


