# SfvbServerLogsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The most logs returned. | [optional] 
**logs** | [**[SfvbServerLog]**](SfvbServerLog.md) | Matching logs, newest first, without their text. | [optional] 
**more_available** | **bool** | True when older logs in the window were not read.  Narrow since, or page by moving since back. | [optional] 
**searched** | **int** | How many of the newest logs in the window were read to find these. | [optional] 
**since** | **str** | The start of the window searched, ISO-8601 in UTC.  Logs are kept for seven days. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


