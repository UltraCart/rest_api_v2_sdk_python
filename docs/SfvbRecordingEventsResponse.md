# SfvbRecordingEventsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_json** | **str** | The page view&#39;s rrweb events as a JSON array in a string, the input an rrweb Replayer takes.  Card number and security code fields are masked by the recorder, but other text the visitor typed can appear in it. | [optional] 
**rrweb_version** | **str** | The rrweb version that recorded the events.  Replay with the same version. | [optional] 
**screen_recording_page_view_uuid** | **str** | The page view these events replay. | [optional] 
**screen_recording_uuid** | **str** | The recording the page view belongs to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


