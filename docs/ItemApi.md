# ultracart.ItemApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_item**](ItemApi.md#delete_item) | **DELETE** /item/items/{merchant_item_oid} | Delete an item
[**get_item**](ItemApi.md#get_item) | **GET** /item/items/{merchant_item_oid} | Retrieve an item
[**get_item_by_merchant_item_id**](ItemApi.md#get_item_by_merchant_item_id) | **GET** /item/items/merchant_item_id/{merchant_item_id} | Retrieve an item by item id
[**get_items**](ItemApi.md#get_items) | **GET** /item/items | Retrieve items
[**get_pricing_tiers**](ItemApi.md#get_pricing_tiers) | **GET** /item/pricing_tiers | Retrieve pricing tiers
[**insert_item**](ItemApi.md#insert_item) | **POST** /item/items | Create an item
[**update_item**](ItemApi.md#update_item) | **PUT** /item/items/{merchant_item_oid} | Update an item
[**update_items**](ItemApi.md#update_items) | **PUT** /item/items/batch | Update multiple items
[**upload_temporary_multimedia**](ItemApi.md#upload_temporary_multimedia) | **POST** /item/temp_multimedia | Upload an image to the temporary multimedia.


# **delete_item**
> delete_item(merchant_item_oid)

Delete an item

Delete an item on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

merchant_item_oid = 56 # int | The item oid to delete.

try:
    # Delete an item
    api_instance.delete_item(merchant_item_oid)
except ApiException as e:
    print("Exception when calling ItemApi->delete_item: %s\n" % e)
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

# **get_item**
> ItemResponse get_item(merchant_item_oid, expand=expand, placeholders=placeholders)

Retrieve an item

Retrieves a single item using the specified item oid. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

merchant_item_oid = 56 # int | The item oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try:
    # Retrieve an item
    api_response = api_instance.get_item(merchant_item_oid, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item: %s\n" % e)
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

# **get_item_by_merchant_item_id**
> ItemResponse get_item_by_merchant_item_id(merchant_item_id, expand=expand, placeholders=placeholders)

Retrieve an item by item id

Retrieves a single item using the specified item id. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

merchant_item_id = 'merchant_item_id_example' # str | The item id to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try:
    # Retrieve an item by item id
    api_response = api_instance.get_item_by_merchant_item_id(merchant_item_id, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_by_merchant_item_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_id** | **str**| The item id to retrieve. | 
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

# **get_items**
> ItemsResponse get_items(parent_category_id=parent_category_id, parent_category_path=parent_category_path, limit=limit, offset=offset, since=since, sort=sort, expand=expand, placeholders=placeholders)

Retrieve items

Retrieves a group of items from the account.  If no parameters are specified, all items will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

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
    api_response = api_instance.get_items(parent_category_id=parent_category_id, parent_category_path=parent_category_path, limit=limit, offset=offset, since=since, sort=sort, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_items: %s\n" % e)
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

# **get_pricing_tiers**
> PricingTiersResponse get_pricing_tiers(expand=expand)

Retrieve pricing tiers

Retrieves the pricing tiers 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve pricing tiers
    api_response = api_instance.get_pricing_tiers(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_pricing_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**PricingTiersResponse**](PricingTiersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_item**
> ItemResponse insert_item(item, expand=expand, placeholders=placeholders)

Create an item

Create a new item on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

item = ultracart.Item() # Item | Item to create
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try:
    # Create an item
    api_response = api_instance.insert_item(item, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->insert_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**Item**](Item.md)| Item to create | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> ItemResponse update_item(item, merchant_item_oid, expand=expand, placeholders=placeholders)

Update an item

Update a new item on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

item = ultracart.Item() # Item | Item to update
merchant_item_oid = 56 # int | The item oid to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try:
    # Update an item
    api_response = api_instance.update_item(item, merchant_item_oid, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**Item**](Item.md)| Item to update | 
 **merchant_item_oid** | **int**| The item oid to update. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_items**
> ItemsResponse update_items(items_request, expand=expand, placeholders=placeholders, _async=_async)

Update multiple items

Update multiple item on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

items_request = ultracart.ItemsRequest() # ItemsRequest | Items to update (synchronous maximum 20 / asynchronous maximum 100)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)
_async = true # bool | True if the operation should be run async.  No result returned (optional)

try:
    # Update multiple items
    api_response = api_instance.update_items(items_request, expand=expand, placeholders=placeholders, _async=_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->update_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_request** | [**ItemsRequest**](ItemsRequest.md)| Items to update (synchronous maximum 20 / asynchronous maximum 100) | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 
 **_async** | **bool**| True if the operation should be run async.  No result returned | [optional] 

### Return type

[**ItemsResponse**](ItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_temporary_multimedia**
> TempMultimediaResponse upload_temporary_multimedia(file)

Upload an image to the temporary multimedia.

Uploads an image and returns back meta information about the image as well as the identifier needed for the item update. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ItemApi.fromApiKey(simple_key, False, True)

file = '/path/to/file.txt' # file | File to upload

try:
    # Upload an image to the temporary multimedia.
    api_response = api_instance.upload_temporary_multimedia(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->upload_temporary_multimedia: %s\n" % e)
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

