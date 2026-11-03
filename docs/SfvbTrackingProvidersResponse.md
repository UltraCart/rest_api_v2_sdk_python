# SfvbTrackingProvidersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_version** | **int** | Bumped whenever a provider or field is added, removed or renamed. | [optional] 
**providers** | [**[SfvbTrackingProvider]**](SfvbTrackingProvider.md) | Every provider, Google first, in the order the admin shows them. | [optional] 
**storefront_oid** | **int** | The storefront.  Also the target_id of a secret request for a provider secret. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


