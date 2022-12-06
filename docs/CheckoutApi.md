# ultracart.CheckoutApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**city_state**](CheckoutApi.md#city_state) | **POST** /checkout/city_state | City/State for Zip
[**finalize_order**](CheckoutApi.md#finalize_order) | **POST** /checkout/cart/finalizeOrder | Finalize Order
[**get_affirm_checkout**](CheckoutApi.md#get_affirm_checkout) | **GET** /checkout/cart/{cart_id}/affirmCheckout | Get affirm checkout (by cart id)
[**get_allowed_countries**](CheckoutApi.md#get_allowed_countries) | **POST** /checkout/allowedCountries | Allowed countries
[**get_cart**](CheckoutApi.md#get_cart) | **GET** /checkout/cart | Get cart
[**get_cart_by_cart_id**](CheckoutApi.md#get_cart_by_cart_id) | **GET** /checkout/cart/{cart_id} | Get cart (by cart id)
[**get_cart_by_return_code**](CheckoutApi.md#get_cart_by_return_code) | **GET** /checkout/return/{return_code} | Get cart (by return code)
[**get_cart_by_return_token**](CheckoutApi.md#get_cart_by_return_token) | **GET** /checkout/return_token | Get cart (by return token)
[**get_state_provinces_for_country**](CheckoutApi.md#get_state_provinces_for_country) | **POST** /checkout/stateProvincesForCountry/{country_code} | Get state/province list for a country code
[**handoff_cart**](CheckoutApi.md#handoff_cart) | **POST** /checkout/cart/handoff | Handoff cart
[**login**](CheckoutApi.md#login) | **POST** /checkout/cart/profile/login | Profile login
[**logout**](CheckoutApi.md#logout) | **POST** /checkout/cart/profile/logout | Profile logout
[**register**](CheckoutApi.md#register) | **POST** /checkout/cart/profile/register | Profile registration
[**register_affiliate_click**](CheckoutApi.md#register_affiliate_click) | **POST** /checkout/affiliateClick/register | Register affiliate click
[**related_items_for_cart**](CheckoutApi.md#related_items_for_cart) | **POST** /checkout/related_items | Related items
[**related_items_for_item**](CheckoutApi.md#related_items_for_item) | **POST** /checkout/relatedItems/{item_id} | Related items (specific item)
[**setup_browser_key**](CheckoutApi.md#setup_browser_key) | **PUT** /checkout/browser_key | Setup Browser Application
[**update_cart**](CheckoutApi.md#update_cart) | **PUT** /checkout/cart | Update cart
[**validate_cart**](CheckoutApi.md#validate_cart) | **POST** /checkout/cart/validate | Validate


# **city_state**
> CityStateZip city_state(cart)

City/State for Zip

Look up the city and state for the shipping zip code.  Useful for building an auto complete for parts of the shipping address 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.city_state_zip import CityStateZip
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart import Cart
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    cart = Cart(
        affiliate=CartAffiliate(
            affiliate_id=1,
            affiliate_sub_id="affiliate_sub_id_example",
        ),
        affiliate_network_pixel_oid=1,
        base_currency_code="base_currency_code_example",
        billing=CartBilling(
            address1="address1_example",
            address2="address2_example",
            cc_emails=[
                "cc_emails_example",
            ],
            cell_phone="cell_phone_example",
            cell_phone_e164="cell_phone_e164_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            email="email_example",
            email_confirm="email_confirm_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=CartBuysafe(
            bond_available=True,
            bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            bond_free=True,
            bond_wanted=True,
            cart_display_text="cart_display_text_example",
            cart_display_url="cart_display_url_example",
        ),
        cart_id="cart_id_example",
        checkout=CartCheckout(
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            ip_address="ip_address_example",
            return_code="return_code_example",
            return_url="return_url_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            storefront_host_name="storefront_host_name_example",
            user_agent="user_agent_example",
        ),
        coupons=[
            CartCoupon(
                coupon_code="coupon_code_example",
            ),
        ],
        currency_code="currency_code_example",
        currency_conversion=CartCurrencyConversion(
            base_currency_code="base_currency_code_example",
            currencies=[
                Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ],
        ),
        customer_profile=CartCustomerProfile(
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_purchase_order=True,
            billing_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            credit_cards=[
                CartCustomerProfileCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_type="AMEX",
                    customer_profile_credit_card_id=1,
                    last_used_date="last_used_date_example",
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            email="email_example",
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            maximum_item_count=1,
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            pricing_tiers=[
                "pricing_tiers_example",
            ],
            shipping_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            tax_exempt=True,
            ups_account_number="ups_account_number_example",
        ),
        exchange_rate=3.14,
        gift=CartGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=CartGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_remaining_balance_after_order=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        items=[
            CartItem(
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                attributes=[
                    CartItemAttribute(
                        name="name_example",
                        type="type_example",
                        value="value_example",
                    ),
                ],
                auto_order_schedule="auto_order_schedule_example",
                default_image_url="default_image_url_example",
                default_thumbnail_url="default_thumbnail_url_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                extended_description="extended_description_example",
                item_id="item_id_example",
                item_oid=1,
                kit=True,
                kit_component_options=[
                    CartKitComponentOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        item_id="item_id_example",
                        item_oid=1,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                manufacturer_suggested_retail_price=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                maximum_quantity=3.14,
                minimum_quantity=3.14,
                multimedia=[
                    CartItemMultimedia(
                        code="code_example",
                        description="description_example",
                        exclude_from_gallery=True,
                        image_height=1,
                        image_width=1,
                        is_default=True,
                        thumbnails=[
                            CartItemMultimediaThumbnail(
                                height=1,
                                png=True,
                                square=True,
                                url="url_example",
                                width=1,
                            ),
                        ],
                        type="Image",
                        url="url_example",
                    ),
                ],
                options=[
                    CartItemOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                phsyical=CartItemPhysical(
                    height=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    length=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                    width=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                ),
                position=1,
                preorder=True,
                quantity=3.14,
                schedules=[
                    "schedules_example",
                ],
                total_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                variations=[
                    CartItemVariationSelection(
                        variation_name="variation_name_example",
                        variation_value="variation_value_example",
                    ),
                ],
                view_url="view_url_example",
            ),
        ],
        language_iso_code="language_iso_code_example",
        logged_in=True,
        marketing=CartMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list_opt_in=True,
        ),
        merchant_id="merchant_id_example",
        payment=CartPayment(
            affirm=CartPaymentAffirm(
                affirm_checkout_token="affirm_checkout_token_example",
            ),
            amazon=CartPaymentAmazon(
                amazon_order_reference_id="amazon_order_reference_id_example",
            ),
            check=CartPaymentCheck(
                check_number=1,
            ),
            credit_card=CartPaymentCreditCard(
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_type="card_type_example",
                card_verification_number="card_verification_number_example",
                card_verification_number_token="card_verification_number_token_example",
                customer_profile_credit_card_id=1,
                store_credit_card=True,
            ),
            payment_method="payment_method_example",
            purchase_order=CartPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rtg_code="rtg_code_example",
        ),
        properties=[
            CartProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        settings=CartSettings(
            billing=CartSettingsBilling(
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
            ),
            gift=CartSettingsGift(
                allow_gifts=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wraps=[
                    CartSettingsGiftWrap(
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        title="title_example",
                        url="url_example",
                    ),
                ],
                max_message_length=1,
            ),
            payment=CartSettingsPayment(
                amazon=CartSettingsPaymentAmazon(
                    amazon_button_url="amazon_button_url_example",
                    amazon_merchant_id="amazon_merchant_id_example",
                    amazon_widget_url="amazon_widget_url_example",
                ),
                credit_card=CartSettingsPaymentCreditCard(
                    collect_credit_card_verification_number=True,
                    credit_card_types=[
                        "credit_card_types_example",
                    ],
                    hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                ),
                need_payment=True,
                paypal=CartSettingsPaymentPayPal(
                    paypal_button_alt_text="paypal_button_alt_text_example",
                    paypal_button_url="paypal_button_url_example",
                    paypal_credit_button_url="paypal_credit_button_url_example",
                    paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                    paypal_credit_legal_url="paypal_credit_legal_url_example",
                ),
                supports_amazon=True,
                supports_check=True,
                supports_cod=True,
                supports_credit_card=True,
                supports_money_order=True,
                supports_paypal=True,
                supports_purchase_order=True,
                supports_quote_request=True,
                supports_wire_transfer=True,
            ),
            shipping=CartSettingsShipping(
                deliver_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
                estimates=[
                    CartSettingsShippingEstimate(
                        allow_3rd_party_billing=True,
                        comment="comment_example",
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_before_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        default_method=True,
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discounted=True,
                        display_name="display_name_example",
                        estimated_delivery="estimated_delivery_example",
                        lift_gate_option=True,
                        name="name_example",
                        pickup=True,
                        tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                    ),
                ],
                need_shipping=True,
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
                ship_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
            ),
            taxes=CartSettingsTaxes(
                counties=[
                    "counties_example",
                ],
            ),
            terms=CartSettingsTerms(
                html="html_example",
                text="text_example",
            ),
        ),
        shipping=CartShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            lift_gate=True,
            postal_code="postal_code_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_method="shipping_method_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
        ),
        summary=CartSummary(
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax_rate=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        taxes=CartTaxes(
            county="county_example",
            exempt=True,
            rate=3.14,
        ),
        upsell_after=CartUpsellAfter(
            finalize_after_dts="finalize_after_dts_example",
            finalize_after_minutes=1,
            upsell_path_code="upsell_path_code_example",
        ),
    ) # Cart | Cart

    # example passing only required values which don't have defaults set
    try:
        # City/State for Zip
        api_response = api_instance.city_state(cart)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->city_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart |

### Return type

[**CityStateZip**](CityStateZip.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_order**
> CartFinalizeOrderResponse finalize_order(finalize_request)

Finalize Order

Finalize the cart into an order.  This method can not be called with browser key authentication.  It is ONLY meant for server side code to call. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_finalize_order_request import CartFinalizeOrderRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart_finalize_order_response import CartFinalizeOrderResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    finalize_request = CartFinalizeOrderRequest(
        cart=Cart(
            affiliate=CartAffiliate(
                affiliate_id=1,
                affiliate_sub_id="affiliate_sub_id_example",
            ),
            affiliate_network_pixel_oid=1,
            base_currency_code="base_currency_code_example",
            billing=CartBilling(
                address1="address1_example",
                address2="address2_example",
                cc_emails=[
                    "cc_emails_example",
                ],
                cell_phone="cell_phone_example",
                cell_phone_e164="cell_phone_e164_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                email="email_example",
                email_confirm="email_confirm_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                title="title_example",
            ),
            buysafe=CartBuysafe(
                bond_available=True,
                bond_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                bond_free=True,
                bond_wanted=True,
                cart_display_text="cart_display_text_example",
                cart_display_url="cart_display_url_example",
            ),
            cart_id="cart_id_example",
            checkout=CartCheckout(
                comments="comments_example",
                custom_field1="custom_field1_example",
                custom_field2="custom_field2_example",
                custom_field3="custom_field3_example",
                custom_field4="custom_field4_example",
                custom_field5="custom_field5_example",
                custom_field6="custom_field6_example",
                custom_field7="custom_field7_example",
                ip_address="ip_address_example",
                return_code="return_code_example",
                return_url="return_url_example",
                screen_branding_theme_code="screen_branding_theme_code_example",
                storefront_host_name="storefront_host_name_example",
                user_agent="user_agent_example",
            ),
            coupons=[
                CartCoupon(
                    coupon_code="coupon_code_example",
                ),
            ],
            currency_code="currency_code_example",
            currency_conversion=CartCurrencyConversion(
                base_currency_code="base_currency_code_example",
                currencies=[
                    Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ],
            ),
            customer_profile=CartCustomerProfile(
                allow_3rd_party_billing=True,
                allow_cod=True,
                allow_purchase_order=True,
                billing_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                credit_cards=[
                    CartCustomerProfileCreditCard(
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_type="AMEX",
                        customer_profile_credit_card_id=1,
                        last_used_date="last_used_date_example",
                    ),
                ],
                customer_profile_oid=1,
                dhl_account_number="dhl_account_number_example",
                dhl_duty_account_number="dhl_duty_account_number_example",
                email="email_example",
                fedex_account_number="fedex_account_number_example",
                free_shipping=True,
                free_shipping_minimum=3.14,
                maximum_item_count=1,
                minimum_item_count=1,
                minimum_subtotal=3.14,
                no_coupons=True,
                no_free_shipping=True,
                no_realtime_charge=True,
                pricing_tiers=[
                    "pricing_tiers_example",
                ],
                shipping_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                signup_dts="signup_dts_example",
                tax_exempt=True,
                ups_account_number="ups_account_number_example",
            ),
            exchange_rate=3.14,
            gift=CartGift(
                gift=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_email="gift_email_example",
                gift_message="gift_message_example",
                gift_wrap_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wrap_title="gift_wrap_title_example",
            ),
            gift_certificate=CartGiftCertificate(
                gift_certificate_amount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_certificate_code="gift_certificate_code_example",
                gift_certificate_remaining_balance_after_order=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            items=[
                CartItem(
                    arbitrary_unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    attributes=[
                        CartItemAttribute(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    auto_order_schedule="auto_order_schedule_example",
                    default_image_url="default_image_url_example",
                    default_thumbnail_url="default_thumbnail_url_example",
                    description="description_example",
                    discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    extended_description="extended_description_example",
                    item_id="item_id_example",
                    item_oid=1,
                    kit=True,
                    kit_component_options=[
                        CartKitComponentOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            item_id="item_id_example",
                            item_oid=1,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    manufacturer_suggested_retail_price=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    maximum_quantity=3.14,
                    minimum_quantity=3.14,
                    multimedia=[
                        CartItemMultimedia(
                            code="code_example",
                            description="description_example",
                            exclude_from_gallery=True,
                            image_height=1,
                            image_width=1,
                            is_default=True,
                            thumbnails=[
                                CartItemMultimediaThumbnail(
                                    height=1,
                                    png=True,
                                    square=True,
                                    url="url_example",
                                    width=1,
                                ),
                            ],
                            type="Image",
                            url="url_example",
                        ),
                    ],
                    options=[
                        CartItemOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    phsyical=CartItemPhysical(
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                    position=1,
                    preorder=True,
                    quantity=3.14,
                    schedules=[
                        "schedules_example",
                    ],
                    total_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    upsell=True,
                    variations=[
                        CartItemVariationSelection(
                            variation_name="variation_name_example",
                            variation_value="variation_value_example",
                        ),
                    ],
                    view_url="view_url_example",
                ),
            ],
            language_iso_code="language_iso_code_example",
            logged_in=True,
            marketing=CartMarketing(
                advertising_source="advertising_source_example",
                cell_phone_opt_in=True,
                mailing_list_opt_in=True,
            ),
            merchant_id="merchant_id_example",
            payment=CartPayment(
                affirm=CartPaymentAffirm(
                    affirm_checkout_token="affirm_checkout_token_example",
                ),
                amazon=CartPaymentAmazon(
                    amazon_order_reference_id="amazon_order_reference_id_example",
                ),
                check=CartPaymentCheck(
                    check_number=1,
                ),
                credit_card=CartPaymentCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    card_verification_number="card_verification_number_example",
                    card_verification_number_token="card_verification_number_token_example",
                    customer_profile_credit_card_id=1,
                    store_credit_card=True,
                ),
                payment_method="payment_method_example",
                purchase_order=CartPaymentPurchaseOrder(
                    purchase_order_number="purchase_order_number_example",
                ),
                rtg_code="rtg_code_example",
            ),
            properties=[
                CartProperty(
                    display=True,
                    expiration_dts="expiration_dts_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
            settings=CartSettings(
                billing=CartSettingsBilling(
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                ),
                gift=CartSettingsGift(
                    allow_gifts=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wraps=[
                        CartSettingsGiftWrap(
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            title="title_example",
                            url="url_example",
                        ),
                    ],
                    max_message_length=1,
                ),
                payment=CartSettingsPayment(
                    amazon=CartSettingsPaymentAmazon(
                        amazon_button_url="amazon_button_url_example",
                        amazon_merchant_id="amazon_merchant_id_example",
                        amazon_widget_url="amazon_widget_url_example",
                    ),
                    credit_card=CartSettingsPaymentCreditCard(
                        collect_credit_card_verification_number=True,
                        credit_card_types=[
                            "credit_card_types_example",
                        ],
                        hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                    ),
                    need_payment=True,
                    paypal=CartSettingsPaymentPayPal(
                        paypal_button_alt_text="paypal_button_alt_text_example",
                        paypal_button_url="paypal_button_url_example",
                        paypal_credit_button_url="paypal_credit_button_url_example",
                        paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                        paypal_credit_legal_url="paypal_credit_legal_url_example",
                    ),
                    supports_amazon=True,
                    supports_check=True,
                    supports_cod=True,
                    supports_credit_card=True,
                    supports_money_order=True,
                    supports_paypal=True,
                    supports_purchase_order=True,
                    supports_quote_request=True,
                    supports_wire_transfer=True,
                ),
                shipping=CartSettingsShipping(
                    deliver_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                    estimates=[
                        CartSettingsShippingEstimate(
                            allow_3rd_party_billing=True,
                            comment="comment_example",
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_before_discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            default_method=True,
                            discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            discounted=True,
                            display_name="display_name_example",
                            estimated_delivery="estimated_delivery_example",
                            lift_gate_option=True,
                            name="name_example",
                            pickup=True,
                            tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            total_tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                        ),
                    ],
                    need_shipping=True,
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                    ship_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                ),
                taxes=CartSettingsTaxes(
                    counties=[
                        "counties_example",
                    ],
                ),
                terms=CartSettingsTerms(
                    html="html_example",
                    text="text_example",
                ),
            ),
            shipping=CartShipping(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                delivery_date="delivery_date_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                lift_gate=True,
                postal_code="postal_code_example",
                ship_on_date="ship_on_date_example",
                ship_to_residential=True,
                shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                shipping_method="shipping_method_example",
                special_instructions="special_instructions_example",
                state_region="state_region_example",
                title="title_example",
            ),
            summary=CartSummary(
                arbitrary_shipping_handling_total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax_rate=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                surcharge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            taxes=CartTaxes(
                county="county_example",
                exempt=True,
                rate=3.14,
            ),
            upsell_after=CartUpsellAfter(
                finalize_after_dts="finalize_after_dts_example",
                finalize_after_minutes=1,
                upsell_path_code="upsell_path_code_example",
            ),
        ),
        options=CartFinalizeOrderRequestOptions(
            auto_approve_purchase_order=True,
            channel_partner_code="channel_partner_code_example",
            channel_partner_oid=1,
            channel_partner_order_id="channel_partner_order_id_example",
            consider_recurring=True,
            credit_card_authorization_amount=3.14,
            credit_card_authorization_date="credit_card_authorization_date_example",
            credit_card_authorization_reference_number="credit_card_authorization_reference_number_example",
            no_realtime_payment_processing=True,
            setup_next_cart=True,
            skip_payment_processing=True,
            store_completed=True,
            store_if_payment_declines=True,
        ),
    ) # CartFinalizeOrderRequest | Finalize request

    # example passing only required values which don't have defaults set
    try:
        # Finalize Order
        api_response = api_instance.finalize_order(finalize_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->finalize_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finalize_request** | [**CartFinalizeOrderRequest**](CartFinalizeOrderRequest.md)| Finalize request |

### Return type

[**CartFinalizeOrderResponse**](CartFinalizeOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affirm_checkout**
> CartAffirmCheckoutResponse get_affirm_checkout(cart_id)

Get affirm checkout (by cart id)

Get a Affirm checkout object for the specified cart_id parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart_affirm_checkout_response import CartAffirmCheckoutResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    cart_id = "cart_id_example" # str | Cart ID to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Get affirm checkout (by cart id)
        api_response = api_instance.get_affirm_checkout(cart_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_affirm_checkout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| Cart ID to retrieve |

### Return type

[**CartAffirmCheckoutResponse**](CartAffirmCheckoutResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allowed_countries**
> CheckoutAllowedCountriesResponse get_allowed_countries()

Allowed countries

Lookup the allowed countries for this merchant id 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.checkout_allowed_countries_response import CheckoutAllowedCountriesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Allowed countries
        api_response = api_instance.get_allowed_countries()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_allowed_countries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckoutAllowedCountriesResponse**](CheckoutAllowedCountriesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart**
> CartResponse get_cart()

Get cart

If the cookie is set on the browser making the request then it will return their active cart.  Otherwise it will create a new cart. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_response import CartResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get cart
        api_response = api_instance.get_cart(expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_cart_id**
> CartResponse get_cart_by_cart_id(cart_id)

Get cart (by cart id)

Get a cart specified by the cart_id parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_response import CartResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    cart_id = "cart_id_example" # str | Cart ID to retrieve
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get cart (by cart id)
        api_response = api_instance.get_cart_by_cart_id(cart_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_cart_by_cart_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get cart (by cart id)
        api_response = api_instance.get_cart_by_cart_id(cart_id, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_cart_by_cart_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| Cart ID to retrieve |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_return_code**
> CartResponse get_cart_by_return_code(return_code)

Get cart (by return code)

Get a cart specified by the return code parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_response import CartResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    return_code = "return_code_example" # str | Return code to lookup cart ID by
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get cart (by return code)
        api_response = api_instance.get_cart_by_return_code(return_code)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_cart_by_return_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get cart (by return code)
        api_response = api_instance.get_cart_by_return_code(return_code, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_cart_by_return_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_code** | **str**| Return code to lookup cart ID by |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_return_token**
> CartResponse get_cart_by_return_token()

Get cart (by return token)

Get a cart specified by the encrypted return token parameter. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_response import CartResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    return_token = "return_token_example" # str | Return token provided by StoreFront Communications (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get cart (by return token)
        api_response = api_instance.get_cart_by_return_token(return_token=return_token, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_cart_by_return_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_token** | **str**| Return token provided by StoreFront Communications | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_provinces_for_country**
> CheckoutStateProvinceResponse get_state_provinces_for_country(country_code)

Get state/province list for a country code

Lookup a state/province list for a given country code 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.checkout_state_province_response import CheckoutStateProvinceResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    country_code = "country_code_example" # str | Two letter ISO country code

    # example passing only required values which don't have defaults set
    try:
        # Get state/province list for a country code
        api_response = api_instance.get_state_provinces_for_country(country_code)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->get_state_provinces_for_country: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter ISO country code |

### Return type

[**CheckoutStateProvinceResponse**](CheckoutStateProvinceResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handoff_cart**
> CheckoutHandoffResponse handoff_cart(handoff_request)

Handoff cart

Handoff the browser to UltraCart for view cart on StoreFront, transfer to PayPal, transfer to Affirm, transfer to Sezzle or finalization of the order (including upsell processing). 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.checkout_handoff_response import CheckoutHandoffResponse
from ultracart.model.checkout_handoff_request import CheckoutHandoffRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    handoff_request = CheckoutHandoffRequest(
        cart=Cart(
            affiliate=CartAffiliate(
                affiliate_id=1,
                affiliate_sub_id="affiliate_sub_id_example",
            ),
            affiliate_network_pixel_oid=1,
            base_currency_code="base_currency_code_example",
            billing=CartBilling(
                address1="address1_example",
                address2="address2_example",
                cc_emails=[
                    "cc_emails_example",
                ],
                cell_phone="cell_phone_example",
                cell_phone_e164="cell_phone_e164_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                email="email_example",
                email_confirm="email_confirm_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                title="title_example",
            ),
            buysafe=CartBuysafe(
                bond_available=True,
                bond_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                bond_free=True,
                bond_wanted=True,
                cart_display_text="cart_display_text_example",
                cart_display_url="cart_display_url_example",
            ),
            cart_id="cart_id_example",
            checkout=CartCheckout(
                comments="comments_example",
                custom_field1="custom_field1_example",
                custom_field2="custom_field2_example",
                custom_field3="custom_field3_example",
                custom_field4="custom_field4_example",
                custom_field5="custom_field5_example",
                custom_field6="custom_field6_example",
                custom_field7="custom_field7_example",
                ip_address="ip_address_example",
                return_code="return_code_example",
                return_url="return_url_example",
                screen_branding_theme_code="screen_branding_theme_code_example",
                storefront_host_name="storefront_host_name_example",
                user_agent="user_agent_example",
            ),
            coupons=[
                CartCoupon(
                    coupon_code="coupon_code_example",
                ),
            ],
            currency_code="currency_code_example",
            currency_conversion=CartCurrencyConversion(
                base_currency_code="base_currency_code_example",
                currencies=[
                    Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ],
            ),
            customer_profile=CartCustomerProfile(
                allow_3rd_party_billing=True,
                allow_cod=True,
                allow_purchase_order=True,
                billing_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                credit_cards=[
                    CartCustomerProfileCreditCard(
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_type="AMEX",
                        customer_profile_credit_card_id=1,
                        last_used_date="last_used_date_example",
                    ),
                ],
                customer_profile_oid=1,
                dhl_account_number="dhl_account_number_example",
                dhl_duty_account_number="dhl_duty_account_number_example",
                email="email_example",
                fedex_account_number="fedex_account_number_example",
                free_shipping=True,
                free_shipping_minimum=3.14,
                maximum_item_count=1,
                minimum_item_count=1,
                minimum_subtotal=3.14,
                no_coupons=True,
                no_free_shipping=True,
                no_realtime_charge=True,
                pricing_tiers=[
                    "pricing_tiers_example",
                ],
                shipping_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                signup_dts="signup_dts_example",
                tax_exempt=True,
                ups_account_number="ups_account_number_example",
            ),
            exchange_rate=3.14,
            gift=CartGift(
                gift=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_email="gift_email_example",
                gift_message="gift_message_example",
                gift_wrap_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wrap_title="gift_wrap_title_example",
            ),
            gift_certificate=CartGiftCertificate(
                gift_certificate_amount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_certificate_code="gift_certificate_code_example",
                gift_certificate_remaining_balance_after_order=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            items=[
                CartItem(
                    arbitrary_unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    attributes=[
                        CartItemAttribute(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    auto_order_schedule="auto_order_schedule_example",
                    default_image_url="default_image_url_example",
                    default_thumbnail_url="default_thumbnail_url_example",
                    description="description_example",
                    discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    extended_description="extended_description_example",
                    item_id="item_id_example",
                    item_oid=1,
                    kit=True,
                    kit_component_options=[
                        CartKitComponentOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            item_id="item_id_example",
                            item_oid=1,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    manufacturer_suggested_retail_price=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    maximum_quantity=3.14,
                    minimum_quantity=3.14,
                    multimedia=[
                        CartItemMultimedia(
                            code="code_example",
                            description="description_example",
                            exclude_from_gallery=True,
                            image_height=1,
                            image_width=1,
                            is_default=True,
                            thumbnails=[
                                CartItemMultimediaThumbnail(
                                    height=1,
                                    png=True,
                                    square=True,
                                    url="url_example",
                                    width=1,
                                ),
                            ],
                            type="Image",
                            url="url_example",
                        ),
                    ],
                    options=[
                        CartItemOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    phsyical=CartItemPhysical(
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                    position=1,
                    preorder=True,
                    quantity=3.14,
                    schedules=[
                        "schedules_example",
                    ],
                    total_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    upsell=True,
                    variations=[
                        CartItemVariationSelection(
                            variation_name="variation_name_example",
                            variation_value="variation_value_example",
                        ),
                    ],
                    view_url="view_url_example",
                ),
            ],
            language_iso_code="language_iso_code_example",
            logged_in=True,
            marketing=CartMarketing(
                advertising_source="advertising_source_example",
                cell_phone_opt_in=True,
                mailing_list_opt_in=True,
            ),
            merchant_id="merchant_id_example",
            payment=CartPayment(
                affirm=CartPaymentAffirm(
                    affirm_checkout_token="affirm_checkout_token_example",
                ),
                amazon=CartPaymentAmazon(
                    amazon_order_reference_id="amazon_order_reference_id_example",
                ),
                check=CartPaymentCheck(
                    check_number=1,
                ),
                credit_card=CartPaymentCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    card_verification_number="card_verification_number_example",
                    card_verification_number_token="card_verification_number_token_example",
                    customer_profile_credit_card_id=1,
                    store_credit_card=True,
                ),
                payment_method="payment_method_example",
                purchase_order=CartPaymentPurchaseOrder(
                    purchase_order_number="purchase_order_number_example",
                ),
                rtg_code="rtg_code_example",
            ),
            properties=[
                CartProperty(
                    display=True,
                    expiration_dts="expiration_dts_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
            settings=CartSettings(
                billing=CartSettingsBilling(
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                ),
                gift=CartSettingsGift(
                    allow_gifts=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wraps=[
                        CartSettingsGiftWrap(
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            title="title_example",
                            url="url_example",
                        ),
                    ],
                    max_message_length=1,
                ),
                payment=CartSettingsPayment(
                    amazon=CartSettingsPaymentAmazon(
                        amazon_button_url="amazon_button_url_example",
                        amazon_merchant_id="amazon_merchant_id_example",
                        amazon_widget_url="amazon_widget_url_example",
                    ),
                    credit_card=CartSettingsPaymentCreditCard(
                        collect_credit_card_verification_number=True,
                        credit_card_types=[
                            "credit_card_types_example",
                        ],
                        hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                    ),
                    need_payment=True,
                    paypal=CartSettingsPaymentPayPal(
                        paypal_button_alt_text="paypal_button_alt_text_example",
                        paypal_button_url="paypal_button_url_example",
                        paypal_credit_button_url="paypal_credit_button_url_example",
                        paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                        paypal_credit_legal_url="paypal_credit_legal_url_example",
                    ),
                    supports_amazon=True,
                    supports_check=True,
                    supports_cod=True,
                    supports_credit_card=True,
                    supports_money_order=True,
                    supports_paypal=True,
                    supports_purchase_order=True,
                    supports_quote_request=True,
                    supports_wire_transfer=True,
                ),
                shipping=CartSettingsShipping(
                    deliver_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                    estimates=[
                        CartSettingsShippingEstimate(
                            allow_3rd_party_billing=True,
                            comment="comment_example",
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_before_discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            default_method=True,
                            discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            discounted=True,
                            display_name="display_name_example",
                            estimated_delivery="estimated_delivery_example",
                            lift_gate_option=True,
                            name="name_example",
                            pickup=True,
                            tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            total_tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                        ),
                    ],
                    need_shipping=True,
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                    ship_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                ),
                taxes=CartSettingsTaxes(
                    counties=[
                        "counties_example",
                    ],
                ),
                terms=CartSettingsTerms(
                    html="html_example",
                    text="text_example",
                ),
            ),
            shipping=CartShipping(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                delivery_date="delivery_date_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                lift_gate=True,
                postal_code="postal_code_example",
                ship_on_date="ship_on_date_example",
                ship_to_residential=True,
                shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                shipping_method="shipping_method_example",
                special_instructions="special_instructions_example",
                state_region="state_region_example",
                title="title_example",
            ),
            summary=CartSummary(
                arbitrary_shipping_handling_total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax_rate=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                surcharge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            taxes=CartTaxes(
                county="county_example",
                exempt=True,
                rate=3.14,
            ),
            upsell_after=CartUpsellAfter(
                finalize_after_dts="finalize_after_dts_example",
                finalize_after_minutes=1,
                upsell_path_code="upsell_path_code_example",
            ),
        ),
        error_parameter_name="error_parameter_name_example",
        error_return_url="error_return_url_example",
        operation="checkout",
        paypal_maximum_upsell_revenue=3.14,
        paypal_return_url="paypal_return_url_example",
        secure_host_name="secure_host_name_example",
        ucacid="ucacid_example",
    ) # CheckoutHandoffRequest | Handoff request
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Handoff cart
        api_response = api_instance.handoff_cart(handoff_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->handoff_cart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Handoff cart
        api_response = api_instance.handoff_cart(handoff_request, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->handoff_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handoff_request** | [**CheckoutHandoffRequest**](CheckoutHandoffRequest.md)| Handoff request |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CheckoutHandoffResponse**](CheckoutHandoffResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> CartProfileLoginResponse login(login_request)

Profile login

Login in to the customer profile specified by cart.billing.email and password 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_profile_login_request import CartProfileLoginRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart_profile_login_response import CartProfileLoginResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    login_request = CartProfileLoginRequest(
        cart=Cart(
            affiliate=CartAffiliate(
                affiliate_id=1,
                affiliate_sub_id="affiliate_sub_id_example",
            ),
            affiliate_network_pixel_oid=1,
            base_currency_code="base_currency_code_example",
            billing=CartBilling(
                address1="address1_example",
                address2="address2_example",
                cc_emails=[
                    "cc_emails_example",
                ],
                cell_phone="cell_phone_example",
                cell_phone_e164="cell_phone_e164_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                email="email_example",
                email_confirm="email_confirm_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                title="title_example",
            ),
            buysafe=CartBuysafe(
                bond_available=True,
                bond_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                bond_free=True,
                bond_wanted=True,
                cart_display_text="cart_display_text_example",
                cart_display_url="cart_display_url_example",
            ),
            cart_id="cart_id_example",
            checkout=CartCheckout(
                comments="comments_example",
                custom_field1="custom_field1_example",
                custom_field2="custom_field2_example",
                custom_field3="custom_field3_example",
                custom_field4="custom_field4_example",
                custom_field5="custom_field5_example",
                custom_field6="custom_field6_example",
                custom_field7="custom_field7_example",
                ip_address="ip_address_example",
                return_code="return_code_example",
                return_url="return_url_example",
                screen_branding_theme_code="screen_branding_theme_code_example",
                storefront_host_name="storefront_host_name_example",
                user_agent="user_agent_example",
            ),
            coupons=[
                CartCoupon(
                    coupon_code="coupon_code_example",
                ),
            ],
            currency_code="currency_code_example",
            currency_conversion=CartCurrencyConversion(
                base_currency_code="base_currency_code_example",
                currencies=[
                    Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ],
            ),
            customer_profile=CartCustomerProfile(
                allow_3rd_party_billing=True,
                allow_cod=True,
                allow_purchase_order=True,
                billing_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                credit_cards=[
                    CartCustomerProfileCreditCard(
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_type="AMEX",
                        customer_profile_credit_card_id=1,
                        last_used_date="last_used_date_example",
                    ),
                ],
                customer_profile_oid=1,
                dhl_account_number="dhl_account_number_example",
                dhl_duty_account_number="dhl_duty_account_number_example",
                email="email_example",
                fedex_account_number="fedex_account_number_example",
                free_shipping=True,
                free_shipping_minimum=3.14,
                maximum_item_count=1,
                minimum_item_count=1,
                minimum_subtotal=3.14,
                no_coupons=True,
                no_free_shipping=True,
                no_realtime_charge=True,
                pricing_tiers=[
                    "pricing_tiers_example",
                ],
                shipping_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                signup_dts="signup_dts_example",
                tax_exempt=True,
                ups_account_number="ups_account_number_example",
            ),
            exchange_rate=3.14,
            gift=CartGift(
                gift=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_email="gift_email_example",
                gift_message="gift_message_example",
                gift_wrap_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wrap_title="gift_wrap_title_example",
            ),
            gift_certificate=CartGiftCertificate(
                gift_certificate_amount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_certificate_code="gift_certificate_code_example",
                gift_certificate_remaining_balance_after_order=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            items=[
                CartItem(
                    arbitrary_unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    attributes=[
                        CartItemAttribute(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    auto_order_schedule="auto_order_schedule_example",
                    default_image_url="default_image_url_example",
                    default_thumbnail_url="default_thumbnail_url_example",
                    description="description_example",
                    discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    extended_description="extended_description_example",
                    item_id="item_id_example",
                    item_oid=1,
                    kit=True,
                    kit_component_options=[
                        CartKitComponentOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            item_id="item_id_example",
                            item_oid=1,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    manufacturer_suggested_retail_price=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    maximum_quantity=3.14,
                    minimum_quantity=3.14,
                    multimedia=[
                        CartItemMultimedia(
                            code="code_example",
                            description="description_example",
                            exclude_from_gallery=True,
                            image_height=1,
                            image_width=1,
                            is_default=True,
                            thumbnails=[
                                CartItemMultimediaThumbnail(
                                    height=1,
                                    png=True,
                                    square=True,
                                    url="url_example",
                                    width=1,
                                ),
                            ],
                            type="Image",
                            url="url_example",
                        ),
                    ],
                    options=[
                        CartItemOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    phsyical=CartItemPhysical(
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                    position=1,
                    preorder=True,
                    quantity=3.14,
                    schedules=[
                        "schedules_example",
                    ],
                    total_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    upsell=True,
                    variations=[
                        CartItemVariationSelection(
                            variation_name="variation_name_example",
                            variation_value="variation_value_example",
                        ),
                    ],
                    view_url="view_url_example",
                ),
            ],
            language_iso_code="language_iso_code_example",
            logged_in=True,
            marketing=CartMarketing(
                advertising_source="advertising_source_example",
                cell_phone_opt_in=True,
                mailing_list_opt_in=True,
            ),
            merchant_id="merchant_id_example",
            payment=CartPayment(
                affirm=CartPaymentAffirm(
                    affirm_checkout_token="affirm_checkout_token_example",
                ),
                amazon=CartPaymentAmazon(
                    amazon_order_reference_id="amazon_order_reference_id_example",
                ),
                check=CartPaymentCheck(
                    check_number=1,
                ),
                credit_card=CartPaymentCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    card_verification_number="card_verification_number_example",
                    card_verification_number_token="card_verification_number_token_example",
                    customer_profile_credit_card_id=1,
                    store_credit_card=True,
                ),
                payment_method="payment_method_example",
                purchase_order=CartPaymentPurchaseOrder(
                    purchase_order_number="purchase_order_number_example",
                ),
                rtg_code="rtg_code_example",
            ),
            properties=[
                CartProperty(
                    display=True,
                    expiration_dts="expiration_dts_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
            settings=CartSettings(
                billing=CartSettingsBilling(
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                ),
                gift=CartSettingsGift(
                    allow_gifts=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wraps=[
                        CartSettingsGiftWrap(
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            title="title_example",
                            url="url_example",
                        ),
                    ],
                    max_message_length=1,
                ),
                payment=CartSettingsPayment(
                    amazon=CartSettingsPaymentAmazon(
                        amazon_button_url="amazon_button_url_example",
                        amazon_merchant_id="amazon_merchant_id_example",
                        amazon_widget_url="amazon_widget_url_example",
                    ),
                    credit_card=CartSettingsPaymentCreditCard(
                        collect_credit_card_verification_number=True,
                        credit_card_types=[
                            "credit_card_types_example",
                        ],
                        hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                    ),
                    need_payment=True,
                    paypal=CartSettingsPaymentPayPal(
                        paypal_button_alt_text="paypal_button_alt_text_example",
                        paypal_button_url="paypal_button_url_example",
                        paypal_credit_button_url="paypal_credit_button_url_example",
                        paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                        paypal_credit_legal_url="paypal_credit_legal_url_example",
                    ),
                    supports_amazon=True,
                    supports_check=True,
                    supports_cod=True,
                    supports_credit_card=True,
                    supports_money_order=True,
                    supports_paypal=True,
                    supports_purchase_order=True,
                    supports_quote_request=True,
                    supports_wire_transfer=True,
                ),
                shipping=CartSettingsShipping(
                    deliver_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                    estimates=[
                        CartSettingsShippingEstimate(
                            allow_3rd_party_billing=True,
                            comment="comment_example",
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_before_discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            default_method=True,
                            discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            discounted=True,
                            display_name="display_name_example",
                            estimated_delivery="estimated_delivery_example",
                            lift_gate_option=True,
                            name="name_example",
                            pickup=True,
                            tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            total_tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                        ),
                    ],
                    need_shipping=True,
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                    ship_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                ),
                taxes=CartSettingsTaxes(
                    counties=[
                        "counties_example",
                    ],
                ),
                terms=CartSettingsTerms(
                    html="html_example",
                    text="text_example",
                ),
            ),
            shipping=CartShipping(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                delivery_date="delivery_date_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                lift_gate=True,
                postal_code="postal_code_example",
                ship_on_date="ship_on_date_example",
                ship_to_residential=True,
                shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                shipping_method="shipping_method_example",
                special_instructions="special_instructions_example",
                state_region="state_region_example",
                title="title_example",
            ),
            summary=CartSummary(
                arbitrary_shipping_handling_total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax_rate=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                surcharge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            taxes=CartTaxes(
                county="county_example",
                exempt=True,
                rate=3.14,
            ),
            upsell_after=CartUpsellAfter(
                finalize_after_dts="finalize_after_dts_example",
                finalize_after_minutes=1,
                upsell_path_code="upsell_path_code_example",
            ),
        ),
        customer_profile_oid=1,
        password="password_example",
    ) # CartProfileLoginRequest | Login request
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Profile login
        api_response = api_instance.login(login_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->login: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Profile login
        api_response = api_instance.login(login_request, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**CartProfileLoginRequest**](CartProfileLoginRequest.md)| Login request |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartProfileLoginResponse**](CartProfileLoginResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> CartResponse logout(cart)

Profile logout

Log the cart out of the current profile.  No error will occur if they are not logged in. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_response import CartResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart import Cart
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    cart = Cart(
        affiliate=CartAffiliate(
            affiliate_id=1,
            affiliate_sub_id="affiliate_sub_id_example",
        ),
        affiliate_network_pixel_oid=1,
        base_currency_code="base_currency_code_example",
        billing=CartBilling(
            address1="address1_example",
            address2="address2_example",
            cc_emails=[
                "cc_emails_example",
            ],
            cell_phone="cell_phone_example",
            cell_phone_e164="cell_phone_e164_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            email="email_example",
            email_confirm="email_confirm_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=CartBuysafe(
            bond_available=True,
            bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            bond_free=True,
            bond_wanted=True,
            cart_display_text="cart_display_text_example",
            cart_display_url="cart_display_url_example",
        ),
        cart_id="cart_id_example",
        checkout=CartCheckout(
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            ip_address="ip_address_example",
            return_code="return_code_example",
            return_url="return_url_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            storefront_host_name="storefront_host_name_example",
            user_agent="user_agent_example",
        ),
        coupons=[
            CartCoupon(
                coupon_code="coupon_code_example",
            ),
        ],
        currency_code="currency_code_example",
        currency_conversion=CartCurrencyConversion(
            base_currency_code="base_currency_code_example",
            currencies=[
                Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ],
        ),
        customer_profile=CartCustomerProfile(
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_purchase_order=True,
            billing_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            credit_cards=[
                CartCustomerProfileCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_type="AMEX",
                    customer_profile_credit_card_id=1,
                    last_used_date="last_used_date_example",
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            email="email_example",
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            maximum_item_count=1,
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            pricing_tiers=[
                "pricing_tiers_example",
            ],
            shipping_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            tax_exempt=True,
            ups_account_number="ups_account_number_example",
        ),
        exchange_rate=3.14,
        gift=CartGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=CartGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_remaining_balance_after_order=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        items=[
            CartItem(
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                attributes=[
                    CartItemAttribute(
                        name="name_example",
                        type="type_example",
                        value="value_example",
                    ),
                ],
                auto_order_schedule="auto_order_schedule_example",
                default_image_url="default_image_url_example",
                default_thumbnail_url="default_thumbnail_url_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                extended_description="extended_description_example",
                item_id="item_id_example",
                item_oid=1,
                kit=True,
                kit_component_options=[
                    CartKitComponentOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        item_id="item_id_example",
                        item_oid=1,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                manufacturer_suggested_retail_price=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                maximum_quantity=3.14,
                minimum_quantity=3.14,
                multimedia=[
                    CartItemMultimedia(
                        code="code_example",
                        description="description_example",
                        exclude_from_gallery=True,
                        image_height=1,
                        image_width=1,
                        is_default=True,
                        thumbnails=[
                            CartItemMultimediaThumbnail(
                                height=1,
                                png=True,
                                square=True,
                                url="url_example",
                                width=1,
                            ),
                        ],
                        type="Image",
                        url="url_example",
                    ),
                ],
                options=[
                    CartItemOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                phsyical=CartItemPhysical(
                    height=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    length=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                    width=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                ),
                position=1,
                preorder=True,
                quantity=3.14,
                schedules=[
                    "schedules_example",
                ],
                total_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                variations=[
                    CartItemVariationSelection(
                        variation_name="variation_name_example",
                        variation_value="variation_value_example",
                    ),
                ],
                view_url="view_url_example",
            ),
        ],
        language_iso_code="language_iso_code_example",
        logged_in=True,
        marketing=CartMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list_opt_in=True,
        ),
        merchant_id="merchant_id_example",
        payment=CartPayment(
            affirm=CartPaymentAffirm(
                affirm_checkout_token="affirm_checkout_token_example",
            ),
            amazon=CartPaymentAmazon(
                amazon_order_reference_id="amazon_order_reference_id_example",
            ),
            check=CartPaymentCheck(
                check_number=1,
            ),
            credit_card=CartPaymentCreditCard(
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_type="card_type_example",
                card_verification_number="card_verification_number_example",
                card_verification_number_token="card_verification_number_token_example",
                customer_profile_credit_card_id=1,
                store_credit_card=True,
            ),
            payment_method="payment_method_example",
            purchase_order=CartPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rtg_code="rtg_code_example",
        ),
        properties=[
            CartProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        settings=CartSettings(
            billing=CartSettingsBilling(
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
            ),
            gift=CartSettingsGift(
                allow_gifts=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wraps=[
                    CartSettingsGiftWrap(
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        title="title_example",
                        url="url_example",
                    ),
                ],
                max_message_length=1,
            ),
            payment=CartSettingsPayment(
                amazon=CartSettingsPaymentAmazon(
                    amazon_button_url="amazon_button_url_example",
                    amazon_merchant_id="amazon_merchant_id_example",
                    amazon_widget_url="amazon_widget_url_example",
                ),
                credit_card=CartSettingsPaymentCreditCard(
                    collect_credit_card_verification_number=True,
                    credit_card_types=[
                        "credit_card_types_example",
                    ],
                    hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                ),
                need_payment=True,
                paypal=CartSettingsPaymentPayPal(
                    paypal_button_alt_text="paypal_button_alt_text_example",
                    paypal_button_url="paypal_button_url_example",
                    paypal_credit_button_url="paypal_credit_button_url_example",
                    paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                    paypal_credit_legal_url="paypal_credit_legal_url_example",
                ),
                supports_amazon=True,
                supports_check=True,
                supports_cod=True,
                supports_credit_card=True,
                supports_money_order=True,
                supports_paypal=True,
                supports_purchase_order=True,
                supports_quote_request=True,
                supports_wire_transfer=True,
            ),
            shipping=CartSettingsShipping(
                deliver_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
                estimates=[
                    CartSettingsShippingEstimate(
                        allow_3rd_party_billing=True,
                        comment="comment_example",
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_before_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        default_method=True,
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discounted=True,
                        display_name="display_name_example",
                        estimated_delivery="estimated_delivery_example",
                        lift_gate_option=True,
                        name="name_example",
                        pickup=True,
                        tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                    ),
                ],
                need_shipping=True,
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
                ship_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
            ),
            taxes=CartSettingsTaxes(
                counties=[
                    "counties_example",
                ],
            ),
            terms=CartSettingsTerms(
                html="html_example",
                text="text_example",
            ),
        ),
        shipping=CartShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            lift_gate=True,
            postal_code="postal_code_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_method="shipping_method_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
        ),
        summary=CartSummary(
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax_rate=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        taxes=CartTaxes(
            county="county_example",
            exempt=True,
            rate=3.14,
        ),
        upsell_after=CartUpsellAfter(
            finalize_after_dts="finalize_after_dts_example",
            finalize_after_minutes=1,
            upsell_path_code="upsell_path_code_example",
        ),
    ) # Cart | Cart
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Profile logout
        api_response = api_instance.logout(cart)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->logout: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Profile logout
        api_response = api_instance.logout(cart, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->logout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> CartProfileRegisterResponse register(register_request)

Profile registration

Register a new customer profile.  Requires the cart.billing object to be populated along with the password. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart_profile_register_response import CartProfileRegisterResponse
from ultracart.model.cart_profile_register_request import CartProfileRegisterRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    register_request = CartProfileRegisterRequest(
        cart=Cart(
            affiliate=CartAffiliate(
                affiliate_id=1,
                affiliate_sub_id="affiliate_sub_id_example",
            ),
            affiliate_network_pixel_oid=1,
            base_currency_code="base_currency_code_example",
            billing=CartBilling(
                address1="address1_example",
                address2="address2_example",
                cc_emails=[
                    "cc_emails_example",
                ],
                cell_phone="cell_phone_example",
                cell_phone_e164="cell_phone_e164_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                email="email_example",
                email_confirm="email_confirm_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                title="title_example",
            ),
            buysafe=CartBuysafe(
                bond_available=True,
                bond_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                bond_free=True,
                bond_wanted=True,
                cart_display_text="cart_display_text_example",
                cart_display_url="cart_display_url_example",
            ),
            cart_id="cart_id_example",
            checkout=CartCheckout(
                comments="comments_example",
                custom_field1="custom_field1_example",
                custom_field2="custom_field2_example",
                custom_field3="custom_field3_example",
                custom_field4="custom_field4_example",
                custom_field5="custom_field5_example",
                custom_field6="custom_field6_example",
                custom_field7="custom_field7_example",
                ip_address="ip_address_example",
                return_code="return_code_example",
                return_url="return_url_example",
                screen_branding_theme_code="screen_branding_theme_code_example",
                storefront_host_name="storefront_host_name_example",
                user_agent="user_agent_example",
            ),
            coupons=[
                CartCoupon(
                    coupon_code="coupon_code_example",
                ),
            ],
            currency_code="currency_code_example",
            currency_conversion=CartCurrencyConversion(
                base_currency_code="base_currency_code_example",
                currencies=[
                    Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ],
            ),
            customer_profile=CartCustomerProfile(
                allow_3rd_party_billing=True,
                allow_cod=True,
                allow_purchase_order=True,
                billing_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                credit_cards=[
                    CartCustomerProfileCreditCard(
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_type="AMEX",
                        customer_profile_credit_card_id=1,
                        last_used_date="last_used_date_example",
                    ),
                ],
                customer_profile_oid=1,
                dhl_account_number="dhl_account_number_example",
                dhl_duty_account_number="dhl_duty_account_number_example",
                email="email_example",
                fedex_account_number="fedex_account_number_example",
                free_shipping=True,
                free_shipping_minimum=3.14,
                maximum_item_count=1,
                minimum_item_count=1,
                minimum_subtotal=3.14,
                no_coupons=True,
                no_free_shipping=True,
                no_realtime_charge=True,
                pricing_tiers=[
                    "pricing_tiers_example",
                ],
                shipping_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                signup_dts="signup_dts_example",
                tax_exempt=True,
                ups_account_number="ups_account_number_example",
            ),
            exchange_rate=3.14,
            gift=CartGift(
                gift=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_email="gift_email_example",
                gift_message="gift_message_example",
                gift_wrap_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wrap_title="gift_wrap_title_example",
            ),
            gift_certificate=CartGiftCertificate(
                gift_certificate_amount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_certificate_code="gift_certificate_code_example",
                gift_certificate_remaining_balance_after_order=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            items=[
                CartItem(
                    arbitrary_unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    attributes=[
                        CartItemAttribute(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    auto_order_schedule="auto_order_schedule_example",
                    default_image_url="default_image_url_example",
                    default_thumbnail_url="default_thumbnail_url_example",
                    description="description_example",
                    discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    extended_description="extended_description_example",
                    item_id="item_id_example",
                    item_oid=1,
                    kit=True,
                    kit_component_options=[
                        CartKitComponentOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            item_id="item_id_example",
                            item_oid=1,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    manufacturer_suggested_retail_price=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    maximum_quantity=3.14,
                    minimum_quantity=3.14,
                    multimedia=[
                        CartItemMultimedia(
                            code="code_example",
                            description="description_example",
                            exclude_from_gallery=True,
                            image_height=1,
                            image_width=1,
                            is_default=True,
                            thumbnails=[
                                CartItemMultimediaThumbnail(
                                    height=1,
                                    png=True,
                                    square=True,
                                    url="url_example",
                                    width=1,
                                ),
                            ],
                            type="Image",
                            url="url_example",
                        ),
                    ],
                    options=[
                        CartItemOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    phsyical=CartItemPhysical(
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                    position=1,
                    preorder=True,
                    quantity=3.14,
                    schedules=[
                        "schedules_example",
                    ],
                    total_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    upsell=True,
                    variations=[
                        CartItemVariationSelection(
                            variation_name="variation_name_example",
                            variation_value="variation_value_example",
                        ),
                    ],
                    view_url="view_url_example",
                ),
            ],
            language_iso_code="language_iso_code_example",
            logged_in=True,
            marketing=CartMarketing(
                advertising_source="advertising_source_example",
                cell_phone_opt_in=True,
                mailing_list_opt_in=True,
            ),
            merchant_id="merchant_id_example",
            payment=CartPayment(
                affirm=CartPaymentAffirm(
                    affirm_checkout_token="affirm_checkout_token_example",
                ),
                amazon=CartPaymentAmazon(
                    amazon_order_reference_id="amazon_order_reference_id_example",
                ),
                check=CartPaymentCheck(
                    check_number=1,
                ),
                credit_card=CartPaymentCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    card_verification_number="card_verification_number_example",
                    card_verification_number_token="card_verification_number_token_example",
                    customer_profile_credit_card_id=1,
                    store_credit_card=True,
                ),
                payment_method="payment_method_example",
                purchase_order=CartPaymentPurchaseOrder(
                    purchase_order_number="purchase_order_number_example",
                ),
                rtg_code="rtg_code_example",
            ),
            properties=[
                CartProperty(
                    display=True,
                    expiration_dts="expiration_dts_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
            settings=CartSettings(
                billing=CartSettingsBilling(
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                ),
                gift=CartSettingsGift(
                    allow_gifts=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wraps=[
                        CartSettingsGiftWrap(
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            title="title_example",
                            url="url_example",
                        ),
                    ],
                    max_message_length=1,
                ),
                payment=CartSettingsPayment(
                    amazon=CartSettingsPaymentAmazon(
                        amazon_button_url="amazon_button_url_example",
                        amazon_merchant_id="amazon_merchant_id_example",
                        amazon_widget_url="amazon_widget_url_example",
                    ),
                    credit_card=CartSettingsPaymentCreditCard(
                        collect_credit_card_verification_number=True,
                        credit_card_types=[
                            "credit_card_types_example",
                        ],
                        hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                    ),
                    need_payment=True,
                    paypal=CartSettingsPaymentPayPal(
                        paypal_button_alt_text="paypal_button_alt_text_example",
                        paypal_button_url="paypal_button_url_example",
                        paypal_credit_button_url="paypal_credit_button_url_example",
                        paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                        paypal_credit_legal_url="paypal_credit_legal_url_example",
                    ),
                    supports_amazon=True,
                    supports_check=True,
                    supports_cod=True,
                    supports_credit_card=True,
                    supports_money_order=True,
                    supports_paypal=True,
                    supports_purchase_order=True,
                    supports_quote_request=True,
                    supports_wire_transfer=True,
                ),
                shipping=CartSettingsShipping(
                    deliver_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                    estimates=[
                        CartSettingsShippingEstimate(
                            allow_3rd_party_billing=True,
                            comment="comment_example",
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_before_discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            default_method=True,
                            discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            discounted=True,
                            display_name="display_name_example",
                            estimated_delivery="estimated_delivery_example",
                            lift_gate_option=True,
                            name="name_example",
                            pickup=True,
                            tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            total_tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                        ),
                    ],
                    need_shipping=True,
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                    ship_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                ),
                taxes=CartSettingsTaxes(
                    counties=[
                        "counties_example",
                    ],
                ),
                terms=CartSettingsTerms(
                    html="html_example",
                    text="text_example",
                ),
            ),
            shipping=CartShipping(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                delivery_date="delivery_date_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                lift_gate=True,
                postal_code="postal_code_example",
                ship_on_date="ship_on_date_example",
                ship_to_residential=True,
                shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                shipping_method="shipping_method_example",
                special_instructions="special_instructions_example",
                state_region="state_region_example",
                title="title_example",
            ),
            summary=CartSummary(
                arbitrary_shipping_handling_total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax_rate=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                surcharge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            taxes=CartTaxes(
                county="county_example",
                exempt=True,
                rate=3.14,
            ),
            upsell_after=CartUpsellAfter(
                finalize_after_dts="finalize_after_dts_example",
                finalize_after_minutes=1,
                upsell_path_code="upsell_path_code_example",
            ),
        ),
        password="password_example",
    ) # CartProfileRegisterRequest | Register request
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Profile registration
        api_response = api_instance.register(register_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->register: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Profile registration
        api_response = api_instance.register(register_request, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->register: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**CartProfileRegisterRequest**](CartProfileRegisterRequest.md)| Register request |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartProfileRegisterResponse**](CartProfileRegisterResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_affiliate_click**
> RegisterAffiliateClickResponse register_affiliate_click(register_affiliate_click_request)

Register affiliate click

Register an affiliate click.  Used by custom checkouts that are completely API based and do not perform checkout handoff. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.register_affiliate_click_request import RegisterAffiliateClickRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.register_affiliate_click_response import RegisterAffiliateClickResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    register_affiliate_click_request = RegisterAffiliateClickRequest(
        affid=1,
        ip_address="ip_address_example",
        landing_page_url="landing_page_url_example",
        referrer_url="referrer_url_example",
        subid="subid_example",
        user_agent="user_agent_example",
    ) # RegisterAffiliateClickRequest | Register affiliate click request
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register affiliate click
        api_response = api_instance.register_affiliate_click(register_affiliate_click_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->register_affiliate_click: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register affiliate click
        api_response = api_instance.register_affiliate_click(register_affiliate_click_request, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->register_affiliate_click: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_affiliate_click_request** | [**RegisterAffiliateClickRequest**](RegisterAffiliateClickRequest.md)| Register affiliate click request |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**RegisterAffiliateClickResponse**](RegisterAffiliateClickResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **related_items_for_cart**
> ItemsResponse related_items_for_cart(cart)

Related items

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.items_response import ItemsResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart import Cart
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    cart = Cart(
        affiliate=CartAffiliate(
            affiliate_id=1,
            affiliate_sub_id="affiliate_sub_id_example",
        ),
        affiliate_network_pixel_oid=1,
        base_currency_code="base_currency_code_example",
        billing=CartBilling(
            address1="address1_example",
            address2="address2_example",
            cc_emails=[
                "cc_emails_example",
            ],
            cell_phone="cell_phone_example",
            cell_phone_e164="cell_phone_e164_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            email="email_example",
            email_confirm="email_confirm_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=CartBuysafe(
            bond_available=True,
            bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            bond_free=True,
            bond_wanted=True,
            cart_display_text="cart_display_text_example",
            cart_display_url="cart_display_url_example",
        ),
        cart_id="cart_id_example",
        checkout=CartCheckout(
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            ip_address="ip_address_example",
            return_code="return_code_example",
            return_url="return_url_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            storefront_host_name="storefront_host_name_example",
            user_agent="user_agent_example",
        ),
        coupons=[
            CartCoupon(
                coupon_code="coupon_code_example",
            ),
        ],
        currency_code="currency_code_example",
        currency_conversion=CartCurrencyConversion(
            base_currency_code="base_currency_code_example",
            currencies=[
                Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ],
        ),
        customer_profile=CartCustomerProfile(
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_purchase_order=True,
            billing_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            credit_cards=[
                CartCustomerProfileCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_type="AMEX",
                    customer_profile_credit_card_id=1,
                    last_used_date="last_used_date_example",
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            email="email_example",
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            maximum_item_count=1,
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            pricing_tiers=[
                "pricing_tiers_example",
            ],
            shipping_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            tax_exempt=True,
            ups_account_number="ups_account_number_example",
        ),
        exchange_rate=3.14,
        gift=CartGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=CartGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_remaining_balance_after_order=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        items=[
            CartItem(
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                attributes=[
                    CartItemAttribute(
                        name="name_example",
                        type="type_example",
                        value="value_example",
                    ),
                ],
                auto_order_schedule="auto_order_schedule_example",
                default_image_url="default_image_url_example",
                default_thumbnail_url="default_thumbnail_url_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                extended_description="extended_description_example",
                item_id="item_id_example",
                item_oid=1,
                kit=True,
                kit_component_options=[
                    CartKitComponentOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        item_id="item_id_example",
                        item_oid=1,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                manufacturer_suggested_retail_price=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                maximum_quantity=3.14,
                minimum_quantity=3.14,
                multimedia=[
                    CartItemMultimedia(
                        code="code_example",
                        description="description_example",
                        exclude_from_gallery=True,
                        image_height=1,
                        image_width=1,
                        is_default=True,
                        thumbnails=[
                            CartItemMultimediaThumbnail(
                                height=1,
                                png=True,
                                square=True,
                                url="url_example",
                                width=1,
                            ),
                        ],
                        type="Image",
                        url="url_example",
                    ),
                ],
                options=[
                    CartItemOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                phsyical=CartItemPhysical(
                    height=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    length=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                    width=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                ),
                position=1,
                preorder=True,
                quantity=3.14,
                schedules=[
                    "schedules_example",
                ],
                total_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                variations=[
                    CartItemVariationSelection(
                        variation_name="variation_name_example",
                        variation_value="variation_value_example",
                    ),
                ],
                view_url="view_url_example",
            ),
        ],
        language_iso_code="language_iso_code_example",
        logged_in=True,
        marketing=CartMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list_opt_in=True,
        ),
        merchant_id="merchant_id_example",
        payment=CartPayment(
            affirm=CartPaymentAffirm(
                affirm_checkout_token="affirm_checkout_token_example",
            ),
            amazon=CartPaymentAmazon(
                amazon_order_reference_id="amazon_order_reference_id_example",
            ),
            check=CartPaymentCheck(
                check_number=1,
            ),
            credit_card=CartPaymentCreditCard(
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_type="card_type_example",
                card_verification_number="card_verification_number_example",
                card_verification_number_token="card_verification_number_token_example",
                customer_profile_credit_card_id=1,
                store_credit_card=True,
            ),
            payment_method="payment_method_example",
            purchase_order=CartPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rtg_code="rtg_code_example",
        ),
        properties=[
            CartProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        settings=CartSettings(
            billing=CartSettingsBilling(
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
            ),
            gift=CartSettingsGift(
                allow_gifts=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wraps=[
                    CartSettingsGiftWrap(
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        title="title_example",
                        url="url_example",
                    ),
                ],
                max_message_length=1,
            ),
            payment=CartSettingsPayment(
                amazon=CartSettingsPaymentAmazon(
                    amazon_button_url="amazon_button_url_example",
                    amazon_merchant_id="amazon_merchant_id_example",
                    amazon_widget_url="amazon_widget_url_example",
                ),
                credit_card=CartSettingsPaymentCreditCard(
                    collect_credit_card_verification_number=True,
                    credit_card_types=[
                        "credit_card_types_example",
                    ],
                    hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                ),
                need_payment=True,
                paypal=CartSettingsPaymentPayPal(
                    paypal_button_alt_text="paypal_button_alt_text_example",
                    paypal_button_url="paypal_button_url_example",
                    paypal_credit_button_url="paypal_credit_button_url_example",
                    paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                    paypal_credit_legal_url="paypal_credit_legal_url_example",
                ),
                supports_amazon=True,
                supports_check=True,
                supports_cod=True,
                supports_credit_card=True,
                supports_money_order=True,
                supports_paypal=True,
                supports_purchase_order=True,
                supports_quote_request=True,
                supports_wire_transfer=True,
            ),
            shipping=CartSettingsShipping(
                deliver_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
                estimates=[
                    CartSettingsShippingEstimate(
                        allow_3rd_party_billing=True,
                        comment="comment_example",
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_before_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        default_method=True,
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discounted=True,
                        display_name="display_name_example",
                        estimated_delivery="estimated_delivery_example",
                        lift_gate_option=True,
                        name="name_example",
                        pickup=True,
                        tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                    ),
                ],
                need_shipping=True,
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
                ship_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
            ),
            taxes=CartSettingsTaxes(
                counties=[
                    "counties_example",
                ],
            ),
            terms=CartSettingsTerms(
                html="html_example",
                text="text_example",
            ),
        ),
        shipping=CartShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            lift_gate=True,
            postal_code="postal_code_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_method="shipping_method_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
        ),
        summary=CartSummary(
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax_rate=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        taxes=CartTaxes(
            county="county_example",
            exempt=True,
            rate=3.14,
        ),
        upsell_after=CartUpsellAfter(
            finalize_after_dts="finalize_after_dts_example",
            finalize_after_minutes=1,
            upsell_path_code="upsell_path_code_example",
        ),
    ) # Cart | Cart
    expand = "_expand_example" # str | The object expansion to perform on the result.  See item resource documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Related items
        api_response = api_instance.related_items_for_cart(cart)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->related_items_for_cart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Related items
        api_response = api_instance.related_items_for_cart(cart, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->related_items_for_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart |
 **expand** | **str**| The object expansion to perform on the result.  See item resource documentation for examples | [optional]

### Return type

[**ItemsResponse**](ItemsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **related_items_for_item**
> ItemsResponse related_items_for_item(item_id, cart)

Related items (specific item)

Retrieve all the related items for the cart contents.  Expansion is limited to content, content.assignments, content.attributes, content.multimedia, content.multimedia.thumbnails, options, pricing, and pricing.tiers. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.items_response import ItemsResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart import Cart
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    item_id = "item_id_example" # str | Item ID to retrieve related items for
    cart = Cart(
        affiliate=CartAffiliate(
            affiliate_id=1,
            affiliate_sub_id="affiliate_sub_id_example",
        ),
        affiliate_network_pixel_oid=1,
        base_currency_code="base_currency_code_example",
        billing=CartBilling(
            address1="address1_example",
            address2="address2_example",
            cc_emails=[
                "cc_emails_example",
            ],
            cell_phone="cell_phone_example",
            cell_phone_e164="cell_phone_e164_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            email="email_example",
            email_confirm="email_confirm_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=CartBuysafe(
            bond_available=True,
            bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            bond_free=True,
            bond_wanted=True,
            cart_display_text="cart_display_text_example",
            cart_display_url="cart_display_url_example",
        ),
        cart_id="cart_id_example",
        checkout=CartCheckout(
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            ip_address="ip_address_example",
            return_code="return_code_example",
            return_url="return_url_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            storefront_host_name="storefront_host_name_example",
            user_agent="user_agent_example",
        ),
        coupons=[
            CartCoupon(
                coupon_code="coupon_code_example",
            ),
        ],
        currency_code="currency_code_example",
        currency_conversion=CartCurrencyConversion(
            base_currency_code="base_currency_code_example",
            currencies=[
                Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ],
        ),
        customer_profile=CartCustomerProfile(
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_purchase_order=True,
            billing_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            credit_cards=[
                CartCustomerProfileCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_type="AMEX",
                    customer_profile_credit_card_id=1,
                    last_used_date="last_used_date_example",
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            email="email_example",
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            maximum_item_count=1,
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            pricing_tiers=[
                "pricing_tiers_example",
            ],
            shipping_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            tax_exempt=True,
            ups_account_number="ups_account_number_example",
        ),
        exchange_rate=3.14,
        gift=CartGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=CartGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_remaining_balance_after_order=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        items=[
            CartItem(
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                attributes=[
                    CartItemAttribute(
                        name="name_example",
                        type="type_example",
                        value="value_example",
                    ),
                ],
                auto_order_schedule="auto_order_schedule_example",
                default_image_url="default_image_url_example",
                default_thumbnail_url="default_thumbnail_url_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                extended_description="extended_description_example",
                item_id="item_id_example",
                item_oid=1,
                kit=True,
                kit_component_options=[
                    CartKitComponentOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        item_id="item_id_example",
                        item_oid=1,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                manufacturer_suggested_retail_price=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                maximum_quantity=3.14,
                minimum_quantity=3.14,
                multimedia=[
                    CartItemMultimedia(
                        code="code_example",
                        description="description_example",
                        exclude_from_gallery=True,
                        image_height=1,
                        image_width=1,
                        is_default=True,
                        thumbnails=[
                            CartItemMultimediaThumbnail(
                                height=1,
                                png=True,
                                square=True,
                                url="url_example",
                                width=1,
                            ),
                        ],
                        type="Image",
                        url="url_example",
                    ),
                ],
                options=[
                    CartItemOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                phsyical=CartItemPhysical(
                    height=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    length=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                    width=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                ),
                position=1,
                preorder=True,
                quantity=3.14,
                schedules=[
                    "schedules_example",
                ],
                total_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                variations=[
                    CartItemVariationSelection(
                        variation_name="variation_name_example",
                        variation_value="variation_value_example",
                    ),
                ],
                view_url="view_url_example",
            ),
        ],
        language_iso_code="language_iso_code_example",
        logged_in=True,
        marketing=CartMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list_opt_in=True,
        ),
        merchant_id="merchant_id_example",
        payment=CartPayment(
            affirm=CartPaymentAffirm(
                affirm_checkout_token="affirm_checkout_token_example",
            ),
            amazon=CartPaymentAmazon(
                amazon_order_reference_id="amazon_order_reference_id_example",
            ),
            check=CartPaymentCheck(
                check_number=1,
            ),
            credit_card=CartPaymentCreditCard(
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_type="card_type_example",
                card_verification_number="card_verification_number_example",
                card_verification_number_token="card_verification_number_token_example",
                customer_profile_credit_card_id=1,
                store_credit_card=True,
            ),
            payment_method="payment_method_example",
            purchase_order=CartPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rtg_code="rtg_code_example",
        ),
        properties=[
            CartProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        settings=CartSettings(
            billing=CartSettingsBilling(
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
            ),
            gift=CartSettingsGift(
                allow_gifts=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wraps=[
                    CartSettingsGiftWrap(
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        title="title_example",
                        url="url_example",
                    ),
                ],
                max_message_length=1,
            ),
            payment=CartSettingsPayment(
                amazon=CartSettingsPaymentAmazon(
                    amazon_button_url="amazon_button_url_example",
                    amazon_merchant_id="amazon_merchant_id_example",
                    amazon_widget_url="amazon_widget_url_example",
                ),
                credit_card=CartSettingsPaymentCreditCard(
                    collect_credit_card_verification_number=True,
                    credit_card_types=[
                        "credit_card_types_example",
                    ],
                    hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                ),
                need_payment=True,
                paypal=CartSettingsPaymentPayPal(
                    paypal_button_alt_text="paypal_button_alt_text_example",
                    paypal_button_url="paypal_button_url_example",
                    paypal_credit_button_url="paypal_credit_button_url_example",
                    paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                    paypal_credit_legal_url="paypal_credit_legal_url_example",
                ),
                supports_amazon=True,
                supports_check=True,
                supports_cod=True,
                supports_credit_card=True,
                supports_money_order=True,
                supports_paypal=True,
                supports_purchase_order=True,
                supports_quote_request=True,
                supports_wire_transfer=True,
            ),
            shipping=CartSettingsShipping(
                deliver_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
                estimates=[
                    CartSettingsShippingEstimate(
                        allow_3rd_party_billing=True,
                        comment="comment_example",
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_before_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        default_method=True,
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discounted=True,
                        display_name="display_name_example",
                        estimated_delivery="estimated_delivery_example",
                        lift_gate_option=True,
                        name="name_example",
                        pickup=True,
                        tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                    ),
                ],
                need_shipping=True,
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
                ship_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
            ),
            taxes=CartSettingsTaxes(
                counties=[
                    "counties_example",
                ],
            ),
            terms=CartSettingsTerms(
                html="html_example",
                text="text_example",
            ),
        ),
        shipping=CartShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            lift_gate=True,
            postal_code="postal_code_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_method="shipping_method_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
        ),
        summary=CartSummary(
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax_rate=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        taxes=CartTaxes(
            county="county_example",
            exempt=True,
            rate=3.14,
        ),
        upsell_after=CartUpsellAfter(
            finalize_after_dts="finalize_after_dts_example",
            finalize_after_minutes=1,
            upsell_path_code="upsell_path_code_example",
        ),
    ) # Cart | Cart
    expand = "_expand_example" # str | The object expansion to perform on the result.  See item resource documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Related items (specific item)
        api_response = api_instance.related_items_for_item(item_id, cart)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->related_items_for_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Related items (specific item)
        api_response = api_instance.related_items_for_item(item_id, cart, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->related_items_for_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item ID to retrieve related items for |
 **cart** | [**Cart**](Cart.md)| Cart |
 **expand** | **str**| The object expansion to perform on the result.  See item resource documentation for examples | [optional]

### Return type

[**ItemsResponse**](ItemsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_browser_key**
> CheckoutSetupBrowserKeyResponse setup_browser_key(browser_key_request)

Setup Browser Application

Setup a browser key authenticated application with checkout permissions.  This REST call must be made with an authentication scheme that is not browser key.  The new application will be linked to the application that makes this call.  If this application is disabled / deleted, then so will the application setup by this call.  The purpose of this call is to allow an OAuth application, such as the Wordpress plugin, to setup the proper browser based authentication for the REST checkout API to use. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.checkout_setup_browser_key_request import CheckoutSetupBrowserKeyRequest
from ultracart.model.checkout_setup_browser_key_response import CheckoutSetupBrowserKeyResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    browser_key_request = CheckoutSetupBrowserKeyRequest(
        allowed_referrers=[
            "allowed_referrers_example",
        ],
    ) # CheckoutSetupBrowserKeyRequest | Setup browser key request

    # example passing only required values which don't have defaults set
    try:
        # Setup Browser Application
        api_response = api_instance.setup_browser_key(browser_key_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->setup_browser_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browser_key_request** | [**CheckoutSetupBrowserKeyRequest**](CheckoutSetupBrowserKeyRequest.md)| Setup browser key request |

### Return type

[**CheckoutSetupBrowserKeyResponse**](CheckoutSetupBrowserKeyResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cart**
> CartResponse update_cart(cart)

Update cart

Update the cart. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.cart_response import CartResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart import Cart
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    cart = Cart(
        affiliate=CartAffiliate(
            affiliate_id=1,
            affiliate_sub_id="affiliate_sub_id_example",
        ),
        affiliate_network_pixel_oid=1,
        base_currency_code="base_currency_code_example",
        billing=CartBilling(
            address1="address1_example",
            address2="address2_example",
            cc_emails=[
                "cc_emails_example",
            ],
            cell_phone="cell_phone_example",
            cell_phone_e164="cell_phone_e164_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            email="email_example",
            email_confirm="email_confirm_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=CartBuysafe(
            bond_available=True,
            bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            bond_free=True,
            bond_wanted=True,
            cart_display_text="cart_display_text_example",
            cart_display_url="cart_display_url_example",
        ),
        cart_id="cart_id_example",
        checkout=CartCheckout(
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            ip_address="ip_address_example",
            return_code="return_code_example",
            return_url="return_url_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            storefront_host_name="storefront_host_name_example",
            user_agent="user_agent_example",
        ),
        coupons=[
            CartCoupon(
                coupon_code="coupon_code_example",
            ),
        ],
        currency_code="currency_code_example",
        currency_conversion=CartCurrencyConversion(
            base_currency_code="base_currency_code_example",
            currencies=[
                Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ],
        ),
        customer_profile=CartCustomerProfile(
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_purchase_order=True,
            billing_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            credit_cards=[
                CartCustomerProfileCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_type="AMEX",
                    customer_profile_credit_card_id=1,
                    last_used_date="last_used_date_example",
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            email="email_example",
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            maximum_item_count=1,
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            pricing_tiers=[
                "pricing_tiers_example",
            ],
            shipping_addresses=[
                CartCustomerProfileAddress(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    oid=1,
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            tax_exempt=True,
            ups_account_number="ups_account_number_example",
        ),
        exchange_rate=3.14,
        gift=CartGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=CartGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_remaining_balance_after_order=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        items=[
            CartItem(
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                attributes=[
                    CartItemAttribute(
                        name="name_example",
                        type="type_example",
                        value="value_example",
                    ),
                ],
                auto_order_schedule="auto_order_schedule_example",
                default_image_url="default_image_url_example",
                default_thumbnail_url="default_thumbnail_url_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                extended_description="extended_description_example",
                item_id="item_id_example",
                item_oid=1,
                kit=True,
                kit_component_options=[
                    CartKitComponentOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        item_id="item_id_example",
                        item_oid=1,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                manufacturer_suggested_retail_price=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                maximum_quantity=3.14,
                minimum_quantity=3.14,
                multimedia=[
                    CartItemMultimedia(
                        code="code_example",
                        description="description_example",
                        exclude_from_gallery=True,
                        image_height=1,
                        image_width=1,
                        is_default=True,
                        thumbnails=[
                            CartItemMultimediaThumbnail(
                                height=1,
                                png=True,
                                square=True,
                                url="url_example",
                                width=1,
                            ),
                        ],
                        type="Image",
                        url="url_example",
                    ),
                ],
                options=[
                    CartItemOption(
                        cost_if_specified=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_letter=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_per_line=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        ignore_if_default=True,
                        label="label_example",
                        name="name_example",
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        selected_value="selected_value_example",
                        type="single",
                        values=[
                            CartItemOptionValue(
                                additional_cost=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                additional_weight=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                default_value=True,
                                display_order=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                phsyical=CartItemPhysical(
                    height=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    length=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                    width=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                ),
                position=1,
                preorder=True,
                quantity=3.14,
                schedules=[
                    "schedules_example",
                ],
                total_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                variations=[
                    CartItemVariationSelection(
                        variation_name="variation_name_example",
                        variation_value="variation_value_example",
                    ),
                ],
                view_url="view_url_example",
            ),
        ],
        language_iso_code="language_iso_code_example",
        logged_in=True,
        marketing=CartMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list_opt_in=True,
        ),
        merchant_id="merchant_id_example",
        payment=CartPayment(
            affirm=CartPaymentAffirm(
                affirm_checkout_token="affirm_checkout_token_example",
            ),
            amazon=CartPaymentAmazon(
                amazon_order_reference_id="amazon_order_reference_id_example",
            ),
            check=CartPaymentCheck(
                check_number=1,
            ),
            credit_card=CartPaymentCreditCard(
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_type="card_type_example",
                card_verification_number="card_verification_number_example",
                card_verification_number_token="card_verification_number_token_example",
                customer_profile_credit_card_id=1,
                store_credit_card=True,
            ),
            payment_method="payment_method_example",
            purchase_order=CartPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rtg_code="rtg_code_example",
        ),
        properties=[
            CartProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        settings=CartSettings(
            billing=CartSettingsBilling(
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
            ),
            gift=CartSettingsGift(
                allow_gifts=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wraps=[
                    CartSettingsGiftWrap(
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        title="title_example",
                        url="url_example",
                    ),
                ],
                max_message_length=1,
            ),
            payment=CartSettingsPayment(
                amazon=CartSettingsPaymentAmazon(
                    amazon_button_url="amazon_button_url_example",
                    amazon_merchant_id="amazon_merchant_id_example",
                    amazon_widget_url="amazon_widget_url_example",
                ),
                credit_card=CartSettingsPaymentCreditCard(
                    collect_credit_card_verification_number=True,
                    credit_card_types=[
                        "credit_card_types_example",
                    ],
                    hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                ),
                need_payment=True,
                paypal=CartSettingsPaymentPayPal(
                    paypal_button_alt_text="paypal_button_alt_text_example",
                    paypal_button_url="paypal_button_url_example",
                    paypal_credit_button_url="paypal_credit_button_url_example",
                    paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                    paypal_credit_legal_url="paypal_credit_legal_url_example",
                ),
                supports_amazon=True,
                supports_check=True,
                supports_cod=True,
                supports_credit_card=True,
                supports_money_order=True,
                supports_paypal=True,
                supports_purchase_order=True,
                supports_quote_request=True,
                supports_wire_transfer=True,
            ),
            shipping=CartSettingsShipping(
                deliver_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
                estimates=[
                    CartSettingsShippingEstimate(
                        allow_3rd_party_billing=True,
                        comment="comment_example",
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        cost_before_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        default_method=True,
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discounted=True,
                        display_name="display_name_example",
                        estimated_delivery="estimated_delivery_example",
                        lift_gate_option=True,
                        name="name_example",
                        pickup=True,
                        tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_tax=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                    ),
                ],
                need_shipping=True,
                provinces=[
                    CartSettingsProvince(
                        code="code_example",
                        province="province_example",
                    ),
                ],
                ship_on_date=CartSettingsShippingCalendar(
                    blackouts=[
                        "blackouts_example",
                    ],
                    days_of_week=[
                        True,
                    ],
                    earliest="earliest_example",
                    require=True,
                    show=True,
                ),
            ),
            taxes=CartSettingsTaxes(
                counties=[
                    "counties_example",
                ],
            ),
            terms=CartSettingsTerms(
                html="html_example",
                text="text_example",
            ),
        ),
        shipping=CartShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            first_name="first_name_example",
            last_name="last_name_example",
            lift_gate=True,
            postal_code="postal_code_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_method="shipping_method_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
        ),
        summary=CartSummary(
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_tax_rate=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            tax=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            taxable_subtotal_with_discount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        taxes=CartTaxes(
            county="county_example",
            exempt=True,
            rate=3.14,
        ),
        upsell_after=CartUpsellAfter(
            finalize_after_dts="finalize_after_dts_example",
            finalize_after_minutes=1,
            upsell_path_code="upsell_path_code_example",
        ),
    ) # Cart | Cart
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update cart
        api_response = api_instance.update_cart(cart)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->update_cart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update cart
        api_response = api_instance.update_cart(cart, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->update_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Cart |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartResponse**](CartResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_cart**
> CartValidationResponse validate_cart(validation_request)

Validate

Validate the cart for errors.  Specific checks can be passed and multiple validations can occur throughout your checkout flow. 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import checkout_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.cart_validation_response import CartValidationResponse
from ultracart.model.cart_validation_request import CartValidationRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    validation_request = CartValidationRequest(
        cart=Cart(
            affiliate=CartAffiliate(
                affiliate_id=1,
                affiliate_sub_id="affiliate_sub_id_example",
            ),
            affiliate_network_pixel_oid=1,
            base_currency_code="base_currency_code_example",
            billing=CartBilling(
                address1="address1_example",
                address2="address2_example",
                cc_emails=[
                    "cc_emails_example",
                ],
                cell_phone="cell_phone_example",
                cell_phone_e164="cell_phone_e164_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                email="email_example",
                email_confirm="email_confirm_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                title="title_example",
            ),
            buysafe=CartBuysafe(
                bond_available=True,
                bond_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                bond_free=True,
                bond_wanted=True,
                cart_display_text="cart_display_text_example",
                cart_display_url="cart_display_url_example",
            ),
            cart_id="cart_id_example",
            checkout=CartCheckout(
                comments="comments_example",
                custom_field1="custom_field1_example",
                custom_field2="custom_field2_example",
                custom_field3="custom_field3_example",
                custom_field4="custom_field4_example",
                custom_field5="custom_field5_example",
                custom_field6="custom_field6_example",
                custom_field7="custom_field7_example",
                ip_address="ip_address_example",
                return_code="return_code_example",
                return_url="return_url_example",
                screen_branding_theme_code="screen_branding_theme_code_example",
                storefront_host_name="storefront_host_name_example",
                user_agent="user_agent_example",
            ),
            coupons=[
                CartCoupon(
                    coupon_code="coupon_code_example",
                ),
            ],
            currency_code="currency_code_example",
            currency_conversion=CartCurrencyConversion(
                base_currency_code="base_currency_code_example",
                currencies=[
                    Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ],
            ),
            customer_profile=CartCustomerProfile(
                allow_3rd_party_billing=True,
                allow_cod=True,
                allow_purchase_order=True,
                billing_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                credit_cards=[
                    CartCustomerProfileCreditCard(
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_type="AMEX",
                        customer_profile_credit_card_id=1,
                        last_used_date="last_used_date_example",
                    ),
                ],
                customer_profile_oid=1,
                dhl_account_number="dhl_account_number_example",
                dhl_duty_account_number="dhl_duty_account_number_example",
                email="email_example",
                fedex_account_number="fedex_account_number_example",
                free_shipping=True,
                free_shipping_minimum=3.14,
                maximum_item_count=1,
                minimum_item_count=1,
                minimum_subtotal=3.14,
                no_coupons=True,
                no_free_shipping=True,
                no_realtime_charge=True,
                pricing_tiers=[
                    "pricing_tiers_example",
                ],
                shipping_addresses=[
                    CartCustomerProfileAddress(
                        address1="address1_example",
                        address2="address2_example",
                        city="city_example",
                        company="company_example",
                        country_code="country_code_example",
                        day_phone="day_phone_example",
                        evening_phone="evening_phone_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        oid=1,
                        postal_code="postal_code_example",
                        state_region="state_region_example",
                        tax_county="tax_county_example",
                        title="title_example",
                    ),
                ],
                signup_dts="signup_dts_example",
                tax_exempt=True,
                ups_account_number="ups_account_number_example",
            ),
            exchange_rate=3.14,
            gift=CartGift(
                gift=True,
                gift_charge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_email="gift_email_example",
                gift_message="gift_message_example",
                gift_wrap_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_wrap_title="gift_wrap_title_example",
            ),
            gift_certificate=CartGiftCertificate(
                gift_certificate_amount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                gift_certificate_code="gift_certificate_code_example",
                gift_certificate_remaining_balance_after_order=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            items=[
                CartItem(
                    arbitrary_unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    attributes=[
                        CartItemAttribute(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    auto_order_schedule="auto_order_schedule_example",
                    default_image_url="default_image_url_example",
                    default_thumbnail_url="default_thumbnail_url_example",
                    description="description_example",
                    discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    extended_description="extended_description_example",
                    item_id="item_id_example",
                    item_oid=1,
                    kit=True,
                    kit_component_options=[
                        CartKitComponentOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            item_id="item_id_example",
                            item_oid=1,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    manufacturer_suggested_retail_price=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    maximum_quantity=3.14,
                    minimum_quantity=3.14,
                    multimedia=[
                        CartItemMultimedia(
                            code="code_example",
                            description="description_example",
                            exclude_from_gallery=True,
                            image_height=1,
                            image_width=1,
                            is_default=True,
                            thumbnails=[
                                CartItemMultimediaThumbnail(
                                    height=1,
                                    png=True,
                                    square=True,
                                    url="url_example",
                                    width=1,
                                ),
                            ],
                            type="Image",
                            url="url_example",
                        ),
                    ],
                    options=[
                        CartItemOption(
                            cost_if_specified=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_letter=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_per_line=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            ignore_if_default=True,
                            label="label_example",
                            name="name_example",
                            one_time_fee=True,
                            option_oid=1,
                            required=True,
                            selected_value="selected_value_example",
                            type="single",
                            values=[
                                CartItemOptionValue(
                                    additional_cost=Currency(
                                        currency_code="currency_code_example",
                                        exchange_rate=3.14,
                                        localized=3.14,
                                        localized_formatted="localized_formatted_example",
                                        value=3.14,
                                    ),
                                    additional_weight=Weight(
                                        uom="KG",
                                        value=3.14,
                                    ),
                                    default_value=True,
                                    display_order=1,
                                    value="value_example",
                                ),
                            ],
                        ),
                    ],
                    phsyical=CartItemPhysical(
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                    position=1,
                    preorder=True,
                    quantity=3.14,
                    schedules=[
                        "schedules_example",
                    ],
                    total_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    unit_cost_with_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    upsell=True,
                    variations=[
                        CartItemVariationSelection(
                            variation_name="variation_name_example",
                            variation_value="variation_value_example",
                        ),
                    ],
                    view_url="view_url_example",
                ),
            ],
            language_iso_code="language_iso_code_example",
            logged_in=True,
            marketing=CartMarketing(
                advertising_source="advertising_source_example",
                cell_phone_opt_in=True,
                mailing_list_opt_in=True,
            ),
            merchant_id="merchant_id_example",
            payment=CartPayment(
                affirm=CartPaymentAffirm(
                    affirm_checkout_token="affirm_checkout_token_example",
                ),
                amazon=CartPaymentAmazon(
                    amazon_order_reference_id="amazon_order_reference_id_example",
                ),
                check=CartPaymentCheck(
                    check_number=1,
                ),
                credit_card=CartPaymentCreditCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    card_verification_number="card_verification_number_example",
                    card_verification_number_token="card_verification_number_token_example",
                    customer_profile_credit_card_id=1,
                    store_credit_card=True,
                ),
                payment_method="payment_method_example",
                purchase_order=CartPaymentPurchaseOrder(
                    purchase_order_number="purchase_order_number_example",
                ),
                rtg_code="rtg_code_example",
            ),
            properties=[
                CartProperty(
                    display=True,
                    expiration_dts="expiration_dts_example",
                    name="name_example",
                    value="value_example",
                ),
            ],
            settings=CartSettings(
                billing=CartSettingsBilling(
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                ),
                gift=CartSettingsGift(
                    allow_gifts=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wraps=[
                        CartSettingsGiftWrap(
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            title="title_example",
                            url="url_example",
                        ),
                    ],
                    max_message_length=1,
                ),
                payment=CartSettingsPayment(
                    amazon=CartSettingsPaymentAmazon(
                        amazon_button_url="amazon_button_url_example",
                        amazon_merchant_id="amazon_merchant_id_example",
                        amazon_widget_url="amazon_widget_url_example",
                    ),
                    credit_card=CartSettingsPaymentCreditCard(
                        collect_credit_card_verification_number=True,
                        credit_card_types=[
                            "credit_card_types_example",
                        ],
                        hosted_fields_shopping_cart_token="hosted_fields_shopping_cart_token_example",
                    ),
                    need_payment=True,
                    paypal=CartSettingsPaymentPayPal(
                        paypal_button_alt_text="paypal_button_alt_text_example",
                        paypal_button_url="paypal_button_url_example",
                        paypal_credit_button_url="paypal_credit_button_url_example",
                        paypal_credit_legal_image_url="paypal_credit_legal_image_url_example",
                        paypal_credit_legal_url="paypal_credit_legal_url_example",
                    ),
                    supports_amazon=True,
                    supports_check=True,
                    supports_cod=True,
                    supports_credit_card=True,
                    supports_money_order=True,
                    supports_paypal=True,
                    supports_purchase_order=True,
                    supports_quote_request=True,
                    supports_wire_transfer=True,
                ),
                shipping=CartSettingsShipping(
                    deliver_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                    estimates=[
                        CartSettingsShippingEstimate(
                            allow_3rd_party_billing=True,
                            comment="comment_example",
                            cost=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            cost_before_discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            default_method=True,
                            discount=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            discounted=True,
                            display_name="display_name_example",
                            estimated_delivery="estimated_delivery_example",
                            lift_gate_option=True,
                            name="name_example",
                            pickup=True,
                            tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                            total_tax=Currency(
                                currency_code="currency_code_example",
                                exchange_rate=3.14,
                                localized=3.14,
                                localized_formatted="localized_formatted_example",
                                value=3.14,
                            ),
                        ),
                    ],
                    need_shipping=True,
                    provinces=[
                        CartSettingsProvince(
                            code="code_example",
                            province="province_example",
                        ),
                    ],
                    ship_on_date=CartSettingsShippingCalendar(
                        blackouts=[
                            "blackouts_example",
                        ],
                        days_of_week=[
                            True,
                        ],
                        earliest="earliest_example",
                        require=True,
                        show=True,
                    ),
                ),
                taxes=CartSettingsTaxes(
                    counties=[
                        "counties_example",
                    ],
                ),
                terms=CartSettingsTerms(
                    html="html_example",
                    text="text_example",
                ),
            ),
            shipping=CartShipping(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                day_phone="day_phone_example",
                delivery_date="delivery_date_example",
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                lift_gate=True,
                postal_code="postal_code_example",
                ship_on_date="ship_on_date_example",
                ship_to_residential=True,
                shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                shipping_method="shipping_method_example",
                special_instructions="special_instructions_example",
                state_region="state_region_example",
                title="title_example",
            ),
            summary=CartSummary(
                arbitrary_shipping_handling_total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_tax_rate=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                arbitrary_taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                shipping_handling_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                surcharge=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                tax=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                taxable_subtotal_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                total=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
            ),
            taxes=CartTaxes(
                county="county_example",
                exempt=True,
                rate=3.14,
            ),
            upsell_after=CartUpsellAfter(
                finalize_after_dts="finalize_after_dts_example",
                finalize_after_minutes=1,
                upsell_path_code="upsell_path_code_example",
            ),
        ),
        checks=[
            "checks_example",
        ],
    ) # CartValidationRequest | Validation request
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Validate
        api_response = api_instance.validate_cart(validation_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->validate_cart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate
        api_response = api_instance.validate_cart(validation_request, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CheckoutApi->validate_cart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_request** | [**CartValidationRequest**](CartValidationRequest.md)| Validation request |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CartValidationResponse**](CartValidationResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

