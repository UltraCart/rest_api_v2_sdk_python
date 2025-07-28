# ultracart.OrderApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_order_total**](OrderApi.md#adjust_order_total) | **POST** /order/orders/{order_id}/adjust_order_total/{desired_total} | Adjusts an order total
[**block_refund_on_order**](OrderApi.md#block_refund_on_order) | **GET** /order/orders/{order_id}/refund_block | Set a refund block on an order
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
[**unblock_refund_on_order**](OrderApi.md#unblock_refund_on_order) | **GET** /order/orders/{order_id}/refund_unblock | Remove a refund block on an order
[**update_accounts_receivable_retry_config**](OrderApi.md#update_accounts_receivable_retry_config) | **POST** /order/accountsReceivableRetryConfig | Update A/R Retry Configuration
[**update_order**](OrderApi.md#update_order) | **PUT** /order/orders/{order_id} | Update an order
[**validate_order**](OrderApi.md#validate_order) | **POST** /order/validate | Validate


# **adjust_order_total**
> BaseResponse adjust_order_total(order_id, desired_total)

Adjusts an order total

Adjusts an order total.  Adjusts individual items appropriately and considers taxes.  Desired total should be provided in the same currency as the order and must be less than the current total and greater than zero.  This call will change the order total.  It returns true if the desired total is achieved.  If the goal seeking algorithm falls short (usually by pennies), this method returns back false.  View the merchant notes for the order for further details. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
"""
OrderApi.adjustOrderTotal() takes a desired order total and performs goal-seeking to adjust all items and taxes
appropriately.  This method was created for merchants dealing with Medicare and Medicaid.  When selling their
medical devices, they would often run into limits approved by Medicare.  As such, they needed to adjust the
order total to match the approved amount.  This is a convenience method to adjust individual items and their
taxes to match the desired total.
"""

from samples import api_client
from ultracart.apis import OrderApi
from ultracart import ApiException
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    # Initialize Order API
    order_api = OrderApi(api_client())

    # Set order details
    order_id = 'DEMO-0009104390'
    desired_total = '21.99'

    # Adjust order total
    api_response = order_api.adjust_order_total(order_id, desired_total)

    # Check for errors
    if api_response.error:
        logger.error(api_response.error.developer_message)
        logger.error(api_response.error.user_message)
        print('Order could not be adjusted. See Python error log.')
        exit()

    # Check success
    if api_response.success:
        print('Order was adjusted successfully. Use get_order() to retrieve the order if needed.')

except ApiException as e:
    logger.error(f"API Exception: {e}")
    print('Order could not be adjusted due to an API error.')
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

# **block_refund_on_order**
> block_refund_on_order(order_id)

Set a refund block on an order

Sets a refund block on an order to prevent a user from performing a refund.  Commonly used when a chargeback has been received. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import logging
from ultracart import ApiException
from ultracart.apis import OrderApi
from samples import api_client

# Enable error logging
logging.basicConfig(level=logging.DEBUG)

##
## blockRefundOnOrder sets an order property that is considered when a refund request is made.
## If the property is present, the refund is denied.  Being an order property allows for querying
## upon it within BigQuery for audit purposes.

# Using the API key to initialize the order API
order_api = OrderApi(api_client())

order_id = 'DEMO-0009105222'

try:
    order_api.block_refund_on_order(order_id, block_reason='Chargeback' )
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->block_refund_on_order: {e}")
    exit()

print('Metho executed successfully. Returns back 204 No Content')
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to block a refund on. |
 **block_reason** | **str**| Block reason code (optional) | [optional]

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
"""
OrderApi.cancelOrder() cancels an order by rejecting it.

Restrictions:
1) Cannot cancel completed orders
2) Cannot cancel already rejected orders
3) Cannot cancel orders transmitted to fulfillment center
4) Cannot cancel orders queued for distribution center transmission
"""

from samples import api_client
from ultracart.apis import OrderApi
from ultracart import ApiException
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    # Initialize Order API
    order_api = OrderApi(api_client())

    # Set order to cancel
    order_id = 'DEMO-0009104390'

    # Cancel order
    api_response = order_api.cancel_order(order_id)

    # Check for errors
    if api_response.error:
        logger.error(api_response.error.developer_message)
        logger.error(api_response.error.user_message)
        print('Order could not be canceled. See Python error log.')
        exit()

    # Check success
    if api_response.success:
        print('Order was canceled successfully.')

except ApiException as e:
    logger.error(f"API Exception: {e}")
    print('Order could not be canceled due to an API error.')
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to cancel. |
 **lock_self_ship_orders** | **bool**| Flag to prevent a order shipping during a refund process | [optional]
 **skip_refund_and_hold** | **bool**| Skip refund and move order to Held Orders department | [optional]

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
"""
OrderApi.deleteOrder() deletes an order. While rejecting orders is often preferred for audit trails,
deleting test orders can help maintain a tidy order history.
"""

from samples import api_client
from ultracart.apis import OrderApi
from ultracart import ApiException
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    # Initialize Order API
    order_api = OrderApi(api_client())

    # Set order to delete
    order_id = 'DEMO-0008104390'

    # Delete order
    order_api.delete_order(order_id)
    print('Order was deleted successfully.')

except ApiException as e:
    logger.error(f"API Exception: {e}")
    print('Order could not be deleted.')
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
from ultracart.apis import OrderApi
from ultracart.model.currency import Currency
from ultracart.model.order_item import OrderItem
from ultracart.model.order_process_payment_request import OrderProcessPaymentRequest
from ultracart.model.weight import Weight
from pprint import pprint
from samples import api_client

# These are the steps for cloning an existing order and charging the customer for it.
# 1. duplicateOrder
# 2. updateOrder (if you wish to change any part of it)
# 3. processPayment to charge the customer.
#
# As a reminder, if you wish to create a new order from scratch, use the CheckoutApi.
# The OrderApi is for managing existing orders.

api_instance = OrderApi(api_client())

expansion = "items"
# for this example, we're going to change the items after we duplicate the order, so
# the only expansion properties we need are the items.
# See: https://www.ultracart.com/api/  for a list of all expansions.

# Step 1. Duplicate the order
order_id_to_duplicate = 'DEMO-0009104436'
api_response = api_instance.duplicate_order(order_id_to_duplicate, expand=expansion)
new_order = api_response.order


# Step 2. Update the items.  I will create a new items array and assign it to the order to remove the old ones completely.
items = []
item = OrderItem()
item.merchant_item_id = 'simple_teapot'
item.quantity = 1.0
item.description = "A lovely teapot"
item.distribution_center_code = 'DFLT'  # where is this item shipping out of?

cost = Currency()
cost.currency_code = 'USD'
cost.value = 9.99
item.cost = cost

weight = Weight()
weight.uom = 'OZ'
weight.value = 6.0
item.weight = weight

items.append(item)
new_order.items = items
update_response = api_instance.update_order(order_id=new_order.order_id, order=new_order, expand=expansion)
updated_order = update_response.order


# Step 3. process the payment.
# the request object below takes two optional arguments.
# The first is an amount if you wish to bill for an amount different from the order.  We do not.
# The second is card_verification_number_token, which is a token you can create by using our hosted fields to
# upload a CVV value.  This will create a token you may use here.  However, most merchants using the duplicate
# order method will be setting up an auto order for a customer.  Those will not make use of the CVV, so we're
# not including it here.  That is why the request object below is does not have any values set.
# For more info on hosted fields, see: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377775/UltraCart+Hosted+Credit+Card+Fields

process_payment_request = OrderProcessPaymentRequest()
payment_response = api_instance.process_payment(new_order.order_id, process_payment_request)
if payment_response.error:
    print(payment_response.error.developer_message)
else:
    transaction_details = payment_response.payment_transaction  # do whatever you wish with this.
    pprint(updated_order)
    pprint(transaction_details)


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
"""
Format an order for display with various customization options.

Returns a text or HTML-formatted block similar to a receipt page.
"""

from samples import api_client
from ultracart.apis import OrderApi
from ultracart.models import OrderFormat
from ultracart import ApiException
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    # Initialize Order API
    order_api = OrderApi(api_client())

    # Configure format options
    format_options = OrderFormat(
        context='receipt',  # Options: unknown,receipt,shipment,refund,quote-request,quote
        format='table',     # Options: text,div,table,email
        show_contact_info=False,
        show_payment_info=False,
        show_merchant_notes=False,
        email_as_link=True,
        link_file_attachments=True,
        show_internal_information=True,
        show_non_sensitive_payment_info=True,
        show_in_merchant_currency=True,
        hide_bill_to_address=False,
        dont_link_email_to_search=True,
        translate=False
    )

    # Specify order ID
    order_id = 'DEMO-0009104390'

    # Format the order
    api_response = order_api.format(order_id, format_options)

    # Get formatted result
    formatted_result = api_response.formatted_result

    # Print CSS links (if needed)
    for link in api_response.css_links:
        print(f'CSS Link: {link}')

    # Print formatted result
    print(formatted_result)

except ApiException as e:
    logger.error(f"API Exception: {e}")
    print('Order formatting failed.')
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
from ultracart.apis import OrderApi
from samples import api_client
import base64

# Create Order API instance
order_api = OrderApi(api_client())

# Define order ID
order_id = 'DEMO-0009104976'

# Generate invoice (returns a base64-encoded PDF)
api_response = order_api.generate_invoice(order_id)
base64_pdf = api_response.pdf_base64

# Decode and save the PDF
decoded_pdf = base64.b64decode(base64_pdf)
with open('invoice.pdf', 'wb') as pdf_file:
    pdf_file.write(decoded_pdf)

print("Invoice PDF saved as 'invoice.pdf'.")
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
from ultracart.apis import OrderApi
from samples import api_client

# Create Order API instance
order_api = OrderApi(api_client())

# Define order ID
order_id = 'DEMO-0009104436'

# Generate order token
order_token_response = order_api.generate_order_token(order_id)
order_token = order_token_response.order_token

# Print the order token
print(f"Order Token is: {order_token}")

# Example token format:
# DEMO:UJZOGiIRLqgE3a10yp5wmEozLPNsGrDHNPiHfxsi0iAEcxgo9H74J/l6SR3X8g==
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


(No example for this operation).



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


(No example for this operation).



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
# This is primarily an internal API call.  It is doubtful you would ever need to use it.
# We do not provide an example for this call.
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
# This is primarily an internal API call.  It is doubtful you would ever need to use it.
# We do not provide an example for this call.
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
from ultracart.apis import OrderApi
from samples import api_client

# Create Order API instance
order_api = OrderApi(api_client())

# The expand variable instructs UltraCart how much information to return. The order object is large and
# while it's easily manageable for a single order, when querying thousands of orders, it is useful to reduce
# payload size.
# See www.ultracart.com/api/ for all the expansion fields available (this list below may become stale).
#
# Possible Order Expansions:
# affiliate           affiliate.ledger                    auto_order
# billing             channel_partner                     checkout
# coupon              customer_profile                    digital_order
# edi                 fraud_score                         gift
# gift_certificate    internal                            item
# linked_shipment     marketing                           payment
# payment.transaction quote                               salesforce
# shipping            shipping.tracking_number_details    summary
# taxes

expand = "item,summary,billing,shipping,shipping.tracking_number_details"

# Define order ID
order_id = 'DEMO-0009104390'

# Retrieve order
api_response = order_api.get_order(order_id, expand=expand)

# Check for errors
if api_response.error:
    print(f"Developer Message: {api_response.error.developer_message}")
    print(f"User Message: {api_response.error.user_message}")
    exit()

# Extract order details
order = api_response.order

# Print order details
print(order)
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
from ultracart.apis import OrderApi
from ultracart.model.order_by_token_query import OrderByTokenQuery
from samples import api_client

# OrderApi.get_order_by_token() was created for use within a custom thank-you page.
# The built-in StoreFront thank-you page displays the customer receipt and allows for unlimited customization.
# However, many merchants wish to process the receipt page on their own servers to do custom processing.
#
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377199/Custom+Thank+You+Page+URL
#
# When setting up a custom thank-you URL in the StoreFronts, you will provide a query parameter that will hold
# this order token. You may extract that from the request parameters and then call get_order_by_token()
# to get the order object.

# Create Order API instance
order_api = OrderApi(api_client())

# The expand variable instructs UltraCart how much information to return. The order object is large and
# while it's easily manageable for a single order, when querying thousands of orders, it is useful to reduce
# payload size.
# See www.ultracart.com/api/ for all the expansion fields available (this list below may become stale).
#
# Possible Order Expansions:
# affiliate           affiliate.ledger                    auto_order
# billing             channel_partner                     checkout
# coupon              customer_profile                    digital_order
# edi                 fraud_score                         gift
# gift_certificate    internal                            item
# linked_shipment     marketing                           payment
# payment.transaction quote                               salesforce
# shipping            shipping.tracking_number_details    summary
# taxes

expand = "billing,checkout,coupon,customer_profile,item,payment,shipping,summary,taxes"

# The token will be in a request parameter defined by you within your storefront.
# StoreFront -> Privacy and Tracking -> Advanced -> CustomThankYouUrl
# Example would be: www.mysite.com/receipt?orderToken=[OrderToken]

# TODO: Handle retrieving the order token from request parameters
order_token = "DEMO:UZBOGywSKKwD2a5wx5JwmkwyIPNsGrDHNPiHfxsi0iAEcxgo9H74J/l6SR3X8g=="  # Replace with actual order token

# To generate an order token manually for testing, refer to generate_order_token.py
# TODO: Handle missing order token (e.g., if this page is called incorrectly by a search engine, etc.)

order_token_query = OrderByTokenQuery(order_token=order_token)

# Retrieve order
api_response = order_api.get_order_by_token(order_token_query, expand=expand)

# Extract order details
order = api_response.order

# Print order details
print(order)
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
from ultracart.apis import OrderApi
from samples import api_client

# get_order_edi_documents() returns all EDI documents associated with an order.
#
# Possible Errors:
# Order.channel_partner_oid is null -> "Order is not associated with an EDI channel partner."

# Create Order API instance
order_api = OrderApi(api_client())

# Order ID to retrieve EDI documents for
order_id = "DEMO-0009104976"

# Retrieve EDI documents
edi_documents = order_api.get_order_edi_documents(order_id).edi_documents

# Print EDI documents
print(edi_documents)
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
from ultracart import ApiException
from ultracart.apis import OrderApi
from samples import api_client

# Increase time limit, pulling all orders could take a long time.
time_limit = 3000
# Set max execution time
time.sleep(time_limit)
# Set display errors
display_errors = 1

# getOrders was the first order query provided by UltraCart. It still functions well, but it is extremely verbose
# because the query call takes a variable for every possible filter. You are advised to use getOrdersByQuery().
# It is easier to use and will result in less code. Still, we provide an example here to be thorough.
#
# For this email, we will query all orders for a particular email address. The getOrdersByQuery() example
# illustrates using a date range to filter and select orders.

# Using the API key to initialize the order API
order_api = OrderApi(api_client())

def get_order_chunk(order_api, offset, limit):
    expand = "item,summary,billing,shipping,shipping.tracking_number_details"
    # See www.ultracart.com/api/ for all the expansion fields available (this list below may become stale)
    # Possible Order Expansions:
    # affiliate           affiliate.ledger                    auto_order
    # billing             channel_partner                     checkout
    # coupon              customer_profile                    digital_order
    # edi                 fraud_score                         gift
    # gift_certificate    internal                            item
    # linked_shipment     marketing                           payment
    # payment.transaction quote                               salesforce
    # shipping            shipping.tracking_number_details    summary
    # taxes

    order_id = None
    payment_method = None
    company = None
    first_name = None
    last_name = None
    city = None
    state_region = None
    postal_code = None
    country_code = None
    phone = None
    email = 'support@ultracart.com'  # <-- this is the only filter we're using.
    cc_email = None
    total = None
    screen_branding_theme_code = None
    storefront_host_name = None
    creation_date_begin = None
    creation_date_end = None
    payment_date_begin = None
    payment_date_end = None
    shipment_date_begin = None
    shipment_date_end = None
    rma = None
    purchase_order_number = None
    item_id = None
    current_stage = None
    channel_partner_code = None
    channel_partner_order_id = None
    _sort = None

    # See all these parameters? That is why you should use getOrdersByQuery() instead of getOrders()
    try:
        api_response = order_api.get_orders(
            order_id=order_id, payment_method=payment_method, company=company, first_name=first_name,
            last_name=last_name, city=city, state_region=state_region, postal_code=postal_code,
            country_code=country_code, phone=phone, email=email, cc_email=cc_email, total=total,
            screen_branding_theme_code=screen_branding_theme_code, storefront_host_name=storefront_host_name,
            creation_date_begin=creation_date_begin, creation_date_end=creation_date_end,
            payment_date_begin=payment_date_begin, payment_date_end=payment_date_end,
            shipment_date_begin=shipment_date_begin, shipment_date_end=shipment_date_end, rma=rma,
            purchase_order_number=purchase_order_number, item_id=item_id, current_stage=current_stage,
            channel_partner_code=channel_partner_code, channel_partner_order_id=channel_partner_order_id,
            limit=limit, offset=offset, _sort=_sort, expand=expand
        )
    except ApiException as e:
        print(f"Exception when calling OrderApi->get_orders: {e}")
        return []

    if api_response.orders is not None:
        return api_response.orders
    return []

# Initialize empty list to hold orders
orders = []

iteration = 1
offset = 0
limit = 200
more_records_to_fetch = True

while more_records_to_fetch:
    print(f"executing iteration {iteration}")
    chunk_of_orders = get_order_chunk(order_api, offset, limit)
    orders.extend(chunk_of_orders)
    offset += limit
    more_records_to_fetch = len(chunk_of_orders) == limit
    iteration += 1

# This could get verbose...
import pprint
pprint.pprint(orders)
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
from ultracart.apis import OrderApi
from ultracart.model.order_query_batch import OrderQueryBatch
from pprint import pprint
from samples import api_client

api_instance = OrderApi(api_client())

## This example shows how to request up to 500 orders by passing in their order ids.

# expansion = "item,summary,billing,shipping,shipping.tracking_number_details"
expansion = 'auto_order,billing,channel_partner,checkout,coupon,edi,gift,gift_certificate,internal,item,payment,payment.transaction,point_of_sale,properties,quote,shipping,shipping.tracking_number_details,summary,taxes,utms'
## see www.ultracart.com/api/ for all the expansion fields available (this list below may become stale)
##
## Possible Order Expansions:
## affiliate           affiliate.ledger                    auto_order
## billing             channel_partner                     checkout
## coupon              customer_profile                    digital_order
## edi                 fraud_score                         gift
## gift_certificate    internal                            item
## linked_shipment     marketing                           payment
## payment.transaction quote                               salesforce
## shipping            shipping.tracking_number_details    summary
## taxes
##

order_batch = OrderQueryBatch()
order_batch.limit = 500
order_batch.limit = 500
order_batch.query_target = "cache"
order_batch.order_ids = [
    'DEMO-0009103110',
    'DEMO-0009103116',
    'DEMO-0009103121',
    'DEMO-0009103416',
    'DEMO-0009103422',
    'DEMO-0009103423',
    'DEMO-0009103424',
    'DEMO-0009103426',
    'DEMO-0009103427'
]

api_response = api_instance.get_orders_batch(order_batch=order_batch, expand=expansion)
orders = api_response.orders

# pprint(orders)
for order in orders:
    pprint(order)
print(f"{len(orders)} were returned.")
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
from ultracart.apis import OrderApi
from ultracart.model.order_query import OrderQuery
from ultracart.model.order import Order
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client
from datetime import datetime, timedelta
import time

start_time = time.time()
api_instance = OrderApi(api_client())

## This example illustrates how to query the OrderQuery object to select a range of records.  It uses a subroutine
## to aggregate the records that span multiple API calls.  This specific example illustrates a work-around to selecting
## all rejected orders.  Because the UltraCart SDK does not have a way to query orders based on whether they
## were rejected, we can instead query based on the rejected_dts, which is null if the order is not rejected.
## So we will simply use a large time frame to ensure we query all rejections.

iteration = 1
offset = 0
limit = 1000
more_records_to_fetch = True
orders = []
date_field = 'payment'

def get_order_chunk():
    # expansion = "item,summary,billing,shipping,shipping.tracking_number_details"
    expansion = 'auto_order,billing,channel_partner,checkout,coupon,edi,gift,gift_certificate,internal,item,payment,payment.transaction,point_of_sale,properties,quote,shipping,shipping.tracking_number_details,summary,taxes,utms'
    ## see www.ultracart.com/api/ for all the expansion fields available (this list below may become stale)
    ##
    ## Possible Order Expansions:
    ## affiliate           affiliate.ledger                    auto_order
    ## billing             channel_partner                     checkout
    ## coupon              customer_profile                    digital_order
    ## edi                 fraud_score                         gift
    ## gift_certificate    internal                            item
    ## linked_shipment     marketing                           payment
    ## payment.transaction quote                               salesforce
    ## shipping            shipping.tracking_number_details    summary
    ## taxes
    ##

    query = OrderQuery()
    ## Uncomment the next line to retrieve a single order.  But there are simpler methods to retrieve a single order than getOrdersByQuery
    ## order_query.order_id = "DEMO-0009104390"

    now = datetime.now()
    six_hours_ago = now - timedelta(hours=6)
    # begin_dts = datetime.strptime('2000-01-01', '%Y-%m-%d').astimezone().isoformat('T', 'milliseconds')
    begin_dts = six_hours_ago.astimezone().isoformat('T', 'milliseconds')

    end_dts = datetime.now().astimezone().isoformat('T', 'milliseconds')
    print(f"Date range: {begin_dts} to {end_dts}")

    if date_field == 'reject':
        query.refund_date_begin = begin_dts
        query.refund_date_end = end_dts
    elif date_field == 'shipment':
        query.shipment_date_begin = begin_dts
        query.shipment_date_end = end_dts
    else:
        query.payment_date_begin = begin_dts
        query.payment_date_end = end_dts

    query.query_target = 'cache'  # cache is much faster, but may be missing the last few minutes of orders.

    api_response = api_instance.get_orders_by_query(order_query=query, limit=limit, offset=offset, expand=expansion, sort='+shipping.state_region,-shipping.city')
    if api_response.orders is not None:
        return api_response.orders
    return []


while more_records_to_fetch:
    print(f"executing iteration {iteration} ")
    chunk_of_orders = get_order_chunk()
    orders.extend(chunk_of_orders)
    offset = offset + limit
    more_records_to_fetch = len(chunk_of_orders) == limit
    iteration = iteration + 1

# pprint(orders)
for order in orders:
    shipping = getattr(order, 'shipping')
    # pprint(shipping)
    print(f"{getattr(shipping, 'state_region', 'NULL')} {getattr(shipping, 'city', 'NULL')} {order.order_id}")
    # pprint(order)
print(f"{len(orders)} were returned.")

# pprint(orders[0])

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The {date_field} date range query took {elapsed_time} seconds to execute.")
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
"""
 * Please do not use OrderApi.insertOrder()
 * This method was provided in the first release of our REST API.
 * It was replaced with our ChannelPartnerApi.importChannelPartnerOrder()
 *
 * Here are your options:
 * If you need to add regular orders that still require payment processing, use the CheckoutApi.
 *    The CheckoutApi has fantastic support for payment processing.
 *
 * If you need to add channel partner orders (eBay, Amazon, your call center, etc), use the ChannelPartnerApi.
 *    The ChannelPartnerApi has appropriate support for processing such orders.
 *
 * We support our entire API forever, so this method remains active.  But, we do not provide any samples for it.
 * You may use it, but we believe it will require extra time and effort and possibly much frustration.
 *
 * Reminder: The ONLY way to provide credit card numbers and cvv numbers to the UltraCart system is through
 * hosted fields.
 * See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377775/UltraCart+Hosted+Credit+Card+Fields
 * See: https://github.com/UltraCart/sdk_samples/blob/master/hosted_fields/hosted_fields.html
"""
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
import logging
from ultracart import ApiException
from ultracart.apis import OrderApi
from samples import api_client

# Enable error logging
logging.basicConfig(level=logging.DEBUG)

# isRefundable queries the UltraCart system whether an order is refundable or not.
# In addition to a simple boolean response, UltraCart also returns back any reasons why
# an order is not refundable.
# Finally, the response also contains any refund or return reasons configured on the account
# in the event that this merchant account is configured to require a reason for a return or refund.

# Using the API key to initialize the order API
order_api = OrderApi(api_client())

order_id = 'DEMO-0009104976'

try:
    api_response = order_api.is_refundable_order(order_id)
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->is_refundable_order: {e}")
    exit()

# This could get verbose...
import pprint
pprint.pprint(api_response)
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
import logging
from ultracart import ApiException
from ultracart.apis import OrderApi
from ultracart.models import OrderItem, Currency, Weight, OrderProcessPaymentRequest
from samples import api_client

# Enable error logging
logging.basicConfig(level=logging.DEBUG)

# OrderApi.processPayment() was designed to charge a customer for an order. It was created to work in tandem with
# duplicateOrder(), which does not accomplish payment on its own. The use-case for this method is to
# duplicate a customer's order and then charge them for it. duplicateOrder() does not charge the customer again,
# which is why processPayment() exists.
#
# These are the steps for cloning an existing order and charging the customer for it.
# 1. duplicateOrder
# 2. updateOrder (if you wish to change any part of it)
# 3. processPayment to charge the customer.
#
# As a reminder, if you wish to create a new order from scratch, use the CheckoutApi or ChannelPartnerApi.
# The OrderApi is for managing existing orders.

# Using the API key to initialize the order API
order_api = OrderApi(api_client())

expand = "items"   # For this example, we're going to change the items after we duplicate the order, so
# the only expansion properties we need are the items.
# See: https://www.ultracart.com/api/ for a list of all expansions.

# Step 1. Duplicate the order
order_id_to_duplicate = 'DEMO-0009104436'
try:
    api_response = order_api.duplicate_order(order_id_to_duplicate, expand=expand)
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->duplicate_order: {e}")
    exit()

new_order = api_response.order

# Step 2. Update the items. I will create a new items array and assign it to the order to remove the old ones completely.
items = []
item = OrderItem()
item.merchant_item_id = 'simple_teapot'
item.quantity = 1
item.description = "A lovely teapot"
item.distribution_center_code = 'DFLT'  # Where is this item shipping out of?

cost = Currency()
cost.currency_code = 'USD'
cost.value = 9.99
item.cost = cost

weight = Weight()
weight.uom = "OZ"
weight.value = 6
item.weight = weight

items.append(item)
new_order.items = items

try:
    update_response = order_api.update_order(new_order.order_id, new_order, expand=expand)
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->update_order: {e}")
    exit()

updated_order = update_response.order

# Step 3. Process the payment.
# The request object below takes two optional arguments.
# The first is an amount if you wish to bill for an amount different from the order.
# We do not bill differently in this example.
# The second is card_verification_number_token, which is a token you can create by using our hosted fields to
# upload a CVV value. This will create a token you may use here. However, most merchants using the duplicate
# order method will be setting up an auto order for a customer. Those will not make use of the CVV, so we're
# not including it here. That is why the request object below is does not have any values set.

process_payment_request = OrderProcessPaymentRequest()
try:
    payment_response = order_api.process_payment(new_order.order_id, process_payment_request)
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->process_payment: {e}")
    exit()

transaction_details = payment_response.payment_transaction  # Do whatever you wish with this.

# This could get verbose...
import pprint
print("New Order (after updated items):")
pprint.pprint(updated_order)
print("\nPayment Response:")
pprint.pprint(payment_response)
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

Perform a refund operation on an order and then update the order if successful.  All of the object properties ending in _refunded should be the TOTAL amount that should end up being refunded.  UltraCart will calculate the actual amount to refund based upon the prior refunds. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import logging
from ultracart import ApiException
from ultracart.apis import OrderApi
from ultracart.models import OrderItem
from samples import api_client

# Enable error logging
logging.basicConfig(level=logging.DEBUG)

# refundOrder() allows for both partial and complete refunds. Both are accomplished with the same steps.
# 1) Retrieve an order object using the SDK.
# 2) Input the refunded quantities for any or all items.
# 3) Call refundOrder, passing in the modified object.
# 4) To do a full refund, set all item refund quantities to their purchased quantities.
#
# This example will perform a full refund.

# Using the API key to initialize the order API
order_api = OrderApi(api_client())

# For the refund, we only need the items expanded to adjust their quantities.
# See: https://www.ultracart.com/api/ for a list of all expansions.
expand = "items"

# Step 1. Retrieve the order
order_id = 'DEMO-0009104436'
try:
    api_response = order_api.get_order(order_id, expand=expand)
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->get_order: {e}")
    exit()

order = api_response.order

# Step 2. Adjust the refunded quantities
for item in order.items:
    item.quantity_refunded = item.quantity

# Step 3. Refund the order with the modified items
reject_after_refund = False
skip_customer_notification = True
cancel_associated_auto_orders = True  # Does not matter for this sample. The order is not a recurring order.
consider_manual_refund_done_externally = False  # No, I want an actual refund done through my gateway.
reverse_affiliate_transactions = True  # Can't let my affiliates get money on a refunded order. Bad business.

try:
    refund_response = order_api.refund_order(order_id, order, reject_after_refund, skip_customer_notification,
                                             cancel_associated_auto_orders, consider_manual_refund_done_externally,
                                             reverse_affiliate_transactions, include_refunded_amounts=False,
                                             reason=None, expand=expand)
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->refund_order: {e}")
    exit()

refunded_order = refund_response.order

# Examining the refunded order and ensuring everything was refunded correctly
import pprint
print("Refunded Order:")
pprint.pprint(refunded_order)
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
 **auto_order_cancel_reason** | **str**| Reason for auto orders cancellation | [optional]
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
from ultracart import ApiException
from ultracart.apis import OrderApi
from ultracart.models import OrderReplacement, OrderReplacementItem
from samples import api_client


'''
 * The use-case for replacement() is to create another order for a customer to replace the items of the existing
 * order.  For example, a merchant is selling perishable goods and the goods arrive late, spoiled.  replacement()
 * helps to create another order to send more goods to the customer.
 *
 * You MUST supply the items you desire in the replacement order.  This is done with the OrderReplacement.items field.
 * All options are displayed below including whether to charge the customer for this replacement order or not.
'''

# Initialize the Order API with the API key
order_api = OrderApi(api_client())

# Step 1. Replace the order
order_id_to_replace = 'DEMO-0009104436'
replacement_options = OrderReplacement()
replacement_options.original_order_id = order_id_to_replace

# Create replacement items
items = []

item1 = OrderReplacementItem()
item1.merchant_item_id = 'TSHIRT'
item1.quantity = 1
# $item1->setArbitraryUnitCost(9.99);  # Optional: Set cost if needed
items.append(item1)

item2 = OrderReplacementItem()
item2.merchant_item_id = 'BONE'
item2.quantity = 2
items.append(item2)

replacement_options.items = items

# Optional: Set various replacement options
replacement_options.immediate_charge = True
replacement_options.skip_payment = True
replacement_options.free = True
replacement_options.custom_field_1 = 'Whatever'
replacement_options.custom_field_4 = 'More Whatever'
replacement_options.additional_merchant_notes_new_order = 'Replacement order for spoiled ice cream'
replacement_options.additional_merchant_notes_original_order = 'This order was replaced.'

# Step 2. Call the replacement API
try:
    api_response = order_api.replacement(order_id_to_replace, replacement_options)
except ApiException as e:
    print(f"Exception when calling OrderApi->replacement: {e}")
    exit()

# Output the replacement order details
print(f"Replacement Order: {api_response.order_id}")
print(f"Success flag: {api_response.successful}")

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
from ultracart import ApiException
from ultracart.apis import OrderApi
from samples import api_client

# OrderApi.resendReceipt() will resend (email) a receipt to a customer.

# Initialize the Order API with the API key
order_api = OrderApi(api_client())

# The order ID to resend the receipt for
order_id = 'DEMO-0009104436'

# Call to resend the receipt
try:
    api_response = order_api.resend_receipt(order_id)
except ApiException as e:
    print(f"Exception when calling OrderApi->resend_receipt: {e}")
    exit()

# Check if there was an error in the API response
if api_response.error is not None:
    print(f"Developer Message: {api_response.error.developer_message}")
    print(f"User Message: {api_response.error.user_message}")
    print('Order could not be adjusted. See the error log.')
    exit()

# Output the result
if api_response.success:
    print('Receipt was resent.')
else:
    print('Failed to resend receipt.')
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
from ultracart import ApiException
from ultracart.apis import OrderApi
from samples import api_client

# OrderApi.resendShipmentConfirmation() will resend (email) a shipment confirmation to a customer.

# Initialize the Order API with the API key
order_api = OrderApi(api_client())

# The order ID to resend the shipment confirmation for
order_id = 'DEMO-0009104436'

# Call to resend the shipment confirmation
try:
    api_response = order_api.resend_shipment_confirmation(order_id)
except ApiException as e:
    print(f"Exception when calling OrderApi->resend_shipment_confirmation: {e}")
    exit()

# Check if there was an error in the API response
if api_response.error is not None:
    print(f"Developer Message: {api_response.error.developer_message}")
    print(f"User Message: {api_response.error.user_message}")
    print('Order could not be adjusted. See the error log.')
    exit()

# Output the result
if api_response.success:
    print('Shipment confirmation was resent.')
else:
    print('Failed to resend shipment confirmation.')
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

# **unblock_refund_on_order**
> unblock_refund_on_order(order_id)

Remove a refund block on an order

Removes a refund block on an order to prevent a user from performing a refund. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import logging
from ultracart import ApiException
from ultracart.apis import OrderApi
from samples import api_client

# Enable error logging
logging.basicConfig(level=logging.DEBUG)

##
## unblockRefundOnOrder removes an order property that is considered when a refund request is made.
## If the property is present, the refund is denied.  Being an order property allows for querying
## upon it within BigQuery for audit purposes.

# Using the API key to initialize the order API
order_api = OrderApi(api_client())

order_id = 'DEMO-0009105222'

try:
    order_api.unblock_refund_on_order(order_id )
except ApiException as e:
    logging.error(f"Exception when calling OrderApi->unblock_refund_on_order: {e}")
    exit()

print('Metho executed successfully. Returns back 204 No Content')
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to unblock a refund on. |

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
# This is primarily an internal API call.  It is doubtful you would ever need to use it.
# We do not provide an example for this call.
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
from ultracart import ApiException
from ultracart.apis import OrderApi
from samples import api_client

# Initialize the Order API with the API key
order_api = OrderApi(api_client())

# Define the expansion to be used in the API call (related to checkout)
expansion = "checkout"  # see the getOrder sample for expansion discussion

# The order ID to retrieve and update
order_id = 'DEMO-0009104976'

# Step 1: Retrieve the order
try:
    api_response = order_api.get_order(order_id, expansion)
    order = api_response.order
except ApiException as e:
    print(f"Exception when calling OrderApi->get_order: {e}")
    exit()

# Output the current order details
print("<html lang='en'><body><pre>")
print(order)

# TODO: Do some updates to the order here.

# Step 2: Update the order
try:
    api_response = order_api.update_order(order_id, order, expansion)
except ApiException as e:
    print(f"Exception when calling OrderApi->update_order: {e}")
    exit()

# Check for errors in the API response
if api_response.error is not None:
    print(f"Developer Message: {api_response.error.developer_message}")
    print(f"User Message: {api_response.error.user_message}")
    exit()

# Output the updated order details
updated_order = api_response.order
print(updated_order)
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

# **validate_order**
> OrderValidationResponse validate_order(validation_request)

Validate

Validate the order for errors.  Specific checks can be passed to fine tune what is validated. Read and write permissions are required because the validate method may fix obvious address issues automatically which require update permission.This rest call makes use of the built-in translation of rest objects to UltraCart internal objects which also contains a multitude of validation checks that cannot be trapped.  Therefore any time this call is made, you should also trap api exceptions and examine their content because it may contain validation issues.  So check the response object and trap any exceptions. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart import ApiException
from ultracart.apis import OrderApi
from ultracart.models import OrderValidationRequest
from samples import api_client

# /*
#     validateOrder may be used to check for any and all validation errors that may result from an insertOrder
#     or updateOrder call.  Because those method are built on our existing infrastructure, some validation
#     errors may not bubble up to the rest api call and instead be returned as generic "something went wrong" errors.
#     This call will return detail validation issues needing correction.
#
#     Within the ValidationRequest, you may leave the 'checks' array null to check for everything, or pass
#     an array of the specific checks you desire.  Here is a list of the checks:
#
#     "Billing Address Provided"
#     "Billing Destination Restriction"
#     "Billing Phone Numbers Provided"
#     "Billing State Abbreviation Valid"
#     "Billing Validate City State Zip"
#     "Email provided if required"
#     "Gift Message Length"
#     "Item Quantity Valid"
#     "Items Present"
#     "Merchant Specific Item Relationships"
#     "One per customer violations"
#     "Referral Code Provided"
#     "Shipping Address Provided"
#     "Shipping Destination Restriction"
#     "Shipping Method Ignore Invalid"
#     "Shipping Method Provided"
#     "Shipping State Abbreviation Valid"
#     "Shipping Validate City State Zip"
#     "Special Instructions Length"
# */


# Initialize the Order API with the API key
order_api = OrderApi(api_client())

# Define the expansion to be used in the API call (related to checkout)
expansion = "checkout"  # see the getOrder sample for expansion discussion

# The order ID to retrieve
order_id = 'DEMO-0009104976'

# Step 1: Retrieve the order
try:
    api_response = order_api.get_order(order_id, expansion)
    order = api_response.order
except ApiException as e:
    print(f"Exception when calling OrderApi->get_order: {e}")
    exit()

# Output the current order details
print("<html lang='en'><body><pre>")
print(order)

# TODO: Do some updates to the order here.

# Step 2: Validate the order
validation_request = OrderValidationRequest()
validation_request.order = order
validation_request.checks = None  # leaving this null to perform all validations

try:
    api_response = order_api.validate_order(validation_request)
except ApiException as e:
    print(f"Exception when calling OrderApi->validate_order: {e}")
    exit()

# Output validation errors, if any
print('Validation errors:<br>')
if api_response.errors is not None:
    for error in api_response.errors:
        print(error)

# Output validation messages, if any
print('Validation messages:<br>')
if api_response.messages is not None:
    for message in api_response.messages:
        print(message)

print('</pre></body></html>')
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_request** | [**OrderValidationRequest**](OrderValidationRequest.md)| Validation request |

### Return type

[**OrderValidationResponse**](OrderValidationResponse.md)

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

