# ultracart.AutoorderApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auto_order**](AutoorderApi.md#get_auto_order) | **GET** /auto_order/auto_orders/{auto_order_oid} | Retrieve an auto order
[**get_auto_order_by_code**](AutoorderApi.md#get_auto_order_by_code) | **GET** /auto_order/auto_orders/code/{auto_order_code} | Retrieve an auto order
[**get_auto_order_by_reference_order_id**](AutoorderApi.md#get_auto_order_by_reference_order_id) | **GET** /auto_order/auto_orders/reference_order_id/{reference_order_id} | Retrieve an auto order
[**get_auto_orders**](AutoorderApi.md#get_auto_orders) | **GET** /auto_order/auto_orders | Retrieve auto orders
[**update_auto_order**](AutoorderApi.md#update_auto_order) | **PUT** /auto_order/auto_orders/{auto_order_oid} | Update an auto order


# **get_auto_order**
> AutoOrderResponse get_auto_order(auto_order_oid, expand=expand)

Retrieve an auto order

Retrieves a single auto order using the specified auto order oid. 

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
api_instance = ultracart.AutoorderApi()
auto_order_oid = 56 # int | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve an auto order
    api_response = api_instance.get_auto_order(auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AutoorderApi->get_auto_order: %s\n" % e
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

Retrieve an auto order

Retrieves a single auto order using the specified reference (original) order id. 

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
api_instance = ultracart.AutoorderApi()
auto_order_code = 'auto_order_code_example' # str | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve an auto order
    api_response = api_instance.get_auto_order_by_code(auto_order_code, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AutoorderApi->get_auto_order_by_code: %s\n" % e
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

Retrieve an auto order

Retrieves a single auto order using the specified reference (original) order id. 

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
api_instance = ultracart.AutoorderApi()
reference_order_id = 'reference_order_id_example' # str | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve an auto order
    api_response = api_instance.get_auto_order_by_reference_order_id(reference_order_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AutoorderApi->get_auto_order_by_reference_order_id: %s\n" % e
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
api_instance = ultracart.AutoorderApi()
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
sort = 'sort_example' # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve auto orders
    api_response = api_instance.get_auto_orders(auto_order_code=auto_order_code, original_order_id=original_order_id, first_name=first_name, last_name=last_name, company=company, city=city, state=state, postal_code=postal_code, country_code=country_code, phone=phone, email=email, original_order_date_begin=original_order_date_begin, original_order_date_end=original_order_date_end, next_shipment_date_begin=next_shipment_date_begin, next_shipment_date_end=next_shipment_date_end, card_type=card_type, item_id=item_id, status=status, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AutoorderApi->get_auto_orders: %s\n" % e
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
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**AutoOrdersResponse**](AutoOrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_order**
> AutoOrderResponse update_auto_order(auto_order, auto_order_oid, expand=expand)

Update an auto order

Update an auto order on the UltraCart account. 

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
api_instance = ultracart.AutoorderApi()
auto_order = ultracart.AutoOrder() # AutoOrder | Auto order to update
auto_order_oid = 56 # int | The auto order oid to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Update an auto order
    api_response = api_instance.update_auto_order(auto_order, auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AutoorderApi->update_auto_order: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order** | [**AutoOrder**](AutoOrder.md)| Auto order to update | 
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

