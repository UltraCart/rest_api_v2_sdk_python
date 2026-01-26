# Cart


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate** | [**CartAffiliate**](CartAffiliate.md) |  | [optional] 
**affiliate_network_pixel_oid** | **int** | The affiliate network pixel identifier associated with the cart | [optional] 
**base_currency_code** | **str** | The ISO-4217 three letter base currency code of the account | [optional] 
**billing** | [**CartBilling**](CartBilling.md) |  | [optional] 
**buysafe** | [**CartBuysafe**](CartBuysafe.md) |  | [optional] 
**cart_id** | **str** | Unique identifier for this cart | [optional] 
**checkout** | [**CartCheckout**](CartCheckout.md) |  | [optional] 
**coupons** | [**[CartCoupon]**](CartCoupon.md) | Coupons | [optional] 
**currency_code** | **str** | The ISO-4217 three letter currency code the customer is viewing prices in | [optional] 
**currency_conversion** | [**CartCurrencyConversion**](CartCurrencyConversion.md) |  | [optional] 
**customer_profile** | [**CartCustomerProfile**](CartCustomerProfile.md) |  | [optional] 
**exchange_rate** | **float** | The exchange rate if the customer is viewing a different currency than the base | [optional] 
**gift** | [**CartGift**](CartGift.md) |  | [optional] 
**gift_certificate** | [**CartGiftCertificate**](CartGiftCertificate.md) |  | [optional] 
**items** | [**[CartItem]**](CartItem.md) | Items | [optional] 
**language_iso_code** | **str** | The ISO-631 three letter code the customer would like to checkout with | [optional] 
**logged_in** | **bool** | True if the customer is logged into their profile | [optional] 
**marketing** | [**CartMarketing**](CartMarketing.md) |  | [optional] 
**merchant_id** | **str** | Merchant ID this cart is associated with | [optional] 
**payment** | [**CartPayment**](CartPayment.md) |  | [optional] 
**properties** | [**[CartProperty]**](CartProperty.md) | Properties associated with the cart | [optional] 
**settings** | [**CartSettings**](CartSettings.md) |  | [optional] 
**shipping** | [**CartShipping**](CartShipping.md) |  | [optional] 
**summary** | [**CartSummary**](CartSummary.md) |  | [optional] 
**taxes** | [**CartTaxes**](CartTaxes.md) |  | [optional] 
**upsell_after** | [**CartUpsellAfter**](CartUpsellAfter.md) |  | [optional] 
**utms** | [**[CartUtm]**](CartUtm.md) | UTM clicks.  The zero index is the most recent (last) UTM click.  Only available in BigQuery and on an abandon webhook. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


