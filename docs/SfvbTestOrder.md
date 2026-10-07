# SfvbTestOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_order** | **bool** | True when the order started an auto order, for working on the subscription pages. | [optional] 
**created** | **str** | When the order was placed, ISO-8601 in UTC. | [optional] 
**currency_code** | **str** | The currency of the total. | [optional] 
**digital_items** | **bool** | True when the order has digital downloads, for working on the digital download page. | [optional] 
**item_count** | **int** | How many item lines the order has. | [optional] 
**order_id** | **str** | The order id.  Pass it as a render&#39;s context_order_id. | [optional] 
**payment_method** | **str** | How the order was paid, such as Credit Card or PayPal. | [optional] 
**stage** | **str** | The order&#39;s current stage code, such as CO (completed), SD (shipping department) or AR (accounts receivable). | [optional] 
**total** | **str** | The order total as a decimal string. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


