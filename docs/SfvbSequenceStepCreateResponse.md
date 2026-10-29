# SfvbSequenceStepCreateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_uuid** | **str** | The new email&#39;s uuid.  Its body is the email container with this owner id. | [optional] 
**notes** | **[str]** | What to do next, such as writing the body, and customers already waiting on the step before it. | [optional] 
**requires_review** | **bool** | True when the new email must pass content review before it sends. | [optional] 
**step** | [**SfvbSequenceStep**](SfvbSequenceStep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


