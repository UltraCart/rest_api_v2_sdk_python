# WebhookEventCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_subscribed** | **bool** | True if any events are subscribed to. | [optional] 
**available_expansions** | **[str]** | Array of available expansion constants | [optional] 
**event_category** | **str** | Name of the event category | [optional] 
**events** | [**[WebhookEventSubscription]**](WebhookEventSubscription.md) | The events within the category.  Individual subscription flags contained within the child object. | [optional] 
**subscribed** | **bool** | True if all the events within this category are subscribed.  This is a convenience flag to make user interfaces easier. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


