# OrderInternal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exported_to_accounting** | **bool** | True if the order has been exported to QuickBooks. If QuickBooks is not configured, then this will already be true | [optional] 
**merchant_notes** | **str** | Merchant notes.  Full notes in non-transactional mode.  Just used to write a new merchant note when transaction merchant notes enabled. | [optional] 
**placed_by_user** | **str** | If placed via the BEOE, this is the user that placed the order | [optional] 
**refund_by_user** | **str** | User that issued the refund | [optional] 
**sales_rep_code** | **str** | Sales rep code associated with the order | [optional] 
**transactional_merchant_notes** | [**[OrderTransactionalMerchantNote]**](OrderTransactionalMerchantNote.md) | Transactional merchant notes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


