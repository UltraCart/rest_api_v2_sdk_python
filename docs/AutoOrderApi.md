# ultracart.AutoOrderApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consolidate_auto_orders**](AutoOrderApi.md#consolidate_auto_orders) | **PUT** /auto_order/auto_orders/{auto_order_oid}/consolidate | Consolidates multiple auto orders
[**establish_auto_order_by_reference_order_id**](AutoOrderApi.md#establish_auto_order_by_reference_order_id) | **POST** /auto_order/auto_orders/reference_order_id/{reference_order_id} | Establish an auto order by referencing a regular order id
[**get_auto_order**](AutoOrderApi.md#get_auto_order) | **GET** /auto_order/auto_orders/{auto_order_oid} | Retrieve an auto order by oid
[**get_auto_order_by_code**](AutoOrderApi.md#get_auto_order_by_code) | **GET** /auto_order/auto_orders/code/{auto_order_code} | Retrieve an auto order by code
[**get_auto_order_by_reference_order_id**](AutoOrderApi.md#get_auto_order_by_reference_order_id) | **GET** /auto_order/auto_orders/reference_order_id/{reference_order_id} | Retrieve an auto order by order id
[**get_auto_orders**](AutoOrderApi.md#get_auto_orders) | **GET** /auto_order/auto_orders | Retrieve auto orders
[**get_auto_orders_batch**](AutoOrderApi.md#get_auto_orders_batch) | **POST** /auto_order/auto_orders/batch | Retrieve auto order batch
[**get_auto_orders_by_query**](AutoOrderApi.md#get_auto_orders_by_query) | **POST** /auto_order/auto_orders/query | Retrieve auto orders by query
[**pause_auto_order**](AutoOrderApi.md#pause_auto_order) | **PUT** /auto_order/auto_orders/{auto_order_oid}/pause | Pause auto order
[**update_auto_order**](AutoOrderApi.md#update_auto_order) | **PUT** /auto_order/auto_orders/{auto_order_oid} | Update an auto order
[**update_auto_order_item_add_ons**](AutoOrderApi.md#update_auto_order_item_add_ons) | **PUT** /auto_order/auto_orders/{auto_order_oid}/items/{auto_order_item_oid}/add_ons | Update an auto order item add ons
[**update_auto_order_item_properties**](AutoOrderApi.md#update_auto_order_item_properties) | **PUT** /auto_order/auto_orders/{auto_order_oid}/items/{auto_order_item_oid}/properties | Update an auto order item properties
[**update_auto_order_properties**](AutoOrderApi.md#update_auto_order_properties) | **PUT** /auto_order/auto_orders/{auto_order_oid}/properties | Update an auto order properties
[**update_auto_orders_batch**](AutoOrderApi.md#update_auto_orders_batch) | **PUT** /auto_order/auto_orders/batch | Update multiple auto orders


# **consolidate_auto_orders**
> AutoOrderResponse consolidate_auto_orders(auto_order_consolidate, auto_order_oid, expand=expand)

Consolidates multiple auto orders

Consolidates mutliple auto orders on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_consolidate = ultracart.AutoOrderConsolidate() # AutoOrderConsolidate | Auto orders to consolidate
auto_order_oid = 56 # int | The auto order oid to consolidate into.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Consolidates multiple auto orders
    api_response = api_instance.consolidate_auto_orders(auto_order_consolidate, auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->consolidate_auto_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_consolidate** | [**AutoOrderConsolidate**](AutoOrderConsolidate.md)| Auto orders to consolidate | 
 **auto_order_oid** | **int**| The auto order oid to consolidate into. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **establish_auto_order_by_reference_order_id**
> AutoOrderResponse establish_auto_order_by_reference_order_id(reference_order_id, expand=expand)

Establish an auto order by referencing a regular order id

Establish an auto order by referencing a regular order id.  The result will be an auto order without any items.  You should add the items and perform an update call.  Orders must be less than 60 days old and use a credit card payment. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

reference_order_id = 'reference_order_id_example' # str | The order id to attach this auto order to
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Establish an auto order by referencing a regular order id
    api_response = api_instance.establish_auto_order_by_reference_order_id(reference_order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->establish_auto_order_by_reference_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_order_id** | **str**| The order id to attach this auto order to | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_order**
> AutoOrderResponse get_auto_order(auto_order_oid, expand=expand)

Retrieve an auto order by oid

Retrieves a single auto order using the specified auto order oid. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_oid = 56 # int | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve an auto order by oid
    api_response = api_instance.get_auto_order(auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->get_auto_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_oid** | **int**| The auto order oid to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_order_by_code**
> AutoOrderResponse get_auto_order_by_code(auto_order_code, expand=expand)

Retrieve an auto order by code

Retrieves a single auto order using the specified reference (original) order id. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_code = 'auto_order_code_example' # str | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve an auto order by code
    api_response = api_instance.get_auto_order_by_code(auto_order_code, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->get_auto_order_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_code** | **str**| The auto order oid to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_order_by_reference_order_id**
> AutoOrderResponse get_auto_order_by_reference_order_id(reference_order_id, expand=expand)

Retrieve an auto order by order id

Retrieves a single auto order using the specified reference (original) order id. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

reference_order_id = 'reference_order_id_example' # str | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve an auto order by order id
    api_response = api_instance.get_auto_order_by_reference_order_id(reference_order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->get_auto_order_by_reference_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_order_id** | **str**| The auto order oid to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_orders**
> AutoOrdersResponse get_auto_orders(auto_order_code=auto_order_code, original_order_id=original_order_id, first_name=first_name, last_name=last_name, company=company, city=city, state=state, postal_code=postal_code, country_code=country_code, phone=phone, email=email, original_order_date_begin=original_order_date_begin, original_order_date_end=original_order_date_end, next_shipment_date_begin=next_shipment_date_begin, next_shipment_date_end=next_shipment_date_end, card_type=card_type, item_id=item_id, status=status, limit=limit, offset=offset, since=since, sort=sort, expand=expand)

Retrieve auto orders

Retrieves auto orders from the account.  If no parameters are specified, all auto orders will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_code = 'auto_order_code_example' # str | Auto order code (optional)
original_order_id = 'original_order_id_example' # str | Original order id (optional)
first_name = 'first_name_example' # str | First name (optional)
last_name = 'last_name_example' # str | Last name (optional)
company = 'company_example' # str | Company (optional)
city = 'city_example' # str | City (optional)
state = 'state_example' # str | State (optional)
postal_code = 'postal_code_example' # str | Postal code (optional)
country_code = 'country_code_example' # str | Country code (ISO-3166 two letter) (optional)
phone = 'phone_example' # str | Phone (optional)
email = 'email_example' # str | Email (optional)
original_order_date_begin = 'original_order_date_begin_example' # str | Original order date begin (optional)
original_order_date_end = 'original_order_date_end_example' # str | Original order date end (optional)
next_shipment_date_begin = 'next_shipment_date_begin_example' # str | Next shipment date begin (optional)
next_shipment_date_end = 'next_shipment_date_end_example' # str | Next shipment date end (optional)
card_type = 'card_type_example' # str | Card type (optional)
item_id = 'item_id_example' # str | Item ID (optional)
status = 'status_example' # str | Status (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
since = 'since_example' # str | Fetch auto orders that have been created/modified since this date/time. (optional)
sort = 'sort_example' # str | The sort order of the auto orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve auto orders
    api_response = api_instance.get_auto_orders(auto_order_code=auto_order_code, original_order_id=original_order_id, first_name=first_name, last_name=last_name, company=company, city=city, state=state, postal_code=postal_code, country_code=country_code, phone=phone, email=email, original_order_date_begin=original_order_date_begin, original_order_date_end=original_order_date_end, next_shipment_date_begin=next_shipment_date_begin, next_shipment_date_end=next_shipment_date_end, card_type=card_type, item_id=item_id, status=status, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->get_auto_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_code** | **str**| Auto order code | [optional] 
 **original_order_id** | **str**| Original order id | [optional] 
 **first_name** | **str**| First name | [optional] 
 **last_name** | **str**| Last name | [optional] 
 **company** | **str**| Company | [optional] 
 **city** | **str**| City | [optional] 
 **state** | **str**| State | [optional] 
 **postal_code** | **str**| Postal code | [optional] 
 **country_code** | **str**| Country code (ISO-3166 two letter) | [optional] 
 **phone** | **str**| Phone | [optional] 
 **email** | **str**| Email | [optional] 
 **original_order_date_begin** | **str**| Original order date begin | [optional] 
 **original_order_date_end** | **str**| Original order date end | [optional] 
 **next_shipment_date_begin** | **str**| Next shipment date begin | [optional] 
 **next_shipment_date_end** | **str**| Next shipment date end | [optional] 
 **card_type** | **str**| Card type | [optional] 
 **item_id** | **str**| Item ID | [optional] 
 **status** | **str**| Status | [optional] 
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **since** | **str**| Fetch auto orders that have been created/modified since this date/time. | [optional] 
 **sort** | **str**| The sort order of the auto orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrdersResponse**](AutoOrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_orders_batch**
> AutoOrdersResponse get_auto_orders_batch(auto_order_batch, expand=expand)

Retrieve auto order batch

Retrieves a group of auto orders from the account based on an array of auto order oids.  If more than 200 auto order ids are specified, the API call will fail with a bad request error. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_batch = ultracart.AutoOrderQueryBatch() # AutoOrderQueryBatch | Auto order batch
expand = 'expand_example' # str | The object expansion to perform on the result. (optional)

try:
    # Retrieve auto order batch
    api_response = api_instance.get_auto_orders_batch(auto_order_batch, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->get_auto_orders_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_batch** | [**AutoOrderQueryBatch**](AutoOrderQueryBatch.md)| Auto order batch | 
 **expand** | **str**| The object expansion to perform on the result. | [optional] 

### Return type

[**AutoOrdersResponse**](AutoOrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_orders_by_query**
> AutoOrdersResponse get_auto_orders_by_query(auto_order_query, limit=limit, offset=offset, sort=sort, expand=expand)

Retrieve auto orders by query

Retrieves a group of auto orders from the account based on a query object.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_query = ultracart.AutoOrderQuery() # AutoOrderQuery | Auto order query
limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the auto orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result. (optional)

try:
    # Retrieve auto orders by query
    api_response = api_instance.get_auto_orders_by_query(auto_order_query, limit=limit, offset=offset, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->get_auto_orders_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_query** | [**AutoOrderQuery**](AutoOrderQuery.md)| Auto order query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the auto orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result. | [optional] 

### Return type

[**AutoOrdersResponse**](AutoOrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_auto_order**
> AutoOrderResponse pause_auto_order(auto_order, auto_order_oid, expand=expand)

Pause auto order

Completely pause an auto order 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order = ultracart.AutoOrder() # AutoOrder | Auto order to pause
auto_order_oid = 56 # int | The auto order oid to pause.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Pause auto order
    api_response = api_instance.pause_auto_order(auto_order, auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->pause_auto_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order** | [**AutoOrder**](AutoOrder.md)| Auto order to pause | 
 **auto_order_oid** | **int**| The auto order oid to pause. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_order**
> AutoOrderResponse update_auto_order(auto_order, auto_order_oid, validate_original_order=validate_original_order, expand=expand)

Update an auto order

Update an auto order on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order = ultracart.AutoOrder() # AutoOrder | Auto order to update
auto_order_oid = 56 # int | The auto order oid to update.
validate_original_order = 'validate_original_order_example' # str | Validate original order before updating (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Update an auto order
    api_response = api_instance.update_auto_order(auto_order, auto_order_oid, validate_original_order=validate_original_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->update_auto_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order** | [**AutoOrder**](AutoOrder.md)| Auto order to update | 
 **auto_order_oid** | **int**| The auto order oid to update. | 
 **validate_original_order** | **str**| Validate original order before updating | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_order_item_add_ons**
> AutoOrderResponse update_auto_order_item_add_ons(auto_order_add_ons_update_request, auto_order_oid, auto_order_item_oid, expand=expand)

Update an auto order item add ons

Update an auto order item add ons.  Returns the auto order based upon expansion 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_add_ons_update_request = ultracart.AutoOrderAddonItemsUpdateRequest() # AutoOrderAddonItemsUpdateRequest | Auto order add ons update request
auto_order_oid = 56 # int | The auto order oid to update.
auto_order_item_oid = 56 # int | The auto order item oid to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Update an auto order item add ons
    api_response = api_instance.update_auto_order_item_add_ons(auto_order_add_ons_update_request, auto_order_oid, auto_order_item_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->update_auto_order_item_add_ons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_add_ons_update_request** | [**AutoOrderAddonItemsUpdateRequest**](AutoOrderAddonItemsUpdateRequest.md)| Auto order add ons update request | 
 **auto_order_oid** | **int**| The auto order oid to update. | 
 **auto_order_item_oid** | **int**| The auto order item oid to update. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_order_item_properties**
> AutoOrderResponse update_auto_order_item_properties(auto_order_properties_update_request, auto_order_oid, auto_order_item_oid, expand=expand)

Update an auto order item properties

Update an auto order item properties.  Returns the auto order based upon expansion 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_properties_update_request = ultracart.AutoOrderPropertiesUpdateRequest() # AutoOrderPropertiesUpdateRequest | Auto order property update request
auto_order_oid = 56 # int | The auto order oid to update.
auto_order_item_oid = 56 # int | The auto order item oid to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Update an auto order item properties
    api_response = api_instance.update_auto_order_item_properties(auto_order_properties_update_request, auto_order_oid, auto_order_item_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->update_auto_order_item_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_properties_update_request** | [**AutoOrderPropertiesUpdateRequest**](AutoOrderPropertiesUpdateRequest.md)| Auto order property update request | 
 **auto_order_oid** | **int**| The auto order oid to update. | 
 **auto_order_item_oid** | **int**| The auto order item oid to update. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_order_properties**
> AutoOrderResponse update_auto_order_properties(auto_order_properties_update_request, auto_order_oid, expand=expand)

Update an auto order properties

Update an auto order properties.  Returns the auto order based upon expansion 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_order_properties_update_request = ultracart.AutoOrderPropertiesUpdateRequest() # AutoOrderPropertiesUpdateRequest | Auto order property update request
auto_order_oid = 56 # int | The auto order oid to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Update an auto order properties
    api_response = api_instance.update_auto_order_properties(auto_order_properties_update_request, auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->update_auto_order_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_properties_update_request** | [**AutoOrderPropertiesUpdateRequest**](AutoOrderPropertiesUpdateRequest.md)| Auto order property update request | 
 **auto_order_oid** | **int**| The auto order oid to update. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_orders_batch**
> AutoOrdersResponse update_auto_orders_batch(auto_orders_request, expand=expand, placeholders=placeholders, _async=_async)

Update multiple auto orders

Update multiple auto orders on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.AutoOrderApi.fromApiKey(simple_key, False, True)

auto_orders_request = ultracart.AutoOrdersRequest() # AutoOrdersRequest | Auto orders to update (synchronous maximum 20 / asynchronous maximum 100)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)
_async = true # bool | True if the operation should be run async.  No result returned (optional)

try:
    # Update multiple auto orders
    api_response = api_instance.update_auto_orders_batch(auto_orders_request, expand=expand, placeholders=placeholders, _async=_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoOrderApi->update_auto_orders_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_orders_request** | [**AutoOrdersRequest**](AutoOrdersRequest.md)| Auto orders to update (synchronous maximum 20 / asynchronous maximum 100) | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 
 **_async** | **bool**| True if the operation should be run async.  No result returned | [optional] 

### Return type

[**AutoOrdersResponse**](AutoOrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

