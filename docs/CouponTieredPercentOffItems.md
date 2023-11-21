# CouponTieredPercentOffItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_tags** | **[str]** | An optional list of item tags which will receive a discount.  If blank, discount applies to all items except excluded items. | [optional] 
**items** | **[str]** | A list of items of which at least one must be purchased for coupon to be valid. | [optional] 
**limit** | **float** | The (optional) maximum quantity of discounted items. | [optional] 
**tiers** | [**[CouponTierQuantityPercent]**](CouponTierQuantityPercent.md) | A list of discount tiers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


