# SfvbRecordingPageView


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The host name of the address. | [optional] 
**events** | [**[SfvbRecordingEvent]**](SfvbRecordingEvent.md) | Named events on this page view in time order, such as rage clicks and script errors. | [optional] 
**first_event_timestamp** | **str** | When recording of this page view began, ISO-8601 in UTC. | [optional] 
**last_event_timestamp** | **str** | When recording of this page view ended, ISO-8601 in UTC. | [optional] 
**missing_events** | **bool** | True when no replay events were stored for this page view. | [optional] 
**params** | [**[SfvbRecordingParameter]**](SfvbRecordingParameter.md) | The query string parameters on the address. | [optional] 
**referrer** | **str** | The referring address, when there was one. | [optional] 
**screen_recording_page_view_uuid** | **str** | Identifies this page view when fetching its replay events. | [optional] 
**time_on_page** | **int** | Seconds the visitor spent on the page. | [optional] 
**timing_dom_content_loaded** | **int** | Milliseconds until DOMContentLoaded fired. | [optional] 
**timing_loaded** | **int** | Milliseconds until the load event fired. | [optional] 
**truncated_events** | **bool** | True when the recorder stopped storing events part way through this page view. | [optional] 
**url** | **str** | The address the visitor viewed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


