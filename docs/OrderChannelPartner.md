# OrderChannelPartner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitrary_pricing_tier_names** | **[str]** | Names of pricing tiers to price this order against, without associating a customer profile.  An unknown tier name will fail the import.  An item that also supplies arbitrary_unit_cost keeps that cost and ignores the tier.  If a customer profile is attached to this order during checkout, these tiers are granted to that profile permanently.  Only applicable on inserting orders. | [optional] 
**auto_approve_purchase_order** | **bool** | If true, any purchase order submitted is automatically approved | [optional] 
**channel_partner_code** | **str** | The code of the channel partner | [optional] 
**channel_partner_data** | **str** | Additional data provided by the channel partner, read-only | [optional] 
**channel_partner_oid** | **int** | Channel partner object identifier, read-only and available on existing channel orders only. | [optional] 
**channel_partner_order_id** | **str** | The order ID assigned by the channel partner for this order. | [optional] 
**ignore_invalid_shipping_method** | **bool** | Set to true to ignore invalid shipping method being specified.  Only applicable on inserting orders. | [optional] 
**no_realtime_payment_processing** | **bool** | Indicates this order should be placed in Account Receivable for later payment processing | [optional] 
**skip_auto_order_setup** | **bool** | Instructs UltraCart to skip auto order setup.  Only applicable on inserting orders. | [optional] 
**skip_payment_processing** | **bool** | Indicates this order was already paid for via a channel purchase and no payment collection should be attempted | [optional] 
**store_completed** | **bool** | Instructs UltraCart to skip shipping department and mark this order as fully complete.  This flag defaults to true.  Set this flag to false to shipped product for this order. | [optional] 
**store_if_payment_declines** | **bool** | If true, any failed payment will place the order in Accounts Receivable rather than rejecting it. | [optional] 
**treat_warnings_as_errors** | **bool** | Any warnings are raised as errors and halt the import of the order | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


