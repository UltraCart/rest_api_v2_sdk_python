# CouponFreeItemWithItemPurchaseAndFreeShipping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **[str]** | A list of free items which will receive a discount if one of the required purchase items is purchased. | [optional] 
**limit** | **int** | The (optional) maximum quantity of discounted items.  Free shipping will apply to all units of the free item ids though. | [optional] 
**match_required_purchase_item_to_free_item** | **bool** | If true then the free item is matched 1:1 with the free item in the list. | [optional] 
**required_purchase_items** | **[str]** | Required items (at least one from the list) that must be purchased for coupon to be valid | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


