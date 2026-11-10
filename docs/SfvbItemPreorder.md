# SfvbItemPreorder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | [**SfvbItemPreorderChange**](SfvbItemPreorderChange.md) |  | [optional] 
**eta** | **str** | The expected date, YYYY-MM-DD, or null when none is set. | [optional] 
**hash_sha256** | **str** | The hash of preorder and eta.  Send it as If-Match, or as the row&#39;s hash_sha256, to change them. | [optional] 
**merchant_item_id** | **str** | The item&#39;s merchant item id. | [optional] 
**merchant_item_oid** | **int** | The item. | [optional] 
**preorder** | **bool** | True when the item is on pre-order.  Shoppers can order it while out of stock, and its orders go to the Pre-ordered stage. | [optional] 
**shoppers_see** | **str** | What itempreorder shows.  preorder_with_eta when on pre-order with an ETA of today or later, preorder_no_eta when on pre-order with no ETA or a past one, nothing when not on pre-order. | [optional] 
**shoppers_see_text** | **str** | shoppers_see in words, such as on pre-order, ETA 2026-11-20. | [optional] 
**variation_values** | [**[SfvbItemPreorderOption]**](SfvbItemPreorderOption.md) | For a variation listed under its parent, the option values that pick it, such as Size 2T. | [optional] 
**warnings** | **[str]** | After a change, things worth knowing about the new values, such as an ETA in the past.  Never a refusal. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


