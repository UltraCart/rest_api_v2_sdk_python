# CartItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitrary_unit_cost** | [**Currency**](Currency.md) |  | [optional] 
**attributes** | [**[CartItemAttribute]**](CartItemAttribute.md) | Attributes | [optional] 
**auto_order_schedule** | **str** | Auto order schedule the customer selected | [optional] 
**default_image_url** | **str** | URL to the default multimedia image | [optional] 
**default_thumbnail_url** | **str** | URL to the default multimedia thumbnail | [optional] 
**description** | **str** | Description of the item | [optional] 
**discount** | [**Currency**](Currency.md) |  | [optional] 
**extended_description** | **str** | Extended description of the item | [optional] 
**item_id** | **str** | Item ID | [optional] 
**item_oid** | **int** | Item object identifier | [optional] 
**kit** | **bool** | True if this item is a kit | [optional] 
**kit_component_options** | [**[CartKitComponentOption]**](CartKitComponentOption.md) | Options associated with the kit components | [optional] 
**manufacturer_suggested_retail_price** | [**Currency**](Currency.md) |  | [optional] 
**maximum_quantity** | **float** | Maximum quantity the customer can purchase | [optional] 
**minimum_quantity** | **float** | Minimum quantity the customer can purchase | [optional] 
**multimedia** | [**[CartItemMultimedia]**](CartItemMultimedia.md) | Multimedia | [optional] 
**options** | [**[CartItemOption]**](CartItemOption.md) | Options | [optional] 
**phsyical** | [**CartItemPhysical**](CartItemPhysical.md) |  | [optional] 
**position** | **int** | Position of the item in the cart | [optional] 
**preorder** | **bool** | True if this item is on pre-order | [optional] 
**quantity** | **float** | quantity | [optional] 
**schedules** | **[str]** | Customer selectable auto order schedules | [optional] 
**total_cost** | [**Currency**](Currency.md) |  | [optional] 
**total_cost_with_discount** | [**Currency**](Currency.md) |  | [optional] 
**unit_cost** | [**Currency**](Currency.md) |  | [optional] 
**unit_cost_with_discount** | [**Currency**](Currency.md) |  | [optional] 
**upsell** | **bool** | True if this item was added to the cart as part of an upsell | [optional] 
**variations** | [**[CartItemVariationSelection]**](CartItemVariationSelection.md) | Variations | [optional] 
**view_url** | **str** | URL to view the product on the site | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


