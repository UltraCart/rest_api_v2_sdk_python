# SfvbCommsLookupResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_sequence_uuid** | **str** | The sequence it belongs to, when there is one. | [optional] 
**kind** | **str** | campaign, flow, sequence, step, email, postcard, list or segment. | [optional] 
**name** | **str** | The campaign, flow, list or segment name, or the email subject. | [optional] 
**next** | **str** | The CLI command that reads it. | [optional] 
**notes** | **[str]** | What the answer means, in sentences. | [optional] 
**owner** | [**SfvbCommsLookupOwner**](SfvbCommsLookupOwner.md) |  | [optional] 
**step_uuid** | **str** | The step that sends it, for an email or postcard a step names, or the step itself. | [optional] 
**storefront_oid** | **int** | The storefront it lives on, for the --storefront option. | [optional] 
**uuid** | **str** | The uuid looked up. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


