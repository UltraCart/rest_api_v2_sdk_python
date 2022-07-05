# ultracart.ChannelPartnerApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order_by_channel_partner_order_id**](ChannelPartnerApi.md#cancel_order_by_channel_partner_order_id) | **DELETE** /channel_partner/cancel/by_channel_partner_order_id/{order_id} | Cancel channel partner order by channel partner order id
[**cancel_order_by_ultra_cart_order_id**](ChannelPartnerApi.md#cancel_order_by_ultra_cart_order_id) | **DELETE** /channel_partner/cancel/by_ultracart_order_id/{order_id} | Cancel channel partner order by UltraCart order id
[**estimate_shipping_for_channel_partner_order**](ChannelPartnerApi.md#estimate_shipping_for_channel_partner_order) | **POST** /channel_partner/estimate_shipping | Estimate shipping for channel partner order
[**estimate_tax_for_channel_partner_order**](ChannelPartnerApi.md#estimate_tax_for_channel_partner_order) | **POST** /channel_partner/estimate_tax | Estimate tax for channel partner order
[**import_channel_partner_order**](ChannelPartnerApi.md#import_channel_partner_order) | **POST** /channel_partner/import | Insert channel partner order


# **cancel_order_by_channel_partner_order_id**
> ChannelPartnerCancelResponse cancel_order_by_channel_partner_order_id(order_id)

Cancel channel partner order by channel partner order id

Cancel channel partner order by channel partner order id 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import channel_partner_api
from ultracart.model.channel_partner_cancel_response import ChannelPartnerCancelResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The channel partner order id to delete.

    # example passing only required values which don't have defaults set
    try:
        # Cancel channel partner order by channel partner order id
        api_response = api_instance.cancel_order_by_channel_partner_order_id(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ChannelPartnerApi->cancel_order_by_channel_partner_order_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The channel partner order id to delete. |

### Return type

[**ChannelPartnerCancelResponse**](ChannelPartnerCancelResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

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

# **cancel_order_by_ultra_cart_order_id**
> ChannelPartnerCancelResponse cancel_order_by_ultra_cart_order_id(order_id)

Cancel channel partner order by UltraCart order id

Cancel channel partner order by UltraCart order id 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import channel_partner_api
from ultracart.model.channel_partner_cancel_response import ChannelPartnerCancelResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The UltraCart order id to delete.

    # example passing only required values which don't have defaults set
    try:
        # Cancel channel partner order by UltraCart order id
        api_response = api_instance.cancel_order_by_ultra_cart_order_id(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ChannelPartnerApi->cancel_order_by_ultra_cart_order_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The UltraCart order id to delete. |

### Return type

[**ChannelPartnerCancelResponse**](ChannelPartnerCancelResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

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

# **estimate_shipping_for_channel_partner_order**
> ChannelPartnerEstimateShippingResponse estimate_shipping_for_channel_partner_order(channel_partner_order)

Estimate shipping for channel partner order

Estimate shipping for order from a channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import channel_partner_api
from ultracart.model.channel_partner_order import ChannelPartnerOrder
from ultracart.model.error_response import ErrorResponse
from ultracart.model.channel_partner_estimate_shipping_response import ChannelPartnerEstimateShippingResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    channel_partner_order = ChannelPartnerOrder(
        advertising_source="advertising_source_example",
        affiliate_id="affiliate_id_example",
        affiliate_sub_id="affiliate_sub_id_example",
        arbitrary_shipping_handling_total=3.14,
        arbitrary_tax=3.14,
        arbitrary_tax_rate=3.14,
        arbitrary_taxable_subtotal=3.14,
        associate_with_customer_profile_if_present=True,
        auto_approve_purchase_order=True,
        billto_address1="billto_address1_example",
        billto_address2="billto_address2_example",
        billto_city="billto_city_example",
        billto_company="billto_company_example",
        billto_country_code="billto_country_code_example",
        billto_day_phone="billto_day_phone_example",
        billto_evening_phone="billto_evening_phone_example",
        billto_first_name="billto_first_name_example",
        billto_last_name="billto_last_name_example",
        billto_postal_code="billto_postal_code_example",
        billto_state_region="billto_state_region_example",
        billto_title="billto_title_example",
        cc_email="cc_email_example",
        channel_partner_order_id="channel_partner_order_id_example",
        consider_recurring=True,
        coupons=[
            "coupons_example",
        ],
        credit_card_authorization_amount=3.14,
        credit_card_authorization_dts="credit_card_authorization_dts_example",
        credit_card_authorization_number="credit_card_authorization_number_example",
        credit_card_expiration_month=1,
        credit_card_expiration_year=1,
        credit_card_type="credit_card_type_example",
        custom_field1="custom_field1_example",
        custom_field2="custom_field2_example",
        custom_field3="custom_field3_example",
        custom_field4="custom_field4_example",
        custom_field5="custom_field5_example",
        custom_field6="custom_field6_example",
        custom_field7="custom_field7_example",
        delivery_date="delivery_date_example",
        email="email_example",
        gift=True,
        gift_email="gift_email_example",
        gift_message="gift_message_example",
        hosted_fields_card_token="hosted_fields_card_token_example",
        hosted_fields_cvv_token="hosted_fields_cvv_token_example",
        insurance_application_id="insurance_application_id_example",
        insurance_claim_id="insurance_claim_id_example",
        ip_address="ip_address_example",
        items=[
            ChannelPartnerOrderItem(
                arbitrary_unit_cost=3.14,
                auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                auto_order_schedule="Weekly",
                merchant_item_id="merchant_item_id_example",
                options=[
                    ChannelPartnerOrderItemOption(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quantity=3.14,
                upsell=True,
            ),
        ],
        least_cost_route=True,
        least_cost_route_shipping_methods=[
            "least_cost_route_shipping_methods_example",
        ],
        mailing_list_opt_in=True,
        no_realtime_payment_processing=True,
        payment_method="Affirm",
        purchase_order_number="purchase_order_number_example",
        rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
        screen_branding_theme_code="screen_branding_theme_code_example",
        ship_on_date="ship_on_date_example",
        ship_to_residential=True,
        shipping_method="shipping_method_example",
        shipto_address1="shipto_address1_example",
        shipto_address2="shipto_address2_example",
        shipto_city="shipto_city_example",
        shipto_company="shipto_company_example",
        shipto_country_code="shipto_country_code_example",
        shipto_day_phone="shipto_day_phone_example",
        shipto_evening_phone="shipto_evening_phone_example",
        shipto_first_name="shipto_first_name_example",
        shipto_last_name="shipto_last_name_example",
        shipto_postal_code="shipto_postal_code_example",
        shipto_state_region="shipto_state_region_example",
        shipto_title="shipto_title_example",
        skip_payment_processing=True,
        special_instructions="special_instructions_example",
        store_completed=True,
        store_if_payment_declines=True,
        tax_county="tax_county_example",
        tax_exempt=True,
        transaction=ChannelPartnerOrderTransaction(
            details=[
                ChannelPartnerOrderTransactionDetail(
                    name="name_example",
                    value="value_example",
                ),
            ],
            successful=True,
        ),
        treat_warnings_as_errors=True,
    ) # ChannelPartnerOrder | Order needing shipping estimate

    # example passing only required values which don't have defaults set
    try:
        # Estimate shipping for channel partner order
        api_response = api_instance.estimate_shipping_for_channel_partner_order(channel_partner_order)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ChannelPartnerApi->estimate_shipping_for_channel_partner_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_order** | [**ChannelPartnerOrder**](ChannelPartnerOrder.md)| Order needing shipping estimate |

### Return type

[**ChannelPartnerEstimateShippingResponse**](ChannelPartnerEstimateShippingResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **estimate_tax_for_channel_partner_order**
> ChannelPartnerEstimateTaxResponse estimate_tax_for_channel_partner_order(channel_partner_order)

Estimate tax for channel partner order

Estimate tax for order from a channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import channel_partner_api
from ultracart.model.channel_partner_order import ChannelPartnerOrder
from ultracart.model.error_response import ErrorResponse
from ultracart.model.channel_partner_estimate_tax_response import ChannelPartnerEstimateTaxResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    channel_partner_order = ChannelPartnerOrder(
        advertising_source="advertising_source_example",
        affiliate_id="affiliate_id_example",
        affiliate_sub_id="affiliate_sub_id_example",
        arbitrary_shipping_handling_total=3.14,
        arbitrary_tax=3.14,
        arbitrary_tax_rate=3.14,
        arbitrary_taxable_subtotal=3.14,
        associate_with_customer_profile_if_present=True,
        auto_approve_purchase_order=True,
        billto_address1="billto_address1_example",
        billto_address2="billto_address2_example",
        billto_city="billto_city_example",
        billto_company="billto_company_example",
        billto_country_code="billto_country_code_example",
        billto_day_phone="billto_day_phone_example",
        billto_evening_phone="billto_evening_phone_example",
        billto_first_name="billto_first_name_example",
        billto_last_name="billto_last_name_example",
        billto_postal_code="billto_postal_code_example",
        billto_state_region="billto_state_region_example",
        billto_title="billto_title_example",
        cc_email="cc_email_example",
        channel_partner_order_id="channel_partner_order_id_example",
        consider_recurring=True,
        coupons=[
            "coupons_example",
        ],
        credit_card_authorization_amount=3.14,
        credit_card_authorization_dts="credit_card_authorization_dts_example",
        credit_card_authorization_number="credit_card_authorization_number_example",
        credit_card_expiration_month=1,
        credit_card_expiration_year=1,
        credit_card_type="credit_card_type_example",
        custom_field1="custom_field1_example",
        custom_field2="custom_field2_example",
        custom_field3="custom_field3_example",
        custom_field4="custom_field4_example",
        custom_field5="custom_field5_example",
        custom_field6="custom_field6_example",
        custom_field7="custom_field7_example",
        delivery_date="delivery_date_example",
        email="email_example",
        gift=True,
        gift_email="gift_email_example",
        gift_message="gift_message_example",
        hosted_fields_card_token="hosted_fields_card_token_example",
        hosted_fields_cvv_token="hosted_fields_cvv_token_example",
        insurance_application_id="insurance_application_id_example",
        insurance_claim_id="insurance_claim_id_example",
        ip_address="ip_address_example",
        items=[
            ChannelPartnerOrderItem(
                arbitrary_unit_cost=3.14,
                auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                auto_order_schedule="Weekly",
                merchant_item_id="merchant_item_id_example",
                options=[
                    ChannelPartnerOrderItemOption(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quantity=3.14,
                upsell=True,
            ),
        ],
        least_cost_route=True,
        least_cost_route_shipping_methods=[
            "least_cost_route_shipping_methods_example",
        ],
        mailing_list_opt_in=True,
        no_realtime_payment_processing=True,
        payment_method="Affirm",
        purchase_order_number="purchase_order_number_example",
        rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
        screen_branding_theme_code="screen_branding_theme_code_example",
        ship_on_date="ship_on_date_example",
        ship_to_residential=True,
        shipping_method="shipping_method_example",
        shipto_address1="shipto_address1_example",
        shipto_address2="shipto_address2_example",
        shipto_city="shipto_city_example",
        shipto_company="shipto_company_example",
        shipto_country_code="shipto_country_code_example",
        shipto_day_phone="shipto_day_phone_example",
        shipto_evening_phone="shipto_evening_phone_example",
        shipto_first_name="shipto_first_name_example",
        shipto_last_name="shipto_last_name_example",
        shipto_postal_code="shipto_postal_code_example",
        shipto_state_region="shipto_state_region_example",
        shipto_title="shipto_title_example",
        skip_payment_processing=True,
        special_instructions="special_instructions_example",
        store_completed=True,
        store_if_payment_declines=True,
        tax_county="tax_county_example",
        tax_exempt=True,
        transaction=ChannelPartnerOrderTransaction(
            details=[
                ChannelPartnerOrderTransactionDetail(
                    name="name_example",
                    value="value_example",
                ),
            ],
            successful=True,
        ),
        treat_warnings_as_errors=True,
    ) # ChannelPartnerOrder | Order needing tax estimate

    # example passing only required values which don't have defaults set
    try:
        # Estimate tax for channel partner order
        api_response = api_instance.estimate_tax_for_channel_partner_order(channel_partner_order)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ChannelPartnerApi->estimate_tax_for_channel_partner_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_order** | [**ChannelPartnerOrder**](ChannelPartnerOrder.md)| Order needing tax estimate |

### Return type

[**ChannelPartnerEstimateTaxResponse**](ChannelPartnerEstimateTaxResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **import_channel_partner_order**
> ChannelPartnerImportResponse import_channel_partner_order(channel_partner_order)

Insert channel partner order

Insert order from a channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import channel_partner_api
from ultracart.model.channel_partner_order import ChannelPartnerOrder
from ultracart.model.error_response import ErrorResponse
from ultracart.model.channel_partner_import_response import ChannelPartnerImportResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    channel_partner_order = ChannelPartnerOrder(
        advertising_source="advertising_source_example",
        affiliate_id="affiliate_id_example",
        affiliate_sub_id="affiliate_sub_id_example",
        arbitrary_shipping_handling_total=3.14,
        arbitrary_tax=3.14,
        arbitrary_tax_rate=3.14,
        arbitrary_taxable_subtotal=3.14,
        associate_with_customer_profile_if_present=True,
        auto_approve_purchase_order=True,
        billto_address1="billto_address1_example",
        billto_address2="billto_address2_example",
        billto_city="billto_city_example",
        billto_company="billto_company_example",
        billto_country_code="billto_country_code_example",
        billto_day_phone="billto_day_phone_example",
        billto_evening_phone="billto_evening_phone_example",
        billto_first_name="billto_first_name_example",
        billto_last_name="billto_last_name_example",
        billto_postal_code="billto_postal_code_example",
        billto_state_region="billto_state_region_example",
        billto_title="billto_title_example",
        cc_email="cc_email_example",
        channel_partner_order_id="channel_partner_order_id_example",
        consider_recurring=True,
        coupons=[
            "coupons_example",
        ],
        credit_card_authorization_amount=3.14,
        credit_card_authorization_dts="credit_card_authorization_dts_example",
        credit_card_authorization_number="credit_card_authorization_number_example",
        credit_card_expiration_month=1,
        credit_card_expiration_year=1,
        credit_card_type="credit_card_type_example",
        custom_field1="custom_field1_example",
        custom_field2="custom_field2_example",
        custom_field3="custom_field3_example",
        custom_field4="custom_field4_example",
        custom_field5="custom_field5_example",
        custom_field6="custom_field6_example",
        custom_field7="custom_field7_example",
        delivery_date="delivery_date_example",
        email="email_example",
        gift=True,
        gift_email="gift_email_example",
        gift_message="gift_message_example",
        hosted_fields_card_token="hosted_fields_card_token_example",
        hosted_fields_cvv_token="hosted_fields_cvv_token_example",
        insurance_application_id="insurance_application_id_example",
        insurance_claim_id="insurance_claim_id_example",
        ip_address="ip_address_example",
        items=[
            ChannelPartnerOrderItem(
                arbitrary_unit_cost=3.14,
                auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                auto_order_schedule="Weekly",
                merchant_item_id="merchant_item_id_example",
                options=[
                    ChannelPartnerOrderItemOption(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quantity=3.14,
                upsell=True,
            ),
        ],
        least_cost_route=True,
        least_cost_route_shipping_methods=[
            "least_cost_route_shipping_methods_example",
        ],
        mailing_list_opt_in=True,
        no_realtime_payment_processing=True,
        payment_method="Affirm",
        purchase_order_number="purchase_order_number_example",
        rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
        screen_branding_theme_code="screen_branding_theme_code_example",
        ship_on_date="ship_on_date_example",
        ship_to_residential=True,
        shipping_method="shipping_method_example",
        shipto_address1="shipto_address1_example",
        shipto_address2="shipto_address2_example",
        shipto_city="shipto_city_example",
        shipto_company="shipto_company_example",
        shipto_country_code="shipto_country_code_example",
        shipto_day_phone="shipto_day_phone_example",
        shipto_evening_phone="shipto_evening_phone_example",
        shipto_first_name="shipto_first_name_example",
        shipto_last_name="shipto_last_name_example",
        shipto_postal_code="shipto_postal_code_example",
        shipto_state_region="shipto_state_region_example",
        shipto_title="shipto_title_example",
        skip_payment_processing=True,
        special_instructions="special_instructions_example",
        store_completed=True,
        store_if_payment_declines=True,
        tax_county="tax_county_example",
        tax_exempt=True,
        transaction=ChannelPartnerOrderTransaction(
            details=[
                ChannelPartnerOrderTransactionDetail(
                    name="name_example",
                    value="value_example",
                ),
            ],
            successful=True,
        ),
        treat_warnings_as_errors=True,
    ) # ChannelPartnerOrder | Order to insert

    # example passing only required values which don't have defaults set
    try:
        # Insert channel partner order
        api_response = api_instance.import_channel_partner_order(channel_partner_order)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ChannelPartnerApi->import_channel_partner_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_order** | [**ChannelPartnerOrder**](ChannelPartnerOrder.md)| Order to insert |

### Return type

[**ChannelPartnerImportResponse**](ChannelPartnerImportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

