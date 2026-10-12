# SfvbEventsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**[SfvbEvent]**](SfvbEvent.md) | Oldest first. | [optional] 
**more** | **bool** | True when more events follow.  Ask again with after set to the last event_id. | [optional] 
**resync_required** | **bool** | True when the cursor is older than the 72 hours of events kept.  Re-list what you were waiting on instead of replaying. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


