# SfvbCommsSequenceStatsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_sequence_uuid** | **str** | The sequence. | [optional] 
**days** | **int** | The window, in days, for the step counts. | [optional] 
**notes** | **[str]** | What the windows are and what a missing count means. | [optional] 
**overall** | [**SfvbCommsStat**](SfvbCommsStat.md) |  | [optional] 
**steps** | [**[SfvbCommsStepStat]**](SfvbCommsStepStat.md) | Each email, SMS, postcard and branch step, in the stored order. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


