# SfvbValidationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Problems that will prevent a write. | [optional] 
**used_elements** | **[str]** | Element types found in the document, sorted. | [optional] 
**valid** | **bool** | True when there are no errors.  Warnings do not affect this flag. | [optional] 
**warnings** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Quality problems that will not prevent a write but should be addressed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


