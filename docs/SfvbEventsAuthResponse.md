# SfvbEventsAuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_dts** | **str** | When the token stops working, ISO 8601.  Ask for a new one to reconnect. | [optional] 
**jwt** | **str** | The connect token on its own. | [optional] 
**websocket_url** | **str** | The websocket URL to open, with the token on it.  Open it before expires_dts; each token opens one connection. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


