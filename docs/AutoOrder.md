# AutoOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_ons** | [**[AutoOrderAddonItem]**](AutoOrderAddonItem.md) | Array of addon objects instructing which items to add to auto order and how many times they should be added. | [optional] 
**auto_order_code** | **str** | Unique code assigned to this auto order | [optional] 
**auto_order_oid** | **int** | Auto order object identifier | [optional] 
**cancel_after_next_x_orders** | **int** | Cancel this auto order after X additional rebills | [optional] 
**cancel_downgrade** | **bool** | True if the auto order was canceled because the customer purchased a downgrade item | [optional] 
**cancel_reason** | **str** | The reason this auto order was canceled by either merchant or customer | [optional] 
**cancel_upgrade** | **bool** | True if the auto order was canceled because the customer purchased an upgrade item | [optional] 
**canceled_by_user** | **str** | The user that canceled the auto order | [optional] 
**canceled_dts** | **str** | The date/time that the auto order was canceled | [optional] 
**completed** | **bool** | True if the auto order ran successfully to completion | [optional] 
**credit_card_attempt** | **int** | The number of credit card attempts that have taken place | [optional] 
**disabled_dts** | **str** | The date/time the auto order was disabled due to failed rebills | [optional] 
**enabled** | **bool** | True if this auto order is enabled | [optional] 
**failure_reason** | **str** | The reason this auto order failed during the last rebill attempt | [optional] 
**items** | [**[AutoOrderItem]**](AutoOrderItem.md) | The items that are setup to rebill | [optional] 
**logs** | [**[AutoOrderLog]**](AutoOrderLog.md) | Logs associated with this auto order | [optional] 
**management** | [**AutoOrderManagement**](AutoOrderManagement.md) |  | [optional] 
**merchant_id** | **str** | UltraCart merchant ID owning this order | [optional] 
**next_attempt** | **str** | The next time that the auto order will be attempted for processing | [optional] 
**original_order** | [**Order**](Order.md) |  | [optional] 
**original_order_id** | **str** | The original order id that this auto order is associated with. | [optional] 
**override_affiliate_id** | **int** | Override the affiliate id given credit for rebills of this auto order | [optional] 
**rebill_orders** | [**[Order]**](Order.md) | Rebill orders that have taken place on this auto order | [optional] 
**rotating_transaction_gateway_code** | **str** | The RTG code associated with this order for future rebills | [optional] 
**status** | **str** | The status of the auto order | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


