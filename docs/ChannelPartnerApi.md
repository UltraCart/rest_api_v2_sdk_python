# ultracart.ChannelPartnerApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order_by_channel_partner_order_id**](ChannelPartnerApi.md#cancel_order_by_channel_partner_order_id) | **DELETE** /channel_partner/cancel/by_channel_partner_order_id/{order_id} | Cancel channel partner order by channel partner order id
[**cancel_order_by_ultra_cart_order_id**](ChannelPartnerApi.md#cancel_order_by_ultra_cart_order_id) | **DELETE** /channel_partner/cancel/by_ultracart_order_id/{order_id} | Cancel channel partner order by UltraCart order id
[**delete_channel_partner_ship_to_preference**](ChannelPartnerApi.md#delete_channel_partner_ship_to_preference) | **DELETE** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences/{channel_partner_ship_to_preference_oid} | Delete a ship to preference record for the channel partner.
[**estimate_shipping_for_channel_partner_order**](ChannelPartnerApi.md#estimate_shipping_for_channel_partner_order) | **POST** /channel_partner/estimate_shipping | Estimate shipping for channel partner order
[**estimate_tax_for_channel_partner_order**](ChannelPartnerApi.md#estimate_tax_for_channel_partner_order) | **POST** /channel_partner/estimate_tax | Estimate tax for channel partner order
[**get_channel_partner_order**](ChannelPartnerApi.md#get_channel_partner_order) | **GET** /channel_partner/orders/{order_id} | Retrieve a channel partner order
[**get_channel_partner_order_by_channel_partner_order_id**](ChannelPartnerApi.md#get_channel_partner_order_by_channel_partner_order_id) | **GET** /channel_partner/orders/by_channel_partner_order_id/{order_id} | Retrieve a channel partner order by the channel partner order id
[**get_channel_partner_reason_codes**](ChannelPartnerApi.md#get_channel_partner_reason_codes) | **GET** /channel_partner/channel_partners/{channel_partner_oid}/reason_codes | Retrieve reject and refund reason codes.
[**get_channel_partner_ship_to_preference**](ChannelPartnerApi.md#get_channel_partner_ship_to_preference) | **GET** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences/{channel_partner_ship_to_preference_oid} | Retrieve the ship to preference associated with the channel partner and the specific id.
[**get_channel_partner_ship_to_preferences**](ChannelPartnerApi.md#get_channel_partner_ship_to_preferences) | **GET** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences | Retrieve the ship to preferences associated with the channel partner.
[**get_channel_partners**](ChannelPartnerApi.md#get_channel_partners) | **GET** /channel_partner/channel_partners | Retrieve the channel partners configured on the account.
[**import_channel_partner_order**](ChannelPartnerApi.md#import_channel_partner_order) | **POST** /channel_partner/import | Insert channel partner order
[**insert_channel_partner_ship_to_preference**](ChannelPartnerApi.md#insert_channel_partner_ship_to_preference) | **POST** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences | Insert a ship to preference record for the channel partner.
[**refund_channel_partner_order**](ChannelPartnerApi.md#refund_channel_partner_order) | **PUT** /channel_partner/orders/{order_id}/refund | Refund a channel partner order
[**update_channel_partner_ship_to_preference**](ChannelPartnerApi.md#update_channel_partner_ship_to_preference) | **PUT** /channel_partner/channel_partners/{channel_partner_oid}/ship_to_preferences/{channel_partner_ship_to_preference_oid} | Update a ship to preference record for the channel partner.


# **cancel_order_by_channel_partner_order_id**
> ChannelPartnerCancelResponse cancel_order_by_channel_partner_order_id(order_id)

Cancel channel partner order by channel partner order id

Cancel channel partner order by channel partner order id 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
"""
cancelOrderByChannelPartnerOrderId takes a channel partner order id, which is the external order id, and attempts
to 'cancel' the order. UltraCart doesn't have a cancel order state, so this needs some explanation of what happens.

Here is the logic of the cancel process:
If the Order stage is [this] then do [that]:
    'Completed Order'       -> Error: "Order has already been completed."
    'Rejected'             -> Error: "Order has already been rejected."
    'Accounts Receivable'  -> Success: order is rejected.
    'Preordered'          -> Success: order is rejected.
    'Quote Sent'          -> Success: order is rejected.
    'Quote Requested'     -> Success: order is rejected.

The remaining stages are Fraud Review and Shipping Department. Orders in these stages have already completed payment.
From this point, complex logic determines if the order has already shipped, or is queued to ship in a way that cannot be canceled.
Here is the logic for those stages, but the gist of it all is this: If you receive any of the errors below, the order has progressed past a point where it can be canceled.

SHIPPING LOGIC:
Iterate through each item and consider it's shipping status:
    Item has already been transmitted to fulfillment center (contains a transmitted dts) -> Error: "The order has already had an item that has been transmitted to the distribution center."
    Does item DC (distribution center) have a transmission mechanism configured?
        YES -> Does the transmission have schedules? If NO -> Error: "The distribution center does not have any schedules so it would be an immediate transmission."
        NO -> Error: "Cant tell if we can cancel because the DC doesnt have a transport configured."

If the above logic completes without errors, the following conditions must be met:
Order has DC activity records. If NO -> Error: "There is no activity in the DC queue when there should be."
There must be at least 5 minutes before the next DC transmission. If NO -> Error: "Activity record is not at least 5 minutes away so we need to bail."

At this point, the order will be canceled with the following activity:
1) Distribution Center activity is cleared
2) The order is refunded. If the order is less than 24 hours old, a void is attempted instead.

Other Possible Errors:
System errors -> "Internal error. Please contact UltraCart Support."
Order does not exist -> "Invalid order ID specified."
During refunding, original transaction could not be found -> "Unable to find original transaction on the order."
During refunding, original transaction was found, but transaction id could not be found -> "Unable to locate original transaction reference number."
During refunding, PayPal was used by no longer configured -> "PayPal is no longer configured on your account to refund against."
Gateway does not support refunds -> [GatewayName] does not support refunds at this time.
"""

from ultracart.apis import ChannelPartnerApi
from ultracart.exceptions import ApiException
from samples import channel_partner_api_client

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

channel_partner_order_id = 'BLAH-BLAH-123'

try:
    cancel_result = channel_partner_api.cancel_order_by_channel_partner_order_id(channel_partner_order_id)
    if not cancel_result.success:
        for error in cancel_result.cancel_errors:
            print(error)

except ApiException as e:
    print(e)  # Prints the exception information
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
"""
Deletes a ChannelPartnerShiptoPreference. These preferences are used by EDI channel partners to automatically
apply return policies and add additional free items to EDI orders based on the EDI code that is present.

Success will return a status code 204 (No content)

Possible Errors:
Attempting to interact with a channel partner other than the one tied to your API Key:
    "Invalid channel_partner_oid specified. Your REST API key may only interact with channel_partner_oid: 12345"
Supply a bad preference oid: "Invalid channel_partner_ship_to_preference_oid specified."
"""

from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

# you will usually get this by calling get_channel_partner_ship_to_preferences()
channel_partner_shipto_preference_oid = 67890
channel_partner_oid = 12345

channel_partner_api.delete_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_shipto_preference_oid)
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

# **delete_channel_partner_ship_to_preference**
> delete_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid)

Delete a ship to preference record for the channel partner.

Delete a ship to preference record for the channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
"""
This is a helper function for call centers to calculate the shipping cost on an order. In a typical flow, the call center
will collect all the shipping information and items being purchased into a ChannelPartnerOrder object.
They will then call this method, passing in the order object. The response will contain the shipping estimates
that the call center can present to the customer. Once the customer selects a particulate estimate,
they can then plug that cost into their call center application and complete the order.

Possible Errors:
Using an API key that is not tied to a channel partner: "This API Key does not have permission to interact with channel partner orders. Please review your Channel Partner configuration."
Order has invalid channel partner code: "Invalid channel partner code"
Order has no items: "null order.items passed." or "order.items array contains a null entry."
Order has no channel partner order id: "order.channelPartnerOrderId must be specified."
Order channel partner order id is a duplicate: "order.channelPartnerOrderId [XYZ] already used."
Channel Partner is inactive: "partner is inactive."
"""

from ultracart.apis import ChannelPartnerApi
from ultracart.models import ChannelPartnerOrder, ChannelPartnerOrderItem, ChannelPartnerOrderItemOption
from samples import channel_partner_api_client
from datetime import datetime, timedelta

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

order = ChannelPartnerOrder()
order.channel_partner_order_id = "widget-1245-abc-1"
order.coupons = ["10OFF"]
# Delivery date will impact shipping estimates if there is a delivery deadline.
# order.delivery_date = (datetime.now() + timedelta(days=14)).isoformat()

item = ChannelPartnerOrderItem()
# item.arbitrary_unit_cost = 9.99
# item.auto_order_last_rebill_dts = (datetime.now() - timedelta(days=30)).isoformat()
# item.auto_order_schedule = "Weekly"
item.merchant_item_id = "shirt"

size_option = ChannelPartnerOrderItemOption()
size_option.name = "Size"
size_option.value = "Small"

color_option = ChannelPartnerOrderItemOption()
color_option.name = "Color"
color_option.value = "Orange"

item.options = [size_option, color_option]
item.quantity = 1
item.upsell = False

order.items = [item]

# order.ship_on_date = (datetime.now() + timedelta(days=7)).isoformat()
order.ship_to_residential = True
order.shipto_address1 = "55 Main Street"
order.shipto_address2 = "Suite 202"
order.shipto_city = "Duluth"
order.shipto_company = "Widgets Inc"
order.shipto_country_code = "US"
order.shipto_day_phone = "6785552323"
order.shipto_evening_phone = "7703334444"
order.shipto_first_name = "Sally"
order.shipto_last_name = "McGonkyDee"
order.shipto_postal_code = "30097"
order.shipto_state_region = "GA"
order.shipto_title = "Director"

api_response = channel_partner_api.estimate_shipping_for_channel_partner_order(order)
estimates = api_response.estimates

# TODO: Apply one estimate shipping method (name) and cost to your channel partner order.

for estimate in estimates:
    print(estimate)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  |
 **channel_partner_ship_to_preference_oid** | **int**|  |

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

# **estimate_shipping_for_channel_partner_order**
> ChannelPartnerEstimateShippingResponse estimate_shipping_for_channel_partner_order(channel_partner_order)

Estimate shipping for channel partner order

Estimate shipping for order from a channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from ultracart.models import ChannelPartnerOrder, ChannelPartnerOrderItem, ChannelPartnerOrderItemOption
from samples import channel_partner_api_client

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

order = ChannelPartnerOrder()
order.channel_partner_order_id = "widget-1245-abc-1"
order.coupons = ["10OFF"]
# DeliveryDate will impact shipping estimates if there is a delivery deadline.
# order.delivery_date = (datetime.now() + timedelta(days=14)).isoformat()

item = ChannelPartnerOrderItem()
# item.arbitrary_unit_cost = 9.99
# item.auto_order_last_rebill_dts = (datetime.now() - timedelta(days=30)).isoformat()
# item.auto_order_schedule = "Weekly"
item.merchant_item_id = "shirt"

size_option = ChannelPartnerOrderItemOption()
size_option.name = "Size"
size_option.value = "Small"

color_option = ChannelPartnerOrderItemOption()
color_option.name = "Color"
color_option.value = "Orange"

item.options = [size_option, color_option]
item.quantity = 1
item.upsell = False

order.items = [item]

# order.ship_on_date = (datetime.now() + timedelta(days=7)).isoformat()
order.ship_to_residential = True
order.shipto_address1 = "55 Main Street"
order.shipto_address2 = "Suite 202"
order.shipto_city = "Duluth"
order.shipto_company = "Widgets Inc"
order.shipto_country_code = "US"
order.shipto_day_phone = "6785552323"
order.shipto_evening_phone = "7703334444"
order.shipto_first_name = "Sally"
order.shipto_last_name = "McGonkyDee"
order.shipto_postal_code = "30097"
order.shipto_state_region = "GA"
order.shipto_title = "Director"

api_response = channel_partner_api.estimate_shipping_for_channel_partner_order(order)
estimates = api_response.estimates

# TODO: Apply one estimate shipping method (name) and cost to your channel partner order.

for estimate in estimates:
    print(estimate)
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
from ultracart.apis import ChannelPartnerApi
from ultracart.models import ChannelPartnerOrder, ChannelPartnerOrderItem, ChannelPartnerOrderItemOption
from samples import channel_partner_api_client

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

order = ChannelPartnerOrder()
order.channel_partner_order_id = "widget-1245-abc-1"
order.coupons = ["10OFF"]
# DeliveryDate will impact shipping estimates if there is a delivery deadline.
# order.delivery_date = (datetime.now() + timedelta(days=14)).isoformat()

item = ChannelPartnerOrderItem()
# item.arbitrary_unit_cost = 9.99
# item.auto_order_last_rebill_dts = (datetime.now() - timedelta(days=30)).isoformat()
# item.auto_order_schedule = "Weekly"
item.merchant_item_id = "shirt"

size_option = ChannelPartnerOrderItemOption()
size_option.name = "Size"
size_option.value = "Small"

color_option = ChannelPartnerOrderItemOption()
color_option.name = "Color"
color_option.value = "Orange"

item.options = [size_option, color_option]
item.quantity = 1
item.upsell = False

order.items = [item]

# order.ship_on_date = (datetime.now() + timedelta(days=7)).isoformat()
order.ship_to_residential = True
order.shipto_address1 = "55 Main Street"
order.shipto_address2 = "Suite 202"
order.shipto_city = "Duluth"
order.shipto_company = "Widgets Inc"
order.shipto_country_code = "US"
order.shipto_day_phone = "6785552323"
ord
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

# **get_channel_partner_order**
> OrderResponse get_channel_partner_order(order_id)

Retrieve a channel partner order

Retrieves a single order using the specified order id.  Only orders belonging to this channel partner may be retrieved. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

# The expansion variable instructs UltraCart how much information to return. The order object is large and
# while it's easily manageable for a single order, when querying thousands of orders, is useful to reduce
# payload size.
# see www.ultracart.com/api/ for all the expansion fields available (this list below may become stale)
"""
Possible Order Expansions:
affiliate           affiliate.ledger                    auto_order
billing             channel_partner                     checkout
coupon              customer_profile                    digital_order
edi                 fraud_score                         gift
gift_certificate    internal                            item
linked_shipment     marketing                          payment
payment.transaction quote                               salesforce
shipping            shipping.tracking_number_details    summary
taxes
"""

# A channel partner will almost always query an order for the purpose of turning around and submitting it to a refund call.
# As such, the expansion most likely needed is listed below.
expand = "item,summary,shipping"

# This order MUST be an order associated with this channel partner or you will receive a 400 Bad Request.
order_id = 'DEMO-0009110366'
api_response = channel_partner_api.get_channel_partner_order(order_id, expand=expand)

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

order = api_response.order

print(order)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See OrderApi.getOrder documentation for examples | [optional]

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

# **get_channel_partner_order_by_channel_partner_order_id**
> OrderResponse get_channel_partner_order_by_channel_partner_order_id(order_id)

Retrieve a channel partner order by the channel partner order id

Retrieves a single order using the channel partner order id, not the ultracart order id.  Only orders belonging to this channel partner may be retrieved. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

# The expansion variable instructs UltraCart how much information to return. The order object is large and
# while it's easily manageable for a single order, when querying thousands of orders, is useful to reduce
# payload size.
# see www.ultracart.com/api/ for all the expansion fields available (this list below may become stale)
"""
Possible Order Expansions:
affiliate           affiliate.ledger                    auto_order
billing             channel_partner                     checkout
coupon              customer_profile                    digital_order
edi                 fraud_score                         gift
gift_certificate    internal                            item
linked_shipment     marketing                           payment
payment.transaction quote                               salesforce
shipping            shipping.tracking_number_details    summary
taxes
"""

# A channel partner will almost always query an order for the purpose of turning around and submitting it to a refund call.
# As such, the expansion most likely needed is listed below.
expand = "item,summary,shipping"

# This order MUST be an order associated with this channel partner or you will receive a 400 Bad Request.
channel_partner_order_id = 'MY-CALL-CENTER-BLAH-BLAH'
api_response = channel_partner_api.get_channel_partner_order_by_channel_partner_order_id(channel_partner_order_id, expand=expand)

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

order = api_response.order

print(order)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The channel partner order id to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See OrderApi.getOrder documentation for examples | [optional]

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

# **get_channel_partner_reason_codes**
> ChanelPartnerReasonCodesResponse get_channel_partner_reason_codes(channel_partner_oid)

Retrieve reject and refund reason codes.

Retrieve reject and refund reason codes. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

api_response = channel_partner_api.get_channel_partner_reason_codes(18413)

print(api_response)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  |

### Return type

[**ChanelPartnerReasonCodesResponse**](ChanelPartnerReasonCodesResponse.md)

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

# **get_channel_partner_ship_to_preference**
> ChannelPartnerShipToPreferenceResponse get_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid)

Retrieve the ship to preference associated with the channel partner and the specific id.

Retrieve the ship to preference associated with the channel partner and the specific id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

"""
Retrieves a shipto preference for a channel partner.
These preferences are used by EDI channel partners to automatically
apply return policies and add additional free items to EDI orders based on the EDI code that is present.

Possible Errors:
Attempting to interact with a channel partner other than the one tied to your API Key:
    "Invalid channel_partner_oid specified.  Your REST API key may only interact with channel_partner_oid: 12345"
Supplying a bad channel partner oid: "Invalid channel_partner_oid specified."
Supplying a bad channel partner shipto preference oid: "Invalid channel_partner_ship_to_preference_oid specified."
"""

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())
channel_partner_oid = 12345
channel_partner_shipto_preference_oid = 67890
api_response = channel_partner_api.get_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_shipto_preference_oid)

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

preference = api_response.ship_to_preference

print(preference)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  |
 **channel_partner_ship_to_preference_oid** | **int**|  |

### Return type

[**ChannelPartnerShipToPreferenceResponse**](ChannelPartnerShipToPreferenceResponse.md)

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

# **get_channel_partner_ship_to_preferences**
> ChannelPartnerShipToPreferencesResponse get_channel_partner_ship_to_preferences(channel_partner_oid)

Retrieve the ship to preferences associated with the channel partner.

Retrieve the ship to preferences associated with the channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

"""
Retrieves all shipto preferences for a channel partner.
These preferences are used by EDI channel partners to automatically
apply return policies and add additional free items to EDI orders based on the EDI code that is present.

Possible Errors:
Attempting to interact with a channel partner other than the one tied to your API Key:
    "Invalid channel_partner_oid specified.  Your REST API key may only interact with channel_partner_oid: 12345"
Supplying a bad channel partner oid: "Invalid channel_partner_oid specified."
"""

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())
channel_partner_oid = 12345
api_response = channel_partner_api.get_channel_partner_ship_to_preferences(channel_partner_oid)

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

preferences = api_response.ship_to_preferences

for preference in preferences:
    print(preference)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  |

### Return type

[**ChannelPartnerShipToPreferencesResponse**](ChannelPartnerShipToPreferencesResponse.md)

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

# **get_channel_partners**
> ChannelPartnersResponse get_channel_partners()

Retrieve the channel partners configured on the account.

Retrieve the channel partners configured on the account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

"""
Retrieves a list of all channel partners configured for this merchant. If the API KEY used is tied to a specific
Channel Partner, then the results will contain only that Channel Partner.
"""

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())
api_response = channel_partner_api.get_channel_partners()

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

channel_partners = api_response.channel_partners

for channel_partner in channel_partners:
    print(channel_partner)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ChannelPartnersResponse**](ChannelPartnersResponse.md)

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

# **import_channel_partner_order**
> ChannelPartnerImportResponse import_channel_partner_order(channel_partner_order)

Insert channel partner order

Insert order from a channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from datetime import datetime
from ultracart.models import (ChannelPartnerOrder, ChannelPartnerOrderItem, 
    ChannelPartnerOrderItemOption, ChannelPartnerOrderTransaction, 
    ChannelPartnerOrderTransactionDetail)
from samples import channel_partner_api_client
from ultracart.apis import ChannelPartnerApi

channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

# ---------------------------------------------
# Example 1 - Order needs payment processing
# ---------------------------------------------

order = ChannelPartnerOrder()

# order.advertising_source = "Friend"  # https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377001/Advertising+Sources
# order.affiliate_id = 856234  # https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377727/Affiliates
# order.affiliate_sub_id = 1234  # https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1376754/Allowing+Affiliates+to+use+Sub-IDs
# order.arbitrary_shipping_handling_total = 9.99
# order.arbitrary_tax = 2.50
# order.arbitrary_tax_rate = 7.0
# order.arbitrary_taxable_subtotal = 69.99

order.associate_with_customer_profile_if_present = True
order.auto_approve_purchase_order = True
order.billto_address1 = "11460 Johns Creek Parkway"
order.billto_address2 = "Suite 101"
order.billto_city = "Duluth"
order.billto_company = "Widgets Inc"
order.billto_country_code = "US"
order.billto_day_phone = "6784153823"
order.billto_evening_phone = "6784154019"
order.billto_first_name = "John"
order.billto_last_name = "Smith"
order.billto_postal_code = "30097"
order.billto_state_region = "GA"
order.billto_title = "Sir"
order.cc_email = "orders@widgets.com"
order.channel_partner_order_id = "widget-1245-abc"
order.consider_recurring = False
order.coupons = ["10OFF", "BUY1GET1"]

# order.credit_card_authorization_amount = 69.99
# order.credit_card_authorization_dts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
# order.credit_card_authorization_number = "1234"

order.credit_card_expiration_month = 5
order.credit_card_expiration_year = 2032
order.credit_card_type = "VISA"
order.custom_field1 = "Whatever"
order.custom_field2 = "You"
order.custom_field3 = "Want"
order.custom_field4 = "Can"
order.custom_field5 = "Go"
order.custom_field6 = "In"
order.custom_field7 = "CustomFields"
order.delivery_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
order.email = "ceo@widgets.com"
order.gift = False

order.gift_email = "sally@aol.com"
order.gift_message = "Congratulations on your promotion!"

order.hosted_fields_card_token = "7C97B0AAA26AB10180B4B29F00380101"
order.hosted_fields_cvv_token = "C684AB4336787F0180B4B51971380101"

# order.insurance_application_id = insurance_application_id  # specialized merchants only
# order.insurance_claim_id = insurance_claim_id  # specialized merchants only

order.ip_address = "34.125.95.217"

# -- Items start ---
item = ChannelPartnerOrderItem()
# item.arbitrary_unit_cost = 9.99
# item.auto_order_last_rebill_dts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
# item.auto_order_schedule = "Weekly"

item.merchant_item_id = "shirt"
item.quantity = 1.0
item.upsell = False

item_option1 = ChannelPartnerOrderItemOption()
item_option1.name = "Size"
item_option1.value = "Small"

item_option2 = ChannelPartnerOrderItemOption()
item_option2.name = "Color"
item_option2.value = "Orange"

item.options = [item_option1, item_option2]

order.items = [item]
# -- Items End ---

order.least_cost_route = True  # Give me the lowest cost shipping
order.least_cost_route_shipping_methods = ["FedEx: Ground", "UPS: Ground", "USPS: Priority"]
order.mailing_list_opt_in = True
order.no_realtime_payment_processing = False
order.payment_method = "Credit Card"
# order.purchase_order_number = "PO-12345"
order.rotating_transaction_gateway_code = "MyStripe"
order.screen_branding_theme_code = "SF1986"
order.ship_on_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
order.ship_to_residential = True
# order.shipping_method = "FedEx: Ground"  # Using LeastCostRoute instead
order.shipto_address1 = "55 Main Street"
order.shipto_address2 = "Suite 202"
order.shipto_city = "Duluth"
order.shipto_company = "Widgets Inc"
order.shipto_country_code = "US"
order.shipto_day_phone = "6785552323"
order.shipto_evening_phone = "7703334444"
order.shipto_first_name = "Sally"
order.shipto_last_name = "McGonkyDee"
order.shipto_postal_code = "30097"
order.shipto_state_region = "GA"
order.shipto_title = "Director"
order.skip_payment_processing = False
order.special_instructions = "Please wrap this in bubble wrap because my FedEx delivery guy is abusive to packages"
order.store_completed = False
order.storefront_host_name = 'store.mysite.com'
order.store_if_payment_declines = False
order.tax_county = "Gwinnett"
order.tax_exempt = False

order_transaction = ChannelPartnerOrderTransaction()
order_transaction.successful = False  # haven't charged card yet
order_transaction.details = []  # haven't charged card yet
order.transaction = order_transaction
order.treat_warnings_as_errors = True

api_response = channel_partner_api.import_channel_partner_order(order)

# ---------------------------------------------
# Example 2 - Order already processed
# ---------------------------------------------

order = ChannelPartnerOrder()

# order.advertising_source = "Friend"
# order.affiliate_id = 856234
# order.affiliate_sub_id = 1234
# order.arbitrary_shipping_handling_total = 9.99
# order.arbitrary_tax = 2.50
# order.arbitrary_tax_rate = 7.0
# order.arbitrary_taxable_subtotal = 69.99

order.associate_with_customer_profile_if_present = True
order.auto_approve_purchase_order = True
order.billto_address1 = "11460 Johns Creek Parkway"
order.billto_address2 = "Suite 101"
order.billto_city = "Duluth"
order.billto_company = "Widgets Inc"
order.billto_country_code = "US"
order.billto_day_phone = "6784153823"
order.billto_evening_phone = "6784154019"
order.billto_first_name = "John"
order.billto_last_name = "Smith"
order.billto_postal_code = "30097"
order.billto_state_region = "GA"
order.billto_title = "Sir"
order.cc_email = "orders@widgets.com"
order.channel_partner_order_id = "widget-1245-abc"
order.consider_recurring = False
order.coupons = ["10OFF", "BUY1GET1"]

order.credit_card_expiration_month = 5
order.credit_card_expiration_year = 2032
order.credit_card_type = "VISA"
order.custom_field1 = "Whatever"
order.custom_field2 = "You"
order.custom_field3 = "Want"
order.custom_field4 = "Can"
order.custom_field5 = "Go"
order.custom_field6 = "In"
order.custom_field7 = "CustomFields"
order.delivery_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
order.email = "ceo@widgets.com"
order.gift = False

order.gift_email = "sally@aol.com"
order.gift_message = "Congratulations on your promotion!"

order.ip_address = "34.125.95.217"

# -- Items start ---
item = ChannelPartnerOrderItem()
item.merchant_item_id = "shirt"
item.quantity = 1.0
item.upsell = False

item_option1 = ChannelPartnerOrderItemOption()
item_option1.name = "Size"
item_option1.value = "Small"

item_option2 = ChannelPartnerOrderItemOption()
item_option2.name = "Color"
item_option2.value = "Orange"

item.options = [item_option1, item_option2]

order.items = [item]
# -- Items End ---

order.mailing_list_opt_in = True
order.no_realtime_payment_processing = True  # payment already collected
order.payment_method = "Credit Card"
order.rotating_transaction_gateway_code = "MyStripe"
order.screen_branding_theme_code = "SF1986"
order.ship_on_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
order.ship_to_residential = True
order.shipping_method = "FedEx: Ground"
order.shipto_address1 = "55 Main Street"
order.shipto_address2 = "Suite 202"
order.shipto_city = "Duluth"
order.shipto_company = "Widgets Inc"
order.shipto_country_code = "US"
order.shipto_day_phone = "6785552323"
order.shipto_evening_phone = "7703334444"
order.shipto_first_name = "Sally"
order.shipto_last_name = "McGonkyDee"
order.shipto_postal_code = "30097"
order.shipto_state_region = "GA"
order.shipto_title = "Director"
order.skip_payment_processing = True  # bypass payment
order.special_instructions = "Please wrap this in bubble wrap because my FedEx delivery guy is abusive to packages"
order.store_completed = True  # old order, just store it
order.storefront_host_name = 'store.mysite.com'
order.store_if_payment_declines = False
order.tax_county = "Gwinnett"
order.tax_exempt = False

order_transaction = ChannelPartnerOrderTransaction()
order_transaction.successful = True

# Create transaction details
td1 = ChannelPartnerOrderTransactionDetail()
td1.name = "AVS Code"
td1.value = "X"

td2 = ChannelPartnerOrderTransactionDetail()
td2.name = "Authorization Code"
td2.value = "123456"

td3 = ChannelPartnerOrderTransactionDetail()
td3.name = "CVV Code"
td3.value = "M"

td4 = ChannelPartnerOrderTransactionDetail()
td4.name = "Response Code"
td4.value = "Authorized"

td5 = ChannelPartnerOrderTransactionDetail()
td5.name = "Reason Code"
td5.value = "1"

td6 = ChannelPartnerOrderTransactionDetail()
td6.name = "Response Subcode"
td6.value = "1"

td7 = ChannelPartnerOrderTransactionDetail()
td7.name = "Transaction ID"
td7.value = "1234567890"

order_transaction.details = [td1, td2, td3, td4, td5, td6, td7]
order.transaction = order_transaction
order.treat_warnings_as_errors = True

api_response = channel_partner_api.import_channel_partner_order(order)
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

# **insert_channel_partner_ship_to_preference**
> ChannelPartnerShipToPreferenceResponse insert_channel_partner_ship_to_preference(channel_partner_oid, ship_to_preference)

Insert a ship to preference record for the channel partner.

Insert a ship to preference record for the channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from ultracart.models import ChannelPartnerShipToPreference
from samples import channel_partner_api_client

# Initialize API
channel_partner_api = ChannelPartnerApi(channel_partner_api_client())
channel_partner_oid = 12345

# Create preference object
preference = ChannelPartnerShipToPreference()
preference.channel_partner_oid = channel_partner_oid
preference.ship_to_edi_code = 'EDI_CODE_HERE'
preference.return_policy = "This is some return policy text that will be printed on the packing slip."
preference.additional_kit_component_item_ids = ['ITEM_ID1', 'ITEM_ID2', 'ITEM_ID3']
preference.description = "This is a merchant friendly description to help me remember what the above setting are."

# Insert the preference
api_response = channel_partner_api.insert_channel_partner_ship_to_preference(channel_partner_oid, preference)

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

inserted_preference = api_response.ship_to_preference
print(inserted_preference)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  |
 **ship_to_preference** | [**ChannelPartnerShipToPreference**](ChannelPartnerShipToPreference.md)| Ship to preference to create |

### Return type

[**ChannelPartnerShipToPreferenceResponse**](ChannelPartnerShipToPreferenceResponse.md)

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

# **refund_channel_partner_order**
> OrderResponse refund_channel_partner_order(order_id, order)

Refund a channel partner order

Perform a refund operation on a channel partner order and then update the order if successful.  All of the object properties ending in _refunded should be the TOTAL amount that should end up being refunded.  UltraCart will calculate the actual amount to refund based upon the prior refunds. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

# Initialize API
channel_partner_api = ChannelPartnerApi(channel_partner_api_client())

# Expansion parameter for order details
expand = "item,summary,shipping"

# Order ID must be associated with this channel partner
order_id = 'DEMO-0009106820'
api_response = channel_partner_api.get_channel_partner_order(order_id, expand=expand)

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

order = api_response.order

# Set refund details
order.refund_reason = 'Damage Product'
order.summary.tax_refunded = order.summary.tax_refunded
order.summary.shipping_handling_refunded = order.summary.shipping_handling_total

# Process refunds for all items
for item in order.items:
    item.refund_reason = 'DifferentItem'
    item.quantity_refunded = item.quantity
    item.total_refunded = item.total_cost_with_discount

# Refund parameters
reject_after_refund = False
skip_customer_notifications = True
auto_order_cancel = False  # Set True to cancel auto orders
manual_refund = False  # Set True if refund processed outside system
reverse_affiliate_transactions = True  # Whether affiliate should get credit
issue_store_credit = False  # True for store credit instead of card refund
auto_order_cancel_reason = None

# Process the refund
api_response = channel_partner_api.refund_channel_partner_order(
    order_id, order, reject_after_refund, skip_customer_notifications,
    auto_order_cancel, manual_refund, reverse_affiliate_transactions,
    issue_store_credit, auto_order_cancel_reason, expand=expand
)

error = api_response.error
updated_order = api_response.order
print(error)
print("\n\n")
print(updated_order)
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
 **expand** | **str**| The object expansion to perform on the result.  See OrderApi.refundOrder documentation for examples | [optional]

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

# **update_channel_partner_ship_to_preference**
> ChannelPartnerShipToPreferenceResponse update_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid, ship_to_preference)

Update a ship to preference record for the channel partner.

Update a ship to preference record for the channel partner. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import ChannelPartnerApi
from samples import channel_partner_api_client

# Initialize API
channel_partner_api = ChannelPartnerApi(channel_partner_api_client())
channel_partner_oid = 12345
channel_partner_ship_to_preference_oid = 67890

# Get existing preference
api_response = channel_partner_api.get_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid)

preference = api_response.ship_to_preference

# Update fields
preference.ship_to_edi_code = 'EDI_CODE_HERE'
preference.return_policy = "This is some return policy text that will be printed on the packing slip."
preference.additional_kit_component_item_ids = ['ITEM_ID1', 'ITEM_ID2', 'ITEM_ID3']
preference.description = "This is a merchant friendly description to help me remember what the above setting are."

# Update the preference
api_response = channel_partner_api.update_channel_partner_ship_to_preference(channel_partner_oid, channel_partner_ship_to_preference_oid, preference)

if api_response.error is not None:
    print(api_response.error.developer_message)
    print(api_response.error.user_message)
    exit()

updated_preference = api_response.ship_to_preference
print(updated_preference)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_partner_oid** | **int**|  |
 **channel_partner_ship_to_preference_oid** | **int**|  |
 **ship_to_preference** | [**ChannelPartnerShipToPreference**](ChannelPartnerShipToPreference.md)| Ship to preference to create |

### Return type

[**ChannelPartnerShipToPreferenceResponse**](ChannelPartnerShipToPreferenceResponse.md)

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

