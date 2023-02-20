# OrderRefundableResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**item_level_refund_reason_required** | **bool** | True if the item level refund reason is required | [optional] 
**item_level_refund_reasons** | [**[OrderReason]**](OrderReason.md) | Reason codes available at the item level. | [optional] 
**item_level_return_reasons** | [**[OrderReason]**](OrderReason.md) | Return codes available at the item level. | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**order_level_refund_reason_required** | **bool** | True if the order level refund reason is required | [optional] 
**order_level_refund_reasons** | [**[OrderReason]**](OrderReason.md) | Reason codes available at the order level. | [optional] 
**order_level_reject_reasons** | [**[OrderReason]**](OrderReason.md) | Reject codes available at the order level. | [optional] 
**refundable** | **bool** | Whether the order is refundable or not.  Null should be interpreted as false. | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


