# PaymentsConfigurationPayPal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_paypal** | **bool** | Master flag that determine if PayPal is an active payment for this account | [optional] 
**accounting_code** | **str** | Optional accounting code that is set to Quickbooks when an order uses this payment method. | [optional] 
**api_password** | **str** | PayPal API password | [optional] 
**api_username** | **str** | PayPal API username | [optional] 
**certificate_on_file** | **bool** | (Legacy) true if there is a PayPal certificate already on file. Used to manage the internal UI | [optional] 
**deposit_to_account** | **str** | The account to deposit funds | [optional] 
**email** | **str** | The main PayPal email address | [optional] 
**environment** | **str** | PayPal configuration, live or sandbox | [optional] 
**header_image_url** | **str** | The URL for the PayPal header | [optional] 
**hide_bill_me_later** | **bool** | True if the Bill Me Later button should be hidden during checkout | [optional] 
**hide_express_checkout_on_view_cart** | **bool** | True if the PayPal express checkout button should be hidden on the view cart page.  This will force the customer to enter address information before being able to checkout with PayPal | [optional] 
**hide_for_unshipped_orders** | **bool** | True if PayPal should be hidden for orders with no shippable product, such as digital orders | [optional] 
**hold_in_ar** | **bool** | If true, PayPal orders are held in Accounts Receivable for review | [optional] 
**landing_page** | **str** | PayPal landing page | [optional] 
**mode** | **str** | The PayPal mode | [optional] 
**private_key_password** | **str** | PayPal API private key password | [optional] 
**processing_fee** | **str** | Optional additional fee to charge if PayPal is used.  It is rare for this to be used. | [optional] 
**processing_percentage** | **str** | The processing percentage charged by PayPal | [optional] 
**push_paypal** | **bool** | True if the internal UI should recommend opening a PayPal account | [optional] 
**restrictions** | [**PaymentsConfigurationRestrictions**](PaymentsConfigurationRestrictions.md) |  | [optional] 
**send_recurring** | **bool** | True if UltraCart should send recurring orders to PayPal.  There are restrictions to what PayPal will accept for recurring orders.  Be careful. | [optional] 
**short_paypal_marketing_text** | **bool** | Short marketing text | [optional] 
**show_card_logos_not_directly_supported** | **bool** | internal ui flag | [optional] 
**show_signature** | **bool** | Internal flag used to manage UI | [optional] 
**signature** | **str** | PayPal signature | [optional] 
**solution_type** | **str** | PayPal solution type | [optional] 
**summary_email** | **str** | The email where PayPal summaries should be sent | [optional] 
**summary_mode** | **str** | Description of what mode PayPal is operating | [optional] 
**zero_dollar_penny** | **bool** | Send free items to PayPal as one cent items and subtract this penny from shipping.  PayPal does not allow the sale of free items. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


