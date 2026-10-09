# SfvbItemRelated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_sha256** | **str** | The hash of the above.  Send it as If-Match to change them. | [optional] 
**merchant_item_id** | **str** | The item&#39;s merchant item id. | [optional] 
**merchant_item_oid** | **int** | The item. | [optional] 
**no_system_calculated_related_items** | **bool** | True when UltraCart does not calculate related items for this item. | [optional] 
**not_relatable** | **bool** | True when this item is never shown as related to another. | [optional] 
**related_items** | [**[SfvbItemRelatedItem]**](SfvbItemRelatedItem.md) | In stored order - the merchant&#39;s own (user, addon, complementary) and UltraCart&#39;s calculated ones (system). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


