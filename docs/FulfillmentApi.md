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
import time
import ultracart
from ultracart.api import fulfillment_api
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fulfillment_api.FulfillmentApi(api_client)
    distribution_center_code = "distribution_center_code_example" # str | Distribution center code
    order_ids = [
        "order_ids_example",
    ] # [str] | Orders to acknowledge receipt of (limit 100)

    # example passing only required values which don't have defaults set
    try:
        # Acknowledge receipt of orders.
        api_instance.acknowledge_orders(distribution_center_code, order_ids)
    except ultracart.ApiException as e:
        print("Exception when calling FulfillmentApi->acknowledge_orders: %s\n" % e)
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
> OrdersResponse generate_packing_slip(distribution_center_code, order_id)

Generate a packing slip for this order for the given distribution center.

The packing slip PDF that is returned is base 64 encoded 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import fulfillment_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.orders_response import OrdersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fulfillment_api.FulfillmentApi(api_client)
    distribution_center_code = "distribution_center_code_example" # str | Distribution center code
    order_id = "order_id_example" # str | Order ID

    # example passing only required values which don't have defaults set
    try:
        # Generate a packing slip for this order for the given distribution center.
        api_response = api_instance.generate_packing_slip(distribution_center_code, order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling FulfillmentApi->generate_packing_slip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code |
 **order_id** | **str**| Order ID |

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

# **get_distribution_center_orders**
> OrdersResponse get_distribution_center_orders(distribution_center_code)

Retrieve orders queued up for this distribution center.

Retrieves up to 100 orders that are queued up in this distribution center.  You must acknowledge them before additional new orders will be returned.  There is NO record chunking.  You'll get the same 100 records again and again until you acknowledge orders.  The orders that are returned contain only items for this distribution center and are by default completely expanded with billing, buysafe, channel_partner, checkout, coupons, customer_profile, edi, gift, gift_certificate, internal, items, payment, shipping, summary, taxes. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import fulfillment_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.orders_response import OrdersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fulfillment_api.FulfillmentApi(api_client)
    distribution_center_code = "distribution_center_code_example" # str | Distribution center code

    # example passing only required values which don't have defaults set
    try:
        # Retrieve orders queued up for this distribution center.
        api_response = api_instance.get_distribution_center_orders(distribution_center_code)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling FulfillmentApi->get_distribution_center_orders: %s\n" % e)
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
import time
import ultracart
from ultracart.api import fulfillment_api
from ultracart.model.distribution_centers_response import DistributionCentersResponse
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fulfillment_api.FulfillmentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve distribution centers
        api_response = api_instance.get_distribution_centers()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling FulfillmentApi->get_distribution_centers: %s\n" % e)
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
import time
import ultracart
from ultracart.api import fulfillment_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.fulfillment_shipment import FulfillmentShipment
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fulfillment_api.FulfillmentApi(api_client)
    distribution_center_code = "distribution_center_code_example" # str | Distribution center code
    shipments = [
        FulfillmentShipment(
            fulfillment_fee=3.14,
            order_id="order_id_example",
            package_cost=3.14,
            shipping_cost=3.14,
            tracking_numbers=[
                "tracking_numbers_example",
            ],
        ),
    ] # [FulfillmentShipment] | Orders to mark shipped

    # example passing only required values which don't have defaults set
    try:
        # Mark orders as shipped
        api_instance.ship_orders(distribution_center_code, shipments)
    except ultracart.ApiException as e:
        print("Exception when calling FulfillmentApi->ship_orders: %s\n" % e)
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
import time
import ultracart
from ultracart.api import fulfillment_api
from ultracart.model.fulfillment_inventory import FulfillmentInventory
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fulfillment_api.FulfillmentApi(api_client)
    distribution_center_code = "distribution_center_code_example" # str | Distribution center code
    inventories = [
        FulfillmentInventory(
            item_id="item_id_example",
            quantity=3.14,
        ),
    ] # [FulfillmentInventory] | Inventory updates (limit 500)

    # example passing only required values which don't have defaults set
    try:
        # Update inventory
        api_instance.update_inventory(distribution_center_code, inventories)
    except ultracart.ApiException as e:
        print("Exception when calling FulfillmentApi->update_inventory: %s\n" % e)
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

