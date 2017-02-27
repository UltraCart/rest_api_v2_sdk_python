# com_ultracart_admin_v2.FulfillmentApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fulfillment_distribution_centers_distribution_center_code_acknowledgements_put**](FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_acknowledgements_put) | **PUT** /fulfillment/distribution_centers/{distribution_center_code}/acknowledgements | Acknowledge receipt of orders.
[**fulfillment_distribution_centers_distribution_center_code_inventory_post**](FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_inventory_post) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/inventory | Update inventory
[**fulfillment_distribution_centers_distribution_center_code_orders_get**](FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_orders_get) | **GET** /fulfillment/distribution_centers/{distribution_center_code}/orders | Retrieve orders queued up for this distribution center.
[**fulfillment_distribution_centers_distribution_center_code_shipments_post**](FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_shipments_post) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/shipments | Mark orders as shipped
[**fulfillment_distribution_centers_get**](FulfillmentApi.md#fulfillment_distribution_centers_get) | **GET** /fulfillment/distribution_centers | Retrieve distribution centers


# **fulfillment_distribution_centers_distribution_center_code_acknowledgements_put**
> fulfillment_distribution_centers_distribution_center_code_acknowledgements_put(distribution_center_code, order_ids)

Acknowledge receipt of orders.

Acknowledge receipt of orders so that they are removed from the fulfillment queue.  This method must be called after receiving and order (via webhook) or retrieving (via retrieve orders method). 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.FulfillmentApi()
distribution_center_code = 'distribution_center_code_example' # str | Distribution center code
order_ids = [com_ultracart_admin_v2.list[str]()] # list[str] | Orders to acknowledge receipt of (limit 100)

try: 
    # Acknowledge receipt of orders.
    api_instance.fulfillment_distribution_centers_distribution_center_code_acknowledgements_put(distribution_center_code, order_ids)
except ApiException as e:
    print "Exception when calling FulfillmentApi->fulfillment_distribution_centers_distribution_center_code_acknowledgements_put: %s\n" % e
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

# **fulfillment_distribution_centers_distribution_center_code_inventory_post**
> fulfillment_distribution_centers_distribution_center_code_inventory_post(distribution_center_code, inventories)

Update inventory

Update the inventory for items associated with this distribution center 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.FulfillmentApi()
distribution_center_code = 'distribution_center_code_example' # str | Distribution center code
inventories = [com_ultracart_admin_v2.FulfillmentInventory()] # list[FulfillmentInventory] | Inventory updates (limit 500)

try: 
    # Update inventory
    api_instance.fulfillment_distribution_centers_distribution_center_code_inventory_post(distribution_center_code, inventories)
except ApiException as e:
    print "Exception when calling FulfillmentApi->fulfillment_distribution_centers_distribution_center_code_inventory_post: %s\n" % e
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

# **fulfillment_distribution_centers_distribution_center_code_orders_get**
> OrdersResponse fulfillment_distribution_centers_distribution_center_code_orders_get(distribution_center_code)

Retrieve orders queued up for this distribution center.

Retrieves up to 100 orders that are queued up in this distribution center.  You must acknowledge them before additional new orders will be returned.  The orders that are returned contain only items for this distribution center and are expanded with billing, buysafe, channel_partner, checkout, coupons, customer_profile, edi, gift, gift_certificate, internal, items, payment, shipping, summary, taxes. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.FulfillmentApi()
distribution_center_code = 'distribution_center_code_example' # str | Distribution center code

try: 
    # Retrieve orders queued up for this distribution center.
    api_response = api_instance.fulfillment_distribution_centers_distribution_center_code_orders_get(distribution_center_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FulfillmentApi->fulfillment_distribution_centers_distribution_center_code_orders_get: %s\n" % e
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

# **fulfillment_distribution_centers_distribution_center_code_shipments_post**
> fulfillment_distribution_centers_distribution_center_code_shipments_post(distribution_center_code, shipments)

Mark orders as shipped

Store the tracking information and mark the order shipped for this distribution center. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.FulfillmentApi()
distribution_center_code = 'distribution_center_code_example' # str | Distribution center code
shipments = [com_ultracart_admin_v2.FulfillmentShipment()] # list[FulfillmentShipment] | Orders to mark shipped

try: 
    # Mark orders as shipped
    api_instance.fulfillment_distribution_centers_distribution_center_code_shipments_post(distribution_center_code, shipments)
except ApiException as e:
    print "Exception when calling FulfillmentApi->fulfillment_distribution_centers_distribution_center_code_shipments_post: %s\n" % e
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

# **fulfillment_distribution_centers_get**
> DistributionCentersResponse fulfillment_distribution_centers_get()

Retrieve distribution centers

Retrieves the distribution centers that this user has access to. 

### Example 
```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = com_ultracart_admin_v2.FulfillmentApi()

try: 
    # Retrieve distribution centers
    api_response = api_instance.fulfillment_distribution_centers_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FulfillmentApi->fulfillment_distribution_centers_get: %s\n" % e
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

