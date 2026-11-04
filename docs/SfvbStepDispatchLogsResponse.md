# SfvbStepDispatchLogsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**SfvbStepCounts**](SfvbStepCounts.md) |  | [optional] 
**entries** | [**[SfvbStepDispatchLog]**](SfvbStepDispatchLog.md) | The entries in the window, newest first. | [optional] 
**next_offset** | **int** | Send this as offset for the next page.  Absent on the last page. | [optional] 
**notes** | **[str]** | What a person should know about reading these entries. | [optional] 
**sequence_uuid** | **str** | The communication sequence the step is in. | [optional] 
**since** | **str** | The start of the window read, as ISO 8601. | [optional] 
**step_type** | **str** | The step&#39;s type, such as email, sms or wait. | [optional] 
**step_uuid** | **str** | The step. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


