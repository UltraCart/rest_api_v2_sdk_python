# ItemPaymentProcessing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_prepaid** | **bool** | True if prepaid cards should be blocked from buying this item | [optional] 
**block_refunds** | **bool** | True if this item should block any refund attempts, set to false otherwise, null value will not update the field | [optional] 
**credit_card_transaction_type** | **str** | Credit card transaction type | [optional] 
**hsa_fsa_eligibility** | **str** | HSA/FSA eligibility. eligible_with_lmn means the customer needs a Letter of Medical Necessity. Kept in sync automatically when Truemed is configured. Empty string clears it, null value will not update the field | [optional] 
**no_realtime_charge** | **bool** | True if no real-time charge should be performed on this item. | [optional] 
**payment_method_validity** | **[str]** | Payment method validity | [optional] 
**rotating_transaction_gateway_codes** | **[str]** | Rotating transaction gateway codes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


