# OrderReplacement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_merchant_notes_new_order** | **str** | Additional merchant notes to append to the new order | [optional] 
**additional_merchant_notes_original_order** | **str** | Additional merchant notes to append to the original order | [optional] 
**custom_field1** | **str** | Custom field 1 | [optional] 
**custom_field2** | **str** | Custom field 2 | [optional] 
**custom_field3** | **str** | Custom field 3 | [optional] 
**custom_field4** | **str** | Custom field 4 | [optional] 
**custom_field5** | **str** | Custom field 5 | [optional] 
**custom_field6** | **str** | Custom field 6 | [optional] 
**custom_field7** | **str** | Custom field 7 | [optional] 
**free** | **bool** | Set to true if this replacement shipment should be free for the customer. | [optional] 
**immediate_charge** | **bool** | Set to true if you want to immediately charge the payment on this order, otherwise it will go to Accounts Receivable. | [optional] 
**items** | [**[OrderReplacementItem]**](OrderReplacementItem.md) | Items to include in the replacement order | [optional] 
**original_order_id** | **str** | Original order id | [optional] 
**shipping_method** | **str** | Shipping method to use.  If not specified or invalid then least cost shipping will take place. | [optional] 
**skip_payment** | **bool** | Set to true if you want to skip the payment as if it was successful. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


