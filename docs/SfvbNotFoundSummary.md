# SfvbNotFoundSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_24_hours** | **[int]** | 404 hits per hour for the last 24 hours, oldest first. | [optional] 
**last_30_days** | **[int]** | 404 hits per day, oldest first, ending today in the server&#39;s time zone.  Bots and shoppers together. | [optional] 
**last_7_days** | **[int]** | 404 hits per day for the last 7 days, oldest first. | [optional] 
**new_paths** | [**[SfvbNotFoundEntry]**](SfvbNotFoundEntry.md) | Up to 10 open paths first seen in the last 30 days, most hits first, leaving out paths only bots have hit. | [optional] 
**notes** | **[str]** | What a person should know about reading these counts. | [optional] 
**total_30_days** | **int** | The sum of last_30_days. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


