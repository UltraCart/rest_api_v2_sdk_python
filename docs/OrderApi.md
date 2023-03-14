# ultracart.OrderApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_order_total**](OrderApi.md#adjust_order_total) | **POST** /order/orders/{order_id}/adjust_order_total/{desired_total} | Adjusts an order total
[**cancel_order**](OrderApi.md#cancel_order) | **POST** /order/orders/{order_id}/cancel | Cancel an order
[**delete_order**](OrderApi.md#delete_order) | **DELETE** /order/orders/{order_id} | Delete an order
[**duplicate_order**](OrderApi.md#duplicate_order) | **POST** /order/orders/{order_id}/duplicate | Duplicate an order
[**format**](OrderApi.md#format) | **POST** /order/orders/{order_id}/format | Format order
[**generate_invoice**](OrderApi.md#generate_invoice) | **GET** /order/orders/{order_id}/invoice | Generate an invoice for this order.
[**generate_order_token**](OrderApi.md#generate_order_token) | **GET** /order/orders/token/{order_id} | Generate an order token for a given order id
[**generate_packing_slip_all_dc**](OrderApi.md#generate_packing_slip_all_dc) | **GET** /order/orders/{order_id}/packing_slip | Generate a packing slip for this order across all distribution centers.
[**generate_packing_slip_specific_dc**](OrderApi.md#generate_packing_slip_specific_dc) | **GET** /order/orders/{order_id}/packing_slip/{distribution_center_code} | Generate a packing slip for this order for the given distribution center.
[**get_accounts_receivable_retry_config**](OrderApi.md#get_accounts_receivable_retry_config) | **GET** /order/accountsReceivableRetryConfig | Retrieve A/R Retry Configuration
[**get_accounts_receivable_retry_stats**](OrderApi.md#get_accounts_receivable_retry_stats) | **GET** /order/accountsReceivableRetryConfig/stats | Retrieve A/R Retry Statistics
[**get_order**](OrderApi.md#get_order) | **GET** /order/orders/{order_id} | Retrieve an order
[**get_order_by_token**](OrderApi.md#get_order_by_token) | **POST** /order/orders/token | Retrieve an order using a token
[**get_order_edi_documents**](OrderApi.md#get_order_edi_documents) | **GET** /order/orders/{order_id}/edi | Retrieve EDI documents associated with this order.
[**get_orders**](OrderApi.md#get_orders) | **GET** /order/orders | Retrieve orders
[**get_orders_batch**](OrderApi.md#get_orders_batch) | **POST** /order/orders/batch | Retrieve order batch
[**get_orders_by_query**](OrderApi.md#get_orders_by_query) | **POST** /order/orders/query | Retrieve orders by query
[**insert_order**](OrderApi.md#insert_order) | **POST** /order/orders | Insert an order
[**is_refundable_order**](OrderApi.md#is_refundable_order) | **GET** /order/orders/{order_id}/refundable | Determine if an order can be refunded
[**process_payment**](OrderApi.md#process_payment) | **POST** /order/orders/{order_id}/process_payment | Process payment
[**refund_order**](OrderApi.md#refund_order) | **PUT** /order/orders/{order_id}/refund | Refund an order
[**replacement**](OrderApi.md#replacement) | **POST** /order/orders/{order_id}/replacement | Replacement order
[**resend_receipt**](OrderApi.md#resend_receipt) | **POST** /order/orders/{order_id}/resend_receipt | Resend receipt
[**resend_shipment_confirmation**](OrderApi.md#resend_shipment_confirmation) | **POST** /order/orders/{order_id}/resend_shipment_confirmation | Resend shipment confirmation
[**update_accounts_receivable_retry_config**](OrderApi.md#update_accounts_receivable_retry_config) | **POST** /order/accountsReceivableRetryConfig | Update A/R Retry Configuration
[**update_order**](OrderApi.md#update_order) | **PUT** /order/orders/{order_id} | Update an order


# **adjust_order_total**
> BaseResponse adjust_order_total(order_id, desired_total)

Adjusts an order total

Adjusts an order total.  Adjusts individual items appropriately and considers taxes.  Desired total should be provided in the same currency as the order and must be less than the current total and greater than zero.  This call will change the order total.  It returns true if the desired total is achieved.  If the goal seeking algorithm falls short (usually by pennies), this method returns back false.  View the merchant notes for the order for further details. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to cancel.
    desired_total = "desired_total_example" # str | The desired total with no formatting. example 123.45

    # example passing only required values which don't have defaults set
    try:
        # Adjusts an order total
        api_response = api_instance.adjust_order_total(order_id, desired_total)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->adjust_order_total: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to cancel. |
 **desired_total** | **str**| The desired total with no formatting. example 123.45 |

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **cancel_order**
> BaseResponse cancel_order(order_id)

Cancel an order

Cancel an order on the UltraCart account.  If the success flag is false, then consult the error message for why it failed. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to cancel.

    # example passing only required values which don't have defaults set
    try:
        # Cancel an order
        api_response = api_instance.cancel_order(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to cancel. |

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **delete_order**
> delete_order(order_id)

Delete an order

Delete an order on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete an order
        api_instance.delete_order(order_id)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->delete_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to delete. |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_order**
> OrderResponse duplicate_order(order_id)

Duplicate an order

Perform a duplicate of the specified order_id and return a new order located in Accounts Receivable. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_response import OrderResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to duplicate.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Duplicate an order
        api_response = api_instance.duplicate_order(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->duplicate_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Duplicate an order
        api_response = api_instance.duplicate_order(order_id, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->duplicate_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to duplicate. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**OrderResponse**](OrderResponse.md)

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

# **format**
> OrderFormatResponse format(order_id, format_options)

Format order

Format the order for display at text or html 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_format_response import OrderFormatResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_format import OrderFormat
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to format
    format_options = OrderFormat(
        context="context_example",
        dont_link_email_to_search=True,
        email_as_link=True,
        filter_distribution_center_oid=1,
        filter_to_items_in_container_oid=1,
        format="text",
        hide_bill_to_address=True,
        hide_price_information=True,
        link_file_attachments=True,
        show_contact_info=True,
        show_in_merchant_currency=True,
        show_internal_information=True,
        show_merchant_notes=True,
        show_non_sensitive_payment_info=True,
        show_payment_info=True,
        translate=True,
    ) # OrderFormat | Format options

    # example passing only required values which don't have defaults set
    try:
        # Format order
        api_response = api_instance.format(order_id, format_options)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->format: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to format |
 **format_options** | [**OrderFormat**](OrderFormat.md)| Format options |

### Return type

[**OrderFormatResponse**](OrderFormatResponse.md)

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

# **generate_invoice**
> OrderInvoiceResponse generate_invoice(order_id)

Generate an invoice for this order.

The invoice PDF that is returned is base 64 encoded 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_invoice_response import OrderInvoiceResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | Order ID

    # example passing only required values which don't have defaults set
    try:
        # Generate an invoice for this order.
        api_response = api_instance.generate_invoice(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->generate_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID |

### Return type

[**OrderInvoiceResponse**](OrderInvoiceResponse.md)

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

# **generate_order_token**
> OrderTokenResponse generate_order_token(order_id)

Generate an order token for a given order id

Retrieves a single order token for a given order id.  The token can be used with the getOrderByToken API. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_token_response import OrderTokenResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to generate a token for.

    # example passing only required values which don't have defaults set
    try:
        # Generate an order token for a given order id
        api_response = api_instance.generate_order_token(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->generate_order_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to generate a token for. |

### Return type

[**OrderTokenResponse**](OrderTokenResponse.md)

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

# **generate_packing_slip_all_dc**
> OrderPackingSlipResponse generate_packing_slip_all_dc(order_id)

Generate a packing slip for this order across all distribution centers.

The packing slip PDF that is returned is base 64 encoded 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_packing_slip_response import OrderPackingSlipResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | Order ID

    # example passing only required values which don't have defaults set
    try:
        # Generate a packing slip for this order across all distribution centers.
        api_response = api_instance.generate_packing_slip_all_dc(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->generate_packing_slip_all_dc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID |

### Return type

[**OrderPackingSlipResponse**](OrderPackingSlipResponse.md)

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

# **generate_packing_slip_specific_dc**
> OrderPackingSlipResponse generate_packing_slip_specific_dc(distribution_center_code, order_id)

Generate a packing slip for this order for the given distribution center.

The packing slip PDF that is returned is base 64 encoded 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_packing_slip_response import OrderPackingSlipResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    distribution_center_code = "distribution_center_code_example" # str | Distribution center code
    order_id = "order_id_example" # str | Order ID

    # example passing only required values which don't have defaults set
    try:
        # Generate a packing slip for this order for the given distribution center.
        api_response = api_instance.generate_packing_slip_specific_dc(distribution_center_code, order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->generate_packing_slip_specific_dc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code |
 **order_id** | **str**| Order ID |

### Return type

[**OrderPackingSlipResponse**](OrderPackingSlipResponse.md)

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

# **get_accounts_receivable_retry_config**
> AccountsReceivableRetryConfigResponse get_accounts_receivable_retry_config()

Retrieve A/R Retry Configuration

Retrieve A/R Retry Configuration. This is primarily an internal API call.  It is doubtful you would ever need to use it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.accounts_receivable_retry_config_response import AccountsReceivableRetryConfigResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve A/R Retry Configuration
        api_response = api_instance.get_accounts_receivable_retry_config()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_accounts_receivable_retry_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountsReceivableRetryConfigResponse**](AccountsReceivableRetryConfigResponse.md)

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

# **get_accounts_receivable_retry_stats**
> AccountsReceivableRetryStatsResponse get_accounts_receivable_retry_stats()

Retrieve A/R Retry Statistics

Retrieve A/R Retry Statistics. This is primarily an internal API call.  It is doubtful you would ever need to use it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.accounts_receivable_retry_stats_response import AccountsReceivableRetryStatsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    _from = "from_example" # str |  (optional)
    to = "to_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve A/R Retry Statistics
        api_response = api_instance.get_accounts_receivable_retry_stats(_from=_from, to=to)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_accounts_receivable_retry_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**|  | [optional]
 **to** | **str**|  | [optional]

### Return type

[**AccountsReceivableRetryStatsResponse**](AccountsReceivableRetryStatsResponse.md)

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

# **get_order**
> OrderResponse get_order(order_id)

Retrieve an order

Retrieves a single order using the specified order id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_response import OrderResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to retrieve.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an order
        api_response = api_instance.get_order(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an order
        api_response = api_instance.get_order(order_id, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**OrderResponse**](OrderResponse.md)

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

# **get_order_by_token**
> OrderResponse get_order_by_token(order_by_token_query)

Retrieve an order using a token

Retrieves a single order using the specified order token. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_by_token_query import OrderByTokenQuery
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_response import OrderResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_by_token_query = OrderByTokenQuery(
        order_token="order_token_example",
    ) # OrderByTokenQuery | Order by token query
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an order using a token
        api_response = api_instance.get_order_by_token(order_by_token_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_order_by_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an order using a token
        api_response = api_instance.get_order_by_token(order_by_token_query, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_order_by_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by_token_query** | [**OrderByTokenQuery**](OrderByTokenQuery.md)| Order by token query |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**OrderResponse**](OrderResponse.md)

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

# **get_order_edi_documents**
> OrderEdiDocumentsResponse get_order_edi_documents(order_id)

Retrieve EDI documents associated with this order.

Retrieve EDI documents associated with this order. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_edi_documents_response import OrderEdiDocumentsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to retrieve EDI documents for.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve EDI documents associated with this order.
        api_response = api_instance.get_order_edi_documents(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_order_edi_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to retrieve EDI documents for. |

### Return type

[**OrderEdiDocumentsResponse**](OrderEdiDocumentsResponse.md)

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

# **get_orders**
> OrdersResponse get_orders()

Retrieve orders

Retrieves a group of orders from the account.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the orders returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.orders_response import OrdersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | Order Id (optional)
    payment_method = "payment_method_example" # str | Payment Method (optional)
    company = "company_example" # str | Company (optional)
    first_name = "first_name_example" # str | First Name (optional)
    last_name = "last_name_example" # str | Last Name (optional)
    city = "city_example" # str | City (optional)
    state_region = "state_region_example" # str | State/Region (optional)
    postal_code = "postal_code_example" # str | Postal Code (optional)
    country_code = "country_code_example" # str | Country Code (ISO-3166 two letter) (optional)
    phone = "phone_example" # str | Phone (optional)
    email = "email_example" # str | Email (optional)
    cc_email = "cc_email_example" # str | CC Email (optional)
    total = 3.14 # float | Total (optional)
    screen_branding_theme_code = "screen_branding_theme_code_example" # str | Screen Branding Theme Code (optional)
    storefront_host_name = "storefront_host_name_example" # str | StoreFront Host Name (optional)
    creation_date_begin = "creation_date_begin_example" # str | Creation Date Begin (optional)
    creation_date_end = "creation_date_end_example" # str | Creation Date End (optional)
    payment_date_begin = "payment_date_begin_example" # str | Payment Date Begin (optional)
    payment_date_end = "payment_date_end_example" # str | Payment Date End (optional)
    shipment_date_begin = "shipment_date_begin_example" # str | Shipment Date Begin (optional)
    shipment_date_end = "shipment_date_end_example" # str | Shipment Date End (optional)
    rma = "rma_example" # str | RMA (optional)
    purchase_order_number = "purchase_order_number_example" # str | Purchase Order Number (optional)
    item_id = "item_id_example" # str | Item Id (optional)
    current_stage = "current_stage_example" # str | Current Stage (optional)
    channel_partner_code = "channel_partner_code_example" # str | Channel Partner Code (optional)
    channel_partner_order_id = "channel_partner_order_id_example" # str | Channel Partner Order ID (optional)
    limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve orders
        api_response = api_instance.get_orders(order_id=order_id, payment_method=payment_method, company=company, first_name=first_name, last_name=last_name, city=city, state_region=state_region, postal_code=postal_code, country_code=country_code, phone=phone, email=email, cc_email=cc_email, total=total, screen_branding_theme_code=screen_branding_theme_code, storefront_host_name=storefront_host_name, creation_date_begin=creation_date_begin, creation_date_end=creation_date_end, payment_date_begin=payment_date_begin, payment_date_end=payment_date_end, shipment_date_begin=shipment_date_begin, shipment_date_end=shipment_date_end, rma=rma, purchase_order_number=purchase_order_number, item_id=item_id, current_stage=current_stage, channel_partner_code=channel_partner_code, channel_partner_order_id=channel_partner_order_id, limit=limit, offset=offset, sort=sort, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order Id | [optional]
 **payment_method** | **str**| Payment Method | [optional]
 **company** | **str**| Company | [optional]
 **first_name** | **str**| First Name | [optional]
 **last_name** | **str**| Last Name | [optional]
 **city** | **str**| City | [optional]
 **state_region** | **str**| State/Region | [optional]
 **postal_code** | **str**| Postal Code | [optional]
 **country_code** | **str**| Country Code (ISO-3166 two letter) | [optional]
 **phone** | **str**| Phone | [optional]
 **email** | **str**| Email | [optional]
 **cc_email** | **str**| CC Email | [optional]
 **total** | **float**| Total | [optional]
 **screen_branding_theme_code** | **str**| Screen Branding Theme Code | [optional]
 **storefront_host_name** | **str**| StoreFront Host Name | [optional]
 **creation_date_begin** | **str**| Creation Date Begin | [optional]
 **creation_date_end** | **str**| Creation Date End | [optional]
 **payment_date_begin** | **str**| Payment Date Begin | [optional]
 **payment_date_end** | **str**| Payment Date End | [optional]
 **shipment_date_begin** | **str**| Shipment Date Begin | [optional]
 **shipment_date_end** | **str**| Shipment Date End | [optional]
 **rma** | **str**| RMA | [optional]
 **purchase_order_number** | **str**| Purchase Order Number | [optional]
 **item_id** | **str**| Item Id | [optional]
 **current_stage** | **str**| Current Stage | [optional]
 **channel_partner_code** | **str**| Channel Partner Code | [optional]
 **channel_partner_order_id** | **str**| Channel Partner Order ID | [optional]
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result. | [optional]

### Return type

[**OrdersResponse**](OrdersResponse.md)

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

# **get_orders_batch**
> OrdersResponse get_orders_batch(order_batch)

Retrieve order batch

Retrieves a group of orders from the account based on an array of order ids.  If more than 500 order ids are specified, the API call will fail with a bad request error. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_query_batch import OrderQueryBatch
from ultracart.model.error_response import ErrorResponse
from ultracart.model.orders_response import OrdersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_batch = OrderQueryBatch(
        order_ids=[
            "order_ids_example",
        ],
    ) # OrderQueryBatch | Order batch
    expand = "_expand_example" # str | The object expansion to perform on the result. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve order batch
        api_response = api_instance.get_orders_batch(order_batch)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_orders_batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve order batch
        api_response = api_instance.get_orders_batch(order_batch, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_orders_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_batch** | [**OrderQueryBatch**](OrderQueryBatch.md)| Order batch |
 **expand** | **str**| The object expansion to perform on the result. | [optional]

### Return type

[**OrdersResponse**](OrdersResponse.md)

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

# **get_orders_by_query**
> OrdersResponse get_orders_by_query(order_query)

Retrieve orders by query

Retrieves a group of orders from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the orders returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_query import OrderQuery
from ultracart.model.orders_response import OrdersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_query = OrderQuery(
        cc_email="cc_email_example",
        channel_partner_code="channel_partner_code_example",
        channel_partner_order_id="channel_partner_order_id_example",
        city="city_example",
        company="company_example",
        country_code="country_code_example",
        creation_date_begin="creation_date_begin_example",
        creation_date_end="creation_date_end_example",
        current_stage="Accounts Receivable",
        custom_field_1="custom_field_1_example",
        custom_field_2="custom_field_2_example",
        custom_field_3="custom_field_3_example",
        custom_field_4="custom_field_4_example",
        custom_field_5="custom_field_5_example",
        custom_field_6="custom_field_6_example",
        custom_field_7="custom_field_7_example",
        customer_profile_oid=1,
        email="email_example",
        first_name="first_name_example",
        item_id="item_id_example",
        last_name="last_name_example",
        order_id="order_id_example",
        payment_date_begin="payment_date_begin_example",
        payment_date_end="payment_date_end_example",
        payment_method="Affirm",
        phone="phone_example",
        postal_code="postal_code_example",
        purchase_order_number="purchase_order_number_example",
        refund_date_begin="refund_date_begin_example",
        refund_date_end="refund_date_end_example",
        rma="rma_example",
        screen_branding_theme_code="screen_branding_theme_code_example",
        shipment_date_begin="shipment_date_begin_example",
        shipment_date_end="shipment_date_end_example",
        shipped_on_date_begin="shipped_on_date_begin_example",
        shipped_on_date_end="shipped_on_date_end_example",
        state_region="state_region_example",
        storefront_host_name="storefront_host_name_example",
        total=3.14,
    ) # OrderQuery | Order query
    limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve orders by query
        api_response = api_instance.get_orders_by_query(order_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_orders_by_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve orders by query
        api_response = api_instance.get_orders_by_query(order_query, limit=limit, offset=offset, sort=sort, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->get_orders_by_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_query** | [**OrderQuery**](OrderQuery.md)| Order query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result. | [optional]

### Return type

[**OrdersResponse**](OrdersResponse.md)

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

# **insert_order**
> OrderResponse insert_order(order)

Insert an order

Inserts a new order on the UltraCart account.  This is probably NOT the method you want.  This is for channel orders.  For regular orders the customer is entering, use the CheckoutApi.  It has many, many more features, checks, and validations. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order import Order
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_response import OrderResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order = Order(
        affiliates=[
            OrderAffiliate(
                affiliate_oid=1,
                ledger_entries=[
                    OrderAffiliateLedger(
                        assigned_by_user="assigned_by_user_example",
                        item_id="item_id_example",
                        tier_number=1,
                        transaction_amount=3.14,
                        transaction_amount_paid=3.14,
                        transaction_dts="transaction_dts_example",
                        transaction_memo="transaction_memo_example",
                        transaction_percentage=3.14,
                        transaction_state="Pending",
                    ),
                ],
                sub_id="sub_id_example",
            ),
        ],
        auto_order=OrderAutoOrder(
            auto_order_code="auto_order_code_example",
            auto_order_oid=1,
            cancel_after_next_x_orders=1,
            cancel_downgrade=True,
            cancel_reason="cancel_reason_example",
            cancel_upgrade=True,
            canceled_by_user="canceled_by_user_example",
            canceled_dts="canceled_dts_example",
            completed=True,
            credit_card_attempt=1,
            disabled_dts="disabled_dts_example",
            enabled=True,
            failure_reason="failure_reason_example",
            items=[
                AutoOrderItem(
                    arbitrary_item_id="arbitrary_item_id_example",
                    arbitrary_percentage_discount=3.14,
                    arbitrary_quantity=3.14,
                    arbitrary_schedule_days=1,
                    arbitrary_unit_cost=3.14,
                    arbitrary_unit_cost_remaining_orders=1,
                    auto_order_item_oid=1,
                    frequency="Weekly",
                    future_schedules=[
                        AutoOrderItemFutureSchedule(
                            item_id="item_id_example",
                            rebill_count=1,
                            shipment_dts="shipment_dts_example",
                            unit_cost=3.14,
                        ),
                    ],
                    last_order_dts="last_order_dts_example",
                    life_time_value=3.14,
                    next_preshipment_notice_dts="next_preshipment_notice_dts_example",
                    next_shipment_dts="next_shipment_dts_example",
                    no_order_after_dts="no_order_after_dts_example",
                    number_of_rebills=1,
                    options=[
                        AutoOrderItemOption(
                            label="label_example",
                            value="value_example",
                        ),
                    ],
                    original_item_id="original_item_id_example",
                    original_quantity=3.14,
                    paypal_payer_id="paypal_payer_id_example",
                    paypal_recurring_payment_profile_id="paypal_recurring_payment_profile_id_example",
                    preshipment_notice_sent=True,
                    rebill_value=3.14,
                    remaining_repeat_count=1,
                    simple_schedule=AutoOrderItemSimpleSchedule(
                        frequency="Weekly",
                        item_id="item_id_example",
                        repeat_count=1,
                    ),
                ),
            ],
            next_attempt="next_attempt_example",
            original_order_id="original_order_id_example",
            override_affiliate_id=1,
            rebill_orders=[
                Order(),
            ],
            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
            status="active",
        ),
        billing=OrderBilling(
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
            day_phone_e164="day_phone_e164_example",
            email="email_example",
            evening_phone="evening_phone_example",
            evening_phone_e164="evening_phone_e164_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=OrderBuysafe(
            buysafe_bond_available=True,
            buysafe_bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            buysafe_bond_free=True,
            buysafe_bond_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            buysafe_bond_wanted=True,
            buysafe_shopping_cart_id="buysafe_shopping_cart_id_example",
        ),
        channel_partner=OrderChannelPartner(
            auto_approve_purchase_order=True,
            channel_partner_code="channel_partner_code_example",
            channel_partner_data="channel_partner_data_example",
            channel_partner_oid=1,
            channel_partner_order_id="channel_partner_order_id_example",
            ignore_invalid_shipping_method=True,
            no_realtime_payment_processing=True,
            skip_payment_processing=True,
            store_completed=True,
            store_if_payment_declines=True,
            treat_warnings_as_errors=True,
        ),
        checkout=OrderCheckout(
            browser=Browser(
                device=BrowserDevice(
                    family="family_example",
                ),
                os=BrowserOS(
                    family="family_example",
                    major="major_example",
                    minor="minor_example",
                    patch="patch_example",
                    patch_minor="patch_minor_example",
                ),
                user_agent=BrowserUserAgent(
                    family="family_example",
                    major="major_example",
                    minor="minor_example",
                    patch="patch_example",
                ),
            ),
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field10="custom_field10_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            custom_field8="custom_field8_example",
            custom_field9="custom_field9_example",
            customer_ip_address="customer_ip_address_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            screen_size="screen_size_example",
            storefront_host_name="storefront_host_name_example",
            upsell_path_code="upsell_path_code_example",
        ),
        coupons=[
            OrderCoupon(
                accounting_code="accounting_code_example",
                automatically_applied=True,
                base_coupon_code="base_coupon_code_example",
                coupon_code="coupon_code_example",
                hdie_from_customer=True,
            ),
        ],
        creation_dts="creation_dts_example",
        currency_code="currency_code_example",
        current_stage="Accounts Receivable",
        customer_profile=Customer(
            activity=CustomerActivity(
                activities=[
                    Activity(
                        action="action_example",
                        channel="channel_example",
                        metric="metric_example",
                        storefront_oid=1,
                        subject="subject_example",
                        ts=1,
                        type="type_example",
                        uuid="uuid_example",
                    ),
                ],
                global_unsubscribed=True,
                global_unsubscribed_dts="global_unsubscribed_dts_example",
                memberships=[
                    ListSegmentMembership(
                        name="name_example",
                        type="type_example",
                        uuid="uuid_example",
                    ),
                ],
                metrics=[
                    Metric(
                        all_time=3.14,
                        all_time_formatted="all_time_formatted_example",
                        last_30=3.14,
                        last_30_formatted="last_30_formatted_example",
                        name="name_example",
                        prior_30=3.14,
                        prior_30_formatted="prior_30_formatted_example",
                        type="type_example",
                    ),
                ],
                properties_list=[
                    ModelProperty(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                spam_complaint=True,
                spam_complaint_dts="spam_complaint_dts_example",
            ),
            affiliate_oid=1,
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_drop_shipping=True,
            allow_purchase_order=True,
            allow_quote_request=True,
            allow_selection_of_address_type=True,
            attachments=[
                CustomerAttachment(
                    customer_profile_attachment_oid=1,
                    description="description_example",
                    file_name="file_name_example",
                    mime_type="mime_type_example",
                    upload_dts="upload_dts_example",
                ),
            ],
            auto_approve_cod=True,
            auto_approve_purchase_order=True,
            automatic_merchant_notes="automatic_merchant_notes_example",
            billing=[
                CustomerBilling(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    customer_billing_oid=1,
                    customer_profile_oid=1,
                    day_phone="day_phone_example",
                    default_billing=True,
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    last_used_dts="last_used_dts_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            business_notes="business_notes_example",
            cards=[
                CustomerCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    customer_profile_credit_card_id=1,
                    customer_profile_oid=1,
                    last_used_dts="last_used_dts_example",
                ),
            ],
            cc_emails=[
                CustomerEmail(
                    customer_profile_email_oid=1,
                    email="email_example",
                    label="label_example",
                    receipt_notification=True,
                    refund_notification=True,
                    shipment_notification=True,
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            edi=CustomerEDI(
                channel_partner_oid=1,
                distribution_center_number="distribution_center_number_example",
                store_number="store_number_example",
            ),
            email="email_example",
            exempt_shipping_handling_charge=True,
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            last_modified_by="last_modified_by_example",
            last_modified_dts="last_modified_dts_example",
            loyalty=CustomerLoyalty(
                current_points=1,
                internal_gift_certificate=GiftCertificate(
                    activated=True,
                    code="code_example",
                    customer_profile_oid=1,
                    deleted=True,
                    email="email_example",
                    expiration_dts="expiration_dts_example",
                    gift_certificate_oid=1,
                    internal=True,
                    ledger_entries=[
                        GiftCertificateLedgerEntry(
                            amount=3.14,
                            description="description_example",
                            entry_dts="entry_dts_example",
                            gift_certificate_ledger_oid=1,
                            gift_certificate_oid=1,
                            reference_order_id="reference_order_id_example",
                        ),
                    ],
                    merchant_id="merchant_id_example",
                    merchant_note="merchant_note_example",
                    original_balance=3.14,
                    reference_order_id="reference_order_id_example",
                    remaining_balance=3.14,
                ),
                internal_gift_certificate_balance="internal_gift_certificate_balance_example",
                internal_gift_certificate_oid=1,
                ledger_entries=[
                    CustomerLoyaltyLedger(
                        created_by="created_by_example",
                        created_dts="created_dts_example",
                        description="description_example",
                        email="email_example",
                        item_id="item_id_example",
                        item_index=1,
                        ledger_dts="ledger_dts_example",
                        loyalty_campaign_oid=1,
                        loyalty_ledger_oid=1,
                        loyalty_points=1,
                        modified_by="modified_by_example",
                        modified_dts="modified_dts_example",
                        order_id="order_id_example",
                        quantity=1,
                        vesting_dts="vesting_dts_example",
                    ),
                ],
                pending_points=1,
                redemptions=[
                    CustomerLoyaltyRedemption(
                        coupon_code="coupon_code_example",
                        coupon_code_oid=1,
                        coupon_used=True,
                        description_for_customer="description_for_customer_example",
                        expiration_dts="expiration_dts_example",
                        gift_certificate_code="gift_certificate_code_example",
                        gift_certificate_oid=1,
                        loyalty_ledger_oid=1,
                        loyalty_points=1,
                        loyalty_redemption_oid=1,
                        order_id="order_id_example",
                        redemption_dts="redemption_dts_example",
                        remaining_balance=3.14,
                    ),
                ],
            ),
            maximum_item_count=1,
            merchant_id="merchant_id_example",
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            orders=[
                Order(),
            ],
            orders_summary=CustomerOrdersSummary(
                first_order_dts="first_order_dts_example",
                last_order_dts="last_order_dts_example",
                order_count=1,
                total=3.14,
            ),
            password="password_example",
            pricing_tiers=[
                CustomerPricingTier(
                    name="name_example",
                    pricing_tier_oid=1,
                ),
            ],
            privacy=CustomerPrivacy(
                last_update_dts="last_update_dts_example",
                marketing=True,
                preference=True,
                statistics=True,
            ),
            qb_class="qb_class_example",
            qb_code="qb_code_example",
            quotes=[
                Order(),
            ],
            quotes_summary=CustomerQuotesSummary(
                first_quote_dts="first_quote_dts_example",
                last_quote_dts="last_quote_dts_example",
                quote_count=1,
                total=3.14,
            ),
            referral_source="referral_source_example",
            reviewer=CustomerReviewer(
                auto_approve=True,
                average_overall_rating=3.14,
                expert=True,
                first_review="first_review_example",
                last_review="last_review_example",
                location="location_example",
                nickname="nickname_example",
                number_helpful_review_votes=1,
                rank=1,
                reviews_contributed=1,
            ),
            sales_rep_code="sales_rep_code_example",
            send_signup_notification=True,
            shipping=[
                CustomerShipping(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    customer_profile_oid=1,
                    customer_shipping_oid=1,
                    day_phone="day_phone_example",
                    default_shipping=True,
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    last_used_dts="last_used_dts_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            software_entitlements=[
                CustomerSoftwareEntitlement(
                    activation_code="activation_code_example",
                    activation_dts="activation_dts_example",
                    customer_software_entitlement_oid=1,
                    expiration_dts="expiration_dts_example",
                    purchased_via_item_description="purchased_via_item_description_example",
                    purchased_via_item_id="purchased_via_item_id_example",
                    purchased_via_order_id="purchased_via_order_id_example",
                    software_sku="software_sku_example",
                ),
            ],
            suppress_buysafe=True,
            tags=[
                CustomerTag(
                    tag_value="tag_value_example",
                ),
            ],
            tax_codes=CustomerTaxCodes(
                avalara_customer_code="avalara_customer_code_example",
                avalara_entity_use_code="avalara_entity_use_code_example",
                sovos_customer_code="sovos_customer_code_example",
                taxjar_customer_id="taxjar_customer_id_example",
                taxjar_exemption_type="taxjar_exemption_type_example",
            ),
            tax_exempt=True,
            tax_id="tax_id_example",
            terms="terms_example",
            track_separately=True,
            unapproved=True,
            ups_account_number="ups_account_number_example",
            website_url="website_url_example",
        ),
        digital_order=OrderDigitalOrder(
            creation_dts="creation_dts_example",
            expiration_dts="expiration_dts_example",
            items=[
                OrderDigitalItem(
                    file_size=1,
                    last_download="last_download_example",
                    last_download_ip_address="last_download_ip_address_example",
                    original_filename="original_filename_example",
                    product_code="product_code_example",
                    product_description="product_description_example",
                    remaining_downloads=1,
                    url="url_example",
                ),
            ],
            url="url_example",
            url_id="url_id_example",
        ),
        edi=OrderEdi(
            bill_to_edi_code="bill_to_edi_code_example",
            edi_department="edi_department_example",
            edi_internal_vendor_number="edi_internal_vendor_number_example",
            ship_to_edi_code="ship_to_edi_code_example",
        ),
        exchange_rate=3.14,
        fraud_score=OrderFraudScore(
            anonymous_proxy=True,
            bin_match="NA",
            carder_email=True,
            country_code="country_code_example",
            country_match=True,
            customer_phone_in_billing_location="customer_phone_in_billing_location_example",
            distance_km=1,
            free_email=True,
            high_risk_country=True,
            ip_city="ip_city_example",
            ip_isp="ip_isp_example",
            ip_latitude="ip_latitude_example",
            ip_longitude="ip_longitude_example",
            ip_org="ip_org_example",
            ip_region="ip_region_example",
            proxy_score=3.14,
            score=3.14,
            ship_forwarder=True,
            spam_score=3.14,
            transparent_proxy=True,
        ),
        gift=OrderGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_charge_accounting_code="gift_charge_accounting_code_example",
            gift_charge_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_accounting_code="gift_wrap_accounting_code_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=OrderGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_oid=1,
        ),
        internal=OrderInternal(
            exported_to_accounting=True,
            merchant_notes="merchant_notes_example",
            placed_by_user="placed_by_user_example",
            refund_by_user="refund_by_user_example",
            sales_rep_code="sales_rep_code_example",
            transactional_merchant_notes=[
                OrderTransactionalMerchantNote(
                    ip_address="ip_address_example",
                    note="note_example",
                    note_dts="note_dts_example",
                    user="user_example",
                ),
            ],
        ),
        items=[
            OrderItem(
                accounting_code="accounting_code_example",
                activation_codes=[
                    "activation_codes_example",
                ],
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                auto_order_schedule="auto_order_schedule_example",
                barcode="barcode_example",
                channel_partner_item_id="channel_partner_item_id_example",
                cogs=3.14,
                component_unit_value=3.14,
                cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                country_code_of_origin="country_code_of_origin_example",
                customs_description="customs_description_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                discount_quantity=3.14,
                discount_shipping_weight=Weight(
                    uom="KG",
                    value=3.14,
                ),
                distribution_center_code="distribution_center_code_example",
                edi=OrderItemEdi(
                    identifications=[
                        OrderItemEdiIdentification(
                            identification="identification_example",
                            quantity=1,
                        ),
                    ],
                    lots=[
                        OrderItemEdiLot(
                            lot_expiration="lot_expiration_example",
                            lot_number="lot_number_example",
                            lot_quantity=1,
                        ),
                    ],
                ),
                exclude_coupon=True,
                free_shipping=True,
                hazmat=True,
                height=Distance(
                    uom="IN",
                    value=3.14,
                ),
                item_index=1,
                item_reference_oid=1,
                kit=True,
                kit_component=True,
                length=Distance(
                    uom="IN",
                    value=3.14,
                ),
                manufacturer_sku="manufacturer_sku_example",
                max_days_time_in_transit=1,
                merchant_item_id="merchant_item_id_example",
                mix_and_match_group_name="mix_and_match_group_name_example",
                mix_and_match_group_oid=1,
                no_shipping_discount=True,
                options=[
                    OrderItemOption(
                        additional_dimension_application="none",
                        cost_change=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        file_attachment=OrderItemOptionFileAttachment(
                            expiration_dts="expiration_dts_example",
                            file_name="file_name_example",
                            mime_type="mime_type_example",
                            size=1,
                        ),
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        hidden=True,
                        label="label_example",
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        one_time_fee=True,
                        value="value_example",
                        weight_change=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
                packed_by_user="packed_by_user_example",
                parent_item_index=1,
                parent_merchant_item_id="parent_merchant_item_id_example",
                perishable_class="perishable_class_example",
                pricing_tier_name="pricing_tier_name_example",
                properties=[
                    OrderItemProperty(
                        display=True,
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quantity=3.14,
                quantity_refunded=3.14,
                quickbooks_class="quickbooks_class_example",
                refund_reason="refund_reason_example",
                return_reason="return_reason_example",
                ship_separately=True,
                shipped_by_user="shipped_by_user_example",
                shipped_dts="shipped_dts_example",
                shipping_status="shipping_status_example",
                special_product_type="special_product_type_example",
                tags=[
                    OrderItemTag(
                        tag_value="tag_value_example",
                    ),
                ],
                tax_free=True,
                tax_product_type="",
                taxable_cost=Currency(
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
                total_refunded=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                transmitted_to_distribution_center_dts="transmitted_to_distribution_center_dts_example",
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                weight=Weight(
                    uom="KG",
                    value=3.14,
                ),
                width=Distance(
                    uom="IN",
                    value=3.14,
                ),
            ),
        ],
        language_iso_code="language_iso_code_example",
        linked_shipment=OrderLinkedShipment(
            has_linked_shipment=True,
            linked_shipment=True,
            linked_shipment_channel_partner_order_ids=[
                "linked_shipment_channel_partner_order_ids_example",
            ],
            linked_shipment_order_ids=[
                "linked_shipment_order_ids_example",
            ],
            linked_shipment_to_order_id="linked_shipment_to_order_id_example",
        ),
        marketing=OrderMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list=True,
            referral_code="referral_code_example",
        ),
        merchant_id="merchant_id_example",
        order_id="order_id_example",
        payment=OrderPayment(
            check=OrderPaymentCheck(
                check_number="check_number_example",
            ),
            credit_card=OrderPaymentCreditCard(
                card_auth_ticket="card_auth_ticket_example",
                card_authorization_amount=3.14,
                card_authorization_dts="card_authorization_dts_example",
                card_authorization_reference_number="card_authorization_reference_number_example",
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_number_truncated=True,
                card_type="AMEX",
                card_verification_number_token="card_verification_number_token_example",
            ),
            echeck=OrderPaymentECheck(
                bank_aba_code="bank_aba_code_example",
                bank_account_name="bank_account_name_example",
                bank_account_number="bank_account_number_example",
                bank_account_type="Checking",
                bank_name="bank_name_example",
                bank_owner_type="Personal",
                customer_tax_id="customer_tax_id_example",
                drivers_license_dob="drivers_license_dob_example",
                drivers_license_number="drivers_license_number_example",
                drivers_license_state="drivers_license_state_example",
            ),
            hold_for_fraud_review=True,
            insurance=OrderPaymentInsurance(
                application_id="application_id_example",
                claim_id="claim_id_example",
                insurance_type="insurance_type_example",
                refund_claim_id="refund_claim_id_example",
            ),
            payment_dts="payment_dts_example",
            payment_method="Affirm",
            payment_method_accounting_code="payment_method_accounting_code_example",
            payment_method_deposit_to_account="payment_method_deposit_to_account_example",
            payment_status="Unprocessed",
            purchase_order=OrderPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge_accounting_code="surcharge_accounting_code_example",
            surcharge_transaction_fee=3.14,
            surcharge_transaction_percentage=3.14,
            test_order=True,
            transactions=[
                OrderPaymentTransaction(
                    details=[
                        OrderPaymentTransactionDetail(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    successful=True,
                    transaction_gateway="transaction_gateway_example",
                    transaction_timestamp="transaction_timestamp_example",
                ),
            ],
        ),
        point_of_sale=OrderPointOfSale(
            location=PointOfSaleLocation(
                adddress2="adddress2_example",
                address1="address1_example",
                city="city_example",
                country="country_example",
                distribution_center_code="distribution_center_code_example",
                external_id="external_id_example",
                merchant_id="merchant_id_example",
                pos_location_oid=1,
                postal_code="postal_code_example",
                state_province="state_province_example",
            ),
            reader=PointOfSaleReader(
                device_type="device_type_example",
                label="label_example",
                merchant_id="merchant_id_example",
                payment_provider="stripe",
                pos_reader_id=1,
                pos_register_oid=1,
                serial_number="serial_number_example",
                stripe_account_id="stripe_account_id_example",
                stripe_reader_id="stripe_reader_id_example",
            ),
            register=PointOfSaleRegister(
                merchant_id="merchant_id_example",
                name="name_example",
                pos_location_oid=1,
                pos_register_oid=1,
            ),
        ),
        properties=[
            OrderProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        quote=OrderQuote(
            quote_expiration_dts="quote_expiration_dts_example",
            quoted_by="quoted_by_example",
            quoted_dts="quoted_dts_example",
        ),
        refund_dts="refund_dts_example",
        refund_reason="refund_reason_example",
        reject_dts="reject_dts_example",
        reject_reason="reject_reason_example",
        salesforce=OrderSalesforce(
            salesforce_opportunity_id="salesforce_opportunity_id_example",
        ),
        shipping=OrderShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            day_phone_e164="day_phone_e164_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            evening_phone_e164="evening_phone_e164_example",
            first_name="first_name_example",
            last_name="last_name_example",
            least_cost_route=True,
            least_cost_route_shipping_methods=[
                "least_cost_route_shipping_methods_example",
            ],
            lift_gate=True,
            postal_code="postal_code_example",
            rma="rma_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_date="shipping_date_example",
            shipping_department_status="shipping_department_status_example",
            shipping_method="shipping_method_example",
            shipping_method_accounting_code="shipping_method_accounting_code_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
            tracking_number_details=[
                OrderTrackingNumberDetails(
                    actual_delivery_date="actual_delivery_date_example",
                    actual_delivery_date_formatted="actual_delivery_date_formatted_example",
                    details=[
                        OrderTrackingNumberDetail(
                            city="city_example",
                            event_dts="event_dts_example",
                            event_local_date="event_local_date_example",
                            event_local_time="event_local_time_example",
                            event_timezone_id="event_timezone_id_example",
                            state="state_example",
                            subtag="subtag_example",
                            subtag_message="subtag_message_example",
                            tag="tag_example",
                            tag_description="tag_description_example",
                            tag_icon="tag_icon_example",
                            zip="zip_example",
                        ),
                    ],
                    easypost_tracker_id="easypost_tracker_id_example",
                    expected_delivery_date="expected_delivery_date_example",
                    expected_delivery_date_formatted="expected_delivery_date_formatted_example",
                    map_url="map_url_example",
                    order_placed_date="order_placed_date_example",
                    order_placed_date_formatted="order_placed_date_formatted_example",
                    payment_processed_date="payment_processed_date_example",
                    payment_processed_date_formatted="payment_processed_date_formatted_example",
                    shipped_date="shipped_date_example",
                    shipped_date_formatted="shipped_date_formatted_example",
                    shipping_method="shipping_method_example",
                    status="status_example",
                    status_description="status_description_example",
                    tracking_number="tracking_number_example",
                    tracking_url="tracking_url_example",
                ),
            ],
            tracking_numbers=[
                "tracking_numbers_example",
            ],
            weight=Weight(
                uom="KG",
                value=3.14,
            ),
        ),
        summary=OrderSummary(
            actual_fulfillment=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            actual_payment_processing=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            actual_shipping=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            internal_gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            internal_gift_certificate_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            other_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_total_discount=Currency(
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
            subtotal_discount_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_refunded=Currency(
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
            tax_refunded=Currency(
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
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        tags=[
            OrderTag(
                tag_value="tag_value_example",
            ),
        ],
        taxes=OrderTaxes(
            arbitrary_tax=3.14,
            arbitrary_tax_rate=3.14,
            arbitrary_taxable_subtotal=3.14,
            tax_city_accounting_code="tax_city_accounting_code_example",
            tax_country_accounting_code="tax_country_accounting_code_example",
            tax_county="tax_county_example",
            tax_county_accounting_code="tax_county_accounting_code_example",
            tax_gift_charge=True,
            tax_postal_code_accounting_code="tax_postal_code_accounting_code_example",
            tax_rate=3.14,
            tax_rate_city=3.14,
            tax_rate_country=3.14,
            tax_rate_county=3.14,
            tax_rate_postal_code=3.14,
            tax_rate_state=3.14,
            tax_shipping=True,
            tax_state_accounting_code="tax_state_accounting_code_example",
        ),
        utms=[
            OrderUtm(
                attribution_first_click_subtotal=3.14,
                attribution_first_click_total=3.14,
                attribution_last_click_subtotal=3.14,
                attribution_last_click_total=3.14,
                attribution_linear_subtotal=3.14,
                attribution_linear_total=3.14,
                attribution_position_based_subtotal=3.14,
                attribution_position_based_total=3.14,
                click_dts="click_dts_example",
                facebook_ad_id="facebook_ad_id_example",
                fbclid="fbclid_example",
                gbraid="gbraid_example",
                glcid="glcid_example",
                msclkid="msclkid_example",
                ttclid="ttclid_example",
                uc_message_id="uc_message_id_example",
                utm_campaign="utm_campaign_example",
                utm_content="utm_content_example",
                utm_id="utm_id_example",
                utm_medium="utm_medium_example",
                utm_source="utm_source_example",
                utm_term="utm_term_example",
                vmcid="vmcid_example",
                wbraid="wbraid_example",
            ),
        ],
    ) # Order | Order to insert
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert an order
        api_response = api_instance.insert_order(order)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->insert_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert an order
        api_response = api_instance.insert_order(order, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->insert_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)| Order to insert |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**OrderResponse**](OrderResponse.md)

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

# **is_refundable_order**
> OrderRefundableResponse is_refundable_order(order_id)

Determine if an order can be refunded

Determine if an order can be refunded based upon payment method and age 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_refundable_response import OrderRefundableResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to check for refundable order.

    # example passing only required values which don't have defaults set
    try:
        # Determine if an order can be refunded
        api_response = api_instance.is_refundable_order(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->is_refundable_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to check for refundable order. |

### Return type

[**OrderRefundableResponse**](OrderRefundableResponse.md)

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

# **process_payment**
> OrderProcessPaymentResponse process_payment(order_id, process_payment_request)

Process payment

Process payment on order 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order_process_payment_request import OrderProcessPaymentRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_process_payment_response import OrderProcessPaymentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to process payment on
    process_payment_request = OrderProcessPaymentRequest(
        amount=3.14,
        card_verification_number_token="card_verification_number_token_example",
    ) # OrderProcessPaymentRequest | Process payment parameters

    # example passing only required values which don't have defaults set
    try:
        # Process payment
        api_response = api_instance.process_payment(order_id, process_payment_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->process_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to process payment on |
 **process_payment_request** | [**OrderProcessPaymentRequest**](OrderProcessPaymentRequest.md)| Process payment parameters |

### Return type

[**OrderProcessPaymentResponse**](OrderProcessPaymentResponse.md)

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

# **refund_order**
> OrderResponse refund_order(order_id, order)

Refund an order

Perform a refund operation on an order and then update the order if successful 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order import Order
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_response import OrderResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to refund.
    order = Order(
        affiliates=[
            OrderAffiliate(
                affiliate_oid=1,
                ledger_entries=[
                    OrderAffiliateLedger(
                        assigned_by_user="assigned_by_user_example",
                        item_id="item_id_example",
                        tier_number=1,
                        transaction_amount=3.14,
                        transaction_amount_paid=3.14,
                        transaction_dts="transaction_dts_example",
                        transaction_memo="transaction_memo_example",
                        transaction_percentage=3.14,
                        transaction_state="Pending",
                    ),
                ],
                sub_id="sub_id_example",
            ),
        ],
        auto_order=OrderAutoOrder(
            auto_order_code="auto_order_code_example",
            auto_order_oid=1,
            cancel_after_next_x_orders=1,
            cancel_downgrade=True,
            cancel_reason="cancel_reason_example",
            cancel_upgrade=True,
            canceled_by_user="canceled_by_user_example",
            canceled_dts="canceled_dts_example",
            completed=True,
            credit_card_attempt=1,
            disabled_dts="disabled_dts_example",
            enabled=True,
            failure_reason="failure_reason_example",
            items=[
                AutoOrderItem(
                    arbitrary_item_id="arbitrary_item_id_example",
                    arbitrary_percentage_discount=3.14,
                    arbitrary_quantity=3.14,
                    arbitrary_schedule_days=1,
                    arbitrary_unit_cost=3.14,
                    arbitrary_unit_cost_remaining_orders=1,
                    auto_order_item_oid=1,
                    frequency="Weekly",
                    future_schedules=[
                        AutoOrderItemFutureSchedule(
                            item_id="item_id_example",
                            rebill_count=1,
                            shipment_dts="shipment_dts_example",
                            unit_cost=3.14,
                        ),
                    ],
                    last_order_dts="last_order_dts_example",
                    life_time_value=3.14,
                    next_preshipment_notice_dts="next_preshipment_notice_dts_example",
                    next_shipment_dts="next_shipment_dts_example",
                    no_order_after_dts="no_order_after_dts_example",
                    number_of_rebills=1,
                    options=[
                        AutoOrderItemOption(
                            label="label_example",
                            value="value_example",
                        ),
                    ],
                    original_item_id="original_item_id_example",
                    original_quantity=3.14,
                    paypal_payer_id="paypal_payer_id_example",
                    paypal_recurring_payment_profile_id="paypal_recurring_payment_profile_id_example",
                    preshipment_notice_sent=True,
                    rebill_value=3.14,
                    remaining_repeat_count=1,
                    simple_schedule=AutoOrderItemSimpleSchedule(
                        frequency="Weekly",
                        item_id="item_id_example",
                        repeat_count=1,
                    ),
                ),
            ],
            next_attempt="next_attempt_example",
            original_order_id="original_order_id_example",
            override_affiliate_id=1,
            rebill_orders=[
                Order(),
            ],
            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
            status="active",
        ),
        billing=OrderBilling(
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
            day_phone_e164="day_phone_e164_example",
            email="email_example",
            evening_phone="evening_phone_example",
            evening_phone_e164="evening_phone_e164_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=OrderBuysafe(
            buysafe_bond_available=True,
            buysafe_bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            buysafe_bond_free=True,
            buysafe_bond_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            buysafe_bond_wanted=True,
            buysafe_shopping_cart_id="buysafe_shopping_cart_id_example",
        ),
        channel_partner=OrderChannelPartner(
            auto_approve_purchase_order=True,
            channel_partner_code="channel_partner_code_example",
            channel_partner_data="channel_partner_data_example",
            channel_partner_oid=1,
            channel_partner_order_id="channel_partner_order_id_example",
            ignore_invalid_shipping_method=True,
            no_realtime_payment_processing=True,
            skip_payment_processing=True,
            store_completed=True,
            store_if_payment_declines=True,
            treat_warnings_as_errors=True,
        ),
        checkout=OrderCheckout(
            browser=Browser(
                device=BrowserDevice(
                    family="family_example",
                ),
                os=BrowserOS(
                    family="family_example",
                    major="major_example",
                    minor="minor_example",
                    patch="patch_example",
                    patch_minor="patch_minor_example",
                ),
                user_agent=BrowserUserAgent(
                    family="family_example",
                    major="major_example",
                    minor="minor_example",
                    patch="patch_example",
                ),
            ),
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field10="custom_field10_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            custom_field8="custom_field8_example",
            custom_field9="custom_field9_example",
            customer_ip_address="customer_ip_address_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            screen_size="screen_size_example",
            storefront_host_name="storefront_host_name_example",
            upsell_path_code="upsell_path_code_example",
        ),
        coupons=[
            OrderCoupon(
                accounting_code="accounting_code_example",
                automatically_applied=True,
                base_coupon_code="base_coupon_code_example",
                coupon_code="coupon_code_example",
                hdie_from_customer=True,
            ),
        ],
        creation_dts="creation_dts_example",
        currency_code="currency_code_example",
        current_stage="Accounts Receivable",
        customer_profile=Customer(
            activity=CustomerActivity(
                activities=[
                    Activity(
                        action="action_example",
                        channel="channel_example",
                        metric="metric_example",
                        storefront_oid=1,
                        subject="subject_example",
                        ts=1,
                        type="type_example",
                        uuid="uuid_example",
                    ),
                ],
                global_unsubscribed=True,
                global_unsubscribed_dts="global_unsubscribed_dts_example",
                memberships=[
                    ListSegmentMembership(
                        name="name_example",
                        type="type_example",
                        uuid="uuid_example",
                    ),
                ],
                metrics=[
                    Metric(
                        all_time=3.14,
                        all_time_formatted="all_time_formatted_example",
                        last_30=3.14,
                        last_30_formatted="last_30_formatted_example",
                        name="name_example",
                        prior_30=3.14,
                        prior_30_formatted="prior_30_formatted_example",
                        type="type_example",
                    ),
                ],
                properties_list=[
                    ModelProperty(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                spam_complaint=True,
                spam_complaint_dts="spam_complaint_dts_example",
            ),
            affiliate_oid=1,
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_drop_shipping=True,
            allow_purchase_order=True,
            allow_quote_request=True,
            allow_selection_of_address_type=True,
            attachments=[
                CustomerAttachment(
                    customer_profile_attachment_oid=1,
                    description="description_example",
                    file_name="file_name_example",
                    mime_type="mime_type_example",
                    upload_dts="upload_dts_example",
                ),
            ],
            auto_approve_cod=True,
            auto_approve_purchase_order=True,
            automatic_merchant_notes="automatic_merchant_notes_example",
            billing=[
                CustomerBilling(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    customer_billing_oid=1,
                    customer_profile_oid=1,
                    day_phone="day_phone_example",
                    default_billing=True,
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    last_used_dts="last_used_dts_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            business_notes="business_notes_example",
            cards=[
                CustomerCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    customer_profile_credit_card_id=1,
                    customer_profile_oid=1,
                    last_used_dts="last_used_dts_example",
                ),
            ],
            cc_emails=[
                CustomerEmail(
                    customer_profile_email_oid=1,
                    email="email_example",
                    label="label_example",
                    receipt_notification=True,
                    refund_notification=True,
                    shipment_notification=True,
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            edi=CustomerEDI(
                channel_partner_oid=1,
                distribution_center_number="distribution_center_number_example",
                store_number="store_number_example",
            ),
            email="email_example",
            exempt_shipping_handling_charge=True,
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            last_modified_by="last_modified_by_example",
            last_modified_dts="last_modified_dts_example",
            loyalty=CustomerLoyalty(
                current_points=1,
                internal_gift_certificate=GiftCertificate(
                    activated=True,
                    code="code_example",
                    customer_profile_oid=1,
                    deleted=True,
                    email="email_example",
                    expiration_dts="expiration_dts_example",
                    gift_certificate_oid=1,
                    internal=True,
                    ledger_entries=[
                        GiftCertificateLedgerEntry(
                            amount=3.14,
                            description="description_example",
                            entry_dts="entry_dts_example",
                            gift_certificate_ledger_oid=1,
                            gift_certificate_oid=1,
                            reference_order_id="reference_order_id_example",
                        ),
                    ],
                    merchant_id="merchant_id_example",
                    merchant_note="merchant_note_example",
                    original_balance=3.14,
                    reference_order_id="reference_order_id_example",
                    remaining_balance=3.14,
                ),
                internal_gift_certificate_balance="internal_gift_certificate_balance_example",
                internal_gift_certificate_oid=1,
                ledger_entries=[
                    CustomerLoyaltyLedger(
                        created_by="created_by_example",
                        created_dts="created_dts_example",
                        description="description_example",
                        email="email_example",
                        item_id="item_id_example",
                        item_index=1,
                        ledger_dts="ledger_dts_example",
                        loyalty_campaign_oid=1,
                        loyalty_ledger_oid=1,
                        loyalty_points=1,
                        modified_by="modified_by_example",
                        modified_dts="modified_dts_example",
                        order_id="order_id_example",
                        quantity=1,
                        vesting_dts="vesting_dts_example",
                    ),
                ],
                pending_points=1,
                redemptions=[
                    CustomerLoyaltyRedemption(
                        coupon_code="coupon_code_example",
                        coupon_code_oid=1,
                        coupon_used=True,
                        description_for_customer="description_for_customer_example",
                        expiration_dts="expiration_dts_example",
                        gift_certificate_code="gift_certificate_code_example",
                        gift_certificate_oid=1,
                        loyalty_ledger_oid=1,
                        loyalty_points=1,
                        loyalty_redemption_oid=1,
                        order_id="order_id_example",
                        redemption_dts="redemption_dts_example",
                        remaining_balance=3.14,
                    ),
                ],
            ),
            maximum_item_count=1,
            merchant_id="merchant_id_example",
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            orders=[
                Order(),
            ],
            orders_summary=CustomerOrdersSummary(
                first_order_dts="first_order_dts_example",
                last_order_dts="last_order_dts_example",
                order_count=1,
                total=3.14,
            ),
            password="password_example",
            pricing_tiers=[
                CustomerPricingTier(
                    name="name_example",
                    pricing_tier_oid=1,
                ),
            ],
            privacy=CustomerPrivacy(
                last_update_dts="last_update_dts_example",
                marketing=True,
                preference=True,
                statistics=True,
            ),
            qb_class="qb_class_example",
            qb_code="qb_code_example",
            quotes=[
                Order(),
            ],
            quotes_summary=CustomerQuotesSummary(
                first_quote_dts="first_quote_dts_example",
                last_quote_dts="last_quote_dts_example",
                quote_count=1,
                total=3.14,
            ),
            referral_source="referral_source_example",
            reviewer=CustomerReviewer(
                auto_approve=True,
                average_overall_rating=3.14,
                expert=True,
                first_review="first_review_example",
                last_review="last_review_example",
                location="location_example",
                nickname="nickname_example",
                number_helpful_review_votes=1,
                rank=1,
                reviews_contributed=1,
            ),
            sales_rep_code="sales_rep_code_example",
            send_signup_notification=True,
            shipping=[
                CustomerShipping(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    customer_profile_oid=1,
                    customer_shipping_oid=1,
                    day_phone="day_phone_example",
                    default_shipping=True,
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    last_used_dts="last_used_dts_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            software_entitlements=[
                CustomerSoftwareEntitlement(
                    activation_code="activation_code_example",
                    activation_dts="activation_dts_example",
                    customer_software_entitlement_oid=1,
                    expiration_dts="expiration_dts_example",
                    purchased_via_item_description="purchased_via_item_description_example",
                    purchased_via_item_id="purchased_via_item_id_example",
                    purchased_via_order_id="purchased_via_order_id_example",
                    software_sku="software_sku_example",
                ),
            ],
            suppress_buysafe=True,
            tags=[
                CustomerTag(
                    tag_value="tag_value_example",
                ),
            ],
            tax_codes=CustomerTaxCodes(
                avalara_customer_code="avalara_customer_code_example",
                avalara_entity_use_code="avalara_entity_use_code_example",
                sovos_customer_code="sovos_customer_code_example",
                taxjar_customer_id="taxjar_customer_id_example",
                taxjar_exemption_type="taxjar_exemption_type_example",
            ),
            tax_exempt=True,
            tax_id="tax_id_example",
            terms="terms_example",
            track_separately=True,
            unapproved=True,
            ups_account_number="ups_account_number_example",
            website_url="website_url_example",
        ),
        digital_order=OrderDigitalOrder(
            creation_dts="creation_dts_example",
            expiration_dts="expiration_dts_example",
            items=[
                OrderDigitalItem(
                    file_size=1,
                    last_download="last_download_example",
                    last_download_ip_address="last_download_ip_address_example",
                    original_filename="original_filename_example",
                    product_code="product_code_example",
                    product_description="product_description_example",
                    remaining_downloads=1,
                    url="url_example",
                ),
            ],
            url="url_example",
            url_id="url_id_example",
        ),
        edi=OrderEdi(
            bill_to_edi_code="bill_to_edi_code_example",
            edi_department="edi_department_example",
            edi_internal_vendor_number="edi_internal_vendor_number_example",
            ship_to_edi_code="ship_to_edi_code_example",
        ),
        exchange_rate=3.14,
        fraud_score=OrderFraudScore(
            anonymous_proxy=True,
            bin_match="NA",
            carder_email=True,
            country_code="country_code_example",
            country_match=True,
            customer_phone_in_billing_location="customer_phone_in_billing_location_example",
            distance_km=1,
            free_email=True,
            high_risk_country=True,
            ip_city="ip_city_example",
            ip_isp="ip_isp_example",
            ip_latitude="ip_latitude_example",
            ip_longitude="ip_longitude_example",
            ip_org="ip_org_example",
            ip_region="ip_region_example",
            proxy_score=3.14,
            score=3.14,
            ship_forwarder=True,
            spam_score=3.14,
            transparent_proxy=True,
        ),
        gift=OrderGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_charge_accounting_code="gift_charge_accounting_code_example",
            gift_charge_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_accounting_code="gift_wrap_accounting_code_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=OrderGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_oid=1,
        ),
        internal=OrderInternal(
            exported_to_accounting=True,
            merchant_notes="merchant_notes_example",
            placed_by_user="placed_by_user_example",
            refund_by_user="refund_by_user_example",
            sales_rep_code="sales_rep_code_example",
            transactional_merchant_notes=[
                OrderTransactionalMerchantNote(
                    ip_address="ip_address_example",
                    note="note_example",
                    note_dts="note_dts_example",
                    user="user_example",
                ),
            ],
        ),
        items=[
            OrderItem(
                accounting_code="accounting_code_example",
                activation_codes=[
                    "activation_codes_example",
                ],
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                auto_order_schedule="auto_order_schedule_example",
                barcode="barcode_example",
                channel_partner_item_id="channel_partner_item_id_example",
                cogs=3.14,
                component_unit_value=3.14,
                cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                country_code_of_origin="country_code_of_origin_example",
                customs_description="customs_description_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                discount_quantity=3.14,
                discount_shipping_weight=Weight(
                    uom="KG",
                    value=3.14,
                ),
                distribution_center_code="distribution_center_code_example",
                edi=OrderItemEdi(
                    identifications=[
                        OrderItemEdiIdentification(
                            identification="identification_example",
                            quantity=1,
                        ),
                    ],
                    lots=[
                        OrderItemEdiLot(
                            lot_expiration="lot_expiration_example",
                            lot_number="lot_number_example",
                            lot_quantity=1,
                        ),
                    ],
                ),
                exclude_coupon=True,
                free_shipping=True,
                hazmat=True,
                height=Distance(
                    uom="IN",
                    value=3.14,
                ),
                item_index=1,
                item_reference_oid=1,
                kit=True,
                kit_component=True,
                length=Distance(
                    uom="IN",
                    value=3.14,
                ),
                manufacturer_sku="manufacturer_sku_example",
                max_days_time_in_transit=1,
                merchant_item_id="merchant_item_id_example",
                mix_and_match_group_name="mix_and_match_group_name_example",
                mix_and_match_group_oid=1,
                no_shipping_discount=True,
                options=[
                    OrderItemOption(
                        additional_dimension_application="none",
                        cost_change=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        file_attachment=OrderItemOptionFileAttachment(
                            expiration_dts="expiration_dts_example",
                            file_name="file_name_example",
                            mime_type="mime_type_example",
                            size=1,
                        ),
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        hidden=True,
                        label="label_example",
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        one_time_fee=True,
                        value="value_example",
                        weight_change=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
                packed_by_user="packed_by_user_example",
                parent_item_index=1,
                parent_merchant_item_id="parent_merchant_item_id_example",
                perishable_class="perishable_class_example",
                pricing_tier_name="pricing_tier_name_example",
                properties=[
                    OrderItemProperty(
                        display=True,
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quantity=3.14,
                quantity_refunded=3.14,
                quickbooks_class="quickbooks_class_example",
                refund_reason="refund_reason_example",
                return_reason="return_reason_example",
                ship_separately=True,
                shipped_by_user="shipped_by_user_example",
                shipped_dts="shipped_dts_example",
                shipping_status="shipping_status_example",
                special_product_type="special_product_type_example",
                tags=[
                    OrderItemTag(
                        tag_value="tag_value_example",
                    ),
                ],
                tax_free=True,
                tax_product_type="",
                taxable_cost=Currency(
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
                total_refunded=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                transmitted_to_distribution_center_dts="transmitted_to_distribution_center_dts_example",
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                weight=Weight(
                    uom="KG",
                    value=3.14,
                ),
                width=Distance(
                    uom="IN",
                    value=3.14,
                ),
            ),
        ],
        language_iso_code="language_iso_code_example",
        linked_shipment=OrderLinkedShipment(
            has_linked_shipment=True,
            linked_shipment=True,
            linked_shipment_channel_partner_order_ids=[
                "linked_shipment_channel_partner_order_ids_example",
            ],
            linked_shipment_order_ids=[
                "linked_shipment_order_ids_example",
            ],
            linked_shipment_to_order_id="linked_shipment_to_order_id_example",
        ),
        marketing=OrderMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list=True,
            referral_code="referral_code_example",
        ),
        merchant_id="merchant_id_example",
        order_id="order_id_example",
        payment=OrderPayment(
            check=OrderPaymentCheck(
                check_number="check_number_example",
            ),
            credit_card=OrderPaymentCreditCard(
                card_auth_ticket="card_auth_ticket_example",
                card_authorization_amount=3.14,
                card_authorization_dts="card_authorization_dts_example",
                card_authorization_reference_number="card_authorization_reference_number_example",
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_number_truncated=True,
                card_type="AMEX",
                card_verification_number_token="card_verification_number_token_example",
            ),
            echeck=OrderPaymentECheck(
                bank_aba_code="bank_aba_code_example",
                bank_account_name="bank_account_name_example",
                bank_account_number="bank_account_number_example",
                bank_account_type="Checking",
                bank_name="bank_name_example",
                bank_owner_type="Personal",
                customer_tax_id="customer_tax_id_example",
                drivers_license_dob="drivers_license_dob_example",
                drivers_license_number="drivers_license_number_example",
                drivers_license_state="drivers_license_state_example",
            ),
            hold_for_fraud_review=True,
            insurance=OrderPaymentInsurance(
                application_id="application_id_example",
                claim_id="claim_id_example",
                insurance_type="insurance_type_example",
                refund_claim_id="refund_claim_id_example",
            ),
            payment_dts="payment_dts_example",
            payment_method="Affirm",
            payment_method_accounting_code="payment_method_accounting_code_example",
            payment_method_deposit_to_account="payment_method_deposit_to_account_example",
            payment_status="Unprocessed",
            purchase_order=OrderPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge_accounting_code="surcharge_accounting_code_example",
            surcharge_transaction_fee=3.14,
            surcharge_transaction_percentage=3.14,
            test_order=True,
            transactions=[
                OrderPaymentTransaction(
                    details=[
                        OrderPaymentTransactionDetail(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    successful=True,
                    transaction_gateway="transaction_gateway_example",
                    transaction_timestamp="transaction_timestamp_example",
                ),
            ],
        ),
        point_of_sale=OrderPointOfSale(
            location=PointOfSaleLocation(
                adddress2="adddress2_example",
                address1="address1_example",
                city="city_example",
                country="country_example",
                distribution_center_code="distribution_center_code_example",
                external_id="external_id_example",
                merchant_id="merchant_id_example",
                pos_location_oid=1,
                postal_code="postal_code_example",
                state_province="state_province_example",
            ),
            reader=PointOfSaleReader(
                device_type="device_type_example",
                label="label_example",
                merchant_id="merchant_id_example",
                payment_provider="stripe",
                pos_reader_id=1,
                pos_register_oid=1,
                serial_number="serial_number_example",
                stripe_account_id="stripe_account_id_example",
                stripe_reader_id="stripe_reader_id_example",
            ),
            register=PointOfSaleRegister(
                merchant_id="merchant_id_example",
                name="name_example",
                pos_location_oid=1,
                pos_register_oid=1,
            ),
        ),
        properties=[
            OrderProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        quote=OrderQuote(
            quote_expiration_dts="quote_expiration_dts_example",
            quoted_by="quoted_by_example",
            quoted_dts="quoted_dts_example",
        ),
        refund_dts="refund_dts_example",
        refund_reason="refund_reason_example",
        reject_dts="reject_dts_example",
        reject_reason="reject_reason_example",
        salesforce=OrderSalesforce(
            salesforce_opportunity_id="salesforce_opportunity_id_example",
        ),
        shipping=OrderShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            day_phone_e164="day_phone_e164_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            evening_phone_e164="evening_phone_e164_example",
            first_name="first_name_example",
            last_name="last_name_example",
            least_cost_route=True,
            least_cost_route_shipping_methods=[
                "least_cost_route_shipping_methods_example",
            ],
            lift_gate=True,
            postal_code="postal_code_example",
            rma="rma_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_date="shipping_date_example",
            shipping_department_status="shipping_department_status_example",
            shipping_method="shipping_method_example",
            shipping_method_accounting_code="shipping_method_accounting_code_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
            tracking_number_details=[
                OrderTrackingNumberDetails(
                    actual_delivery_date="actual_delivery_date_example",
                    actual_delivery_date_formatted="actual_delivery_date_formatted_example",
                    details=[
                        OrderTrackingNumberDetail(
                            city="city_example",
                            event_dts="event_dts_example",
                            event_local_date="event_local_date_example",
                            event_local_time="event_local_time_example",
                            event_timezone_id="event_timezone_id_example",
                            state="state_example",
                            subtag="subtag_example",
                            subtag_message="subtag_message_example",
                            tag="tag_example",
                            tag_description="tag_description_example",
                            tag_icon="tag_icon_example",
                            zip="zip_example",
                        ),
                    ],
                    easypost_tracker_id="easypost_tracker_id_example",
                    expected_delivery_date="expected_delivery_date_example",
                    expected_delivery_date_formatted="expected_delivery_date_formatted_example",
                    map_url="map_url_example",
                    order_placed_date="order_placed_date_example",
                    order_placed_date_formatted="order_placed_date_formatted_example",
                    payment_processed_date="payment_processed_date_example",
                    payment_processed_date_formatted="payment_processed_date_formatted_example",
                    shipped_date="shipped_date_example",
                    shipped_date_formatted="shipped_date_formatted_example",
                    shipping_method="shipping_method_example",
                    status="status_example",
                    status_description="status_description_example",
                    tracking_number="tracking_number_example",
                    tracking_url="tracking_url_example",
                ),
            ],
            tracking_numbers=[
                "tracking_numbers_example",
            ],
            weight=Weight(
                uom="KG",
                value=3.14,
            ),
        ),
        summary=OrderSummary(
            actual_fulfillment=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            actual_payment_processing=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            actual_shipping=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            internal_gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            internal_gift_certificate_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            other_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_total_discount=Currency(
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
            subtotal_discount_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_refunded=Currency(
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
            tax_refunded=Currency(
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
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        tags=[
            OrderTag(
                tag_value="tag_value_example",
            ),
        ],
        taxes=OrderTaxes(
            arbitrary_tax=3.14,
            arbitrary_tax_rate=3.14,
            arbitrary_taxable_subtotal=3.14,
            tax_city_accounting_code="tax_city_accounting_code_example",
            tax_country_accounting_code="tax_country_accounting_code_example",
            tax_county="tax_county_example",
            tax_county_accounting_code="tax_county_accounting_code_example",
            tax_gift_charge=True,
            tax_postal_code_accounting_code="tax_postal_code_accounting_code_example",
            tax_rate=3.14,
            tax_rate_city=3.14,
            tax_rate_country=3.14,
            tax_rate_county=3.14,
            tax_rate_postal_code=3.14,
            tax_rate_state=3.14,
            tax_shipping=True,
            tax_state_accounting_code="tax_state_accounting_code_example",
        ),
        utms=[
            OrderUtm(
                attribution_first_click_subtotal=3.14,
                attribution_first_click_total=3.14,
                attribution_last_click_subtotal=3.14,
                attribution_last_click_total=3.14,
                attribution_linear_subtotal=3.14,
                attribution_linear_total=3.14,
                attribution_position_based_subtotal=3.14,
                attribution_position_based_total=3.14,
                click_dts="click_dts_example",
                facebook_ad_id="facebook_ad_id_example",
                fbclid="fbclid_example",
                gbraid="gbraid_example",
                glcid="glcid_example",
                msclkid="msclkid_example",
                ttclid="ttclid_example",
                uc_message_id="uc_message_id_example",
                utm_campaign="utm_campaign_example",
                utm_content="utm_content_example",
                utm_id="utm_id_example",
                utm_medium="utm_medium_example",
                utm_source="utm_source_example",
                utm_term="utm_term_example",
                vmcid="vmcid_example",
                wbraid="wbraid_example",
            ),
        ],
    ) # Order | Order to refund
    reject_after_refund = False # bool | Reject order after refund (optional) if omitted the server will use the default value of False
    skip_customer_notification = False # bool | Skip customer email notification (optional) if omitted the server will use the default value of False
    auto_order_cancel = False # bool | Cancel associated auto orders (optional) if omitted the server will use the default value of False
    manual_refund = False # bool | Consider a manual refund done externally (optional) if omitted the server will use the default value of False
    reverse_affiliate_transactions = True # bool | Reverse affiliate transactions (optional) if omitted the server will use the default value of True
    issue_store_credit = False # bool | Issue a store credit instead of refunding the original payment method, loyalty must be configured on merchant account (optional) if omitted the server will use the default value of False
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Refund an order
        api_response = api_instance.refund_order(order_id, order)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->refund_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Refund an order
        api_response = api_instance.refund_order(order_id, order, reject_after_refund=reject_after_refund, skip_customer_notification=skip_customer_notification, auto_order_cancel=auto_order_cancel, manual_refund=manual_refund, reverse_affiliate_transactions=reverse_affiliate_transactions, issue_store_credit=issue_store_credit, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->refund_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to refund. |
 **order** | [**Order**](Order.md)| Order to refund |
 **reject_after_refund** | **bool**| Reject order after refund | [optional] if omitted the server will use the default value of False
 **skip_customer_notification** | **bool**| Skip customer email notification | [optional] if omitted the server will use the default value of False
 **auto_order_cancel** | **bool**| Cancel associated auto orders | [optional] if omitted the server will use the default value of False
 **manual_refund** | **bool**| Consider a manual refund done externally | [optional] if omitted the server will use the default value of False
 **reverse_affiliate_transactions** | **bool**| Reverse affiliate transactions | [optional] if omitted the server will use the default value of True
 **issue_store_credit** | **bool**| Issue a store credit instead of refunding the original payment method, loyalty must be configured on merchant account | [optional] if omitted the server will use the default value of False
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**OrderResponse**](OrderResponse.md)

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

# **replacement**
> OrderReplacementResponse replacement(order_id, replacement)

Replacement order

Create a replacement order based upon a previous order 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_replacement import OrderReplacement
from ultracart.model.order_replacement_response import OrderReplacementResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to generate a replacement for.
    replacement = OrderReplacement(
        additional_merchant_notes_new_order="additional_merchant_notes_new_order_example",
        additional_merchant_notes_original_order="additional_merchant_notes_original_order_example",
        custom_field1="custom_field1_example",
        custom_field2="custom_field2_example",
        custom_field3="custom_field3_example",
        custom_field4="custom_field4_example",
        custom_field5="custom_field5_example",
        custom_field6="custom_field6_example",
        custom_field7="custom_field7_example",
        free=True,
        immediate_charge=True,
        items=[
            OrderReplacementItem(
                arbitrary_unit_cost=3.14,
                merchant_item_id="merchant_item_id_example",
                quantity=3.14,
            ),
        ],
        original_order_id="original_order_id_example",
        shipping_method="shipping_method_example",
        skip_payment=True,
    ) # OrderReplacement | Replacement order details

    # example passing only required values which don't have defaults set
    try:
        # Replacement order
        api_response = api_instance.replacement(order_id, replacement)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->replacement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to generate a replacement for. |
 **replacement** | [**OrderReplacement**](OrderReplacement.md)| Replacement order details |

### Return type

[**OrderReplacementResponse**](OrderReplacementResponse.md)

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

# **resend_receipt**
> BaseResponse resend_receipt(order_id)

Resend receipt

Resend the receipt for an order on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to resend the receipt for.

    # example passing only required values which don't have defaults set
    try:
        # Resend receipt
        api_response = api_instance.resend_receipt(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->resend_receipt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to resend the receipt for. |

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **resend_shipment_confirmation**
> BaseResponse resend_shipment_confirmation(order_id)

Resend shipment confirmation

Resend shipment confirmation for an order on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to resend the shipment notification for.

    # example passing only required values which don't have defaults set
    try:
        # Resend shipment confirmation
        api_response = api_instance.resend_shipment_confirmation(order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->resend_shipment_confirmation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to resend the shipment notification for. |

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **update_accounts_receivable_retry_config**
> BaseResponse update_accounts_receivable_retry_config(retry_config)

Update A/R Retry Configuration

Update A/R Retry Configuration.  This is primarily an internal API call.  It is doubtful you would ever need to use it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from ultracart.model.accounts_receivable_retry_config import AccountsReceivableRetryConfig
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    retry_config = AccountsReceivableRetryConfig(
        active=True,
        allow_process_linked_accounts=True,
        cancel_auto_order=True,
        current_service_plan="current_service_plan_example",
        daily_activity_list=[
            AccountsReceivableRetryDayActivity(
                charge=True,
                coupon_code="coupon_code_example",
                day=1,
            ),
        ],
        managed_by_linked_account_merchant_id=True,
        merchant_id="merchant_id_example",
        notify_emails=[
            "notify_emails_example",
        ],
        notify_rejections=True,
        notify_successes=True,
        process_linked_accounts=True,
        processing_percentage="processing_percentage_example",
        reject_at_end=True,
        trial_mode=True,
        trial_mode_expiration_dts="trial_mode_expiration_dts_example",
    ) # AccountsReceivableRetryConfig | AccountsReceivableRetryConfig object

    # example passing only required values which don't have defaults set
    try:
        # Update A/R Retry Configuration
        api_response = api_instance.update_accounts_receivable_retry_config(retry_config)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->update_accounts_receivable_retry_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retry_config** | [**AccountsReceivableRetryConfig**](AccountsReceivableRetryConfig.md)| AccountsReceivableRetryConfig object |

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **update_order**
> OrderResponse update_order(order_id, order)

Update an order

Update a new order on the UltraCart account.  This is probably NOT the method you want.  It is rare to update a completed order.  This will not trigger charges, emails, or any other automation. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import order_api
from ultracart.model.order import Order
from ultracart.model.error_response import ErrorResponse
from ultracart.model.order_response import OrderResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    order_id = "order_id_example" # str | The order id to update.
    order = Order(
        affiliates=[
            OrderAffiliate(
                affiliate_oid=1,
                ledger_entries=[
                    OrderAffiliateLedger(
                        assigned_by_user="assigned_by_user_example",
                        item_id="item_id_example",
                        tier_number=1,
                        transaction_amount=3.14,
                        transaction_amount_paid=3.14,
                        transaction_dts="transaction_dts_example",
                        transaction_memo="transaction_memo_example",
                        transaction_percentage=3.14,
                        transaction_state="Pending",
                    ),
                ],
                sub_id="sub_id_example",
            ),
        ],
        auto_order=OrderAutoOrder(
            auto_order_code="auto_order_code_example",
            auto_order_oid=1,
            cancel_after_next_x_orders=1,
            cancel_downgrade=True,
            cancel_reason="cancel_reason_example",
            cancel_upgrade=True,
            canceled_by_user="canceled_by_user_example",
            canceled_dts="canceled_dts_example",
            completed=True,
            credit_card_attempt=1,
            disabled_dts="disabled_dts_example",
            enabled=True,
            failure_reason="failure_reason_example",
            items=[
                AutoOrderItem(
                    arbitrary_item_id="arbitrary_item_id_example",
                    arbitrary_percentage_discount=3.14,
                    arbitrary_quantity=3.14,
                    arbitrary_schedule_days=1,
                    arbitrary_unit_cost=3.14,
                    arbitrary_unit_cost_remaining_orders=1,
                    auto_order_item_oid=1,
                    frequency="Weekly",
                    future_schedules=[
                        AutoOrderItemFutureSchedule(
                            item_id="item_id_example",
                            rebill_count=1,
                            shipment_dts="shipment_dts_example",
                            unit_cost=3.14,
                        ),
                    ],
                    last_order_dts="last_order_dts_example",
                    life_time_value=3.14,
                    next_preshipment_notice_dts="next_preshipment_notice_dts_example",
                    next_shipment_dts="next_shipment_dts_example",
                    no_order_after_dts="no_order_after_dts_example",
                    number_of_rebills=1,
                    options=[
                        AutoOrderItemOption(
                            label="label_example",
                            value="value_example",
                        ),
                    ],
                    original_item_id="original_item_id_example",
                    original_quantity=3.14,
                    paypal_payer_id="paypal_payer_id_example",
                    paypal_recurring_payment_profile_id="paypal_recurring_payment_profile_id_example",
                    preshipment_notice_sent=True,
                    rebill_value=3.14,
                    remaining_repeat_count=1,
                    simple_schedule=AutoOrderItemSimpleSchedule(
                        frequency="Weekly",
                        item_id="item_id_example",
                        repeat_count=1,
                    ),
                ),
            ],
            next_attempt="next_attempt_example",
            original_order_id="original_order_id_example",
            override_affiliate_id=1,
            rebill_orders=[
                Order(),
            ],
            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
            status="active",
        ),
        billing=OrderBilling(
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
            day_phone_e164="day_phone_e164_example",
            email="email_example",
            evening_phone="evening_phone_example",
            evening_phone_e164="evening_phone_e164_example",
            first_name="first_name_example",
            last_name="last_name_example",
            postal_code="postal_code_example",
            state_region="state_region_example",
            title="title_example",
        ),
        buysafe=OrderBuysafe(
            buysafe_bond_available=True,
            buysafe_bond_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            buysafe_bond_free=True,
            buysafe_bond_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            buysafe_bond_wanted=True,
            buysafe_shopping_cart_id="buysafe_shopping_cart_id_example",
        ),
        channel_partner=OrderChannelPartner(
            auto_approve_purchase_order=True,
            channel_partner_code="channel_partner_code_example",
            channel_partner_data="channel_partner_data_example",
            channel_partner_oid=1,
            channel_partner_order_id="channel_partner_order_id_example",
            ignore_invalid_shipping_method=True,
            no_realtime_payment_processing=True,
            skip_payment_processing=True,
            store_completed=True,
            store_if_payment_declines=True,
            treat_warnings_as_errors=True,
        ),
        checkout=OrderCheckout(
            browser=Browser(
                device=BrowserDevice(
                    family="family_example",
                ),
                os=BrowserOS(
                    family="family_example",
                    major="major_example",
                    minor="minor_example",
                    patch="patch_example",
                    patch_minor="patch_minor_example",
                ),
                user_agent=BrowserUserAgent(
                    family="family_example",
                    major="major_example",
                    minor="minor_example",
                    patch="patch_example",
                ),
            ),
            comments="comments_example",
            custom_field1="custom_field1_example",
            custom_field10="custom_field10_example",
            custom_field2="custom_field2_example",
            custom_field3="custom_field3_example",
            custom_field4="custom_field4_example",
            custom_field5="custom_field5_example",
            custom_field6="custom_field6_example",
            custom_field7="custom_field7_example",
            custom_field8="custom_field8_example",
            custom_field9="custom_field9_example",
            customer_ip_address="customer_ip_address_example",
            screen_branding_theme_code="screen_branding_theme_code_example",
            screen_size="screen_size_example",
            storefront_host_name="storefront_host_name_example",
            upsell_path_code="upsell_path_code_example",
        ),
        coupons=[
            OrderCoupon(
                accounting_code="accounting_code_example",
                automatically_applied=True,
                base_coupon_code="base_coupon_code_example",
                coupon_code="coupon_code_example",
                hdie_from_customer=True,
            ),
        ],
        creation_dts="creation_dts_example",
        currency_code="currency_code_example",
        current_stage="Accounts Receivable",
        customer_profile=Customer(
            activity=CustomerActivity(
                activities=[
                    Activity(
                        action="action_example",
                        channel="channel_example",
                        metric="metric_example",
                        storefront_oid=1,
                        subject="subject_example",
                        ts=1,
                        type="type_example",
                        uuid="uuid_example",
                    ),
                ],
                global_unsubscribed=True,
                global_unsubscribed_dts="global_unsubscribed_dts_example",
                memberships=[
                    ListSegmentMembership(
                        name="name_example",
                        type="type_example",
                        uuid="uuid_example",
                    ),
                ],
                metrics=[
                    Metric(
                        all_time=3.14,
                        all_time_formatted="all_time_formatted_example",
                        last_30=3.14,
                        last_30_formatted="last_30_formatted_example",
                        name="name_example",
                        prior_30=3.14,
                        prior_30_formatted="prior_30_formatted_example",
                        type="type_example",
                    ),
                ],
                properties_list=[
                    ModelProperty(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                spam_complaint=True,
                spam_complaint_dts="spam_complaint_dts_example",
            ),
            affiliate_oid=1,
            allow_3rd_party_billing=True,
            allow_cod=True,
            allow_drop_shipping=True,
            allow_purchase_order=True,
            allow_quote_request=True,
            allow_selection_of_address_type=True,
            attachments=[
                CustomerAttachment(
                    customer_profile_attachment_oid=1,
                    description="description_example",
                    file_name="file_name_example",
                    mime_type="mime_type_example",
                    upload_dts="upload_dts_example",
                ),
            ],
            auto_approve_cod=True,
            auto_approve_purchase_order=True,
            automatic_merchant_notes="automatic_merchant_notes_example",
            billing=[
                CustomerBilling(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    customer_billing_oid=1,
                    customer_profile_oid=1,
                    day_phone="day_phone_example",
                    default_billing=True,
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    last_used_dts="last_used_dts_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            business_notes="business_notes_example",
            cards=[
                CustomerCard(
                    card_expiration_month=1,
                    card_expiration_year=1,
                    card_number="card_number_example",
                    card_number_token="card_number_token_example",
                    card_type="card_type_example",
                    customer_profile_credit_card_id=1,
                    customer_profile_oid=1,
                    last_used_dts="last_used_dts_example",
                ),
            ],
            cc_emails=[
                CustomerEmail(
                    customer_profile_email_oid=1,
                    email="email_example",
                    label="label_example",
                    receipt_notification=True,
                    refund_notification=True,
                    shipment_notification=True,
                ),
            ],
            customer_profile_oid=1,
            dhl_account_number="dhl_account_number_example",
            dhl_duty_account_number="dhl_duty_account_number_example",
            edi=CustomerEDI(
                channel_partner_oid=1,
                distribution_center_number="distribution_center_number_example",
                store_number="store_number_example",
            ),
            email="email_example",
            exempt_shipping_handling_charge=True,
            fedex_account_number="fedex_account_number_example",
            free_shipping=True,
            free_shipping_minimum=3.14,
            last_modified_by="last_modified_by_example",
            last_modified_dts="last_modified_dts_example",
            loyalty=CustomerLoyalty(
                current_points=1,
                internal_gift_certificate=GiftCertificate(
                    activated=True,
                    code="code_example",
                    customer_profile_oid=1,
                    deleted=True,
                    email="email_example",
                    expiration_dts="expiration_dts_example",
                    gift_certificate_oid=1,
                    internal=True,
                    ledger_entries=[
                        GiftCertificateLedgerEntry(
                            amount=3.14,
                            description="description_example",
                            entry_dts="entry_dts_example",
                            gift_certificate_ledger_oid=1,
                            gift_certificate_oid=1,
                            reference_order_id="reference_order_id_example",
                        ),
                    ],
                    merchant_id="merchant_id_example",
                    merchant_note="merchant_note_example",
                    original_balance=3.14,
                    reference_order_id="reference_order_id_example",
                    remaining_balance=3.14,
                ),
                internal_gift_certificate_balance="internal_gift_certificate_balance_example",
                internal_gift_certificate_oid=1,
                ledger_entries=[
                    CustomerLoyaltyLedger(
                        created_by="created_by_example",
                        created_dts="created_dts_example",
                        description="description_example",
                        email="email_example",
                        item_id="item_id_example",
                        item_index=1,
                        ledger_dts="ledger_dts_example",
                        loyalty_campaign_oid=1,
                        loyalty_ledger_oid=1,
                        loyalty_points=1,
                        modified_by="modified_by_example",
                        modified_dts="modified_dts_example",
                        order_id="order_id_example",
                        quantity=1,
                        vesting_dts="vesting_dts_example",
                    ),
                ],
                pending_points=1,
                redemptions=[
                    CustomerLoyaltyRedemption(
                        coupon_code="coupon_code_example",
                        coupon_code_oid=1,
                        coupon_used=True,
                        description_for_customer="description_for_customer_example",
                        expiration_dts="expiration_dts_example",
                        gift_certificate_code="gift_certificate_code_example",
                        gift_certificate_oid=1,
                        loyalty_ledger_oid=1,
                        loyalty_points=1,
                        loyalty_redemption_oid=1,
                        order_id="order_id_example",
                        redemption_dts="redemption_dts_example",
                        remaining_balance=3.14,
                    ),
                ],
            ),
            maximum_item_count=1,
            merchant_id="merchant_id_example",
            minimum_item_count=1,
            minimum_subtotal=3.14,
            no_coupons=True,
            no_free_shipping=True,
            no_realtime_charge=True,
            orders=[
                Order(),
            ],
            orders_summary=CustomerOrdersSummary(
                first_order_dts="first_order_dts_example",
                last_order_dts="last_order_dts_example",
                order_count=1,
                total=3.14,
            ),
            password="password_example",
            pricing_tiers=[
                CustomerPricingTier(
                    name="name_example",
                    pricing_tier_oid=1,
                ),
            ],
            privacy=CustomerPrivacy(
                last_update_dts="last_update_dts_example",
                marketing=True,
                preference=True,
                statistics=True,
            ),
            qb_class="qb_class_example",
            qb_code="qb_code_example",
            quotes=[
                Order(),
            ],
            quotes_summary=CustomerQuotesSummary(
                first_quote_dts="first_quote_dts_example",
                last_quote_dts="last_quote_dts_example",
                quote_count=1,
                total=3.14,
            ),
            referral_source="referral_source_example",
            reviewer=CustomerReviewer(
                auto_approve=True,
                average_overall_rating=3.14,
                expert=True,
                first_review="first_review_example",
                last_review="last_review_example",
                location="location_example",
                nickname="nickname_example",
                number_helpful_review_votes=1,
                rank=1,
                reviews_contributed=1,
            ),
            sales_rep_code="sales_rep_code_example",
            send_signup_notification=True,
            shipping=[
                CustomerShipping(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    customer_profile_oid=1,
                    customer_shipping_oid=1,
                    day_phone="day_phone_example",
                    default_shipping=True,
                    evening_phone="evening_phone_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    last_used_dts="last_used_dts_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    tax_county="tax_county_example",
                    title="title_example",
                ),
            ],
            signup_dts="signup_dts_example",
            software_entitlements=[
                CustomerSoftwareEntitlement(
                    activation_code="activation_code_example",
                    activation_dts="activation_dts_example",
                    customer_software_entitlement_oid=1,
                    expiration_dts="expiration_dts_example",
                    purchased_via_item_description="purchased_via_item_description_example",
                    purchased_via_item_id="purchased_via_item_id_example",
                    purchased_via_order_id="purchased_via_order_id_example",
                    software_sku="software_sku_example",
                ),
            ],
            suppress_buysafe=True,
            tags=[
                CustomerTag(
                    tag_value="tag_value_example",
                ),
            ],
            tax_codes=CustomerTaxCodes(
                avalara_customer_code="avalara_customer_code_example",
                avalara_entity_use_code="avalara_entity_use_code_example",
                sovos_customer_code="sovos_customer_code_example",
                taxjar_customer_id="taxjar_customer_id_example",
                taxjar_exemption_type="taxjar_exemption_type_example",
            ),
            tax_exempt=True,
            tax_id="tax_id_example",
            terms="terms_example",
            track_separately=True,
            unapproved=True,
            ups_account_number="ups_account_number_example",
            website_url="website_url_example",
        ),
        digital_order=OrderDigitalOrder(
            creation_dts="creation_dts_example",
            expiration_dts="expiration_dts_example",
            items=[
                OrderDigitalItem(
                    file_size=1,
                    last_download="last_download_example",
                    last_download_ip_address="last_download_ip_address_example",
                    original_filename="original_filename_example",
                    product_code="product_code_example",
                    product_description="product_description_example",
                    remaining_downloads=1,
                    url="url_example",
                ),
            ],
            url="url_example",
            url_id="url_id_example",
        ),
        edi=OrderEdi(
            bill_to_edi_code="bill_to_edi_code_example",
            edi_department="edi_department_example",
            edi_internal_vendor_number="edi_internal_vendor_number_example",
            ship_to_edi_code="ship_to_edi_code_example",
        ),
        exchange_rate=3.14,
        fraud_score=OrderFraudScore(
            anonymous_proxy=True,
            bin_match="NA",
            carder_email=True,
            country_code="country_code_example",
            country_match=True,
            customer_phone_in_billing_location="customer_phone_in_billing_location_example",
            distance_km=1,
            free_email=True,
            high_risk_country=True,
            ip_city="ip_city_example",
            ip_isp="ip_isp_example",
            ip_latitude="ip_latitude_example",
            ip_longitude="ip_longitude_example",
            ip_org="ip_org_example",
            ip_region="ip_region_example",
            proxy_score=3.14,
            score=3.14,
            ship_forwarder=True,
            spam_score=3.14,
            transparent_proxy=True,
        ),
        gift=OrderGift(
            gift=True,
            gift_charge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_charge_accounting_code="gift_charge_accounting_code_example",
            gift_charge_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_email="gift_email_example",
            gift_message="gift_message_example",
            gift_wrap_accounting_code="gift_wrap_accounting_code_example",
            gift_wrap_cost=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_wrap_title="gift_wrap_title_example",
        ),
        gift_certificate=OrderGiftCertificate(
            gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            gift_certificate_code="gift_certificate_code_example",
            gift_certificate_oid=1,
        ),
        internal=OrderInternal(
            exported_to_accounting=True,
            merchant_notes="merchant_notes_example",
            placed_by_user="placed_by_user_example",
            refund_by_user="refund_by_user_example",
            sales_rep_code="sales_rep_code_example",
            transactional_merchant_notes=[
                OrderTransactionalMerchantNote(
                    ip_address="ip_address_example",
                    note="note_example",
                    note_dts="note_dts_example",
                    user="user_example",
                ),
            ],
        ),
        items=[
            OrderItem(
                accounting_code="accounting_code_example",
                activation_codes=[
                    "activation_codes_example",
                ],
                arbitrary_unit_cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                auto_order_schedule="auto_order_schedule_example",
                barcode="barcode_example",
                channel_partner_item_id="channel_partner_item_id_example",
                cogs=3.14,
                component_unit_value=3.14,
                cost=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                country_code_of_origin="country_code_of_origin_example",
                customs_description="customs_description_example",
                description="description_example",
                discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                discount_quantity=3.14,
                discount_shipping_weight=Weight(
                    uom="KG",
                    value=3.14,
                ),
                distribution_center_code="distribution_center_code_example",
                edi=OrderItemEdi(
                    identifications=[
                        OrderItemEdiIdentification(
                            identification="identification_example",
                            quantity=1,
                        ),
                    ],
                    lots=[
                        OrderItemEdiLot(
                            lot_expiration="lot_expiration_example",
                            lot_number="lot_number_example",
                            lot_quantity=1,
                        ),
                    ],
                ),
                exclude_coupon=True,
                free_shipping=True,
                hazmat=True,
                height=Distance(
                    uom="IN",
                    value=3.14,
                ),
                item_index=1,
                item_reference_oid=1,
                kit=True,
                kit_component=True,
                length=Distance(
                    uom="IN",
                    value=3.14,
                ),
                manufacturer_sku="manufacturer_sku_example",
                max_days_time_in_transit=1,
                merchant_item_id="merchant_item_id_example",
                mix_and_match_group_name="mix_and_match_group_name_example",
                mix_and_match_group_oid=1,
                no_shipping_discount=True,
                options=[
                    OrderItemOption(
                        additional_dimension_application="none",
                        cost_change=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        file_attachment=OrderItemOptionFileAttachment(
                            expiration_dts="expiration_dts_example",
                            file_name="file_name_example",
                            mime_type="mime_type_example",
                            size=1,
                        ),
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        hidden=True,
                        label="label_example",
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        one_time_fee=True,
                        value="value_example",
                        weight_change=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
                packed_by_user="packed_by_user_example",
                parent_item_index=1,
                parent_merchant_item_id="parent_merchant_item_id_example",
                perishable_class="perishable_class_example",
                pricing_tier_name="pricing_tier_name_example",
                properties=[
                    OrderItemProperty(
                        display=True,
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quantity=3.14,
                quantity_refunded=3.14,
                quickbooks_class="quickbooks_class_example",
                refund_reason="refund_reason_example",
                return_reason="return_reason_example",
                ship_separately=True,
                shipped_by_user="shipped_by_user_example",
                shipped_dts="shipped_dts_example",
                shipping_status="shipping_status_example",
                special_product_type="special_product_type_example",
                tags=[
                    OrderItemTag(
                        tag_value="tag_value_example",
                    ),
                ],
                tax_free=True,
                tax_product_type="",
                taxable_cost=Currency(
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
                total_refunded=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                transmitted_to_distribution_center_dts="transmitted_to_distribution_center_dts_example",
                unit_cost_with_discount=Currency(
                    currency_code="currency_code_example",
                    exchange_rate=3.14,
                    localized=3.14,
                    localized_formatted="localized_formatted_example",
                    value=3.14,
                ),
                upsell=True,
                weight=Weight(
                    uom="KG",
                    value=3.14,
                ),
                width=Distance(
                    uom="IN",
                    value=3.14,
                ),
            ),
        ],
        language_iso_code="language_iso_code_example",
        linked_shipment=OrderLinkedShipment(
            has_linked_shipment=True,
            linked_shipment=True,
            linked_shipment_channel_partner_order_ids=[
                "linked_shipment_channel_partner_order_ids_example",
            ],
            linked_shipment_order_ids=[
                "linked_shipment_order_ids_example",
            ],
            linked_shipment_to_order_id="linked_shipment_to_order_id_example",
        ),
        marketing=OrderMarketing(
            advertising_source="advertising_source_example",
            cell_phone_opt_in=True,
            mailing_list=True,
            referral_code="referral_code_example",
        ),
        merchant_id="merchant_id_example",
        order_id="order_id_example",
        payment=OrderPayment(
            check=OrderPaymentCheck(
                check_number="check_number_example",
            ),
            credit_card=OrderPaymentCreditCard(
                card_auth_ticket="card_auth_ticket_example",
                card_authorization_amount=3.14,
                card_authorization_dts="card_authorization_dts_example",
                card_authorization_reference_number="card_authorization_reference_number_example",
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_number_truncated=True,
                card_type="AMEX",
                card_verification_number_token="card_verification_number_token_example",
            ),
            echeck=OrderPaymentECheck(
                bank_aba_code="bank_aba_code_example",
                bank_account_name="bank_account_name_example",
                bank_account_number="bank_account_number_example",
                bank_account_type="Checking",
                bank_name="bank_name_example",
                bank_owner_type="Personal",
                customer_tax_id="customer_tax_id_example",
                drivers_license_dob="drivers_license_dob_example",
                drivers_license_number="drivers_license_number_example",
                drivers_license_state="drivers_license_state_example",
            ),
            hold_for_fraud_review=True,
            insurance=OrderPaymentInsurance(
                application_id="application_id_example",
                claim_id="claim_id_example",
                insurance_type="insurance_type_example",
                refund_claim_id="refund_claim_id_example",
            ),
            payment_dts="payment_dts_example",
            payment_method="Affirm",
            payment_method_accounting_code="payment_method_accounting_code_example",
            payment_method_deposit_to_account="payment_method_deposit_to_account_example",
            payment_status="Unprocessed",
            purchase_order=OrderPaymentPurchaseOrder(
                purchase_order_number="purchase_order_number_example",
            ),
            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
            surcharge=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            surcharge_accounting_code="surcharge_accounting_code_example",
            surcharge_transaction_fee=3.14,
            surcharge_transaction_percentage=3.14,
            test_order=True,
            transactions=[
                OrderPaymentTransaction(
                    details=[
                        OrderPaymentTransactionDetail(
                            name="name_example",
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    successful=True,
                    transaction_gateway="transaction_gateway_example",
                    transaction_timestamp="transaction_timestamp_example",
                ),
            ],
        ),
        point_of_sale=OrderPointOfSale(
            location=PointOfSaleLocation(
                adddress2="adddress2_example",
                address1="address1_example",
                city="city_example",
                country="country_example",
                distribution_center_code="distribution_center_code_example",
                external_id="external_id_example",
                merchant_id="merchant_id_example",
                pos_location_oid=1,
                postal_code="postal_code_example",
                state_province="state_province_example",
            ),
            reader=PointOfSaleReader(
                device_type="device_type_example",
                label="label_example",
                merchant_id="merchant_id_example",
                payment_provider="stripe",
                pos_reader_id=1,
                pos_register_oid=1,
                serial_number="serial_number_example",
                stripe_account_id="stripe_account_id_example",
                stripe_reader_id="stripe_reader_id_example",
            ),
            register=PointOfSaleRegister(
                merchant_id="merchant_id_example",
                name="name_example",
                pos_location_oid=1,
                pos_register_oid=1,
            ),
        ),
        properties=[
            OrderProperty(
                display=True,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        quote=OrderQuote(
            quote_expiration_dts="quote_expiration_dts_example",
            quoted_by="quoted_by_example",
            quoted_dts="quoted_dts_example",
        ),
        refund_dts="refund_dts_example",
        refund_reason="refund_reason_example",
        reject_dts="reject_dts_example",
        reject_reason="reject_reason_example",
        salesforce=OrderSalesforce(
            salesforce_opportunity_id="salesforce_opportunity_id_example",
        ),
        shipping=OrderShipping(
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            company="company_example",
            country_code="country_code_example",
            day_phone="day_phone_example",
            day_phone_e164="day_phone_e164_example",
            delivery_date="delivery_date_example",
            evening_phone="evening_phone_example",
            evening_phone_e164="evening_phone_e164_example",
            first_name="first_name_example",
            last_name="last_name_example",
            least_cost_route=True,
            least_cost_route_shipping_methods=[
                "least_cost_route_shipping_methods_example",
            ],
            lift_gate=True,
            postal_code="postal_code_example",
            rma="rma_example",
            ship_on_date="ship_on_date_example",
            ship_to_residential=True,
            shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
            shipping_date="shipping_date_example",
            shipping_department_status="shipping_department_status_example",
            shipping_method="shipping_method_example",
            shipping_method_accounting_code="shipping_method_accounting_code_example",
            special_instructions="special_instructions_example",
            state_region="state_region_example",
            title="title_example",
            tracking_number_details=[
                OrderTrackingNumberDetails(
                    actual_delivery_date="actual_delivery_date_example",
                    actual_delivery_date_formatted="actual_delivery_date_formatted_example",
                    details=[
                        OrderTrackingNumberDetail(
                            city="city_example",
                            event_dts="event_dts_example",
                            event_local_date="event_local_date_example",
                            event_local_time="event_local_time_example",
                            event_timezone_id="event_timezone_id_example",
                            state="state_example",
                            subtag="subtag_example",
                            subtag_message="subtag_message_example",
                            tag="tag_example",
                            tag_description="tag_description_example",
                            tag_icon="tag_icon_example",
                            zip="zip_example",
                        ),
                    ],
                    easypost_tracker_id="easypost_tracker_id_example",
                    expected_delivery_date="expected_delivery_date_example",
                    expected_delivery_date_formatted="expected_delivery_date_formatted_example",
                    map_url="map_url_example",
                    order_placed_date="order_placed_date_example",
                    order_placed_date_formatted="order_placed_date_formatted_example",
                    payment_processed_date="payment_processed_date_example",
                    payment_processed_date_formatted="payment_processed_date_formatted_example",
                    shipped_date="shipped_date_example",
                    shipped_date_formatted="shipped_date_formatted_example",
                    shipping_method="shipping_method_example",
                    status="status_example",
                    status_description="status_description_example",
                    tracking_number="tracking_number_example",
                    tracking_url="tracking_url_example",
                ),
            ],
            tracking_numbers=[
                "tracking_numbers_example",
            ],
            weight=Weight(
                uom="KG",
                value=3.14,
            ),
        ),
        summary=OrderSummary(
            actual_fulfillment=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            actual_payment_processing=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            actual_shipping=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            arbitrary_shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            internal_gift_certificate_amount=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            internal_gift_certificate_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            other_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            shipping_handling_total_discount=Currency(
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
            subtotal_discount_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            subtotal_refunded=Currency(
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
            tax_refunded=Currency(
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
            total=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
            total_refunded=Currency(
                currency_code="currency_code_example",
                exchange_rate=3.14,
                localized=3.14,
                localized_formatted="localized_formatted_example",
                value=3.14,
            ),
        ),
        tags=[
            OrderTag(
                tag_value="tag_value_example",
            ),
        ],
        taxes=OrderTaxes(
            arbitrary_tax=3.14,
            arbitrary_tax_rate=3.14,
            arbitrary_taxable_subtotal=3.14,
            tax_city_accounting_code="tax_city_accounting_code_example",
            tax_country_accounting_code="tax_country_accounting_code_example",
            tax_county="tax_county_example",
            tax_county_accounting_code="tax_county_accounting_code_example",
            tax_gift_charge=True,
            tax_postal_code_accounting_code="tax_postal_code_accounting_code_example",
            tax_rate=3.14,
            tax_rate_city=3.14,
            tax_rate_country=3.14,
            tax_rate_county=3.14,
            tax_rate_postal_code=3.14,
            tax_rate_state=3.14,
            tax_shipping=True,
            tax_state_accounting_code="tax_state_accounting_code_example",
        ),
        utms=[
            OrderUtm(
                attribution_first_click_subtotal=3.14,
                attribution_first_click_total=3.14,
                attribution_last_click_subtotal=3.14,
                attribution_last_click_total=3.14,
                attribution_linear_subtotal=3.14,
                attribution_linear_total=3.14,
                attribution_position_based_subtotal=3.14,
                attribution_position_based_total=3.14,
                click_dts="click_dts_example",
                facebook_ad_id="facebook_ad_id_example",
                fbclid="fbclid_example",
                gbraid="gbraid_example",
                glcid="glcid_example",
                msclkid="msclkid_example",
                ttclid="ttclid_example",
                uc_message_id="uc_message_id_example",
                utm_campaign="utm_campaign_example",
                utm_content="utm_content_example",
                utm_id="utm_id_example",
                utm_medium="utm_medium_example",
                utm_source="utm_source_example",
                utm_term="utm_term_example",
                vmcid="vmcid_example",
                wbraid="wbraid_example",
            ),
        ],
    ) # Order | Order to update
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an order
        api_response = api_instance.update_order(order_id, order)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->update_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an order
        api_response = api_instance.update_order(order_id, order, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling OrderApi->update_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to update. |
 **order** | [**Order**](Order.md)| Order to update |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**OrderResponse**](OrderResponse.md)

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

