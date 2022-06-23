# OrderPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check** | [**OrderPaymentCheck**](OrderPaymentCheck.md) |  | [optional] 
**credit_card** | [**OrderPaymentCreditCard**](OrderPaymentCreditCard.md) |  | [optional] 
**echeck** | [**OrderPaymentECheck**](OrderPaymentECheck.md) |  | [optional] 
**hold_for_fraud_review** | **bool** | True if order has been held for fraud review | [optional] 
**insurance** | [**OrderPaymentInsurance**](OrderPaymentInsurance.md) |  | [optional] 
**payment_dts** | **str** | Date/time that the payment was successfully processed, for new orders, this field is only considered if channel_partner.skip_payment_processing is true | [optional] 
**payment_method** | **str** | Payment method | [optional] 
**payment_method_accounting_code** | **str** | Payment method QuickBooks code | [optional] 
**payment_method_deposit_to_account** | **str** | Payment method QuickBooks deposit account | [optional] 
**payment_status** | **str** | Payment status | [optional] 
**purchase_order** | [**OrderPaymentPurchaseOrder**](OrderPaymentPurchaseOrder.md) |  | [optional] 
**rotating_transaction_gateway_code** | **str** | Rotating transaction gateway code used to process this order | [optional] 
**surcharge** | [**Currency**](Currency.md) |  | [optional] 
**surcharge_accounting_code** | **str** | Surcharge accounting code | [optional] 
**surcharge_transaction_fee** | **float** | Surcharge transaction fee | [optional] 
**surcharge_transaction_percentage** | **float** | Surcharge transaction percentage | [optional] 
**test_order** | **bool** | True if this is a test order | [optional] 
**transactions** | [**[OrderPaymentTransaction]**](OrderPaymentTransaction.md) | Transactions associated with processing this payment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


