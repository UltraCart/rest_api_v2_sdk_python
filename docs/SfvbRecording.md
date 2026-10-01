# SfvbRecording


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_platform** | [**ScreenRecordingAdPlatform**](ScreenRecordingAdPlatform.md) |  | [optional] 
**browser** | **str** | Browser name from the user agent. | [optional] 
**browser_version** | **str** | Browser version from the user agent. | [optional] 
**converted** | **bool** | True when the session ended in an order. | [optional] 
**device** | **str** | Device name from the user agent. | [optional] 
**end_timestamp** | **str** | When the session ended, ISO-8601 in UTC. | [optional] 
**geolocation_country** | **str** | Country the visitor was in. | [optional] 
**geolocation_state** | **str** | State or region the visitor was in. | [optional] 
**language_iso_code** | **str** | The browser language. | [optional] 
**order_id** | **str** | The order placed during the session, when there was one. | [optional] 
**os** | **str** | Operating system from the user agent. | [optional] 
**page_view_count** | **int** | How many pages the visitor viewed. | [optional] 
**page_views** | [**[SfvbRecordingPageView]**](SfvbRecordingPageView.md) | The pages viewed, in order. | [optional] 
**referrer_domain** | **str** | The domain that referred the visitor. | [optional] 
**rrweb_version** | **str** | The rrweb version that recorded the session.  Replay with the same version. | [optional] 
**screen_recording_uuid** | **str** | Identifies the recording. | [optional] 
**start_timestamp** | **str** | When the session started, ISO-8601 in UTC. | [optional] 
**time_on_site** | **int** | Seconds the visitor spent on the site. | [optional] 
**utm_campaign** | **str** | utm_campaign on arrival. | [optional] 
**utm_source** | **str** | utm_source on arrival. | [optional] 
**window_height** | **int** | Browser window height in pixels. | [optional] 
**window_width** | **int** | Browser window width in pixels. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


