# OrderCancelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_self_ship_orders** | **bool** | Flag to prevent a order shipping during a refund process | [optional] 
**reject_reason** | **str** | Reason stored on the order when it is rejected without a refund (Accounts Receivable, Pre-order, Quote or Hold), the same as the reject reason in the UI. | [optional] 
**skip_refund_and_hold** | **bool** | Skip refund and move order to Held Orders department | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


