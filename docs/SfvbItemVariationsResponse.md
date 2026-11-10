# SfvbItemVariationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_needed** | **bool** | True when the change needs an approved item.variations request. | [optional] 
**axes** | [**[SfvbItemVariationAxis]**](SfvbItemVariationAxis.md) | The axes in order. | [optional] 
**changes** | [**[SfvbItemVariationChangeResult]**](SfvbItemVariationChangeResult.md) | What each change did, or would do on a dry run. | [optional] 
**combinations** | [**[SfvbItemVariationCombination]**](SfvbItemVariationCombination.md) | Every filled combination. | [optional] 
**description** | **str** | The parent item&#39;s description. | [optional] 
**dry_run** | **bool** | True when nothing was saved. | [optional] 
**hash_sha256** | **str** | Hash of the variations as returned. | [optional] 
**merchant_item_id** | **str** | The parent item&#39;s id. | [optional] 
**merchant_item_oid** | **int** | The parent item&#39;s oid. | [optional] 
**unfilled_combinations** | **int** | How many combinations of the options have no child. | [optional] 
**warnings** | **[str]** | Things worth knowing, such as combinations left unfilled. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


