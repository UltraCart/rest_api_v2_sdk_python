# ItemPaymentProcessing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_prepaid** | **bool** | True if prepaid cards should be blocked from buying this item | [optional] 
**block_refunds** | **bool** | True if this item should block any refund attempts, set to false otherwise, null value will not update the field | [optional] 
**credit_card_transaction_type** | **str** | Credit card transaction type | [optional] 
**no_realtime_charge** | **bool** | True if no real-time charge should be performed on this item. | [optional] 
**payment_method_validity** | **list[str]** | Payment method validity | [optional] 
**rotating_transaction_gateway_codes** | **list[str]** | Rotating transaction gateway codes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


