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
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.FulfillmentApi.fromApiKey(simple_key, False, True)

distribution_center_code = 'distribution_center_code_example' # str | Distribution center code
order_ids = [ultracart.list[str]()] # list[str] | Orders to acknowledge receipt of (limit 100)

try:
    # Acknowledge receipt of orders.
    api_instance.acknowledge_orders(distribution_center_code, order_ids)
except ApiException as e:
    print("Exception when calling FulfillmentApi->acknowledge_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code | 
 **order_ids** | **list[str]**| Orders to acknowledge receipt of (limit 100) | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_packing_slip**
> OrderPackingSlipResponse generate_packing_slip(distribution_center_code, order_id)

Generate a packing slip for this order for the given distribution center.

The packing slip PDF that is returned is base 64 encoded 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.FulfillmentApi.fromApiKey(simple_key, False, True)

distribution_center_code = 'distribution_center_code_example' # str | Distribution center code
order_id = 'order_id_example' # str | Order ID

try:
    # Generate a packing slip for this order for the given distribution center.
    api_response = api_instance.generate_packing_slip(distribution_center_code, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->generate_packing_slip: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_center_orders**
> OrdersResponse get_distribution_center_orders(distribution_center_code)

Retrieve orders queued up for this distribution center.

Retrieves up to 100 orders that are queued up in this distribution center.  You must acknowledge them before additional new orders will be returned.  There is NO record chunking.  You'll get the same 100 records again and again until you acknowledge orders.  The orders that are returned contain only items for this distribution center and are by default completely expanded with billing, channel_partner, checkout, coupons, customer_profile, edi, gift, gift_certificate, internal, items, payment, shipping, summary, taxes. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.FulfillmentApi.fromApiKey(simple_key, False, True)

distribution_center_code = 'distribution_center_code_example' # str | Distribution center code

try:
    # Retrieve orders queued up for this distribution center.
    api_response = api_instance.get_distribution_center_orders(distribution_center_code)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_centers**
> DistributionCentersResponse get_distribution_centers()

Retrieve distribution centers

Retrieves the distribution centers that this user has access to. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.FulfillmentApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve distribution centers
    api_response = api_instance.get_distribution_centers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->get_distribution_centers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DistributionCentersResponse**](DistributionCentersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ship_orders**
> ship_orders(distribution_center_code, shipments)

Mark orders as shipped

Store the tracking information and mark the order shipped for this distribution center. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.FulfillmentApi.fromApiKey(simple_key, False, True)

distribution_center_code = 'distribution_center_code_example' # str | Distribution center code
shipments = [ultracart.FulfillmentShipment()] # list[FulfillmentShipment] | Orders to mark shipped

try:
    # Mark orders as shipped
    api_instance.ship_orders(distribution_center_code, shipments)
except ApiException as e:
    print("Exception when calling FulfillmentApi->ship_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code | 
 **shipments** | [**list[FulfillmentShipment]**](FulfillmentShipment.md)| Orders to mark shipped | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory**
> update_inventory(distribution_center_code, inventories)

Update inventory

Update the inventory for items associated with this distribution center 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.FulfillmentApi.fromApiKey(simple_key, False, True)

distribution_center_code = 'distribution_center_code_example' # str | Distribution center code
inventories = [ultracart.FulfillmentInventory()] # list[FulfillmentInventory] | Inventory updates (limit 500)

try:
    # Update inventory
    api_instance.update_inventory(distribution_center_code, inventories)
except ApiException as e:
    print("Exception when calling FulfillmentApi->update_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_center_code** | **str**| Distribution center code | 
 **inventories** | [**list[FulfillmentInventory]**](FulfillmentInventory.md)| Inventory updates (limit 500) | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

