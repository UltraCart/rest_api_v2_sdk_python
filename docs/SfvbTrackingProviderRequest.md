# SfvbTrackingProviderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_cost** | **bool** | True to accept the cost of turning on Google Tag Gateway.  Required to turn it on. | [optional] 
**consent** | [**SfvbTrackingProviderConsent**](SfvbTrackingProviderConsent.md) |  | [optional] 
**dry_run** | **bool** | True to check the change and report it without saving. | [optional] 
**events** | **bool, date, datetime, dict, float, int, list, str, none_type** | Standard events by name, true to send. | [optional] 
**fields** | **bool, date, datetime, dict, float, int, list, str, none_type** | Plain field values by key.  An empty string clears one.  Booleans are true or false.  Secrets go in secrets instead. | [optional] 
**secrets** | [**SfvbTrackingProviderSecrets**](SfvbTrackingProviderSecrets.md) |  | [optional] 
**unset** | **[str]** | Plain field keys to clear. | [optional] 
**wholesale_tiers** | [**[SfvbTrackingWholesaleTier]**](SfvbTrackingWholesaleTier.md) | For google_analytics, account numbers by pricing_tier_oid. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


