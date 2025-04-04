# Coupon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_oid** | **int** | Associates an order with an affiliate when this value is set. | [optional] 
**allow_multiple_one_time_codes** | **bool** | True if multiple one time codes for this coupon can be used on a cart at the same time. | [optional] 
**amount_off_items** | [**CouponAmountOffItems**](CouponAmountOffItems.md) |  | [optional] 
**amount_off_shipping** | [**CouponAmountOffShipping**](CouponAmountOffShipping.md) |  | [optional] 
**amount_off_shipping_with_items_purchase** | [**CouponAmountOffShippingWithItemsPurchase**](CouponAmountOffShippingWithItemsPurchase.md) |  | [optional] 
**amount_off_subtotal** | [**CouponAmountOffSubtotal**](CouponAmountOffSubtotal.md) |  | [optional] 
**amount_off_subtotal_and_free_shipping** | [**CouponAmountOffSubtotalFreeShippingWithPurchase**](CouponAmountOffSubtotalFreeShippingWithPurchase.md) |  | [optional] 
**amount_off_subtotal_and_shipping** | [**CouponAmountOffSubtotalAndShipping**](CouponAmountOffSubtotalAndShipping.md) |  | [optional] 
**amount_off_subtotal_with_block_purchase** | [**CouponAmountOffSubtotalWithBlockPurchase**](CouponAmountOffSubtotalWithBlockPurchase.md) |  | [optional] 
**amount_off_subtotal_with_items_purchase** | [**CouponAmountOffSubtotalWithItemsPurchase**](CouponAmountOffSubtotalWithItemsPurchase.md) |  | [optional] 
**amount_off_subtotal_with_purchase** | [**CouponAmountOffSubtotalWithPurchase**](CouponAmountOffSubtotalWithPurchase.md) |  | [optional] 
**amount_shipping_with_subtotal** | [**CouponAmountShippingWithSubtotal**](CouponAmountShippingWithSubtotal.md) |  | [optional] 
**automatically_apply_coupon_codes** | [**CouponAutomaticallyApplyCouponCodes**](CouponAutomaticallyApplyCouponCodes.md) |  | [optional] 
**buy_one_get_one** | [**CouponBuyOneGetOneLimit**](CouponBuyOneGetOneLimit.md) |  | [optional] 
**calculated_description** | **str** | Calculated description displayed to the customer if no description is specified. | [optional] 
**can_be_used_with_other_coupons** | **bool** | True if this coupon can be used with other coupons in a single order. | [optional] 
**coupon_oid** | **int** | Coupon oid. | [optional] 
**coupon_type** | **str** | Coupon type. | [optional] 
**description** | **str** | Description of the coupon up to 50 characters. | [optional] 
**discount_item_with_item_purchase** | [**CouponDiscountItemWithItemPurchase**](CouponDiscountItemWithItemPurchase.md) |  | [optional] 
**discount_items** | [**CouponDiscountItems**](CouponDiscountItems.md) |  | [optional] 
**expiration_dts** | **str** | Date/time when coupon expires | [optional] 
**free_item_and_shipping_with_subtotal** | [**CouponFreeItemAndShippingWithSubtotal**](CouponFreeItemAndShippingWithSubtotal.md) |  | [optional] 
**free_item_with_item_purchase** | [**CouponFreeItemWithItemPurchase**](CouponFreeItemWithItemPurchase.md) |  | [optional] 
**free_item_with_item_purchase_and_free_shipping** | [**CouponFreeItemWithItemPurchaseAndFreeShipping**](CouponFreeItemWithItemPurchaseAndFreeShipping.md) |  | [optional] 
**free_item_with_subtotal** | [**CouponFreeItemWithSubtotal**](CouponFreeItemWithSubtotal.md) |  | [optional] 
**free_items_with_item_purchase** | [**CouponFreeItemsWithItemPurchase**](CouponFreeItemsWithItemPurchase.md) |  | [optional] 
**free_items_with_mixmatch_purchase** | [**CouponFreeItemsWithMixMatchPurchase**](CouponFreeItemsWithMixMatchPurchase.md) |  | [optional] 
**free_shipping** | [**CouponFreeShipping**](CouponFreeShipping.md) |  | [optional] 
**free_shipping_specific_items** | [**CouponFreeShippingSpecificItems**](CouponFreeShippingSpecificItems.md) |  | [optional] 
**free_shipping_with_items_purchase** | [**CouponFreeShippingWithItemsPurchase**](CouponFreeShippingWithItemsPurchase.md) |  | [optional] 
**free_shipping_with_subtotal** | [**CouponFreeShippingWithSubtotal**](CouponFreeShippingWithSubtotal.md) |  | [optional] 
**hide_from_customer** | **bool** | Hide coupon from customer during checkout.  Often used when coupons are automatic discounting mechanisms. | [optional] 
**merchant_code** | **str** | Merchant code of coupon up to 20 characters. | [optional] 
**merchant_notes** | **str** | Internal notes about this coupon.  These are not visible to customer. | [optional] 
**more_loyalty_cashback** | [**CouponMoreLoyaltyCashback**](CouponMoreLoyaltyCashback.md) |  | [optional] 
**more_loyalty_points** | [**CouponMoreLoyaltyPoints**](CouponMoreLoyaltyPoints.md) |  | [optional] 
**multiple_amounts_off_items** | [**CouponMultipleAmountsOffItems**](CouponMultipleAmountsOffItems.md) |  | [optional] 
**no_discount** | [**CouponNoDiscount**](CouponNoDiscount.md) |  | [optional] 
**percent_more_loyalty_cashback** | [**CouponPercentMoreLoyaltyCashback**](CouponPercentMoreLoyaltyCashback.md) |  | [optional] 
**percent_more_loyalty_points** | [**CouponPercentMoreLoyaltyPoints**](CouponPercentMoreLoyaltyPoints.md) |  | [optional] 
**percent_off_item_with_items_quantity_purchase** | [**CouponPercentOffItemWithItemsQuantityPurchase**](CouponPercentOffItemWithItemsQuantityPurchase.md) |  | [optional] 
**percent_off_items** | [**CouponPercentOffItems**](CouponPercentOffItems.md) |  | [optional] 
**percent_off_items_and_free_shipping** | [**CouponPercentOffItemsAndFreeShipping**](CouponPercentOffItemsAndFreeShipping.md) |  | [optional] 
**percent_off_items_with_items_purchase** | [**CouponPercentOffItemsWithItemsPurchase**](CouponPercentOffItemsWithItemsPurchase.md) |  | [optional] 
**percent_off_msrp_items** | [**CouponPercentOffMsrpItems**](CouponPercentOffMsrpItems.md) |  | [optional] 
**percent_off_retail_price_items** | [**CouponPercentOffRetailPriceItems**](CouponPercentOffRetailPriceItems.md) |  | [optional] 
**percent_off_shipping** | [**CouponPercentOffShipping**](CouponPercentOffShipping.md) |  | [optional] 
**percent_off_subtotal** | [**CouponPercentOffSubtotal**](CouponPercentOffSubtotal.md) |  | [optional] 
**percent_off_subtotal_and_free_shipping** | [**CouponPercentOffSubtotalAndFreeShipping**](CouponPercentOffSubtotalAndFreeShipping.md) |  | [optional] 
**percent_off_subtotal_limit** | [**CouponPercentOffSubtotalLimit**](CouponPercentOffSubtotalLimit.md) |  | [optional] 
**percent_off_subtotal_with_items_purchase** | [**CouponPercentOffSubtotalWithItemsPurchase**](CouponPercentOffSubtotalWithItemsPurchase.md) |  | [optional] 
**percent_off_subtotal_with_subtotal** | [**CouponPercentOffSubtotalWithSubtotal**](CouponPercentOffSubtotalWithSubtotal.md) |  | [optional] 
**quickbooks_code** | **str** | Quickbooks accounting code. | [optional] 
**restrict_by_postal_codes** | **[str]** | Optional list of postal codes which restrict a coupon to within these postal codes. | [optional] 
**restrict_by_screen_branding_theme_codes** | [**[CouponRestriction]**](CouponRestriction.md) | Optional list of legacy screen branding theme codes to limit coupon use to only those themes. | [optional] 
**restrict_by_storefronts** | [**[CouponRestriction]**](CouponRestriction.md) | Optional list of storefronts to limit coupon use to only those storefronts. | [optional] 
**skip_on_rebill** | **bool** | Skip this coupon when it is on a rebill of an auto order. | [optional] 
**start_dts** | **str** | Date/time when coupon is valid | [optional] 
**super_coupon** | **bool** | If true, this coupon can be used with ANY other coupon regardless of the other coupons configuration | [optional] 
**tiered_amount_off_items** | [**CouponTieredAmountOffItems**](CouponTieredAmountOffItems.md) |  | [optional] 
**tiered_amount_off_subtotal** | [**CouponTieredAmountOffSubtotal**](CouponTieredAmountOffSubtotal.md) |  | [optional] 
**tiered_percent_off_items** | [**CouponTieredPercentOffItems**](CouponTieredPercentOffItems.md) |  | [optional] 
**tiered_percent_off_shipping** | [**CouponTieredPercentOffShipping**](CouponTieredPercentOffShipping.md) |  | [optional] 
**tiered_percent_off_subtotal** | [**CouponTieredPercentOffSubtotal**](CouponTieredPercentOffSubtotal.md) |  | [optional] 
**tiered_percent_off_subtotal_based_on_msrp** | [**CouponTieredPercentOffSubtotalBasedOnMSRP**](CouponTieredPercentOffSubtotalBasedOnMSRP.md) |  | [optional] 
**usable_by** | **str** | Who may use this coupon. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


