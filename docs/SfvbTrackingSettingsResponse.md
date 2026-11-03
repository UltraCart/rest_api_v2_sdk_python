# SfvbTrackingSettingsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced** | [**SfvbTrackingAdvanced**](SfvbTrackingAdvanced.md) |  | [optional] 
**changes** | [**[SfvbTrackingChange]**](SfvbTrackingChange.md) | On a write, each setting it changed, or would change on a dry run.  Empty when nothing changed.  Absent on a read. | [optional] 
**currencies** | **[str]** | The currency codes default_currency accepts. | [optional] 
**dry_run** | **bool** | On a write, true when nothing was saved.  Absent on a read. | [optional] 
**privacy** | [**SfvbTrackingPrivacy**](SfvbTrackingPrivacy.md) |  | [optional] 
**storefront_oid** | **int** | The storefront these settings belong to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


