# SfvbTrackingProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_path** | **str** | Where the provider is in the admin. | [optional] 
**approval_needed** | **bool** | On a dry run, whether the real write needs an approved tracking_provider.change request. | [optional] 
**changes** | [**[SfvbTrackingChange]**](SfvbTrackingChange.md) | On a write, each setting it changed, or would change on a dry run.  Secrets read only set or cleared. | [optional] 
**configured** | **bool** | True when the provider is on, which means one of its identifying fields is set. | [optional] 
**consent** | [**SfvbTrackingProviderConsent**](SfvbTrackingProviderConsent.md) |  | [optional] 
**consent_supported** | **bool** | True when the provider can be held back until the shopper consents. | [optional] 
**cost** | **str** | For google_tag_manager, what turning on Google Tag Gateway costs. | [optional] 
**dry_run** | **bool** | On a write, true when nothing was saved. | [optional] 
**events** | [**[SfvbTrackingProviderEvent]**](SfvbTrackingProviderEvent.md) | For a provider with standard events, each one and whether it is sent. | [optional] 
**fields** | [**[SfvbTrackingProviderField]**](SfvbTrackingProviderField.md) | Every field, in the order the admin shows them. | [optional] 
**group** | **str** | google or other, the admin tab it is on. | [optional] 
**hash_sha256** | **str** | The hash of the stored settings.  A secret counts by its mask and length only.  Send it as If-Match when changing or clearing the provider. | [optional] 
**key** | **str** | The provider key, such as facebook or google_analytics. | [optional] 
**name** | **str** | The name the admin shows. | [optional] 
**notes** | **[str]** | Anything for a person to know or do, such as a field the provider needs before it sends anything, or an OAuth connection to disconnect in the admin after a write. | [optional] 
**oauth** | [**SfvbTrackingProviderOauth**](SfvbTrackingProviderOauth.md) |  | [optional] 
**server_side** | **str** | What the provider also sends from UltraCart&#39;s servers.  A consent gate holds back only the browser pixel, not these.  Absent when it sends nothing server side. | [optional] 
**wholesale_tiers** | [**[SfvbTrackingWholesaleTier]**](SfvbTrackingWholesaleTier.md) | For google_analytics, the account number per wholesale pricing tier. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


