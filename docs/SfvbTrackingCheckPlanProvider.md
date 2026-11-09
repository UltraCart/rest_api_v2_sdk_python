# SfvbTrackingCheckPlanProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**[SfvbTrackingCheckPlanEvent]**](SfvbTrackingCheckPlanEvent.md) | The dataLayer, gtag and fbq calls it makes, where the template makes them. | [optional] 
**expect** | **str** | must_load, must_not_load (held back by a gate this consent state and region have not granted, or never sent for this event), or may_load (depends on something the plan cannot know).  A missing may_load request is a warning, never a fail. | [optional] 
**gate** | [**SfvbTrackingCheckPlanGate**](SfvbTrackingCheckPlanGate.md) |  | [optional] 
**name** | **str** | A name to show. | [optional] 
**note** | **str** | Why the expectation is what it is, when that is not obvious. | [optional] 
**provider** | **str** | The provider key, as tracking/providers names it.  For custom or affiliate network HTML, the host. | [optional] 
**requests** | [**[SfvbTrackingCheckPlanRequest]**](SfvbTrackingCheckPlanRequest.md) | The requests it makes. | [optional] 
**source** | **str** | provider for a provider in the catalog, custom_html for the storefront Tracking or Conversion HTML, affiliate_network for an affiliate network pixel. | [optional] 
**template** | **str** | The storefront template that writes it, tracking.vm or conversion.vm.  Left out for custom and affiliate network HTML. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


