# SfvbRecordingEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The event name, such as rage click, script error, checkout error or add to cart. | [optional] 
**params** | [**[SfvbRecordingParameter]**](SfvbRecordingParameter.md) | The event&#39;s parameters as name and value pairs.  Omitted for input change events, whose values are what the visitor typed. | [optional] 
**sub_text** | **str** | A short human readable summary of the event, when the recorder produced one. | [optional] 
**timestamp** | **str** | When it happened, ISO-8601 in UTC.  Subtract the page view&#39;s first_event_timestamp for the offset into the replay. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


