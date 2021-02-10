# ultracart.OrderApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_order_total**](OrderApi.md#adjust_order_total) | **POST** /order/orders/{order_id}/adjust_order_total/{desired_total} | Adjusts an order total
[**cancel_order**](OrderApi.md#cancel_order) | **POST** /order/orders/{order_id}/cancel | Cancel an order
[**delete_order**](OrderApi.md#delete_order) | **DELETE** /order/orders/{order_id} | Delete an order
[**format**](OrderApi.md#format) | **POST** /order/orders/{order_id}/format | Format order
[**generate_order_token**](OrderApi.md#generate_order_token) | **GET** /order/orders/token/{order_id} | Generate an order token for a given order id
[**get_accounts_receivable_retry_config**](OrderApi.md#get_accounts_receivable_retry_config) | **GET** /order/accountsReceivableRetryConfig | Retrieve A/R Retry Configuration
[**get_accounts_receivable_retry_stats**](OrderApi.md#get_accounts_receivable_retry_stats) | **GET** /order/accountsReceivableRetryConfig/stats | Retrieve A/R Retry Statistics
[**get_order**](OrderApi.md#get_order) | **GET** /order/orders/{order_id} | Retrieve an order
[**get_order_by_token**](OrderApi.md#get_order_by_token) | **POST** /order/orders/token | Retrieve an order using a token
[**get_orders**](OrderApi.md#get_orders) | **GET** /order/orders | Retrieve orders
[**get_orders_batch**](OrderApi.md#get_orders_batch) | **POST** /order/orders/batch | Retrieve order batch
[**get_orders_by_query**](OrderApi.md#get_orders_by_query) | **POST** /order/orders/query | Retrieve orders by query
[**insert_order**](OrderApi.md#insert_order) | **POST** /order/orders | Insert an order
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

Adjusts an order total.  Adjusts individual items appropriately and considers taxes.  Desired total should be provided in the same currency as the order.  Returns true if successful. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to cancel.
desired_total = 'desired_total_example' # str | The desired total with no formatting. example 123.45

try:
    # Adjusts an order total
    api_response = api_instance.adjust_order_total(order_id, desired_total)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> BaseResponse cancel_order(order_id)

Cancel an order

Cancel an order on the UltraCart account.  If the success flag is false, then consult the error message for why it failed. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to cancel.

try:
    # Cancel an order
    api_response = api_instance.cancel_order(order_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order**
> delete_order(order_id)

Delete an order

Delete an order on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to delete.

try:
    # Delete an order
    api_instance.delete_order(order_id)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **format**
> OrderFormatResponse format(order_id, format_options)

Format order

Format the order for display at text or html 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to format
format_options = ultracart.OrderFormat() # OrderFormat | Format options

try:
    # Format order
    api_response = api_instance.format(order_id, format_options)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_order_token**
> OrderTokenResponse generate_order_token(order_id)

Generate an order token for a given order id

Retrieves a single order token for a given order id.  The token can be used with the getOrderByToken API. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to generate a token for.

try:
    # Generate an order token for a given order id
    api_response = api_instance.generate_order_token(order_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_receivable_retry_config**
> AccountsReceivableRetryConfigResponse get_accounts_receivable_retry_config()

Retrieve A/R Retry Configuration

Retrieve A/R Retry Configuration. This is primarily an internal API call.  It is doubtful you would ever need to use it. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve A/R Retry Configuration
    api_response = api_instance.get_accounts_receivable_retry_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get_accounts_receivable_retry_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountsReceivableRetryConfigResponse**](AccountsReceivableRetryConfigResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_receivable_retry_stats**
> AccountsReceivableRetryStatsResponse get_accounts_receivable_retry_stats(_from=_from, to=to)

Retrieve A/R Retry Statistics

Retrieve A/R Retry Statistics. This is primarily an internal API call.  It is doubtful you would ever need to use it. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

_from = '_from_example' # str |  (optional)
to = 'to_example' # str |  (optional)

try:
    # Retrieve A/R Retry Statistics
    api_response = api_instance.get_accounts_receivable_retry_stats(_from=_from, to=to)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OrderResponse get_order(order_id, expand=expand)

Retrieve an order

Retrieves a single order using the specified order id. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve an order
    api_response = api_instance.get_order(order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_token**
> OrderResponse get_order_by_token(order_by_token_query, expand=expand)

Retrieve an order using a token

Retrieves a single order using the specified order token. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_by_token_query = ultracart.OrderByTokenQuery() # OrderByTokenQuery | Order by token query
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve an order using a token
    api_response = api_instance.get_order_by_token(order_by_token_query, expand=expand)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> OrdersResponse get_orders(order_id=order_id, payment_method=payment_method, company=company, first_name=first_name, last_name=last_name, city=city, state_region=state_region, postal_code=postal_code, country_code=country_code, phone=phone, email=email, cc_email=cc_email, total=total, screen_branding_theme_code=screen_branding_theme_code, storefront_host_name=storefront_host_name, creation_date_begin=creation_date_begin, creation_date_end=creation_date_end, payment_date_begin=payment_date_begin, payment_date_end=payment_date_end, shipment_date_begin=shipment_date_begin, shipment_date_end=shipment_date_end, rma=rma, purchase_order_number=purchase_order_number, item_id=item_id, current_stage=current_stage, channel_partner_code=channel_partner_code, channel_partner_order_id=channel_partner_order_id, customer_profile_oid=customer_profile_oid, refund_date_begin=refund_date_begin, refund_date_end=refund_date_end, limit=limit, offset=offset, sort=sort, expand=expand)

Retrieve orders

Retrieves a group of orders from the account.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the orders returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

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
total = 8.14 # float | Total (optional)
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
customer_profile_oid = 56 # int |  (optional)
refund_date_begin = 'refund_date_begin_example' # str |  (optional)
refund_date_end = 'refund_date_end_example' # str |  (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result. (optional)

try:
    # Retrieve orders
    api_response = api_instance.get_orders(order_id=order_id, payment_method=payment_method, company=company, first_name=first_name, last_name=last_name, city=city, state_region=state_region, postal_code=postal_code, country_code=country_code, phone=phone, email=email, cc_email=cc_email, total=total, screen_branding_theme_code=screen_branding_theme_code, storefront_host_name=storefront_host_name, creation_date_begin=creation_date_begin, creation_date_end=creation_date_end, payment_date_begin=payment_date_begin, payment_date_end=payment_date_end, shipment_date_begin=shipment_date_begin, shipment_date_end=shipment_date_end, rma=rma, purchase_order_number=purchase_order_number, item_id=item_id, current_stage=current_stage, channel_partner_code=channel_partner_code, channel_partner_order_id=channel_partner_order_id, customer_profile_oid=customer_profile_oid, refund_date_begin=refund_date_begin, refund_date_end=refund_date_end, limit=limit, offset=offset, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
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
 **customer_profile_oid** | **int**|  | [optional] 
 **refund_date_begin** | **str**|  | [optional] 
 **refund_date_end** | **str**|  | [optional] 
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

# **get_orders_batch**
> OrdersResponse get_orders_batch(order_batch, expand=expand)

Retrieve order batch

Retrieves a group of orders from the account based on an array of order ids.  If more than 500 order ids are specified, the API call will fail with a bad request error. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_batch = ultracart.OrderQueryBatch() # OrderQueryBatch | Order batch
expand = 'expand_example' # str | The object expansion to perform on the result. (optional)

try:
    # Retrieve order batch
    api_response = api_instance.get_orders_batch(order_batch, expand=expand)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_by_query**
> OrdersResponse get_orders_by_query(order_query, limit=limit, offset=offset, sort=sort, expand=expand)

Retrieve orders by query

Retrieves a group of orders from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the orders returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_query = ultracart.OrderQuery() # OrderQuery | Order query
limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result. (optional)

try:
    # Retrieve orders by query
    api_response = api_instance.get_orders_by_query(order_query, limit=limit, offset=offset, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get_orders_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_query** | [**OrderQuery**](OrderQuery.md)| Order query | 
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

# **insert_order**
> OrderResponse insert_order(order, expand=expand)

Insert an order

Inserts a new order on the UltraCart account.  This is probably NOT the method you want.  This is for channel orders.  For regular orders the customer is entering, use the CheckoutApi.  It has many, many more features, checks, and validations. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order = ultracart.Order() # Order | Order to insert
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Insert an order
    api_response = api_instance.insert_order(order, expand=expand)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_payment**
> OrderProcessPaymentResponse process_payment(order_id, process_payment_request)

Process payment

Process payment on order 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to process payment on
process_payment_request = ultracart.OrderProcessPaymentRequest() # OrderProcessPaymentRequest | Process payment parameters

try:
    # Process payment
    api_response = api_instance.process_payment(order_id, process_payment_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_order**
> OrderResponse refund_order(order, order_id, reject_after_refund=reject_after_refund, skip_customer_notification=skip_customer_notification, auto_order_cancel=auto_order_cancel, manual_refund=manual_refund, reverse_affiliate_transactions=reverse_affiliate_transactions, expand=expand)

Refund an order

Perform a refund operation on an order and then update the order if successful 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order = ultracart.Order() # Order | Order to refund
order_id = 'order_id_example' # str | The order id to refund.
reject_after_refund = false # bool | Reject order after refund (optional) (default to false)
skip_customer_notification = false # bool | Skip customer email notification (optional) (default to false)
auto_order_cancel = false # bool | Cancel associated auto orders (optional) (default to false)
manual_refund = false # bool | Consider a manual refund done externally (optional) (default to false)
reverse_affiliate_transactions = true # bool | Reverse affiliate transactions (optional) (default to true)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Refund an order
    api_response = api_instance.refund_order(order, order_id, reject_after_refund=reject_after_refund, skip_customer_notification=skip_customer_notification, auto_order_cancel=auto_order_cancel, manual_refund=manual_refund, reverse_affiliate_transactions=reverse_affiliate_transactions, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->refund_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)| Order to refund | 
 **order_id** | **str**| The order id to refund. | 
 **reject_after_refund** | **bool**| Reject order after refund | [optional] [default to false]
 **skip_customer_notification** | **bool**| Skip customer email notification | [optional] [default to false]
 **auto_order_cancel** | **bool**| Cancel associated auto orders | [optional] [default to false]
 **manual_refund** | **bool**| Consider a manual refund done externally | [optional] [default to false]
 **reverse_affiliate_transactions** | **bool**| Reverse affiliate transactions | [optional] [default to true]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replacement**
> OrderReplacementResponse replacement(order_id, replacement)

Replacement order

Create a replacement order based upon a previous order 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to generate a replacement for.
replacement = ultracart.OrderReplacement() # OrderReplacement | Replacement order details

try:
    # Replacement order
    api_response = api_instance.replacement(order_id, replacement)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_receipt**
> BaseResponse resend_receipt(order_id)

Resend receipt

Resend the receipt for an order on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to resend the receipt for.

try:
    # Resend receipt
    api_response = api_instance.resend_receipt(order_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_shipment_confirmation**
> BaseResponse resend_shipment_confirmation(order_id)

Resend shipment confirmation

Resend shipment confirmation for an order on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order_id = 'order_id_example' # str | The order id to resend the shipment notification for.

try:
    # Resend shipment confirmation
    api_response = api_instance.resend_shipment_confirmation(order_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_accounts_receivable_retry_config**
> BaseResponse update_accounts_receivable_retry_config(retry_config)

Update A/R Retry Configuration

Update A/R Retry Configuration.  This is primarily an internal API call.  It is doubtful you would ever need to use it. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

retry_config = ultracart.AccountsReceivableRetryConfig() # AccountsReceivableRetryConfig | AccountsReceivableRetryConfig object

try:
    # Update A/R Retry Configuration
    api_response = api_instance.update_accounts_receivable_retry_config(retry_config)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> OrderResponse update_order(order, order_id, expand=expand)

Update an order

Update a new order on the UltraCart account.  This is probably NOT the method you want.  It is rare to update a completed order.  This will not trigger charges, emails, or any other automation. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.OrderApi.fromApiKey(simple_key, False, True)

order = ultracart.Order() # Order | Order to update
order_id = 'order_id_example' # str | The order id to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Update an order
    api_response = api_instance.update_order(order, order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->update_order: %s\n" % e)
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

