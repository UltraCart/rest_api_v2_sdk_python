# SfvbSequenceStepCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_step_uuid** | **str** | The step the new step follows, in the same list.  Not an end, continue or merge step. | [optional] 
**branch_step_uuid** | **str** | A condition, split or inboxgeek step.  With side, the new step goes first on that side. | [optional] 
**preview_text** | **str** | The new email&#39;s preview text, 5 to 150 characters. | [optional] 
**side** | **str** | With branch_step_uuid, the side&#39;s label from the sequence read.  yes or no for a condition, left or right for a split or inboxgeek step. | [optional] 
**subject** | **str** | The new email&#39;s subject line, 5 to 150 characters. | [optional] 
**type** | **str** | The kind of step.  Only email for now. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


