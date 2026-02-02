# ChannelPartnerOrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitrary_unit_cost** | **float** | Arbitrary unit cost for this item that differs from the listed price | [optional] 
**auto_order_last_rebill_dts** | **str** | Optional date/time of the last rebill if this item is part of an auto (recurring) order | [optional] 
**auto_order_schedule** | **str** | The frequency schedule for this item if this item is part of an auto (recurring) order | [optional] 
**merchant_item_id** | **str** | Item ID | [optional] 
**options** | [**list[ChannelPartnerOrderItemOption]**](ChannelPartnerOrderItemOption.md) | Item options | [optional] 
**properties** | [**list[ChannelPartnerOrderItemProperty]**](ChannelPartnerOrderItemProperty.md) | Properties | [optional] 
**quantity** | **float** | Quantity | [optional] 
**upsell** | **bool** | True if this item was an upsell item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


