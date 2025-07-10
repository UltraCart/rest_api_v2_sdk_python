# ultracart.FulfillmentApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_orders**](FulfillmentApi.md#acknowledge_orders) | **PUT** /fulfillment/distribution_centers/{distribution_center_code}/acknowledgements | Acknowledge receipt of orders.
[**generate_packing_slip**](FulfillmentApi.md#generate_packing_slip) | **GET** /fulfillment/distribution_centers/{distribution_center_code}/orders/{order_id} | Generate a packing slip for this order for the given distribution center.
[**get_distribution_center_orders**](FulfillmentApi.md#get_distribution_center_orders) | **GET** /fulfillment/distribution_centers/{distribution_center_code}/orders | Retrieve orders queued up for this distribution center.
[**get_distribution_centers**](FulfillmentApi.md#get_distribution_centers) | **GET** /fulfillment/distribution_centers | Retrieve distribution centers
[**ship_orders**](FulfillmentApi.md#ship_orders) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/shipments | Mark orders as shipped
[**update_inventory**](FulfillmentApi.md#update_inventory) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/inventory | Update inventory


# **acknowledge_orders**
> acknowledge_orders(distribution_center_code, order_ids)

Acknowledge receipt of orders.

Acknowledge receipt of orders so that they are removed from the fulfillment queue.  This method must be called after receiving and order (via webhook) or retrieving (via retrieve orders method). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FulfillmentApi
from samples import api_client
from ultracart.rest import ApiException

"""
acknowledgeOrders informs UltraCart that you (the fulfillment center) have received an order and have queued it for
shipping. This method is NOT used to notify an order has shipped, only that it is going to be shipped at some
point in the future.

This method should be called by a fulfillment center after receiving an order either by 1) getDistributionCenterOrders
or 2) webhook. Webhooks are the most efficient means for receiving orders, but if your fulfillment center lacks
the ability to consume webhooks, polling by getDistributionCenterOrders is an alternate means.

This method is important for notifying UltraCart that a fulfillment center has the action on an order. Until this
call is made, UltraCart will continue to notify a fulfillment center of an order either by 1) subsequent webhooks or
2) continue to include an order in subsequent getDistributionCenterOrders.

You will need the distribution center (DC) code. UltraCart allows for multiple DC and the code is a
unique short string you assign to a DC as an easy mnemonic.

For more information about UltraCart distribution centers, please see:
https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377114/Distribution+Center

If you do not know your DC code, query a list of all DC and print them out:
result = fulfillment_api.get_distribution_centers()
print(result)

A successful call will receive back a status code 204 (No Content).

Possible Errors:
More than 100 order ids provided -> "order_ids can not contain more than 100 records at a time"
"""

fulfillment_api = FulfillmentApi(api_client())

distribution_center_code = 'RAMI'
orders_ids = ['DEMO-12345', 'DEMO-12346', 'DEMO-12347', 'DEMO-12348', 'DEMO-12349']

try:
    # limit is 100 acknowledgements at a time
    fulfillment_api.acknowledge_orders(distribution_center_code, orders_ids)
    print("done")
except ApiException as e:
    # update inventory failed. examine the reason.
    print(f'Exception when calling FulfillmentApi->acknowledge_orders: {e}')
    exit(1)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code |
 **order_ids** | **[str]**| Orders to acknowledge receipt of (limit 100) |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **generate_packing_slip**
> OrderPackingSlipResponse generate_packing_slip(distribution_center_code, order_id)

Generate a packing slip for this order for the given distribution center.

The packing slip PDF that is returned is base 64 encoded 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FulfillmentApi
from samples import api_client
from ultracart.rest import ApiException
import base64

"""
generatePackingSlip accepts a distribution center code and order_id and returns back a base64 encoded byte array pdf.
Both the dc code and order_id are needed because an order may have multiple items shipping via different DCs.

You will need the distribution center (DC) code. UltraCart allows for multiple DC and the code is a
unique short string you assign to a DC as an easy mnemonic.

For more information about UltraCart distribution centers, please see:
https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377114/Distribution+Center

If you do not know your DC code, query a list of all DC and print them out:
result = fulfillment_api.get_distribution_centers()
print(result)
"""

fulfillment_api = FulfillmentApi(api_client())

distribution_center_code = 'RAMI'
orders_id = 'DEMO-12345'

try:
    # limit is 500 inventory updates at a time. batch them if you're going large.
    api_response = fulfillment_api.generate_packing_slip(distribution_center_code, orders_id)
    base64_pdf = api_response.get_pdf_base64()
    decoded_pdf = base64.b64decode(base64_pdf)

    with open('packing_slip.pdf', 'wb') as f:
        f.write(decoded_pdf)

    print("done")
except ApiException as e:
    # update inventory failed. examine the reason.
    print(f'Exception when calling FulfillmentApi->generate_packing_slip: {e}')
    exit(1)
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

# **get_distribution_center_orders**
> OrdersResponse get_distribution_center_orders(distribution_center_code)

Retrieve orders queued up for this distribution center.

Retrieves up to 100 orders that are queued up in this distribution center.  You must acknowledge them before additional new orders will be returned.  There is NO record chunking.  You'll get the same 100 records again and again until you acknowledge orders.  The orders that are returned contain only items for this distribution center and are by default completely expanded with billing, channel_partner, checkout, coupons, customer_profile, edi, gift, gift_certificate, internal, items, payment, shipping, summary, taxes. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FulfillmentApi
from samples import api_client
from ultracart.rest import ApiException

"""
getDistributionCenterOrders accepts a distribution center code and returns back up to 100 orders that need shipping.
There is NO pagination with this method call. Once you receive the orders, you should insert them into your
system, and acknowledge them via the acknowledgeOrders call. After you acknowledge the orders, subsequent calls
to getDistributionCenterOrders will return another batch of 100 orders.

The orders that are returned contain only items for THIS distribution center and are by default completely expanded
with billing, channel_partner, checkout, coupons, customer_profile, edi, gift, gift_certificate, internal,
items, payment, shipping, summary, taxes

You will need the distribution center (DC) code. UltraCart allows for multiple DC and the code is a
unique short string you assign to a DC as an easy mnemonic.

For more information about UltraCart distribution centers, please see:
https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377114/Distribution+Center

If you do not know your DC code, query a list of all DC and print them out:
result = fulfillment_api.get_distribution_centers()
print(result)
"""

fulfillment_api = FulfillmentApi(api_client())

try:
    acknowledged_orders = []
    distribution_center_code = 'RAMI'
    result = fulfillment_api.get_distribution_center_orders(distribution_center_code)
    orders = result.get_orders()

    for order in orders:
        print(order)
        # TODO: do something useful with this order, like adding it to your shipping queue.
        acknowledged_orders.append(order.get_order_id())

    # TODO: once you've securely and completely received it into your system, acknowledge the order.
    fulfillment_api.acknowledge_orders(distribution_center_code, acknowledged_orders)

    # After acknowledging orders, you should call get_distribution_center_orders again until you receive zero orders to ship.

    print("done")
except ApiException as e:
    # update inventory failed. examine the reason.
    print(f'Exception when calling FulfillmentApi->get_distribution_center_orders: {e}')
    exit(1)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code |

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

# **get_distribution_centers**
> DistributionCentersResponse get_distribution_centers()

Retrieve distribution centers

Retrieves the distribution centers that this user has access to. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FulfillmentApi
from samples import api_client
from ultracart.rest import ApiException

"""
This method returns back a list of all distribution centers configured for a merchant.

You will need the distribution center (DC) code for most operations.
UltraCart allows for multiple DC and the code is a unique short string you assign to a DC as an easy mnemonic.
This method call is an easy way to determine what a DC code is for a particular distribution center.

For more information about UltraCart distribution centers, please see:
https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377114/Distribution+Center
"""

fulfillment_api = FulfillmentApi(api_client())

try:
    result = fulfillment_api.get_distribution_centers()
    print(result)

    print("done")
except ApiException as e:
    # update inventory failed. examine the reason.
    print(f'Exception when calling FulfillmentApi->get_distribution_centers: {e}')
    exit(1)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DistributionCentersResponse**](DistributionCentersResponse.md)

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

# **ship_orders**
> ship_orders(distribution_center_code, shipments)

Mark orders as shipped

Store the tracking information and mark the order shipped for this distribution center. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FulfillmentApi
from ultracart.models import FulfillmentShipment
from samples import api_client
from ultracart.rest import ApiException

"""
shipOrders informs UltraCart that you (the fulfillment center) have shipped an order and allows you to provide
UltraCart with tracking information.

You will need the distribution center (DC) code. UltraCart allows for multiple DC and the code is a
unique short string you assign to a DC as an easy mnemonic.

For more information about UltraCart distribution centers, please see:
https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377114/Distribution+Center

If you do not know your DC code, query a list of all DC and print them out:
result = fulfillment_api.get_distribution_centers()
print(result)

A successful call will receive back a status code 204 (No Content).

Possible Errors:
More than 100 order ids provided -> "shipments can not contain more than 100 records at a time"
"""

fulfillment_api = FulfillmentApi(api_client())
distribution_center_code = 'RAMI'

shipment = FulfillmentShipment()
shipment.set_order_id('DEMO-12345')
shipment.set_tracking_numbers(['UPS-1234567890', 'USPS-BLAH-BLAH-BLAH'])  # this order had two boxes
shipment.set_shipping_cost(16.99)  # the actual cost to ship this order
shipment.set_fulfillment_fee(8.99)  # this fulfillment center is kinda pricey
shipment.set_package_cost(11.99)  # 11.99? we use only the finest packaging

shipments = [shipment]  # up to 100 shipments per call

try:
    # limit is 100 shipments updates at a time
    fulfillment_api.ship_orders(distribution_center_code, shipments)
    print("done")
except ApiException as e:
    # update inventory failed. examine the reason.
    print(f'Exception when calling FulfillmentApi->ship_orders: {e}')
    exit(1)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code |
 **shipments** | [**[FulfillmentShipment]**](FulfillmentShipment.md)| Orders to mark shipped |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_inventory**
> update_inventory(distribution_center_code, inventories)

Update inventory

Update the inventory for items associated with this distribution center 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FulfillmentApi
from ultracart.models import FulfillmentInventory
from samples import api_client
from ultracart.rest import ApiException

"""
updateInventory is a simple means of updating UltraCart inventory for one or more items (500 max per call)
You will need the distribution center (DC) code. UltraCart allows for multiple DC and the code is a
unique short string you assign to a DC as an easy mnemonic.

For more information about UltraCart distribution centers, please see:
https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1377114/Distribution+Center

If you do not know your DC code, query a list of all DC and print them out:
result = fulfillment_api.get_distribution_centers()
print(result)

Possible Errors:
More than 500 items provided -> "inventories can not contain more than 500 records at a time"
"""

fulfillment_api = FulfillmentApi(api_client())
distribution_center_code = 'RAMI'

sku = '9780982021361'
quantity = 9
first_inventory = FulfillmentInventory()
first_inventory.set_item_id(sku)
first_inventory.set_quantity(quantity)
inventory_updates = [first_inventory]  # for this example, we're only updating one item.

print(inventory_updates)

try:
    # limit is 500 inventory updates at a time. batch them if you're going large.
    fulfillment_api.update_inventory(distribution_center_code, inventory_updates)
    print("done")
except ApiException as e:
    # update inventory failed. examine the reason.
    print(f'Exception when calling FulfillmentApi->update_inventory: {e}')
    exit(1)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code |
 **inventories** | [**[FulfillmentInventory]**](FulfillmentInventory.md)| Inventory updates (limit 500) |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

