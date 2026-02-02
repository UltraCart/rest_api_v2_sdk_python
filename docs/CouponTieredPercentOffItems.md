# CouponTieredPercentOffItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_tags** | **list[str]** | An optional list of item tags which will receive a discount.  If blank, discount applies to all items except excluded items. | [optional] 
**items** | **list[str]** | A list of items of which at least one must be purchased for coupon to be valid. | [optional] 
**limit** | **float** | The (optional) maximum quantity of discounted items. | [optional] 
**tiers** | [**list[CouponTierQuantityPercent]**](CouponTierQuantityPercent.md) | A list of discount tiers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


