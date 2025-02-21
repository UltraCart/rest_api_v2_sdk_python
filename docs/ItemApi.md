# ultracart.ItemApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_digital_item**](ItemApi.md#delete_digital_item) | **DELETE** /item/digital_library/{digital_item_oid} | Delete a digital item, which is a file within the digital library, not an actual merchant item
[**delete_item**](ItemApi.md#delete_item) | **DELETE** /item/items/{merchant_item_oid} | Delete an item
[**delete_review**](ItemApi.md#delete_review) | **DELETE** /item/items/{merchant_item_oid}/reviews/{review_oid} | Delete a review
[**get_digital_item**](ItemApi.md#get_digital_item) | **GET** /item/digital_library/{digital_item_oid} | Retrieve a digital item from the digital library, which are digital files that may be attached to normal items
[**get_digital_items**](ItemApi.md#get_digital_items) | **GET** /item/digital_library | Retrieve digital items from the digital library which are digital files that may be attached to normal items
[**get_digital_items_by_external_id**](ItemApi.md#get_digital_items_by_external_id) | **GET** /item/digital_library/by_external/{external_id} | Retrieves digital items from the digital library (which are digital files that may be attached to normal items) that having a matching external id
[**get_inventory_snapshot**](ItemApi.md#get_inventory_snapshot) | **GET** /item/items/inventory_snapshot | Retrieve a list of item inventories.  This method may be called once every 15 minutes.  More than that will result in a 429 response.
[**get_item**](ItemApi.md#get_item) | **GET** /item/items/{merchant_item_oid} | Retrieve an item
[**get_item_by_merchant_item_id**](ItemApi.md#get_item_by_merchant_item_id) | **GET** /item/items/merchant_item_id/{merchant_item_id} | Retrieve an item by item id
[**get_items**](ItemApi.md#get_items) | **GET** /item/items | Retrieve items
[**get_pricing_tiers**](ItemApi.md#get_pricing_tiers) | **GET** /item/pricing_tiers | Retrieve pricing tiers
[**get_review**](ItemApi.md#get_review) | **GET** /item/items/{merchant_item_oid}/reviews/{review_oid} | Get a review
[**get_reviews**](ItemApi.md#get_reviews) | **GET** /item/items/{merchant_item_oid}/reviews | Get reviews for an item
[**get_unassociated_digital_items**](ItemApi.md#get_unassociated_digital_items) | **GET** /item/digital_library/unassociated | Retrieve digital items from the digital library (which are digital files that may be attached to normal items) not yet associated with actual items
[**insert_digital_item**](ItemApi.md#insert_digital_item) | **POST** /item/digital_library | Create a file within the digital library
[**insert_item**](ItemApi.md#insert_item) | **POST** /item/items | Create an item
[**insert_review**](ItemApi.md#insert_review) | **POST** /item/items/{merchant_item_oid}/reviews | Insert a review
[**insert_update_item_content_attribute**](ItemApi.md#insert_update_item_content_attribute) | **POST** /item/items/{merchant_item_oid}/content/attributes | Upsert an item content attribute
[**update_digital_item**](ItemApi.md#update_digital_item) | **PUT** /item/digital_library/{digital_item_oid} | Updates a file within the digital library
[**update_item**](ItemApi.md#update_item) | **PUT** /item/items/{merchant_item_oid} | Update an item
[**update_items**](ItemApi.md#update_items) | **PUT** /item/items/batch | Update multiple items
[**update_review**](ItemApi.md#update_review) | **PUT** /item/items/{merchant_item_oid}/reviews/{review_oid} | Update a review
[**upload_temporary_multimedia**](ItemApi.md#upload_temporary_multimedia) | **POST** /item/temp_multimedia | Upload an image to the temporary multimedia.


# **delete_digital_item**
> delete_digital_item(digital_item_oid)

Delete a digital item, which is a file within the digital library, not an actual merchant item

Delete a digital item on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    digital_item_oid = 1 # int | The digital item oid to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a digital item, which is a file within the digital library, not an actual merchant item
        api_instance.delete_digital_item(digital_item_oid)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->delete_digital_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_item_oid** | **int**| The digital item oid to delete. |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_item**
> delete_item(merchant_item_oid)

Delete an item

Delete an item on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_item_oid = 1 # int | The item oid to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete an item
        api_instance.delete_item(merchant_item_oid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
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

# **delete_review**
> delete_review(review_oid, merchant_item_oid)

Delete a review

Delete an item review. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    review_oid = 1 # int | The review oid to delete.
    merchant_item_oid = 1 # int | The item oid the review is associated with.

    # example passing only required values which don't have defaults set
    try:
        # Delete a review
        api_instance.delete_review(review_oid, merchant_item_oid)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->delete_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_oid** | **int**| The review oid to delete. |
 **merchant_item_oid** | **int**| The item oid the review is associated with. |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_digital_item**
> ItemDigitalItemResponse get_digital_item(digital_item_oid)

Retrieve a digital item from the digital library, which are digital files that may be attached to normal items

Retrieves a digital item (file information) from the account.  Be aware that these are not normal items that can be added to a shopping cart. Rather, they are digital files that may be associated with normal items. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_digital_item_response import ItemDigitalItemResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    digital_item_oid = 1 # int | The digital item oid to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a digital item from the digital library, which are digital files that may be attached to normal items
        api_response = api_instance.get_digital_item(digital_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_digital_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_item_oid** | **int**| The digital item oid to retrieve. |

### Return type

[**ItemDigitalItemResponse**](ItemDigitalItemResponse.md)

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

# **get_digital_items**
> ItemDigitalItemsResponse get_digital_items()

Retrieve digital items from the digital library which are digital files that may be attached to normal items

Retrieves a group of digital items (file information) from the account.  If no parameters are specified, all digital items will be returned.  Be aware that these are not normal items that can be added to a shopping cart. Rather, they are digital files that may be associated with normal items.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_digital_items_response import ItemDigitalItemsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 2000) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    since = "_since_example" # str | Fetch items that have been created/modified since this date/time. (optional)
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve digital items from the digital library which are digital files that may be attached to normal items
        api_response = api_instance.get_digital_items(limit=limit, offset=offset, since=since, sort=sort, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_digital_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 2000) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch items that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**ItemDigitalItemsResponse**](ItemDigitalItemsResponse.md)

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

# **get_digital_items_by_external_id**
> ItemDigitalItemsResponse get_digital_items_by_external_id(external_id)

Retrieves digital items from the digital library (which are digital files that may be attached to normal items) that having a matching external id

Retrieves digital items from the digital library (which are digital files that may be attached to normal items) that having a matching external id.  Be aware that these are not normal items that can be added to a shopping cart. Rather, they are digital files that may be associated with normal items. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_digital_items_response import ItemDigitalItemsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    external_id = "external_id_example" # str | The external id to match against.

    # example passing only required values which don't have defaults set
    try:
        # Retrieves digital items from the digital library (which are digital files that may be attached to normal items) that having a matching external id
        api_response = api_instance.get_digital_items_by_external_id(external_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_digital_items_by_external_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| The external id to match against. |

### Return type

[**ItemDigitalItemsResponse**](ItemDigitalItemsResponse.md)

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

# **get_inventory_snapshot**
> ItemInventorySnapshotResponse get_inventory_snapshot()

Retrieve a list of item inventories.  This method may be called once every 15 minutes.  More than that will result in a 429 response.

Retrieve a list of item inventories.  This method may be called once every 15 minutes.  More than that will result in a 429 response. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_inventory_snapshot_response import ItemInventorySnapshotResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of item inventories.  This method may be called once every 15 minutes.  More than that will result in a 429 response.
        api_response = api_instance.get_inventory_snapshot()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_inventory_snapshot: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ItemInventorySnapshotResponse**](ItemInventorySnapshotResponse.md)

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

# **get_item**
> ItemResponse get_item(merchant_item_oid)

Retrieve an item

Retrieves a single item using the specified item oid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_response import ItemResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_item_oid = 1 # int | The item oid to retrieve.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an item
        api_response = api_instance.get_item(merchant_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an item
        api_response = api_instance.get_item(merchant_item_oid, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_item_by_merchant_item_id**
> ItemResponse get_item_by_merchant_item_id(merchant_item_id)

Retrieve an item by item id

Retrieves a single item using the specified item id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_response import ItemResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_item_id = "merchant_item_id_example" # str | The item id to retrieve.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an item by item id
        api_response = api_instance.get_item_by_merchant_item_id(merchant_item_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_item_by_merchant_item_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an item by item id
        api_response = api_instance.get_item_by_merchant_item_id(merchant_item_id, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_items**
> ItemsResponse get_items()

Retrieve items

Retrieves a group of items from the account.  If no parameters are specified, all items will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.items_response import ItemsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    parent_category_id = 1 # int | The parent category object id to retrieve items for.  Unspecified means all items on the account.  0 = root (optional)
    parent_category_path = "parent_category_path_example" # str | The parent category path to retrieve items for.  Unspecified means all items on the account.  / = root (optional)
    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 2000) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    since = "_since_example" # str | Fetch items that have been created/modified since this date/time. (optional)
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve items
        api_response = api_instance.get_items(parent_category_id=parent_category_id, parent_category_path=parent_category_path, limit=limit, offset=offset, since=since, sort=sort, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_category_id** | **int**| The parent category object id to retrieve items for.  Unspecified means all items on the account.  0 &#x3D; root | [optional]
 **parent_category_path** | **str**| The parent category path to retrieve items for.  Unspecified means all items on the account.  / &#x3D; root | [optional]
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 2000) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch items that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**ItemsResponse**](ItemsResponse.md)

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

# **get_pricing_tiers**
> PricingTiersResponse get_pricing_tiers()

Retrieve pricing tiers

Retrieves the pricing tiers 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.pricing_tiers_response import PricingTiersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve pricing tiers
        api_response = api_instance.get_pricing_tiers(expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_review**
> ItemReviewResponse get_review(review_oid, merchant_item_oid)

Get a review

Retrieve an item review. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_review_response import ItemReviewResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    review_oid = 1 # int | The review oid to retrieve.
    merchant_item_oid = 1 # int | The item oid the review is associated with.

    # example passing only required values which don't have defaults set
    try:
        # Get a review
        api_response = api_instance.get_review(review_oid, merchant_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_oid** | **int**| The review oid to retrieve. |
 **merchant_item_oid** | **int**| The item oid the review is associated with. |

### Return type

[**ItemReviewResponse**](ItemReviewResponse.md)

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

# **get_reviews**
> ItemReviewsResponse get_reviews(merchant_item_oid)

Get reviews for an item

Retrieve item reviews. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_reviews_response import ItemReviewsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_item_oid = 1 # int | The item oid the review is associated with.

    # example passing only required values which don't have defaults set
    try:
        # Get reviews for an item
        api_response = api_instance.get_reviews(merchant_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_reviews: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid the review is associated with. |

### Return type

[**ItemReviewsResponse**](ItemReviewsResponse.md)

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

# **get_unassociated_digital_items**
> ItemDigitalItemsResponse get_unassociated_digital_items()

Retrieve digital items from the digital library (which are digital files that may be attached to normal items) not yet associated with actual items

Retrieves a group of digital items (file information) from the account that are not yet associated with any actual items.  If no parameters are specified, all digital items will be returned.  Be aware that these are not normal items that can be added to a shopping cart. Rather, they are digital files that may be associated with normal items.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_digital_items_response import ItemDigitalItemsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 2000) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    since = "_since_example" # str | Fetch items that have been created/modified since this date/time. (optional)
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve digital items from the digital library (which are digital files that may be attached to normal items) not yet associated with actual items
        api_response = api_instance.get_unassociated_digital_items(limit=limit, offset=offset, since=since, sort=sort, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->get_unassociated_digital_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 2000) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch items that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**ItemDigitalItemsResponse**](ItemDigitalItemsResponse.md)

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

# **insert_digital_item**
> ItemDigitalItemResponse insert_digital_item(digital_item)

Create a file within the digital library

Create a file within the digital library.  This does not create an item, but makes this digital file available and selectable as part (or all) of an item. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_digital_item_response import ItemDigitalItemResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_digital_item import ItemDigitalItem
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    digital_item = ItemDigitalItem(
        click_wrap_agreement="click_wrap_agreement_example",
        creation_dts="creation_dts_example",
        description="description_example",
        digital_item_oid=1,
        external_id="external_id_example",
        file_size=1,
        import_from_url="import_from_url_example",
        mime_type="mime_type_example",
        original_filename="original_filename_example",
        pdf_meta=ItemDigitalItemPdfMeta(
            assembly_allowed=True,
            copy_allowed=True,
            custom_footer="custom_footer_example",
            custom_header="custom_header_example",
            degraded_printing_allowed=True,
            fillin_allowed=True,
            modify_annotations_allowed=True,
            modify_contents_allowed=True,
            printing_allowed=True,
            screen_readers_allowed=True,
            tagged=True,
        ),
    ) # ItemDigitalItem | Digital item to create

    # example passing only required values which don't have defaults set
    try:
        # Create a file within the digital library
        api_response = api_instance.insert_digital_item(digital_item)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->insert_digital_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_item** | [**ItemDigitalItem**](ItemDigitalItem.md)| Digital item to create |

### Return type

[**ItemDigitalItemResponse**](ItemDigitalItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **insert_item**
> ItemResponse insert_item(item)

Create an item

Create a new item on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_response import ItemResponse
from ultracart.model.item import Item
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    item = Item(
        accounting=ItemAccounting(
            accounting_code="accounting_code_example",
            qb_class="qb_class_example",
        ),
        amember=ItemAmember(
            amember_payment_duration_days=1,
            amember_product_id="amember_product_id_example",
        ),
        auto_order=ItemAutoOrder(
            auth_future_amount=3.14,
            auth_test_amount=3.14,
            auto_order_cancel_charge_minimum_balance=True,
            auto_order_cancel_item_id="auto_order_cancel_item_id_example",
            auto_order_cancel_item_oid=1,
            auto_order_cancel_minimum_life_time_count=1,
            auto_order_cancel_minimum_life_time_value=3.14,
            auto_order_cancel_minimum_rebill_count=1,
            auto_order_cancel_minimum_rebill_value=3.14,
            auto_order_downgrade_items=[
                "auto_order_downgrade_items_example",
            ],
            auto_order_paused=True,
            auto_order_prohibit_expiring_cards=1,
            auto_order_schedules=[
                "auto_order_schedules_example",
            ],
            auto_order_upgrade_items=[
                "auto_order_upgrade_items_example",
            ],
            auto_order_upsell=True,
            auto_order_upsell_no_easy_cancel=True,
            auto_order_upsell_one_per_customer=True,
            auto_orderable=True,
            cancel_other_auto_orders=True,
            free_shipping_auto_order=True,
            refund_other_auto_orders=True,
            steps=[
                ItemAutoOrderStep(
                    arbitrary_schedule_days=1,
                    arbitrary_unit_cost=3.14,
                    arbitrary_unit_cost_schedules=[
                        ItemAutoOrderStepArbitraryUnitCostSchedule(
                            arbitrary_unit_cost=3.14,
                            retry_days=1,
                        ),
                    ],
                    grandfather_pricing=[
                        ItemAutoOrderStepGrandfatherPricing(
                            on_or_before_date="on_or_before_date_example",
                            unit_cost=3.14,
                        ),
                    ],
                    managed_by="managed_by_example",
                    pause_days=1,
                    pause_until_date="pause_until_date_example",
                    pause_until_day_of_month=1,
                    pause_until_minimum_delay_days=1,
                    preshipment_notice_days=1,
                    recurring_merchant_item_id="recurring_merchant_item_id_example",
                    recurring_merchant_item_oid=1,
                    repeat_count=1,
                    schedule="schedule_example",
                    subscribe_email_list_name="subscribe_email_list_name_example",
                    subscribe_email_list_oid=1,
                    type="item",
                ),
            ],
        ),
        ccbill=ItemCCBill(
            ccbill_allowed_currencies="ccbill_allowed_currencies_example",
            ccbill_allowed_types="ccbill_allowed_types_example",
            ccbill_currency_code="ccbill_currency_code_example",
            ccbill_form_name="ccbill_form_name_example",
            ccbill_subaccount_id="ccbill_subaccount_id_example",
            ccbill_subscription_type_id="ccbill_subscription_type_id_example",
        ),
        channel_partner_item_mappings=[
            ItemChannelPartnerMapping(
                barcode_ua="barcode_ua_example",
                barcode_uc="barcode_uc_example",
                barcode_ui="barcode_ui_example",
                barcode_uk="barcode_uk_example",
                buyer_catalog_number="buyer_catalog_number_example",
                buyer_dpci="buyer_dpci_example",
                buyer_item_number="buyer_item_number_example",
                channel_partner_code="channel_partner_code_example",
                channel_partner_oid=1,
                cost=3.14,
                from_item_id="from_item_id_example",
                from_sku="from_sku_example",
                mutually_defined_number="mutually_defined_number_example",
                quantity_ratio_cp=1,
                quantity_ratio_uc=1,
                sku="sku_example",
                unit_of_measure="unit_of_measure_example",
                vendor_number="vendor_number_example",
                vendor_style_number="vendor_style_number_example",
            ),
        ],
        chargeback=ItemChargeback(
            addendums=[
                ItemChargebackAddendum(
                    chargeback_addendum_oid=1,
                    description="description_example",
                    file_size=1,
                    pages=1,
                ),
            ],
            adjustment_requests=[
                ItemChargebackAdjustmentRequest(
                    chargeback_adjustment_request_oid=1,
                    description="description_example",
                    reason_code="reason_code_example",
                ),
            ],
        ),
        checkout=ItemCheckout(
            suppress_buysafe=True,
            terms="terms_example",
            terms_if_auto_order=True,
            terms_translated_text_instance_oid=1,
        ),
        content=ItemContent(
            assignments=[
                ItemContentAssignment(
                    default_assignment=True,
                    group_oid=1,
                    group_path="group_path_example",
                    host="host_example",
                    sort_order=1,
                    url_part="url_part_example",
                ),
            ],
            attributes=[
                ItemContentAttribute(
                    name="name_example",
                    translated_text_instance_oid=1,
                    type="type_example",
                    value="value_example",
                ),
            ],
            custom_thank_you_url="custom_thank_you_url_example",
            exclude_from_search=True,
            exclude_from_sitemap=True,
            exclude_from_top_sellers=True,
            extended_description="extended_description_example",
            extended_description_translated_text_instance_oid=1,
            meta_description="meta_description_example",
            meta_keywords="meta_keywords_example",
            meta_title="meta_title_example",
            multimedia=[
                ItemContentMultimedia(
                    cloud_url="cloud_url_example",
                    cloud_url_expiration="cloud_url_expiration_example",
                    code="code_example",
                    description="description_example",
                    exclude_from_gallery=True,
                    file_name="file_name_example",
                    height=1,
                    merchant_item_multimedia_oid=1,
                    orphan=True,
                    placeholder=True,
                    temp_multimedia_oid=1,
                    thumbnails=[
                        ItemContentMultimediaThumbnail(
                            height=1,
                            http_url="http_url_example",
                            https_url="https_url_example",
                            png_format=True,
                            square=True,
                            width=1,
                        ),
                    ],
                    type="Image",
                    url="url_example",
                    width=1,
                ),
            ],
            new_item=True,
            new_item_end="new_item_end_example",
            new_item_start="new_item_start_example",
            view_url="view_url_example",
        ),
        creation_dts="creation_dts_example",
        description="description_example",
        description_translated_text_instance_oid=1,
        digital_delivery=ItemDigitalDelivery(
            activation_code_description="activation_code_description_example",
            activation_code_low_warning=1,
            activation_code_realtime_url="activation_code_realtime_url_example",
            activation_code_shared_secret="activation_code_shared_secret_example",
            activation_code_type="activation_code_type_example",
            digital_items=[
                ItemDigitalItem(
                    click_wrap_agreement="click_wrap_agreement_example",
                    creation_dts="creation_dts_example",
                    description="description_example",
                    digital_item_oid=1,
                    external_id="external_id_example",
                    file_size=1,
                    import_from_url="import_from_url_example",
                    mime_type="mime_type_example",
                    original_filename="original_filename_example",
                    pdf_meta=ItemDigitalItemPdfMeta(
                        assembly_allowed=True,
                        copy_allowed=True,
                        custom_footer="custom_footer_example",
                        custom_header="custom_header_example",
                        degraded_printing_allowed=True,
                        fillin_allowed=True,
                        modify_annotations_allowed=True,
                        modify_contents_allowed=True,
                        printing_allowed=True,
                        screen_readers_allowed=True,
                        tagged=True,
                    ),
                ),
            ],
        ),
        ebay=ItemEbay(
            active=True,
            category_id=1,
            category_specifics=[
                ItemEbayCategorySpecific(
                    name="name_example",
                    value="value_example",
                ),
            ],
            condition_description="condition_description_example",
            condition_id=1,
            consecutive_failures=1,
            custom_category1=1,
            custom_category2=1,
            dispatch_time_max=1,
            domestic_1_additional_cost=3.14,
            domestic_1_first_cost=3.14,
            domestic_2_additional_cost=3.14,
            domestic_2_first_cost=3.14,
            domestic_3_additional_cost=3.14,
            domestic_3_first_cost=3.14,
            domestic_4_additional_cost=3.14,
            domestic_4_first_cost=3.14,
            ebay_auction_id="ebay_auction_id_example",
            ebay_specific_inventory=1,
            ebay_template_name="ebay_template_name_example",
            ebay_template_oid=1,
            end_time="end_time_example",
            free_shipping=True,
            free_shipping_method="free_shipping_method_example",
            international_1_additional_cost=3.14,
            international_1_first_cost=3.14,
            international_2_additional_cost=3.14,
            international_2_first_cost=3.14,
            international_3_additional_cost=3.14,
            international_3_first_cost=3.14,
            international_4_additional_cost=3.14,
            international_4_first_cost=3.14,
            last_status_dts="last_status_dts_example",
            listed_dispatch_time_max=1,
            listed_ebay_template_oid=1,
            listing_dts="listing_dts_example",
            listing_duration="listing_duration_example",
            listing_price=3.14,
            listing_price_override=3.14,
            listing_type="listing_type_example",
            marketplace_analysis=ItemEbayMarketPlaceAnalysis(
                adjusted_price=3.14,
                adjusted_shipping=3.14,
                adjusted_total=3.14,
                cogs=3.14,
                final_value_fee=3.14,
                minimum_advertised_price=3.14,
                other_listings=[
                    ItemEbayMarketListing(
                        auction_id="auction_id_example",
                        price=3.14,
                        seller="seller_example",
                        shipping=3.14,
                        total=3.14,
                    ),
                ],
                our_listing=ItemEbayMarketListing(
                    auction_id="auction_id_example",
                    price=3.14,
                    seller="seller_example",
                    shipping=3.14,
                    total=3.14,
                ),
                overhead=3.14,
                profit_potential=3.14,
            ),
            marketplace_analysis_perform=True,
            marketplace_final_value_fee_percentage=3.14,
            marketplace_last_check_dts="marketplace_last_check_dts_example",
            marketplace_lowest=True,
            marketplace_map_violation=True,
            marketplace_multiplier=3.14,
            marketplace_other_price=3.14,
            marketplace_other_seller="marketplace_other_seller_example",
            marketplace_other_shipping=3.14,
            marketplace_other_total=3.14,
            marketplace_our_additional_profit_potential=3.14,
            marketplace_our_price=3.14,
            marketplace_our_profit=3.14,
            marketplace_our_shipping=3.14,
            marketplace_our_total=3.14,
            marketplace_overhead=3.14,
            marketplace_profitable=True,
            next_attempt_dts="next_attempt_dts_example",
            next_listing_duration="next_listing_duration_example",
            no_promotional_shipping=True,
            packaging_handling_costs=3.14,
            previous_ebay_auction_id="previous_ebay_auction_id_example",
            quantity=1,
            reserve_price=3.14,
            send_dimensions_and_weight="send_dimensions_and_weight_example",
            start_time="start_time_example",
            status="status_example",
            target_dispatch_time_max=1,
        ),
        email_notifications=ItemEmailNotifications(
            skip_receipt=True,
            skip_shipment_notification=True,
        ),
        enrollment123=ItemEnrollment123(
            enrollment123_product_code="enrollment123_product_code_example",
        ),
        fulfillment_addons=[
            ItemFulfillmentAddon(
                add_item_id="add_item_id_example",
                add_item_oid=1,
                initial_order_only=True,
                once_per_order=True,
                quantity=1,
            ),
        ],
        gift_certificate=ItemGiftCertificate(
            gift_certificate=True,
            gift_certificate_expiration_days=1,
        ),
        google_product_search=ItemGoogleProductSearch(
            adwords_grouping="adwords_grouping_example",
            adwords_label1="adwords_label1_example",
            adwords_label2="adwords_label2_example",
            adwords_label3="adwords_label3_example",
            adwords_label4="adwords_label4_example",
            adwords_label5="adwords_label5_example",
            age_group="age_group_example",
            available_at_physical_store=True,
            book_author="book_author_example",
            book_format="book_format_example",
            book_isbn="book_isbn_example",
            book_publisher="book_publisher_example",
            category_description="category_description_example",
            color="color_example",
            condition="condition_example",
            custom_label0="custom_label0_example",
            custom_label1="custom_label1_example",
            custom_label2="custom_label2_example",
            custom_label3="custom_label3_example",
            custom_label4="custom_label4_example",
            gender="gender_example",
            google_product_category="google_product_category_example",
            music_artist="music_artist_example",
            music_format="music_format_example",
            music_release_date="music_release_date_example",
            omit_from_feed=True,
            product_type="product_type_example",
            promotion_id1="promotion_id1_example",
            promotion_id10="promotion_id10_example",
            promotion_id2="promotion_id2_example",
            promotion_id3="promotion_id3_example",
            promotion_id4="promotion_id4_example",
            promotion_id5="promotion_id5_example",
            promotion_id6="promotion_id6_example",
            promotion_id7="promotion_id7_example",
            promotion_id8="promotion_id8_example",
            promotion_id9="promotion_id9_example",
            search_dts="search_dts_example",
            search_lowest_price=3.14,
            search_lowest_url="search_lowest_url_example",
            search_position=1,
            shipping_label="shipping_label_example",
            size="size_example",
            video_director="video_director_example",
            video_format="video_format_example",
            video_rating="video_rating_example",
            video_release_date="video_release_date_example",
            video_starring="video_starring_example",
        ),
        identifiers=ItemIdentifiers(
            barcode="barcode_example",
            barcode_gtin12="barcode_gtin12_example",
            barcode_gtin14="barcode_gtin14_example",
            barcode_upc11="barcode_upc11_example",
            barcode_upc12="barcode_upc12_example",
            manufacturer_name="manufacturer_name_example",
            manufacturer_sku="manufacturer_sku_example",
            unspsc="unspsc_example",
        ),
        inactive=True,
        instant_payment_notifications=ItemInstantPaymentNotifications(
            notifications=[
                ItemInstantPaymentNotification(
                    post_operation=True,
                    successful_response_text="successful_response_text_example",
                    url="url_example",
                ),
            ],
        ),
        internal=ItemInternal(
            memo="memo_example",
        ),
        kit=True,
        kit_component_only=True,
        kit_definition=ItemKitDefinition(
            components=[
                ItemKitComponent(
                    component_cost=3.14,
                    component_description="component_description_example",
                    component_merchant_item_id="component_merchant_item_id_example",
                    component_merchant_item_oid=1,
                    quantity=1,
                ),
            ],
        ),
        last_modified_dts="last_modified_dts_example",
        merchant_id="merchant_id_example",
        merchant_item_id="merchant_item_id_example",
        merchant_item_oid=1,
        options=[
            ItemOption(
                cost_if_specified=3.14,
                cost_per_letter=3.14,
                cost_per_line=3.14,
                ignore_if_default=True,
                label="label_example",
                label_translated_text_instance_oid=1,
                name="name_example",
                name_translated_text_instance_oid=1,
                one_time_fee=True,
                option_oid=1,
                required=True,
                system_option=True,
                type="dropdown",
                values=[
                    ItemOptionValue(
                        additional_dimension_application="none",
                        additional_items=[
                            ItemOptionValueAdditionalItem(
                                additional_merchant_item_id="additional_merchant_item_id_example",
                                additional_merchant_item_oid=1,
                            ),
                        ],
                        cost_change=3.14,
                        default_value=True,
                        digital_items=[
                            ItemOptionValueDigitalItem(
                                digital_item_oid=1,
                                original_filename="original_filename_example",
                            ),
                        ],
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        merchant_item_multimedia_oid=1,
                        option_value_oid=1,
                        percent_cost_change=3.14,
                        translated_text_instance_oid=1,
                        value="value_example",
                        weight_change=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        weight_change_percent=3.14,
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
            ),
        ],
        parent_category_id=1,
        parent_category_path="parent_category_path_example",
        payment_processing=ItemPaymentProcessing(
            block_prepaid=True,
            block_refunds=True,
            credit_card_transaction_type="credit_card_transaction_type_example",
            no_realtime_charge=True,
            payment_method_validity=[
                "payment_method_validity_example",
            ],
            rotating_transaction_gateway_codes=[
                "rotating_transaction_gateway_codes_example",
            ],
        ),
        physical=ItemPhysical(
            height=Distance(
                uom="IN",
                value=3.14,
            ),
            length=Distance(
                uom="IN",
                value=3.14,
            ),
            weight=Weight(
                uom="KG",
                value=3.14,
            ),
            width=Distance(
                uom="IN",
                value=3.14,
            ),
        ),
        pricing=ItemPricing(
            allow_arbitrary_cost=True,
            arbitrary_cost_velocity_code="arbitrary_cost_velocity_code_example",
            auto_order_cost=3.14,
            automatic_pricing_tier_name="automatic_pricing_tier_name_example",
            automatic_pricing_tier_oid=1,
            cogs=3.14,
            cost=3.14,
            currency_code="currency_code_example",
            manufacturer_suggested_retail_price=3.14,
            maximum_arbitrary_cost=3.14,
            minimum_advertised_price=3.14,
            minimum_arbitrary_cost=3.14,
            mix_and_match_group="mix_and_match_group_example",
            mix_and_match_group_oid=1,
            sale_cost=3.14,
            sale_end="sale_end_example",
            sale_start="sale_start_example",
            tiers=[
                ItemPricingTier(
                    default_tier=True,
                    discounts=[
                        ItemPricingTierDiscount(
                            cost=3.14,
                            quantity=1,
                        ),
                    ],
                    limit=ItemPricingTierLimit(
                        cumulative_order_limit=1,
                        exempt_from_minimum_item_count=True,
                        individual_order_limit=1,
                        multiple_quantity=1,
                        payment_method_validity=[
                            "payment_method_validity_example",
                        ],
                    ),
                    name="name_example",
                    pricing_tier_oid=1,
                ),
            ],
        ),
        properties=[
            ItemProperty(
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        realtime_pricing=ItemRealtimePricing(
            realtime_pricing_parameter="realtime_pricing_parameter_example",
            realtime_pricing_provider="realtime_pricing_provider_example",
            realtime_pricing_provider_oid=1,
        ),
        recommend_replenishment_days=1,
        related=ItemRelated(
            no_system_calculated_related_items=True,
            not_relatable=True,
            related_items=[
                ItemRelatedItem(
                    related_merchant_item_id="related_merchant_item_id_example",
                    related_merchant_item_oid=1,
                    type="System",
                ),
            ],
        ),
        reporting=ItemReporting(
            report_as_upsell=True,
            report_pickable_quantities=[
                1,
            ],
        ),
        restriction=ItemRestriction(
            exclude_coupon=True,
            exclude_from_free_promotion=True,
            items=[
                ItemRestrictionItem(
                    restrict_merchant_item_id="restrict_merchant_item_id_example",
                    restrict_merchant_item_oid=1,
                    type="can not be purchased with",
                ),
            ],
            maximum_quantity=1,
            minimum_quantity=1,
            multiple_quantity=1,
            one_per_customer=True,
            purchase_separately=True,
        ),
        revguard=ItemRevguard(
            revguard_canceled_csr_prompt_group=1,
            revguard_canceled_ivr_prompt_group=1,
            revguard_canceled_web_prompt_group=1,
            revguard_client_brand=1,
            revguard_csr_prompt_group=1,
            revguard_ivr_prompt_group=1,
            revguard_web_prompt_group=1,
        ),
        reviews=ItemReviews(
            has_approved_review=True,
            has_review=True,
            individual_reviews=[
                ItemReview(
                    customer_profile_oid=1,
                    featured=True,
                    helperful_no_votes=1,
                    helpful_yes_votes=1,
                    merchant_reply="merchant_reply_example",
                    order_id="order_id_example",
                    overall=3.14,
                    rating_name1="rating_name1_example",
                    rating_name10="rating_name10_example",
                    rating_name2="rating_name2_example",
                    rating_name3="rating_name3_example",
                    rating_name4="rating_name4_example",
                    rating_name5="rating_name5_example",
                    rating_name6="rating_name6_example",
                    rating_name7="rating_name7_example",
                    rating_name8="rating_name8_example",
                    rating_name9="rating_name9_example",
                    rating_score1=3.14,
                    rating_score10=3.14,
                    rating_score2=3.14,
                    rating_score3=3.14,
                    rating_score4=3.14,
                    rating_score5=3.14,
                    rating_score6=3.14,
                    rating_score7=3.14,
                    rating_score8=3.14,
                    rating_score9=3.14,
                    recommend_store_to_friend=1,
                    recommend_to_friend=True,
                    review="review_example",
                    review_oid=1,
                    reviewed_nickname="reviewed_nickname_example",
                    reviewer_email="reviewer_email_example",
                    reviewer_location="reviewer_location_example",
                    status="approved",
                    store_feedback="store_feedback_example",
                    submitted_dts="submitted_dts_example",
                    title="title_example",
                ),
            ],
            review_count=1,
            review_overall=3.14,
            review_template_name="review_template_name_example",
            review_template_oid=1,
            reviewable=True,
            share_reviews_with_merchant_item_id="share_reviews_with_merchant_item_id_example",
            share_reviews_with_merchant_item_oid=1,
        ),
        salesforce=ItemSalesforce(
            sfdc_pricebook_id="sfdc_pricebook_id_example",
            sfdc_product_id="sfdc_product_id_example",
        ),
        shipping=ItemShipping(
            allow_back_order=True,
            amazon_fba=True,
            case_inner_packs=1,
            case_units=1,
            cases=[
                ItemShippingCase(
                    case_label="case_label_example",
                    case_merchant_item_id="case_merchant_item_id_example",
                    case_merchant_item_oid=1,
                    quantity=1,
                ),
            ],
            collect_serial_numbers=True,
            country_code_of_origin="country_code_of_origin_example",
            customs_description="customs_description_example",
            customs_value=3.14,
            delivery_on_friday=True,
            delivery_on_monday=True,
            delivery_on_saturday=True,
            delivery_on_sunday=True,
            delivery_on_thursday=True,
            delivery_on_tuesday=True,
            delivery_on_wednesday=True,
            destination_markups=[
                ItemShippingDestinationMarkup(
                    adult_signature_required=True,
                    country_code="country_code_example",
                    flat_fee=3.14,
                    per_item=3.14,
                    postal_code="postal_code_example",
                    shipping_method="shipping_method_example",
                    state="state_example",
                ),
            ],
            destination_restrictions=[
                ItemShippingDestinationRestriction(
                    country_code="country_code_example",
                    state="state_example",
                    validity="valid only for",
                ),
            ],
            distribution_centers=[
                ItemShippingDistributionCenter(
                    allocated_to_placed_orders=3.14,
                    allocated_to_shopping_carts=3.14,
                    available_to_allocate=3.14,
                    cogs=3.14,
                    desired_inventory_level=3.14,
                    distribution_center_code="distribution_center_code_example",
                    distribution_center_oid=1,
                    eta="eta_example",
                    handles=True,
                    inventory_level=3.14,
                    maximum_backorder=1,
                    reorder_inventory_level=3.14,
                    sku="sku_example",
                    stock_picking_location="stock_picking_location_example",
                ),
            ],
            eta="eta_example",
            free_shipping=True,
            freight_class="freight_class_example",
            hazmat=True,
            hold_for_transmission=True,
            made_to_order=True,
            made_to_order_lead_time=1,
            max_days_time_in_transit=1,
            methods=[
                ItemShippingMethod(
                    cost=3.14,
                    each_additional_item_markup=3.14,
                    filter_to_if_available=True,
                    first_item_markup=3.14,
                    fixed_shipping_cost=3.14,
                    flat_fee_markup=3.14,
                    free_shipping=True,
                    per_item_fee_markup=3.14,
                    percentage_markup=3.14,
                    percentage_of_item_markup=3.14,
                    relax_restrictions_on_upsell=True,
                    shipping_method="shipping_method_example",
                    shipping_method_oid=1,
                    shipping_method_validity="invalid for",
                    signature_required=True,
                ),
            ],
            no_shipping_discount=True,
            package_requirements=[
                ItemShippingPackageRequirement(
                    package_name="package_name_example",
                    package_oid=1,
                ),
            ],
            perishable_class_name="perishable_class_name_example",
            perishable_class_oid=1,
            preorder=True,
            require_delivery_date=True,
            restrict_shipment_on_friday=True,
            restrict_shipment_on_monday=True,
            restrict_shipment_on_saturday=True,
            restrict_shipment_on_sunday=True,
            restrict_shipment_on_thursday=True,
            restrict_shipment_on_tuesday=True,
            restrict_shipment_on_wednesday=True,
            ship_separately=True,
            ship_separately_additional_weight=Weight(
                uom="KG",
                value=3.14,
            ),
            ship_separately_height=Distance(
                uom="IN",
                value=3.14,
            ),
            ship_separately_length=Distance(
                uom="IN",
                value=3.14,
            ),
            ship_separately_package_special_type="ship_separately_package_special_type_example",
            ship_separately_width=Distance(
                uom="IN",
                value=3.14,
            ),
            special_product_type="special_product_type_example",
            track_inventory=True,
        ),
        tags=ItemTags(
            tags=[
                ItemTag(
                    tag_type="item",
                    tag_value="tag_value_example",
                ),
            ],
        ),
        tax=ItemTax(
            exemptions=[
                ItemTaxExemption(
                    city="city_example",
                    country_code="country_code_example",
                    county="county_example",
                    postal_code="postal_code_example",
                    state_code="state_code_example",
                ),
            ],
            tax_free=True,
            tax_product_type="",
            taxable_cost=3.14,
        ),
        third_party_email_marketing=[
            ItemThirdPartyEmailMarketing(
                add_tags=[
                    "add_tags_example",
                ],
                provider_name="ActiveCampaign",
                remove_tags=[
                    "remove_tags_example",
                ],
                subscribe_lists=[
                    "subscribe_lists_example",
                ],
                unsubscribe_lists=[
                    "unsubscribe_lists_example",
                ],
            ),
        ],
        variant_items=[
            ItemVariantItem(
                description="description_example",
                merchant_item_multimedia_oid=1,
                variant_merchant_item_id="variant_merchant_item_id_example",
                variant_merchant_item_oid=1,
                variation_options=[
                    "variation_options_example",
                ],
                variations=[
                    "variations_example",
                ],
            ),
        ],
        variations=[
            ItemVariation(
                default_text="default_text_example",
                default_text_translated_text_instance_oid=1,
                name="name_example",
                name_translated_text_instance_oid=1,
                options=[
                    ItemVariationOption(
                        default_option=True,
                        merchant_item_multimedia_oid=1,
                        translated_text_instance_oid=1,
                        value="value_example",
                    ),
                ],
            ),
        ],
        wishlist_member=ItemWishlistMember(
            wishlist_member_instance_description="wishlist_member_instance_description_example",
            wishlist_member_instance_oid=1,
            wishlist_member_sku="wishlist_member_sku_example",
        ),
    ) # Item | Item to create
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an item
        api_response = api_instance.insert_item(item)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->insert_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an item
        api_response = api_instance.insert_item(item, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **insert_review**
> ItemReviewResponse insert_review(merchant_item_oid, review)

Insert a review

Insert a item review. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_review import ItemReview
from ultracart.model.item_review_response import ItemReviewResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_item_oid = 1 # int | The item oid the review is associated with.
    review = ItemReview(
        customer_profile_oid=1,
        featured=True,
        helperful_no_votes=1,
        helpful_yes_votes=1,
        merchant_reply="merchant_reply_example",
        order_id="order_id_example",
        overall=3.14,
        rating_name1="rating_name1_example",
        rating_name10="rating_name10_example",
        rating_name2="rating_name2_example",
        rating_name3="rating_name3_example",
        rating_name4="rating_name4_example",
        rating_name5="rating_name5_example",
        rating_name6="rating_name6_example",
        rating_name7="rating_name7_example",
        rating_name8="rating_name8_example",
        rating_name9="rating_name9_example",
        rating_score1=3.14,
        rating_score10=3.14,
        rating_score2=3.14,
        rating_score3=3.14,
        rating_score4=3.14,
        rating_score5=3.14,
        rating_score6=3.14,
        rating_score7=3.14,
        rating_score8=3.14,
        rating_score9=3.14,
        recommend_store_to_friend=1,
        recommend_to_friend=True,
        review="review_example",
        review_oid=1,
        reviewed_nickname="reviewed_nickname_example",
        reviewer_email="reviewer_email_example",
        reviewer_location="reviewer_location_example",
        status="approved",
        store_feedback="store_feedback_example",
        submitted_dts="submitted_dts_example",
        title="title_example",
    ) # ItemReview | Review to insert

    # example passing only required values which don't have defaults set
    try:
        # Insert a review
        api_response = api_instance.insert_review(merchant_item_oid, review)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->insert_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid the review is associated with. |
 **review** | [**ItemReview**](ItemReview.md)| Review to insert |

### Return type

[**ItemReviewResponse**](ItemReviewResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **insert_update_item_content_attribute**
> insert_update_item_content_attribute(merchant_item_oid, item_attribute)

Upsert an item content attribute

Update an item content attribute, creating it new if it does not yet exist. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_content_attribute import ItemContentAttribute
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_item_oid = 1 # int | The item oid to modify.
    item_attribute = ItemContentAttribute(
        name="name_example",
        translated_text_instance_oid=1,
        type="type_example",
        value="value_example",
    ) # ItemContentAttribute | Item content attribute to upsert

    # example passing only required values which don't have defaults set
    try:
        # Upsert an item content attribute
        api_instance.insert_update_item_content_attribute(merchant_item_oid, item_attribute)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->insert_update_item_content_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid to modify. |
 **item_attribute** | [**ItemContentAttribute**](ItemContentAttribute.md)| Item content attribute to upsert |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_digital_item**
> ItemDigitalItemResponse update_digital_item(digital_item_oid, digital_item)

Updates a file within the digital library

Updates a file within the digital library.  This does not update an item, but updates a digital file available and selectable as part (or all) of an item. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_digital_item_response import ItemDigitalItemResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_digital_item import ItemDigitalItem
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    digital_item_oid = 1 # int | The digital item oid to update.
    digital_item = ItemDigitalItem(
        click_wrap_agreement="click_wrap_agreement_example",
        creation_dts="creation_dts_example",
        description="description_example",
        digital_item_oid=1,
        external_id="external_id_example",
        file_size=1,
        import_from_url="import_from_url_example",
        mime_type="mime_type_example",
        original_filename="original_filename_example",
        pdf_meta=ItemDigitalItemPdfMeta(
            assembly_allowed=True,
            copy_allowed=True,
            custom_footer="custom_footer_example",
            custom_header="custom_header_example",
            degraded_printing_allowed=True,
            fillin_allowed=True,
            modify_annotations_allowed=True,
            modify_contents_allowed=True,
            printing_allowed=True,
            screen_readers_allowed=True,
            tagged=True,
        ),
    ) # ItemDigitalItem | Digital item to update

    # example passing only required values which don't have defaults set
    try:
        # Updates a file within the digital library
        api_response = api_instance.update_digital_item(digital_item_oid, digital_item)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->update_digital_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_item_oid** | **int**| The digital item oid to update. |
 **digital_item** | [**ItemDigitalItem**](ItemDigitalItem.md)| Digital item to update |

### Return type

[**ItemDigitalItemResponse**](ItemDigitalItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **update_item**
> ItemResponse update_item(merchant_item_oid, item)

Update an item

Update a new item on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.item_response import ItemResponse
from ultracart.model.item import Item
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_item_oid = 1 # int | The item oid to update.
    item = Item(
        accounting=ItemAccounting(
            accounting_code="accounting_code_example",
            qb_class="qb_class_example",
        ),
        amember=ItemAmember(
            amember_payment_duration_days=1,
            amember_product_id="amember_product_id_example",
        ),
        auto_order=ItemAutoOrder(
            auth_future_amount=3.14,
            auth_test_amount=3.14,
            auto_order_cancel_charge_minimum_balance=True,
            auto_order_cancel_item_id="auto_order_cancel_item_id_example",
            auto_order_cancel_item_oid=1,
            auto_order_cancel_minimum_life_time_count=1,
            auto_order_cancel_minimum_life_time_value=3.14,
            auto_order_cancel_minimum_rebill_count=1,
            auto_order_cancel_minimum_rebill_value=3.14,
            auto_order_downgrade_items=[
                "auto_order_downgrade_items_example",
            ],
            auto_order_paused=True,
            auto_order_prohibit_expiring_cards=1,
            auto_order_schedules=[
                "auto_order_schedules_example",
            ],
            auto_order_upgrade_items=[
                "auto_order_upgrade_items_example",
            ],
            auto_order_upsell=True,
            auto_order_upsell_no_easy_cancel=True,
            auto_order_upsell_one_per_customer=True,
            auto_orderable=True,
            cancel_other_auto_orders=True,
            free_shipping_auto_order=True,
            refund_other_auto_orders=True,
            steps=[
                ItemAutoOrderStep(
                    arbitrary_schedule_days=1,
                    arbitrary_unit_cost=3.14,
                    arbitrary_unit_cost_schedules=[
                        ItemAutoOrderStepArbitraryUnitCostSchedule(
                            arbitrary_unit_cost=3.14,
                            retry_days=1,
                        ),
                    ],
                    grandfather_pricing=[
                        ItemAutoOrderStepGrandfatherPricing(
                            on_or_before_date="on_or_before_date_example",
                            unit_cost=3.14,
                        ),
                    ],
                    managed_by="managed_by_example",
                    pause_days=1,
                    pause_until_date="pause_until_date_example",
                    pause_until_day_of_month=1,
                    pause_until_minimum_delay_days=1,
                    preshipment_notice_days=1,
                    recurring_merchant_item_id="recurring_merchant_item_id_example",
                    recurring_merchant_item_oid=1,
                    repeat_count=1,
                    schedule="schedule_example",
                    subscribe_email_list_name="subscribe_email_list_name_example",
                    subscribe_email_list_oid=1,
                    type="item",
                ),
            ],
        ),
        ccbill=ItemCCBill(
            ccbill_allowed_currencies="ccbill_allowed_currencies_example",
            ccbill_allowed_types="ccbill_allowed_types_example",
            ccbill_currency_code="ccbill_currency_code_example",
            ccbill_form_name="ccbill_form_name_example",
            ccbill_subaccount_id="ccbill_subaccount_id_example",
            ccbill_subscription_type_id="ccbill_subscription_type_id_example",
        ),
        channel_partner_item_mappings=[
            ItemChannelPartnerMapping(
                barcode_ua="barcode_ua_example",
                barcode_uc="barcode_uc_example",
                barcode_ui="barcode_ui_example",
                barcode_uk="barcode_uk_example",
                buyer_catalog_number="buyer_catalog_number_example",
                buyer_dpci="buyer_dpci_example",
                buyer_item_number="buyer_item_number_example",
                channel_partner_code="channel_partner_code_example",
                channel_partner_oid=1,
                cost=3.14,
                from_item_id="from_item_id_example",
                from_sku="from_sku_example",
                mutually_defined_number="mutually_defined_number_example",
                quantity_ratio_cp=1,
                quantity_ratio_uc=1,
                sku="sku_example",
                unit_of_measure="unit_of_measure_example",
                vendor_number="vendor_number_example",
                vendor_style_number="vendor_style_number_example",
            ),
        ],
        chargeback=ItemChargeback(
            addendums=[
                ItemChargebackAddendum(
                    chargeback_addendum_oid=1,
                    description="description_example",
                    file_size=1,
                    pages=1,
                ),
            ],
            adjustment_requests=[
                ItemChargebackAdjustmentRequest(
                    chargeback_adjustment_request_oid=1,
                    description="description_example",
                    reason_code="reason_code_example",
                ),
            ],
        ),
        checkout=ItemCheckout(
            suppress_buysafe=True,
            terms="terms_example",
            terms_if_auto_order=True,
            terms_translated_text_instance_oid=1,
        ),
        content=ItemContent(
            assignments=[
                ItemContentAssignment(
                    default_assignment=True,
                    group_oid=1,
                    group_path="group_path_example",
                    host="host_example",
                    sort_order=1,
                    url_part="url_part_example",
                ),
            ],
            attributes=[
                ItemContentAttribute(
                    name="name_example",
                    translated_text_instance_oid=1,
                    type="type_example",
                    value="value_example",
                ),
            ],
            custom_thank_you_url="custom_thank_you_url_example",
            exclude_from_search=True,
            exclude_from_sitemap=True,
            exclude_from_top_sellers=True,
            extended_description="extended_description_example",
            extended_description_translated_text_instance_oid=1,
            meta_description="meta_description_example",
            meta_keywords="meta_keywords_example",
            meta_title="meta_title_example",
            multimedia=[
                ItemContentMultimedia(
                    cloud_url="cloud_url_example",
                    cloud_url_expiration="cloud_url_expiration_example",
                    code="code_example",
                    description="description_example",
                    exclude_from_gallery=True,
                    file_name="file_name_example",
                    height=1,
                    merchant_item_multimedia_oid=1,
                    orphan=True,
                    placeholder=True,
                    temp_multimedia_oid=1,
                    thumbnails=[
                        ItemContentMultimediaThumbnail(
                            height=1,
                            http_url="http_url_example",
                            https_url="https_url_example",
                            png_format=True,
                            square=True,
                            width=1,
                        ),
                    ],
                    type="Image",
                    url="url_example",
                    width=1,
                ),
            ],
            new_item=True,
            new_item_end="new_item_end_example",
            new_item_start="new_item_start_example",
            view_url="view_url_example",
        ),
        creation_dts="creation_dts_example",
        description="description_example",
        description_translated_text_instance_oid=1,
        digital_delivery=ItemDigitalDelivery(
            activation_code_description="activation_code_description_example",
            activation_code_low_warning=1,
            activation_code_realtime_url="activation_code_realtime_url_example",
            activation_code_shared_secret="activation_code_shared_secret_example",
            activation_code_type="activation_code_type_example",
            digital_items=[
                ItemDigitalItem(
                    click_wrap_agreement="click_wrap_agreement_example",
                    creation_dts="creation_dts_example",
                    description="description_example",
                    digital_item_oid=1,
                    external_id="external_id_example",
                    file_size=1,
                    import_from_url="import_from_url_example",
                    mime_type="mime_type_example",
                    original_filename="original_filename_example",
                    pdf_meta=ItemDigitalItemPdfMeta(
                        assembly_allowed=True,
                        copy_allowed=True,
                        custom_footer="custom_footer_example",
                        custom_header="custom_header_example",
                        degraded_printing_allowed=True,
                        fillin_allowed=True,
                        modify_annotations_allowed=True,
                        modify_contents_allowed=True,
                        printing_allowed=True,
                        screen_readers_allowed=True,
                        tagged=True,
                    ),
                ),
            ],
        ),
        ebay=ItemEbay(
            active=True,
            category_id=1,
            category_specifics=[
                ItemEbayCategorySpecific(
                    name="name_example",
                    value="value_example",
                ),
            ],
            condition_description="condition_description_example",
            condition_id=1,
            consecutive_failures=1,
            custom_category1=1,
            custom_category2=1,
            dispatch_time_max=1,
            domestic_1_additional_cost=3.14,
            domestic_1_first_cost=3.14,
            domestic_2_additional_cost=3.14,
            domestic_2_first_cost=3.14,
            domestic_3_additional_cost=3.14,
            domestic_3_first_cost=3.14,
            domestic_4_additional_cost=3.14,
            domestic_4_first_cost=3.14,
            ebay_auction_id="ebay_auction_id_example",
            ebay_specific_inventory=1,
            ebay_template_name="ebay_template_name_example",
            ebay_template_oid=1,
            end_time="end_time_example",
            free_shipping=True,
            free_shipping_method="free_shipping_method_example",
            international_1_additional_cost=3.14,
            international_1_first_cost=3.14,
            international_2_additional_cost=3.14,
            international_2_first_cost=3.14,
            international_3_additional_cost=3.14,
            international_3_first_cost=3.14,
            international_4_additional_cost=3.14,
            international_4_first_cost=3.14,
            last_status_dts="last_status_dts_example",
            listed_dispatch_time_max=1,
            listed_ebay_template_oid=1,
            listing_dts="listing_dts_example",
            listing_duration="listing_duration_example",
            listing_price=3.14,
            listing_price_override=3.14,
            listing_type="listing_type_example",
            marketplace_analysis=ItemEbayMarketPlaceAnalysis(
                adjusted_price=3.14,
                adjusted_shipping=3.14,
                adjusted_total=3.14,
                cogs=3.14,
                final_value_fee=3.14,
                minimum_advertised_price=3.14,
                other_listings=[
                    ItemEbayMarketListing(
                        auction_id="auction_id_example",
                        price=3.14,
                        seller="seller_example",
                        shipping=3.14,
                        total=3.14,
                    ),
                ],
                our_listing=ItemEbayMarketListing(
                    auction_id="auction_id_example",
                    price=3.14,
                    seller="seller_example",
                    shipping=3.14,
                    total=3.14,
                ),
                overhead=3.14,
                profit_potential=3.14,
            ),
            marketplace_analysis_perform=True,
            marketplace_final_value_fee_percentage=3.14,
            marketplace_last_check_dts="marketplace_last_check_dts_example",
            marketplace_lowest=True,
            marketplace_map_violation=True,
            marketplace_multiplier=3.14,
            marketplace_other_price=3.14,
            marketplace_other_seller="marketplace_other_seller_example",
            marketplace_other_shipping=3.14,
            marketplace_other_total=3.14,
            marketplace_our_additional_profit_potential=3.14,
            marketplace_our_price=3.14,
            marketplace_our_profit=3.14,
            marketplace_our_shipping=3.14,
            marketplace_our_total=3.14,
            marketplace_overhead=3.14,
            marketplace_profitable=True,
            next_attempt_dts="next_attempt_dts_example",
            next_listing_duration="next_listing_duration_example",
            no_promotional_shipping=True,
            packaging_handling_costs=3.14,
            previous_ebay_auction_id="previous_ebay_auction_id_example",
            quantity=1,
            reserve_price=3.14,
            send_dimensions_and_weight="send_dimensions_and_weight_example",
            start_time="start_time_example",
            status="status_example",
            target_dispatch_time_max=1,
        ),
        email_notifications=ItemEmailNotifications(
            skip_receipt=True,
            skip_shipment_notification=True,
        ),
        enrollment123=ItemEnrollment123(
            enrollment123_product_code="enrollment123_product_code_example",
        ),
        fulfillment_addons=[
            ItemFulfillmentAddon(
                add_item_id="add_item_id_example",
                add_item_oid=1,
                initial_order_only=True,
                once_per_order=True,
                quantity=1,
            ),
        ],
        gift_certificate=ItemGiftCertificate(
            gift_certificate=True,
            gift_certificate_expiration_days=1,
        ),
        google_product_search=ItemGoogleProductSearch(
            adwords_grouping="adwords_grouping_example",
            adwords_label1="adwords_label1_example",
            adwords_label2="adwords_label2_example",
            adwords_label3="adwords_label3_example",
            adwords_label4="adwords_label4_example",
            adwords_label5="adwords_label5_example",
            age_group="age_group_example",
            available_at_physical_store=True,
            book_author="book_author_example",
            book_format="book_format_example",
            book_isbn="book_isbn_example",
            book_publisher="book_publisher_example",
            category_description="category_description_example",
            color="color_example",
            condition="condition_example",
            custom_label0="custom_label0_example",
            custom_label1="custom_label1_example",
            custom_label2="custom_label2_example",
            custom_label3="custom_label3_example",
            custom_label4="custom_label4_example",
            gender="gender_example",
            google_product_category="google_product_category_example",
            music_artist="music_artist_example",
            music_format="music_format_example",
            music_release_date="music_release_date_example",
            omit_from_feed=True,
            product_type="product_type_example",
            promotion_id1="promotion_id1_example",
            promotion_id10="promotion_id10_example",
            promotion_id2="promotion_id2_example",
            promotion_id3="promotion_id3_example",
            promotion_id4="promotion_id4_example",
            promotion_id5="promotion_id5_example",
            promotion_id6="promotion_id6_example",
            promotion_id7="promotion_id7_example",
            promotion_id8="promotion_id8_example",
            promotion_id9="promotion_id9_example",
            search_dts="search_dts_example",
            search_lowest_price=3.14,
            search_lowest_url="search_lowest_url_example",
            search_position=1,
            shipping_label="shipping_label_example",
            size="size_example",
            video_director="video_director_example",
            video_format="video_format_example",
            video_rating="video_rating_example",
            video_release_date="video_release_date_example",
            video_starring="video_starring_example",
        ),
        identifiers=ItemIdentifiers(
            barcode="barcode_example",
            barcode_gtin12="barcode_gtin12_example",
            barcode_gtin14="barcode_gtin14_example",
            barcode_upc11="barcode_upc11_example",
            barcode_upc12="barcode_upc12_example",
            manufacturer_name="manufacturer_name_example",
            manufacturer_sku="manufacturer_sku_example",
            unspsc="unspsc_example",
        ),
        inactive=True,
        instant_payment_notifications=ItemInstantPaymentNotifications(
            notifications=[
                ItemInstantPaymentNotification(
                    post_operation=True,
                    successful_response_text="successful_response_text_example",
                    url="url_example",
                ),
            ],
        ),
        internal=ItemInternal(
            memo="memo_example",
        ),
        kit=True,
        kit_component_only=True,
        kit_definition=ItemKitDefinition(
            components=[
                ItemKitComponent(
                    component_cost=3.14,
                    component_description="component_description_example",
                    component_merchant_item_id="component_merchant_item_id_example",
                    component_merchant_item_oid=1,
                    quantity=1,
                ),
            ],
        ),
        last_modified_dts="last_modified_dts_example",
        merchant_id="merchant_id_example",
        merchant_item_id="merchant_item_id_example",
        merchant_item_oid=1,
        options=[
            ItemOption(
                cost_if_specified=3.14,
                cost_per_letter=3.14,
                cost_per_line=3.14,
                ignore_if_default=True,
                label="label_example",
                label_translated_text_instance_oid=1,
                name="name_example",
                name_translated_text_instance_oid=1,
                one_time_fee=True,
                option_oid=1,
                required=True,
                system_option=True,
                type="dropdown",
                values=[
                    ItemOptionValue(
                        additional_dimension_application="none",
                        additional_items=[
                            ItemOptionValueAdditionalItem(
                                additional_merchant_item_id="additional_merchant_item_id_example",
                                additional_merchant_item_oid=1,
                            ),
                        ],
                        cost_change=3.14,
                        default_value=True,
                        digital_items=[
                            ItemOptionValueDigitalItem(
                                digital_item_oid=1,
                                original_filename="original_filename_example",
                            ),
                        ],
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        merchant_item_multimedia_oid=1,
                        option_value_oid=1,
                        percent_cost_change=3.14,
                        translated_text_instance_oid=1,
                        value="value_example",
                        weight_change=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        weight_change_percent=3.14,
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
            ),
        ],
        parent_category_id=1,
        parent_category_path="parent_category_path_example",
        payment_processing=ItemPaymentProcessing(
            block_prepaid=True,
            block_refunds=True,
            credit_card_transaction_type="credit_card_transaction_type_example",
            no_realtime_charge=True,
            payment_method_validity=[
                "payment_method_validity_example",
            ],
            rotating_transaction_gateway_codes=[
                "rotating_transaction_gateway_codes_example",
            ],
        ),
        physical=ItemPhysical(
            height=Distance(
                uom="IN",
                value=3.14,
            ),
            length=Distance(
                uom="IN",
                value=3.14,
            ),
            weight=Weight(
                uom="KG",
                value=3.14,
            ),
            width=Distance(
                uom="IN",
                value=3.14,
            ),
        ),
        pricing=ItemPricing(
            allow_arbitrary_cost=True,
            arbitrary_cost_velocity_code="arbitrary_cost_velocity_code_example",
            auto_order_cost=3.14,
            automatic_pricing_tier_name="automatic_pricing_tier_name_example",
            automatic_pricing_tier_oid=1,
            cogs=3.14,
            cost=3.14,
            currency_code="currency_code_example",
            manufacturer_suggested_retail_price=3.14,
            maximum_arbitrary_cost=3.14,
            minimum_advertised_price=3.14,
            minimum_arbitrary_cost=3.14,
            mix_and_match_group="mix_and_match_group_example",
            mix_and_match_group_oid=1,
            sale_cost=3.14,
            sale_end="sale_end_example",
            sale_start="sale_start_example",
            tiers=[
                ItemPricingTier(
                    default_tier=True,
                    discounts=[
                        ItemPricingTierDiscount(
                            cost=3.14,
                            quantity=1,
                        ),
                    ],
                    limit=ItemPricingTierLimit(
                        cumulative_order_limit=1,
                        exempt_from_minimum_item_count=True,
                        individual_order_limit=1,
                        multiple_quantity=1,
                        payment_method_validity=[
                            "payment_method_validity_example",
                        ],
                    ),
                    name="name_example",
                    pricing_tier_oid=1,
                ),
            ],
        ),
        properties=[
            ItemProperty(
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        realtime_pricing=ItemRealtimePricing(
            realtime_pricing_parameter="realtime_pricing_parameter_example",
            realtime_pricing_provider="realtime_pricing_provider_example",
            realtime_pricing_provider_oid=1,
        ),
        recommend_replenishment_days=1,
        related=ItemRelated(
            no_system_calculated_related_items=True,
            not_relatable=True,
            related_items=[
                ItemRelatedItem(
                    related_merchant_item_id="related_merchant_item_id_example",
                    related_merchant_item_oid=1,
                    type="System",
                ),
            ],
        ),
        reporting=ItemReporting(
            report_as_upsell=True,
            report_pickable_quantities=[
                1,
            ],
        ),
        restriction=ItemRestriction(
            exclude_coupon=True,
            exclude_from_free_promotion=True,
            items=[
                ItemRestrictionItem(
                    restrict_merchant_item_id="restrict_merchant_item_id_example",
                    restrict_merchant_item_oid=1,
                    type="can not be purchased with",
                ),
            ],
            maximum_quantity=1,
            minimum_quantity=1,
            multiple_quantity=1,
            one_per_customer=True,
            purchase_separately=True,
        ),
        revguard=ItemRevguard(
            revguard_canceled_csr_prompt_group=1,
            revguard_canceled_ivr_prompt_group=1,
            revguard_canceled_web_prompt_group=1,
            revguard_client_brand=1,
            revguard_csr_prompt_group=1,
            revguard_ivr_prompt_group=1,
            revguard_web_prompt_group=1,
        ),
        reviews=ItemReviews(
            has_approved_review=True,
            has_review=True,
            individual_reviews=[
                ItemReview(
                    customer_profile_oid=1,
                    featured=True,
                    helperful_no_votes=1,
                    helpful_yes_votes=1,
                    merchant_reply="merchant_reply_example",
                    order_id="order_id_example",
                    overall=3.14,
                    rating_name1="rating_name1_example",
                    rating_name10="rating_name10_example",
                    rating_name2="rating_name2_example",
                    rating_name3="rating_name3_example",
                    rating_name4="rating_name4_example",
                    rating_name5="rating_name5_example",
                    rating_name6="rating_name6_example",
                    rating_name7="rating_name7_example",
                    rating_name8="rating_name8_example",
                    rating_name9="rating_name9_example",
                    rating_score1=3.14,
                    rating_score10=3.14,
                    rating_score2=3.14,
                    rating_score3=3.14,
                    rating_score4=3.14,
                    rating_score5=3.14,
                    rating_score6=3.14,
                    rating_score7=3.14,
                    rating_score8=3.14,
                    rating_score9=3.14,
                    recommend_store_to_friend=1,
                    recommend_to_friend=True,
                    review="review_example",
                    review_oid=1,
                    reviewed_nickname="reviewed_nickname_example",
                    reviewer_email="reviewer_email_example",
                    reviewer_location="reviewer_location_example",
                    status="approved",
                    store_feedback="store_feedback_example",
                    submitted_dts="submitted_dts_example",
                    title="title_example",
                ),
            ],
            review_count=1,
            review_overall=3.14,
            review_template_name="review_template_name_example",
            review_template_oid=1,
            reviewable=True,
            share_reviews_with_merchant_item_id="share_reviews_with_merchant_item_id_example",
            share_reviews_with_merchant_item_oid=1,
        ),
        salesforce=ItemSalesforce(
            sfdc_pricebook_id="sfdc_pricebook_id_example",
            sfdc_product_id="sfdc_product_id_example",
        ),
        shipping=ItemShipping(
            allow_back_order=True,
            amazon_fba=True,
            case_inner_packs=1,
            case_units=1,
            cases=[
                ItemShippingCase(
                    case_label="case_label_example",
                    case_merchant_item_id="case_merchant_item_id_example",
                    case_merchant_item_oid=1,
                    quantity=1,
                ),
            ],
            collect_serial_numbers=True,
            country_code_of_origin="country_code_of_origin_example",
            customs_description="customs_description_example",
            customs_value=3.14,
            delivery_on_friday=True,
            delivery_on_monday=True,
            delivery_on_saturday=True,
            delivery_on_sunday=True,
            delivery_on_thursday=True,
            delivery_on_tuesday=True,
            delivery_on_wednesday=True,
            destination_markups=[
                ItemShippingDestinationMarkup(
                    adult_signature_required=True,
                    country_code="country_code_example",
                    flat_fee=3.14,
                    per_item=3.14,
                    postal_code="postal_code_example",
                    shipping_method="shipping_method_example",
                    state="state_example",
                ),
            ],
            destination_restrictions=[
                ItemShippingDestinationRestriction(
                    country_code="country_code_example",
                    state="state_example",
                    validity="valid only for",
                ),
            ],
            distribution_centers=[
                ItemShippingDistributionCenter(
                    allocated_to_placed_orders=3.14,
                    allocated_to_shopping_carts=3.14,
                    available_to_allocate=3.14,
                    cogs=3.14,
                    desired_inventory_level=3.14,
                    distribution_center_code="distribution_center_code_example",
                    distribution_center_oid=1,
                    eta="eta_example",
                    handles=True,
                    inventory_level=3.14,
                    maximum_backorder=1,
                    reorder_inventory_level=3.14,
                    sku="sku_example",
                    stock_picking_location="stock_picking_location_example",
                ),
            ],
            eta="eta_example",
            free_shipping=True,
            freight_class="freight_class_example",
            hazmat=True,
            hold_for_transmission=True,
            made_to_order=True,
            made_to_order_lead_time=1,
            max_days_time_in_transit=1,
            methods=[
                ItemShippingMethod(
                    cost=3.14,
                    each_additional_item_markup=3.14,
                    filter_to_if_available=True,
                    first_item_markup=3.14,
                    fixed_shipping_cost=3.14,
                    flat_fee_markup=3.14,
                    free_shipping=True,
                    per_item_fee_markup=3.14,
                    percentage_markup=3.14,
                    percentage_of_item_markup=3.14,
                    relax_restrictions_on_upsell=True,
                    shipping_method="shipping_method_example",
                    shipping_method_oid=1,
                    shipping_method_validity="invalid for",
                    signature_required=True,
                ),
            ],
            no_shipping_discount=True,
            package_requirements=[
                ItemShippingPackageRequirement(
                    package_name="package_name_example",
                    package_oid=1,
                ),
            ],
            perishable_class_name="perishable_class_name_example",
            perishable_class_oid=1,
            preorder=True,
            require_delivery_date=True,
            restrict_shipment_on_friday=True,
            restrict_shipment_on_monday=True,
            restrict_shipment_on_saturday=True,
            restrict_shipment_on_sunday=True,
            restrict_shipment_on_thursday=True,
            restrict_shipment_on_tuesday=True,
            restrict_shipment_on_wednesday=True,
            ship_separately=True,
            ship_separately_additional_weight=Weight(
                uom="KG",
                value=3.14,
            ),
            ship_separately_height=Distance(
                uom="IN",
                value=3.14,
            ),
            ship_separately_length=Distance(
                uom="IN",
                value=3.14,
            ),
            ship_separately_package_special_type="ship_separately_package_special_type_example",
            ship_separately_width=Distance(
                uom="IN",
                value=3.14,
            ),
            special_product_type="special_product_type_example",
            track_inventory=True,
        ),
        tags=ItemTags(
            tags=[
                ItemTag(
                    tag_type="item",
                    tag_value="tag_value_example",
                ),
            ],
        ),
        tax=ItemTax(
            exemptions=[
                ItemTaxExemption(
                    city="city_example",
                    country_code="country_code_example",
                    county="county_example",
                    postal_code="postal_code_example",
                    state_code="state_code_example",
                ),
            ],
            tax_free=True,
            tax_product_type="",
            taxable_cost=3.14,
        ),
        third_party_email_marketing=[
            ItemThirdPartyEmailMarketing(
                add_tags=[
                    "add_tags_example",
                ],
                provider_name="ActiveCampaign",
                remove_tags=[
                    "remove_tags_example",
                ],
                subscribe_lists=[
                    "subscribe_lists_example",
                ],
                unsubscribe_lists=[
                    "unsubscribe_lists_example",
                ],
            ),
        ],
        variant_items=[
            ItemVariantItem(
                description="description_example",
                merchant_item_multimedia_oid=1,
                variant_merchant_item_id="variant_merchant_item_id_example",
                variant_merchant_item_oid=1,
                variation_options=[
                    "variation_options_example",
                ],
                variations=[
                    "variations_example",
                ],
            ),
        ],
        variations=[
            ItemVariation(
                default_text="default_text_example",
                default_text_translated_text_instance_oid=1,
                name="name_example",
                name_translated_text_instance_oid=1,
                options=[
                    ItemVariationOption(
                        default_option=True,
                        merchant_item_multimedia_oid=1,
                        translated_text_instance_oid=1,
                        value="value_example",
                    ),
                ],
            ),
        ],
        wishlist_member=ItemWishlistMember(
            wishlist_member_instance_description="wishlist_member_instance_description_example",
            wishlist_member_instance_oid=1,
            wishlist_member_sku="wishlist_member_sku_example",
        ),
    ) # Item | Item to update
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an item
        api_response = api_instance.update_item(merchant_item_oid, item)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->update_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an item
        api_response = api_instance.update_item(merchant_item_oid, item, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->update_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid to update. |
 **item** | [**Item**](Item.md)| Item to update |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **update_items**
> ItemsResponse update_items(items_request)

Update multiple items

Update multiple item on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.items_response import ItemsResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.items_request import ItemsRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    items_request = ItemsRequest(
        items=[
            Item(
                accounting=ItemAccounting(
                    accounting_code="accounting_code_example",
                    qb_class="qb_class_example",
                ),
                amember=ItemAmember(
                    amember_payment_duration_days=1,
                    amember_product_id="amember_product_id_example",
                ),
                auto_order=ItemAutoOrder(
                    auth_future_amount=3.14,
                    auth_test_amount=3.14,
                    auto_order_cancel_charge_minimum_balance=True,
                    auto_order_cancel_item_id="auto_order_cancel_item_id_example",
                    auto_order_cancel_item_oid=1,
                    auto_order_cancel_minimum_life_time_count=1,
                    auto_order_cancel_minimum_life_time_value=3.14,
                    auto_order_cancel_minimum_rebill_count=1,
                    auto_order_cancel_minimum_rebill_value=3.14,
                    auto_order_downgrade_items=[
                        "auto_order_downgrade_items_example",
                    ],
                    auto_order_paused=True,
                    auto_order_prohibit_expiring_cards=1,
                    auto_order_schedules=[
                        "auto_order_schedules_example",
                    ],
                    auto_order_upgrade_items=[
                        "auto_order_upgrade_items_example",
                    ],
                    auto_order_upsell=True,
                    auto_order_upsell_no_easy_cancel=True,
                    auto_order_upsell_one_per_customer=True,
                    auto_orderable=True,
                    cancel_other_auto_orders=True,
                    free_shipping_auto_order=True,
                    refund_other_auto_orders=True,
                    steps=[
                        ItemAutoOrderStep(
                            arbitrary_schedule_days=1,
                            arbitrary_unit_cost=3.14,
                            arbitrary_unit_cost_schedules=[
                                ItemAutoOrderStepArbitraryUnitCostSchedule(
                                    arbitrary_unit_cost=3.14,
                                    retry_days=1,
                                ),
                            ],
                            grandfather_pricing=[
                                ItemAutoOrderStepGrandfatherPricing(
                                    on_or_before_date="on_or_before_date_example",
                                    unit_cost=3.14,
                                ),
                            ],
                            managed_by="managed_by_example",
                            pause_days=1,
                            pause_until_date="pause_until_date_example",
                            pause_until_day_of_month=1,
                            pause_until_minimum_delay_days=1,
                            preshipment_notice_days=1,
                            recurring_merchant_item_id="recurring_merchant_item_id_example",
                            recurring_merchant_item_oid=1,
                            repeat_count=1,
                            schedule="schedule_example",
                            subscribe_email_list_name="subscribe_email_list_name_example",
                            subscribe_email_list_oid=1,
                            type="item",
                        ),
                    ],
                ),
                ccbill=ItemCCBill(
                    ccbill_allowed_currencies="ccbill_allowed_currencies_example",
                    ccbill_allowed_types="ccbill_allowed_types_example",
                    ccbill_currency_code="ccbill_currency_code_example",
                    ccbill_form_name="ccbill_form_name_example",
                    ccbill_subaccount_id="ccbill_subaccount_id_example",
                    ccbill_subscription_type_id="ccbill_subscription_type_id_example",
                ),
                channel_partner_item_mappings=[
                    ItemChannelPartnerMapping(
                        barcode_ua="barcode_ua_example",
                        barcode_uc="barcode_uc_example",
                        barcode_ui="barcode_ui_example",
                        barcode_uk="barcode_uk_example",
                        buyer_catalog_number="buyer_catalog_number_example",
                        buyer_dpci="buyer_dpci_example",
                        buyer_item_number="buyer_item_number_example",
                        channel_partner_code="channel_partner_code_example",
                        channel_partner_oid=1,
                        cost=3.14,
                        from_item_id="from_item_id_example",
                        from_sku="from_sku_example",
                        mutually_defined_number="mutually_defined_number_example",
                        quantity_ratio_cp=1,
                        quantity_ratio_uc=1,
                        sku="sku_example",
                        unit_of_measure="unit_of_measure_example",
                        vendor_number="vendor_number_example",
                        vendor_style_number="vendor_style_number_example",
                    ),
                ],
                chargeback=ItemChargeback(
                    addendums=[
                        ItemChargebackAddendum(
                            chargeback_addendum_oid=1,
                            description="description_example",
                            file_size=1,
                            pages=1,
                        ),
                    ],
                    adjustment_requests=[
                        ItemChargebackAdjustmentRequest(
                            chargeback_adjustment_request_oid=1,
                            description="description_example",
                            reason_code="reason_code_example",
                        ),
                    ],
                ),
                checkout=ItemCheckout(
                    suppress_buysafe=True,
                    terms="terms_example",
                    terms_if_auto_order=True,
                    terms_translated_text_instance_oid=1,
                ),
                content=ItemContent(
                    assignments=[
                        ItemContentAssignment(
                            default_assignment=True,
                            group_oid=1,
                            group_path="group_path_example",
                            host="host_example",
                            sort_order=1,
                            url_part="url_part_example",
                        ),
                    ],
                    attributes=[
                        ItemContentAttribute(
                            name="name_example",
                            translated_text_instance_oid=1,
                            type="type_example",
                            value="value_example",
                        ),
                    ],
                    custom_thank_you_url="custom_thank_you_url_example",
                    exclude_from_search=True,
                    exclude_from_sitemap=True,
                    exclude_from_top_sellers=True,
                    extended_description="extended_description_example",
                    extended_description_translated_text_instance_oid=1,
                    meta_description="meta_description_example",
                    meta_keywords="meta_keywords_example",
                    meta_title="meta_title_example",
                    multimedia=[
                        ItemContentMultimedia(
                            cloud_url="cloud_url_example",
                            cloud_url_expiration="cloud_url_expiration_example",
                            code="code_example",
                            description="description_example",
                            exclude_from_gallery=True,
                            file_name="file_name_example",
                            height=1,
                            merchant_item_multimedia_oid=1,
                            orphan=True,
                            placeholder=True,
                            temp_multimedia_oid=1,
                            thumbnails=[
                                ItemContentMultimediaThumbnail(
                                    height=1,
                                    http_url="http_url_example",
                                    https_url="https_url_example",
                                    png_format=True,
                                    square=True,
                                    width=1,
                                ),
                            ],
                            type="Image",
                            url="url_example",
                            width=1,
                        ),
                    ],
                    new_item=True,
                    new_item_end="new_item_end_example",
                    new_item_start="new_item_start_example",
                    view_url="view_url_example",
                ),
                creation_dts="creation_dts_example",
                description="description_example",
                description_translated_text_instance_oid=1,
                digital_delivery=ItemDigitalDelivery(
                    activation_code_description="activation_code_description_example",
                    activation_code_low_warning=1,
                    activation_code_realtime_url="activation_code_realtime_url_example",
                    activation_code_shared_secret="activation_code_shared_secret_example",
                    activation_code_type="activation_code_type_example",
                    digital_items=[
                        ItemDigitalItem(
                            click_wrap_agreement="click_wrap_agreement_example",
                            creation_dts="creation_dts_example",
                            description="description_example",
                            digital_item_oid=1,
                            external_id="external_id_example",
                            file_size=1,
                            import_from_url="import_from_url_example",
                            mime_type="mime_type_example",
                            original_filename="original_filename_example",
                            pdf_meta=ItemDigitalItemPdfMeta(
                                assembly_allowed=True,
                                copy_allowed=True,
                                custom_footer="custom_footer_example",
                                custom_header="custom_header_example",
                                degraded_printing_allowed=True,
                                fillin_allowed=True,
                                modify_annotations_allowed=True,
                                modify_contents_allowed=True,
                                printing_allowed=True,
                                screen_readers_allowed=True,
                                tagged=True,
                            ),
                        ),
                    ],
                ),
                ebay=ItemEbay(
                    active=True,
                    category_id=1,
                    category_specifics=[
                        ItemEbayCategorySpecific(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    condition_description="condition_description_example",
                    condition_id=1,
                    consecutive_failures=1,
                    custom_category1=1,
                    custom_category2=1,
                    dispatch_time_max=1,
                    domestic_1_additional_cost=3.14,
                    domestic_1_first_cost=3.14,
                    domestic_2_additional_cost=3.14,
                    domestic_2_first_cost=3.14,
                    domestic_3_additional_cost=3.14,
                    domestic_3_first_cost=3.14,
                    domestic_4_additional_cost=3.14,
                    domestic_4_first_cost=3.14,
                    ebay_auction_id="ebay_auction_id_example",
                    ebay_specific_inventory=1,
                    ebay_template_name="ebay_template_name_example",
                    ebay_template_oid=1,
                    end_time="end_time_example",
                    free_shipping=True,
                    free_shipping_method="free_shipping_method_example",
                    international_1_additional_cost=3.14,
                    international_1_first_cost=3.14,
                    international_2_additional_cost=3.14,
                    international_2_first_cost=3.14,
                    international_3_additional_cost=3.14,
                    international_3_first_cost=3.14,
                    international_4_additional_cost=3.14,
                    international_4_first_cost=3.14,
                    last_status_dts="last_status_dts_example",
                    listed_dispatch_time_max=1,
                    listed_ebay_template_oid=1,
                    listing_dts="listing_dts_example",
                    listing_duration="listing_duration_example",
                    listing_price=3.14,
                    listing_price_override=3.14,
                    listing_type="listing_type_example",
                    marketplace_analysis=ItemEbayMarketPlaceAnalysis(
                        adjusted_price=3.14,
                        adjusted_shipping=3.14,
                        adjusted_total=3.14,
                        cogs=3.14,
                        final_value_fee=3.14,
                        minimum_advertised_price=3.14,
                        other_listings=[
                            ItemEbayMarketListing(
                                auction_id="auction_id_example",
                                price=3.14,
                                seller="seller_example",
                                shipping=3.14,
                                total=3.14,
                            ),
                        ],
                        our_listing=ItemEbayMarketListing(
                            auction_id="auction_id_example",
                            price=3.14,
                            seller="seller_example",
                            shipping=3.14,
                            total=3.14,
                        ),
                        overhead=3.14,
                        profit_potential=3.14,
                    ),
                    marketplace_analysis_perform=True,
                    marketplace_final_value_fee_percentage=3.14,
                    marketplace_last_check_dts="marketplace_last_check_dts_example",
                    marketplace_lowest=True,
                    marketplace_map_violation=True,
                    marketplace_multiplier=3.14,
                    marketplace_other_price=3.14,
                    marketplace_other_seller="marketplace_other_seller_example",
                    marketplace_other_shipping=3.14,
                    marketplace_other_total=3.14,
                    marketplace_our_additional_profit_potential=3.14,
                    marketplace_our_price=3.14,
                    marketplace_our_profit=3.14,
                    marketplace_our_shipping=3.14,
                    marketplace_our_total=3.14,
                    marketplace_overhead=3.14,
                    marketplace_profitable=True,
                    next_attempt_dts="next_attempt_dts_example",
                    next_listing_duration="next_listing_duration_example",
                    no_promotional_shipping=True,
                    packaging_handling_costs=3.14,
                    previous_ebay_auction_id="previous_ebay_auction_id_example",
                    quantity=1,
                    reserve_price=3.14,
                    send_dimensions_and_weight="send_dimensions_and_weight_example",
                    start_time="start_time_example",
                    status="status_example",
                    target_dispatch_time_max=1,
                ),
                email_notifications=ItemEmailNotifications(
                    skip_receipt=True,
                    skip_shipment_notification=True,
                ),
                enrollment123=ItemEnrollment123(
                    enrollment123_product_code="enrollment123_product_code_example",
                ),
                fulfillment_addons=[
                    ItemFulfillmentAddon(
                        add_item_id="add_item_id_example",
                        add_item_oid=1,
                        initial_order_only=True,
                        once_per_order=True,
                        quantity=1,
                    ),
                ],
                gift_certificate=ItemGiftCertificate(
                    gift_certificate=True,
                    gift_certificate_expiration_days=1,
                ),
                google_product_search=ItemGoogleProductSearch(
                    adwords_grouping="adwords_grouping_example",
                    adwords_label1="adwords_label1_example",
                    adwords_label2="adwords_label2_example",
                    adwords_label3="adwords_label3_example",
                    adwords_label4="adwords_label4_example",
                    adwords_label5="adwords_label5_example",
                    age_group="age_group_example",
                    available_at_physical_store=True,
                    book_author="book_author_example",
                    book_format="book_format_example",
                    book_isbn="book_isbn_example",
                    book_publisher="book_publisher_example",
                    category_description="category_description_example",
                    color="color_example",
                    condition="condition_example",
                    custom_label0="custom_label0_example",
                    custom_label1="custom_label1_example",
                    custom_label2="custom_label2_example",
                    custom_label3="custom_label3_example",
                    custom_label4="custom_label4_example",
                    gender="gender_example",
                    google_product_category="google_product_category_example",
                    music_artist="music_artist_example",
                    music_format="music_format_example",
                    music_release_date="music_release_date_example",
                    omit_from_feed=True,
                    product_type="product_type_example",
                    promotion_id1="promotion_id1_example",
                    promotion_id10="promotion_id10_example",
                    promotion_id2="promotion_id2_example",
                    promotion_id3="promotion_id3_example",
                    promotion_id4="promotion_id4_example",
                    promotion_id5="promotion_id5_example",
                    promotion_id6="promotion_id6_example",
                    promotion_id7="promotion_id7_example",
                    promotion_id8="promotion_id8_example",
                    promotion_id9="promotion_id9_example",
                    search_dts="search_dts_example",
                    search_lowest_price=3.14,
                    search_lowest_url="search_lowest_url_example",
                    search_position=1,
                    shipping_label="shipping_label_example",
                    size="size_example",
                    video_director="video_director_example",
                    video_format="video_format_example",
                    video_rating="video_rating_example",
                    video_release_date="video_release_date_example",
                    video_starring="video_starring_example",
                ),
                identifiers=ItemIdentifiers(
                    barcode="barcode_example",
                    barcode_gtin12="barcode_gtin12_example",
                    barcode_gtin14="barcode_gtin14_example",
                    barcode_upc11="barcode_upc11_example",
                    barcode_upc12="barcode_upc12_example",
                    manufacturer_name="manufacturer_name_example",
                    manufacturer_sku="manufacturer_sku_example",
                    unspsc="unspsc_example",
                ),
                inactive=True,
                instant_payment_notifications=ItemInstantPaymentNotifications(
                    notifications=[
                        ItemInstantPaymentNotification(
                            post_operation=True,
                            successful_response_text="successful_response_text_example",
                            url="url_example",
                        ),
                    ],
                ),
                internal=ItemInternal(
                    memo="memo_example",
                ),
                kit=True,
                kit_component_only=True,
                kit_definition=ItemKitDefinition(
                    components=[
                        ItemKitComponent(
                            component_cost=3.14,
                            component_description="component_description_example",
                            component_merchant_item_id="component_merchant_item_id_example",
                            component_merchant_item_oid=1,
                            quantity=1,
                        ),
                    ],
                ),
                last_modified_dts="last_modified_dts_example",
                merchant_id="merchant_id_example",
                merchant_item_id="merchant_item_id_example",
                merchant_item_oid=1,
                options=[
                    ItemOption(
                        cost_if_specified=3.14,
                        cost_per_letter=3.14,
                        cost_per_line=3.14,
                        ignore_if_default=True,
                        label="label_example",
                        label_translated_text_instance_oid=1,
                        name="name_example",
                        name_translated_text_instance_oid=1,
                        one_time_fee=True,
                        option_oid=1,
                        required=True,
                        system_option=True,
                        type="dropdown",
                        values=[
                            ItemOptionValue(
                                additional_dimension_application="none",
                                additional_items=[
                                    ItemOptionValueAdditionalItem(
                                        additional_merchant_item_id="additional_merchant_item_id_example",
                                        additional_merchant_item_oid=1,
                                    ),
                                ],
                                cost_change=3.14,
                                default_value=True,
                                digital_items=[
                                    ItemOptionValueDigitalItem(
                                        digital_item_oid=1,
                                        original_filename="original_filename_example",
                                    ),
                                ],
                                height=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                length=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                merchant_item_multimedia_oid=1,
                                option_value_oid=1,
                                percent_cost_change=3.14,
                                translated_text_instance_oid=1,
                                value="value_example",
                                weight_change=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                weight_change_percent=3.14,
                                width=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                            ),
                        ],
                    ),
                ],
                parent_category_id=1,
                parent_category_path="parent_category_path_example",
                payment_processing=ItemPaymentProcessing(
                    block_prepaid=True,
                    block_refunds=True,
                    credit_card_transaction_type="credit_card_transaction_type_example",
                    no_realtime_charge=True,
                    payment_method_validity=[
                        "payment_method_validity_example",
                    ],
                    rotating_transaction_gateway_codes=[
                        "rotating_transaction_gateway_codes_example",
                    ],
                ),
                physical=ItemPhysical(
                    height=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    length=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                    width=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                ),
                pricing=ItemPricing(
                    allow_arbitrary_cost=True,
                    arbitrary_cost_velocity_code="arbitrary_cost_velocity_code_example",
                    auto_order_cost=3.14,
                    automatic_pricing_tier_name="automatic_pricing_tier_name_example",
                    automatic_pricing_tier_oid=1,
                    cogs=3.14,
                    cost=3.14,
                    currency_code="currency_code_example",
                    manufacturer_suggested_retail_price=3.14,
                    maximum_arbitrary_cost=3.14,
                    minimum_advertised_price=3.14,
                    minimum_arbitrary_cost=3.14,
                    mix_and_match_group="mix_and_match_group_example",
                    mix_and_match_group_oid=1,
                    sale_cost=3.14,
                    sale_end="sale_end_example",
                    sale_start="sale_start_example",
                    tiers=[
                        ItemPricingTier(
                            default_tier=True,
                            discounts=[
                                ItemPricingTierDiscount(
                                    cost=3.14,
                                    quantity=1,
                                ),
                            ],
                            limit=ItemPricingTierLimit(
                                cumulative_order_limit=1,
                                exempt_from_minimum_item_count=True,
                                individual_order_limit=1,
                                multiple_quantity=1,
                                payment_method_validity=[
                                    "payment_method_validity_example",
                                ],
                            ),
                            name="name_example",
                            pricing_tier_oid=1,
                        ),
                    ],
                ),
                properties=[
                    ItemProperty(
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                realtime_pricing=ItemRealtimePricing(
                    realtime_pricing_parameter="realtime_pricing_parameter_example",
                    realtime_pricing_provider="realtime_pricing_provider_example",
                    realtime_pricing_provider_oid=1,
                ),
                recommend_replenishment_days=1,
                related=ItemRelated(
                    no_system_calculated_related_items=True,
                    not_relatable=True,
                    related_items=[
                        ItemRelatedItem(
                            related_merchant_item_id="related_merchant_item_id_example",
                            related_merchant_item_oid=1,
                            type="System",
                        ),
                    ],
                ),
                reporting=ItemReporting(
                    report_as_upsell=True,
                    report_pickable_quantities=[
                        1,
                    ],
                ),
                restriction=ItemRestriction(
                    exclude_coupon=True,
                    exclude_from_free_promotion=True,
                    items=[
                        ItemRestrictionItem(
                            restrict_merchant_item_id="restrict_merchant_item_id_example",
                            restrict_merchant_item_oid=1,
                            type="can not be purchased with",
                        ),
                    ],
                    maximum_quantity=1,
                    minimum_quantity=1,
                    multiple_quantity=1,
                    one_per_customer=True,
                    purchase_separately=True,
                ),
                revguard=ItemRevguard(
                    revguard_canceled_csr_prompt_group=1,
                    revguard_canceled_ivr_prompt_group=1,
                    revguard_canceled_web_prompt_group=1,
                    revguard_client_brand=1,
                    revguard_csr_prompt_group=1,
                    revguard_ivr_prompt_group=1,
                    revguard_web_prompt_group=1,
                ),
                reviews=ItemReviews(
                    has_approved_review=True,
                    has_review=True,
                    individual_reviews=[
                        ItemReview(
                            customer_profile_oid=1,
                            featured=True,
                            helperful_no_votes=1,
                            helpful_yes_votes=1,
                            merchant_reply="merchant_reply_example",
                            order_id="order_id_example",
                            overall=3.14,
                            rating_name1="rating_name1_example",
                            rating_name10="rating_name10_example",
                            rating_name2="rating_name2_example",
                            rating_name3="rating_name3_example",
                            rating_name4="rating_name4_example",
                            rating_name5="rating_name5_example",
                            rating_name6="rating_name6_example",
                            rating_name7="rating_name7_example",
                            rating_name8="rating_name8_example",
                            rating_name9="rating_name9_example",
                            rating_score1=3.14,
                            rating_score10=3.14,
                            rating_score2=3.14,
                            rating_score3=3.14,
                            rating_score4=3.14,
                            rating_score5=3.14,
                            rating_score6=3.14,
                            rating_score7=3.14,
                            rating_score8=3.14,
                            rating_score9=3.14,
                            recommend_store_to_friend=1,
                            recommend_to_friend=True,
                            review="review_example",
                            review_oid=1,
                            reviewed_nickname="reviewed_nickname_example",
                            reviewer_email="reviewer_email_example",
                            reviewer_location="reviewer_location_example",
                            status="approved",
                            store_feedback="store_feedback_example",
                            submitted_dts="submitted_dts_example",
                            title="title_example",
                        ),
                    ],
                    review_count=1,
                    review_overall=3.14,
                    review_template_name="review_template_name_example",
                    review_template_oid=1,
                    reviewable=True,
                    share_reviews_with_merchant_item_id="share_reviews_with_merchant_item_id_example",
                    share_reviews_with_merchant_item_oid=1,
                ),
                salesforce=ItemSalesforce(
                    sfdc_pricebook_id="sfdc_pricebook_id_example",
                    sfdc_product_id="sfdc_product_id_example",
                ),
                shipping=ItemShipping(
                    allow_back_order=True,
                    amazon_fba=True,
                    case_inner_packs=1,
                    case_units=1,
                    cases=[
                        ItemShippingCase(
                            case_label="case_label_example",
                            case_merchant_item_id="case_merchant_item_id_example",
                            case_merchant_item_oid=1,
                            quantity=1,
                        ),
                    ],
                    collect_serial_numbers=True,
                    country_code_of_origin="country_code_of_origin_example",
                    customs_description="customs_description_example",
                    customs_value=3.14,
                    delivery_on_friday=True,
                    delivery_on_monday=True,
                    delivery_on_saturday=True,
                    delivery_on_sunday=True,
                    delivery_on_thursday=True,
                    delivery_on_tuesday=True,
                    delivery_on_wednesday=True,
                    destination_markups=[
                        ItemShippingDestinationMarkup(
                            adult_signature_required=True,
                            country_code="country_code_example",
                            flat_fee=3.14,
                            per_item=3.14,
                            postal_code="postal_code_example",
                            shipping_method="shipping_method_example",
                            state="state_example",
                        ),
                    ],
                    destination_restrictions=[
                        ItemShippingDestinationRestriction(
                            country_code="country_code_example",
                            state="state_example",
                            validity="valid only for",
                        ),
                    ],
                    distribution_centers=[
                        ItemShippingDistributionCenter(
                            allocated_to_placed_orders=3.14,
                            allocated_to_shopping_carts=3.14,
                            available_to_allocate=3.14,
                            cogs=3.14,
                            desired_inventory_level=3.14,
                            distribution_center_code="distribution_center_code_example",
                            distribution_center_oid=1,
                            eta="eta_example",
                            handles=True,
                            inventory_level=3.14,
                            maximum_backorder=1,
                            reorder_inventory_level=3.14,
                            sku="sku_example",
                            stock_picking_location="stock_picking_location_example",
                        ),
                    ],
                    eta="eta_example",
                    free_shipping=True,
                    freight_class="freight_class_example",
                    hazmat=True,
                    hold_for_transmission=True,
                    made_to_order=True,
                    made_to_order_lead_time=1,
                    max_days_time_in_transit=1,
                    methods=[
                        ItemShippingMethod(
                            cost=3.14,
                            each_additional_item_markup=3.14,
                            filter_to_if_available=True,
                            first_item_markup=3.14,
                            fixed_shipping_cost=3.14,
                            flat_fee_markup=3.14,
                            free_shipping=True,
                            per_item_fee_markup=3.14,
                            percentage_markup=3.14,
                            percentage_of_item_markup=3.14,
                            relax_restrictions_on_upsell=True,
                            shipping_method="shipping_method_example",
                            shipping_method_oid=1,
                            shipping_method_validity="invalid for",
                            signature_required=True,
                        ),
                    ],
                    no_shipping_discount=True,
                    package_requirements=[
                        ItemShippingPackageRequirement(
                            package_name="package_name_example",
                            package_oid=1,
                        ),
                    ],
                    perishable_class_name="perishable_class_name_example",
                    perishable_class_oid=1,
                    preorder=True,
                    require_delivery_date=True,
                    restrict_shipment_on_friday=True,
                    restrict_shipment_on_monday=True,
                    restrict_shipment_on_saturday=True,
                    restrict_shipment_on_sunday=True,
                    restrict_shipment_on_thursday=True,
                    restrict_shipment_on_tuesday=True,
                    restrict_shipment_on_wednesday=True,
                    ship_separately=True,
                    ship_separately_additional_weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                    ship_separately_height=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    ship_separately_length=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    ship_separately_package_special_type="ship_separately_package_special_type_example",
                    ship_separately_width=Distance(
                        uom="IN",
                        value=3.14,
                    ),
                    special_product_type="special_product_type_example",
                    track_inventory=True,
                ),
                tags=ItemTags(
                    tags=[
                        ItemTag(
                            tag_type="item",
                            tag_value="tag_value_example",
                        ),
                    ],
                ),
                tax=ItemTax(
                    exemptions=[
                        ItemTaxExemption(
                            city="city_example",
                            country_code="country_code_example",
                            county="county_example",
                            postal_code="postal_code_example",
                            state_code="state_code_example",
                        ),
                    ],
                    tax_free=True,
                    tax_product_type="",
                    taxable_cost=3.14,
                ),
                third_party_email_marketing=[
                    ItemThirdPartyEmailMarketing(
                        add_tags=[
                            "add_tags_example",
                        ],
                        provider_name="ActiveCampaign",
                        remove_tags=[
                            "remove_tags_example",
                        ],
                        subscribe_lists=[
                            "subscribe_lists_example",
                        ],
                        unsubscribe_lists=[
                            "unsubscribe_lists_example",
                        ],
                    ),
                ],
                variant_items=[
                    ItemVariantItem(
                        description="description_example",
                        merchant_item_multimedia_oid=1,
                        variant_merchant_item_id="variant_merchant_item_id_example",
                        variant_merchant_item_oid=1,
                        variation_options=[
                            "variation_options_example",
                        ],
                        variations=[
                            "variations_example",
                        ],
                    ),
                ],
                variations=[
                    ItemVariation(
                        default_text="default_text_example",
                        default_text_translated_text_instance_oid=1,
                        name="name_example",
                        name_translated_text_instance_oid=1,
                        options=[
                            ItemVariationOption(
                                default_option=True,
                                merchant_item_multimedia_oid=1,
                                translated_text_instance_oid=1,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
                wishlist_member=ItemWishlistMember(
                    wishlist_member_instance_description="wishlist_member_instance_description_example",
                    wishlist_member_instance_oid=1,
                    wishlist_member_sku="wishlist_member_sku_example",
                ),
            ),
        ],
    ) # ItemsRequest | Items to update (synchronous maximum 20 / asynchronous maximum 100)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)
    _async = True # bool | True if the operation should be run async.  No result returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple items
        api_response = api_instance.update_items(items_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->update_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple items
        api_response = api_instance.update_items(items_request, expand=expand, placeholders=placeholders, _async=_async)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **update_review**
> ItemReviewResponse update_review(review_oid, merchant_item_oid, review)

Update a review

Update an item review. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.item_review import ItemReview
from ultracart.model.item_review_response import ItemReviewResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    review_oid = 1 # int | The review oid to update.
    merchant_item_oid = 1 # int | The item oid the review is associated with.
    review = ItemReview(
        customer_profile_oid=1,
        featured=True,
        helperful_no_votes=1,
        helpful_yes_votes=1,
        merchant_reply="merchant_reply_example",
        order_id="order_id_example",
        overall=3.14,
        rating_name1="rating_name1_example",
        rating_name10="rating_name10_example",
        rating_name2="rating_name2_example",
        rating_name3="rating_name3_example",
        rating_name4="rating_name4_example",
        rating_name5="rating_name5_example",
        rating_name6="rating_name6_example",
        rating_name7="rating_name7_example",
        rating_name8="rating_name8_example",
        rating_name9="rating_name9_example",
        rating_score1=3.14,
        rating_score10=3.14,
        rating_score2=3.14,
        rating_score3=3.14,
        rating_score4=3.14,
        rating_score5=3.14,
        rating_score6=3.14,
        rating_score7=3.14,
        rating_score8=3.14,
        rating_score9=3.14,
        recommend_store_to_friend=1,
        recommend_to_friend=True,
        review="review_example",
        review_oid=1,
        reviewed_nickname="reviewed_nickname_example",
        reviewer_email="reviewer_email_example",
        reviewer_location="reviewer_location_example",
        status="approved",
        store_feedback="store_feedback_example",
        submitted_dts="submitted_dts_example",
        title="title_example",
    ) # ItemReview | Review to update

    # example passing only required values which don't have defaults set
    try:
        # Update a review
        api_response = api_instance.update_review(review_oid, merchant_item_oid, review)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->update_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_oid** | **int**| The review oid to update. |
 **merchant_item_oid** | **int**| The item oid the review is associated with. |
 **review** | [**ItemReview**](ItemReview.md)| Review to update |

### Return type

[**ItemReviewResponse**](ItemReviewResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **upload_temporary_multimedia**
> TempMultimediaResponse upload_temporary_multimedia(file)

Upload an image to the temporary multimedia.

Uploads an image and returns back meta information about the image as well as the identifier needed for the item update. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import item_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.temp_multimedia_response import TempMultimediaResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    file = open('/path/to/file', 'rb') # file_type | File to upload

    # example passing only required values which don't have defaults set
    try:
        # Upload an image to the temporary multimedia.
        api_response = api_instance.upload_temporary_multimedia(file)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ItemApi->upload_temporary_multimedia: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| File to upload |

### Return type

[**TempMultimediaResponse**](TempMultimediaResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

