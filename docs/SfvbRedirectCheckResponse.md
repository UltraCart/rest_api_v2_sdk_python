# SfvbRedirectCheckResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Findings that block the rule. | [optional] 
**source** | **str** | The source as it matches, lower case without a trailing index.html. | [optional] 
**type** | **str** | exact or pattern. | [optional] 
**valid** | **bool** | True when nothing blocks the rule. | [optional] 
**warnings** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Findings that do not block it.  A chain carries the final target as its suggestion. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


