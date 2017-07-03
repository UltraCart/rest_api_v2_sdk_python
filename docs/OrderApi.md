# ultracart.OrderApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OrderApi.md#cancel_order) | **POST** /order/orders/{order_id}/cancel | Cancel an order
[**delete_order**](OrderApi.md#delete_order) | **DELETE** /order/orders/{order_id} | Delete an order
[**get_order**](OrderApi.md#get_order) | **GET** /order/orders/{order_id} | Retrieve an order
[**get_orders**](OrderApi.md#get_orders) | **GET** /order/orders | Retrieve orders
[**resend_receipt**](OrderApi.md#resend_receipt) | **POST** /order/orders/{order_id}/resend_receipt | Resend receipt
[**resend_shipment_confirmation**](OrderApi.md#resend_shipment_confirmation) | **POST** /order/orders/{order_id}/resend_shipment_confirmation | Resend shipment confirmation
[**update_order**](OrderApi.md#update_order) | **PUT** /order/orders/{order_id} | Update an order


# **cancel_order**
> BaseResponse cancel_order(order_id)

Cancel an order

Cancel an order on the UltraCart account.  If the success flag is false, then consult the error message for why it failed. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.OrderApi()
order_id = 'order_id_example' # str | The order id to cancel.

try: 
    # Cancel an order
    api_response = api_instance.cancel_order(order_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrderApi->cancel_order: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order**
> delete_order(order_id)

Delete an order

Delete an order on the UltraCart account. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.OrderApi()
order_id = 'order_id_example' # str | The order id to delete.

try: 
    # Delete an order
    api_instance.delete_order(order_id)
except ApiException as e:
    print "Exception when calling OrderApi->delete_order: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OrderResponse get_order(order_id, expand=expand)

Retrieve an order

Retrieves a single order using the specified order id. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.OrderApi()
order_id = 'order_id_example' # str | The order id to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve an order
    api_response = api_instance.get_order(order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrderApi->get_order: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> OrdersResponse get_orders(order_id=order_id, payment_method=payment_method, company=company, first_name=first_name, last_name=last_name, city=city, state_region=state_region, postal_code=postal_code, country_code=country_code, phone=phone, email=email, cc_email=cc_email, total=total, screen_branding_theme_code=screen_branding_theme_code, storefront_host_name=storefront_host_name, creation_date_begin=creation_date_begin, creation_date_end=creation_date_end, payment_date_begin=payment_date_begin, payment_date_end=payment_date_end, shipment_date_begin=shipment_date_begin, shipment_date_end=shipment_date_end, rma=rma, purchase_order_number=purchase_order_number, item_id=item_id, current_stage=current_stage, channel_partner_code=channel_partner_code, channel_partner_order_id=channel_partner_order_id, limit=limit, offset=offset, sort=sort, expand=expand)

Retrieve orders

Retrieves a group of orders from the account.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the orders returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.OrderApi()
order_id = 'order_id_example' # str | Order Id (optional)
payment_method = 'payment_method_example' # str | Payment Method (optional)
company = 'company_example' # str | Company (optional)
first_name = 'first_name_example' # str | First Name (optional)
last_name = 'last_name_example' # str | Last Name (optional)
city = 'city_example' # str | City (optional)
state_region = 'state_region_example' # str | State/Region (optional)
postal_code = 'postal_code_example' # str | Postal Code (optional)
country_code = 'country_code_example' # str | Country Code (ISO-3166 two letter) (optional)
phone = 'phone_example' # str | Phone (optional)
email = 'email_example' # str | Email (optional)
cc_email = 'cc_email_example' # str | CC Email (optional)
total = 3.4 # float | Total (optional)
screen_branding_theme_code = 'screen_branding_theme_code_example' # str | Screen Branding Theme Code (optional)
storefront_host_name = 'storefront_host_name_example' # str | StoreFront Host Name (optional)
creation_date_begin = 'creation_date_begin_example' # str | Creation Date Begin (optional)
creation_date_end = 'creation_date_end_example' # str | Creation Date End (optional)
payment_date_begin = 'payment_date_begin_example' # str | Payment Date Begin (optional)
payment_date_end = 'payment_date_end_example' # str | Payment Date End (optional)
shipment_date_begin = 'shipment_date_begin_example' # str | Shipment Date Begin (optional)
shipment_date_end = 'shipment_date_end_example' # str | Shipment Date End (optional)
rma = 'rma_example' # str | RMA (optional)
purchase_order_number = 'purchase_order_number_example' # str | Purchase Order Number (optional)
item_id = 'item_id_example' # str | Item Id (optional)
current_stage = 'current_stage_example' # str | Current Stage (optional)
channel_partner_code = 'channel_partner_code_example' # str | Channel Partner Code (optional)
channel_partner_order_id = 'channel_partner_order_id_example' # str | Channel Partner Order ID (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result. (optional)

try: 
    # Retrieve orders
    api_response = api_instance.get_orders(order_id=order_id, payment_method=payment_method, company=company, first_name=first_name, last_name=last_name, city=city, state_region=state_region, postal_code=postal_code, country_code=country_code, phone=phone, email=email, cc_email=cc_email, total=total, screen_branding_theme_code=screen_branding_theme_code, storefront_host_name=storefront_host_name, creation_date_begin=creation_date_begin, creation_date_end=creation_date_end, payment_date_begin=payment_date_begin, payment_date_end=payment_date_end, shipment_date_begin=shipment_date_begin, shipment_date_end=shipment_date_end, rma=rma, purchase_order_number=purchase_order_number, item_id=item_id, current_stage=current_stage, channel_partner_code=channel_partner_code, channel_partner_order_id=channel_partner_order_id, limit=limit, offset=offset, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrderApi->get_orders: %s\n" % e
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
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result. | [optional] 

### Return type

[**OrdersResponse**](OrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_receipt**
> BaseResponse resend_receipt(order_id)

Resend receipt

Resend the receipt for an order on the UltraCart account. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.OrderApi()
order_id = 'order_id_example' # str | The order id to resend the receipt for.

try: 
    # Resend receipt
    api_response = api_instance.resend_receipt(order_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrderApi->resend_receipt: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_shipment_confirmation**
> BaseResponse resend_shipment_confirmation(order_id)

Resend shipment confirmation

Resend shipment confirmation for an order on the UltraCart account. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.OrderApi()
order_id = 'order_id_example' # str | The order id to resend the shipment notification for.

try: 
    # Resend shipment confirmation
    api_response = api_instance.resend_shipment_confirmation(order_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrderApi->resend_shipment_confirmation: %s\n" % e
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> OrderResponse update_order(order, order_id, expand=expand)

Update an order

Update a new order on the UltraCart account. 

### Example 
```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'

# create an instance of the API class
api_instance = ultracart.OrderApi()
order = ultracart.Order() # Order | Order to update
order_id = 'order_id_example' # str | The order id to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Update an order
    api_response = api_instance.update_order(order, order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling OrderApi->update_order: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)| Order to update | 
 **order_id** | **str**| The order id to update. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

