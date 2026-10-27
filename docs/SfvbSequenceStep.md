# SfvbSequenceStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**[SfvbSequenceBranch]**](SfvbSequenceBranch.md) | Its two sides, for a condition, split or InboxGeek step.  Absent for every other type. | [optional] 
**config_error** | **bool** | True when the step&#39;s settings could not be read. | [optional] 
**config_json** | **str** | The step&#39;s settings as the admin stores them.  A webhook&#39;s header and parameter values are masked. | [optional] 
**config_merchant_notes** | **str** | A note stored inside the step&#39;s settings, when there is one. | [optional] 
**disabled** | **bool** | True when the step is switched off in its settings. | [optional] 
**email_uuids** | **[str]** | The emails it sends.  One for an email step, one per variant for an experiment. | [optional] 
**filter_profile_equation_json** | **str** | The step&#39;s audience filter as stored, when it has one. | [optional] 
**item_ids** | **[str]** | The items it names, for a cart or rate limiter step. | [optional] 
**label** | **str** | The type as the admin names it, such as Time Delay.  The type itself for one it doesn&#39;t know. | [optional] 
**list_uuids** | **[str]** | The lists it subscribes or unsubscribes, for a list step. | [optional] 
**merchant_notes** | **str** | The note stored on the step. | [optional] 
**name** | **str** | The step&#39;s own display name from its settings, when it has one. | [optional] 
**number_waiting** | **int** | How many customers are waiting on this step now.  Only when waiting counts were asked for. | [optional] 
**postcard_uuid** | **str** | The postcard it sends, for a postcard step. | [optional] 
**step_uuid** | **str** | The step uuid. | [optional] 
**type** | **str** | The step type, such as email, wait, condition or webhook. | [optional] 
**unreachable** | **bool** | True for a step no branch leads to.  Listed at the end so nothing is hidden. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


