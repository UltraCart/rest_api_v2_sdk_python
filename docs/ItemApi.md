# com_ultracart_admin_v2.ItemApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_order_auto_orders_auto_order_oid_get**](ItemApi.md#auto_order_auto_orders_auto_order_oid_get) | **GET** /auto_order/auto_orders/{auto_order_oid} | Retrieve an auto order
[**auto_order_auto_orders_auto_order_oid_put**](ItemApi.md#auto_order_auto_orders_auto_order_oid_put) | **PUT** /auto_order/auto_orders/{auto_order_oid} | Update an auto order
[**auto_order_auto_orders_get**](ItemApi.md#auto_order_auto_orders_get) | **GET** /auto_order/auto_orders | Retrieve auto orders
[**item_items_get**](ItemApi.md#item_items_get) | **GET** /item/items | Retrieve items
[**item_items_merchant_item_oid_delete**](ItemApi.md#item_items_merchant_item_oid_delete) | **DELETE** /item/items/{merchant_item_oid} | Delete an item
[**item_items_merchant_item_oid_get**](ItemApi.md#item_items_merchant_item_oid_get) | **GET** /item/items/{merchant_item_oid} | Retrieve an item
[**item_items_merchant_item_oid_put**](ItemApi.md#item_items_merchant_item_oid_put) | **PUT** /item/items/{merchant_item_oid} | Update an item
[**item_items_post**](ItemApi.md#item_items_post) | **POST** /item/items | Create an item
[**item_temp_multimedia_post**](ItemApi.md#item_temp_multimedia_post) | **POST** /item/temp_multimedia | Upload an image to the temporary multimedia.


# **auto_order_auto_orders_auto_order_oid_get**
> AutoOrderResponse auto_order_auto_orders_auto_order_oid_get(auto_order_oid, expand=expand)

Retrieve an auto order

Retrieves a single auto order using the specified auto order oid. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
auto_order_oid = 56 # int | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve an auto order
    api_response = api_instance.auto_order_auto_orders_auto_order_oid_get(auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->auto_order_auto_orders_auto_order_oid_get: %s\n" % e
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

# **auto_order_auto_orders_auto_order_oid_put**
> AutoOrderResponse auto_order_auto_orders_auto_order_oid_put(auto_order, auto_order_oid)

Update an auto order

Update an auto order on the UltraCart account. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
auto_order = com_ultracart_admin_v2.AutoOrder() # AutoOrder | Auto order to update
auto_order_oid = 56 # int | The auto order oid to update.

try: 
    # Update an auto order
    api_response = api_instance.auto_order_auto_orders_auto_order_oid_put(auto_order, auto_order_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->auto_order_auto_orders_auto_order_oid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order** | [**AutoOrder**](AutoOrder.md)| Auto order to update | 
 **auto_order_oid** | **int**| The auto order oid to update. | 

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_order_auto_orders_get**
> AutoOrdersResponse auto_order_auto_orders_get(auto_order_code=auto_order_code, original_order_id=original_order_id, first_name=first_name, last_name=last_name, company=company, city=city, state=state, postal_code=postal_code, country_code=country_code, phone=phone, email=email, original_order_date_begin=original_order_date_begin, original_order_date_end=original_order_date_end, next_shipment_date_begin=next_shipment_date_begin, next_shipment_date_end=next_shipment_date_end, card_type=card_type, item_id=item_id, status=status, limit=limit, offset=offset, since=since, sort=sort, expand=expand)

Retrieve auto orders

Retrieves auto orders from the account.  If no parameters are specified, all auto orders will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
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
    api_response = api_instance.auto_order_auto_orders_get(auto_order_code=auto_order_code, original_order_id=original_order_id, first_name=first_name, last_name=last_name, company=company, city=city, state=state, postal_code=postal_code, country_code=country_code, phone=phone, email=email, original_order_date_begin=original_order_date_begin, original_order_date_end=original_order_date_end, next_shipment_date_begin=next_shipment_date_begin, next_shipment_date_end=next_shipment_date_end, card_type=card_type, item_id=item_id, status=status, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->auto_order_auto_orders_get: %s\n" % e
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

# **item_items_get**
> ItemsResponse item_items_get(parent_category_id=parent_category_id, parent_category_path=parent_category_path, limit=limit, offset=offset, since=since, sort=sort, expand=expand, placeholders=placeholders)

Retrieve items

Retrieves a group of items from the account.  If no parameters are specified, all items will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
parent_category_id = 56 # int | The parent category object id to retrieve items for.  Unspecified means all items on the account.  0 = root (optional)
parent_category_path = 'parent_category_path_example' # str | The parent category path to retrieve items for.  Unspecified means all items on the account.  / = root (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 2000) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
since = 'since_example' # str | Fetch items that have been created/modified since this date/time. (optional)
sort = 'sort_example' # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try: 
    # Retrieve items
    api_response = api_instance.item_items_get(parent_category_id=parent_category_id, parent_category_path=parent_category_path, limit=limit, offset=offset, since=since, sort=sort, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->item_items_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_category_id** | **int**| The parent category object id to retrieve items for.  Unspecified means all items on the account.  0 &#x3D; root | [optional] 
 **parent_category_path** | **str**| The parent category path to retrieve items for.  Unspecified means all items on the account.  / &#x3D; root | [optional] 
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 2000) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **since** | **str**| Fetch items that have been created/modified since this date/time. | [optional] 
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 

### Return type

[**ItemsResponse**](ItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_items_merchant_item_oid_delete**
> item_items_merchant_item_oid_delete(merchant_item_oid)

Delete an item

Delete an item on the UltraCart account. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
merchant_item_oid = 56 # int | The item oid to delete.

try: 
    # Delete an item
    api_instance.item_items_merchant_item_oid_delete(merchant_item_oid)
except ApiException as e:
    print "Exception when calling ItemApi->item_items_merchant_item_oid_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid to delete. | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_items_merchant_item_oid_get**
> ItemResponse item_items_merchant_item_oid_get(merchant_item_oid, expand=expand, placeholders=placeholders)

Retrieve an item

Retrieves a single item using the specified item oid. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
merchant_item_oid = 56 # int | The item oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try: 
    # Retrieve an item
    api_response = api_instance.item_items_merchant_item_oid_get(merchant_item_oid, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->item_items_merchant_item_oid_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_items_merchant_item_oid_put**
> ItemResponse item_items_merchant_item_oid_put(item, merchant_item_oid)

Update an item

Update a new item on the UltraCart account. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
item = com_ultracart_admin_v2.Item() # Item | Item to update
merchant_item_oid = 56 # int | The item oid to update.

try: 
    # Update an item
    api_response = api_instance.item_items_merchant_item_oid_put(item, merchant_item_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->item_items_merchant_item_oid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**Item**](Item.md)| Item to update | 
 **merchant_item_oid** | **int**| The item oid to update. | 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_items_post**
> ItemResponse item_items_post(item)

Create an item

Create a new item on the UltraCart account. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
item = com_ultracart_admin_v2.Item() # Item | Item to create

try: 
    # Create an item
    api_response = api_instance.item_items_post(item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->item_items_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**Item**](Item.md)| Item to create | 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_temp_multimedia_post**
> TempMultimediaResponse item_temp_multimedia_post(file)

Upload an image to the temporary multimedia.

Uploads an image and returns back meta information about the image as well as the identifier needed for the item update. 

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
api_instance = com_ultracart_admin_v2.ItemApi()
file = '/path/to/file.txt' # file | File to upload

try: 
    # Upload an image to the temporary multimedia.
    api_response = api_instance.item_temp_multimedia_post(file)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->item_temp_multimedia_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 

### Return type

[**TempMultimediaResponse**](TempMultimediaResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

