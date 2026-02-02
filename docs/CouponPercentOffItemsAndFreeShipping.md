# CouponPercentOffItemsAndFreeShipping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_percent** | **float** | The percentage of subtotal discount | [optional] 
**excluded_item_tags** | **[str]** | A list of item tags which cannot be discounted. | [optional] 
**excluded_items** | **[str]** | A list of items which cannot be discounted. | [optional] 
**item_tags** | **[str]** | An optional list of item tags which will receive a discount.  If blank, discount applies to all items except excluded items. | [optional] 
**items** | **[str]** | An optional list of items which will receive a discount.  If blank, discount applies to all items except excluded items. | [optional] 
**shipping_methods** | **[str]** | One or more shipping methods that may be used with this coupon.  If not specified or empty, methods that are marked as qualifies for free shipping will be the only free methods | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


