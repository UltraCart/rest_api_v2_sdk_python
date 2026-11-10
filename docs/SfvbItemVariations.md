# SfvbItemVariations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axes** | [**[SfvbItemVariationAxis]**](SfvbItemVariationAxis.md) | The axes in order.  Empty when the item has no variations. | [optional] 
**combinations** | [**[SfvbItemVariationCombination]**](SfvbItemVariationCombination.md) | Every filled combination.  A combination not listed has no child, and shoppers see it as unavailable. | [optional] 
**description** | **str** | The parent item&#39;s description. | [optional] 
**hash_sha256** | **str** | Hash of the variations.  Send it as If-Match on the update. | [optional] 
**merchant_item_id** | **str** | The parent item&#39;s id. | [optional] 
**merchant_item_oid** | **int** | The parent item&#39;s oid. | [optional] 
**unfilled_combinations** | **int** | How many combinations of the options have no child. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


