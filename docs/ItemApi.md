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
[**get_item_shipping_distribution_center_by_code**](ItemApi.md#get_item_shipping_distribution_center_by_code) | **GET** /item/items/{merchant_item_oid}/shipping/distribution_centers/by_code/{distribution_center_code} | Retrieve an item shipping distribution center
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
[**update_item_shipping_distribution_center_by_code**](ItemApi.md#update_item_shipping_distribution_center_by_code) | **PUT** /item/items/{merchant_item_oid}/shipping/distribution_centers/by_code/{distribution_center_code} | Update an item shipping distribution center
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
# Digital item operations sample script

from ultracart.api_client import ApiException
from item_functions import insert_sample_digital_item, delete_sample_digital_item

try:
    digital_item_oid = insert_sample_digital_item()
    delete_sample_digital_item(digital_item_oid)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)  # Handle gracefully as noted in original comment
    exit(1)
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
# Sample item operations script

from ultracart.api_client import ApiException
from item_functions import insert_sample_item, delete_sample_item

try:
    item_oid = insert_sample_item()
    delete_sample_item(item_oid)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)  # Handle gracefully as noted in original comment
    exit(1)
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
# Delete a specific user review for an item
#
# This would most likely be used by a merchant who has cached all
# reviews on a separate site and then wishes to remove a particular review.
#
# The merchant_item_oid is a unique identifier used by UltraCart. If you do not know your item's oid, call
# ItemApi.get_item_by_merchant_item_id() to retrieve the item, and then get its oid
#
# The review_oid is a unique identifier used by UltraCart. If you do not know a review's oid, call
# ItemApi.get_reviews() to get all reviews where you can then grab the oid from an item.
#
# Success returns back a status code of 204 (No Content)

from ultracart.apis import ItemApi
from samples import api_client

# Create item API instance
item_api = ItemApi(api_client())

# Specify item and review OIDs
merchant_item_oid = 123456
review_oid = 987654

# Delete the review
item_api.delete_review(review_oid, merchant_item_oid)
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
# Digital Item Retrieval Example
#
# Please Note!
# Digital Items are not normal items you sell on your site. They are digital files that you may add to
# a library and then attach to a normal item as an accessory or the main item itself.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1376485/Digital+Items

from ultracart.api_client import ApiException
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_digital_item, delete_sample_digital_item

try:
    # Create a digital item to retrieve
    digital_item_oid = insert_sample_digital_item()

    # Get the item API and retrieve the digital item
    item_api = ItemApi(api_client())
    api_response = item_api.get_digital_item(digital_item_oid)
    digital_item = api_response.digital_item

    # Print the retrieved item
    print('The following item was retrieved via get_digital_item():')
    print(digital_item)

    # Clean up the sample digital item
    delete_sample_digital_item(digital_item_oid)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)  # Handle gracefully as noted in original comment
    exit(1)
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
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_digital_item

try:
    """
    Please Note!
    Digital Items are not normal items you sell on your site.  They are digital files that you may add to
    a library and then attach to a normal item as an accessory or the main item itself.
    See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1376485/Digital+Items
    """

    # Create a digital item to get an item
    digital_item_oid = insert_sample_digital_item()

    # Create Item API client
    item_api = ItemApi(api_client())

    # Set parameters for getDigitalItems
    limit = 100
    offset = 0
    since = None  # digital items do not use since. leave as None.
    sort = None  # if None, use default of original_filename
    expand = None  # digital items have no expansion. leave as None. this value is ignored
    placeholders = None  # digital items have no placeholders. leave as None.

    # Retrieve digital items
    api_response = item_api.get_digital_items(limit=limit, offset=offset, since=since,
                                              sort=sort, expand=expand,
                                              placeholders=placeholders)
    digital_items = api_response.get_digital_items()  # assuming this succeeded

    print('The following items were retrieved via get_digital_items():')
    for digital_item in digital_items:
        print(digital_item)

except Exception as e:
    print('An exception occurred. Please review the following error:')
    print(e)
    raise
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
import uuid
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_digital_item, delete_sample_digital_item

try:
    """
    Please Note!
    Digital Items are not normal items you sell on your site.  They are digital files that you may add to
    a library and then attach to a normal item as an accessory or the main item itself.
    See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1376485/Digital+Items
    """

    # Generate a unique external ID
    external_id = str(uuid.uuid4())
    print(f'My external id is {external_id}')

    # Create digital item with a specific external id I can later use
    digital_item_oid = insert_sample_digital_item(external_id)

    # Create Item API client
    item_api = ItemApi(api_client())

    # Retrieve digital items by external ID
    api_response = item_api.get_digital_items_by_external_id(external_id)
    digital_items = api_response.get_digital_items()  # assuming this succeeded

    print('The following item was retrieved via get_digital_items_by_external_id():')
    print(digital_items)

    # Delete the sample digital item
    delete_sample_digital_item(digital_item_oid)

except Exception as e:
    print('An exception occurred. Please review the following error:')
    print(e)
    raise
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
# Retrieve a list of item inventories.
# This method may be called once every 15 minutes.  More than that will result in a 429 response.

from ultracart.apis import ItemApi
from ultracart.api_client import ApiException
from samples import api_client

try:
    # Create the Item API instance
    item_api = ItemApi(api_client())

    # Get the inventory snapshot
    api_response = item_api.get_inventory_snapshot()
    inventories = api_response.inventories

    # Iterate and print inventories
    for inventory in inventories:
        print(inventory)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)  # Handle gracefully as noted in original comment
    exit(1)
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
from ultracart.apis import ItemApi, CustomerApi
from samples import api_client
from item_functions import insert_sample_item, delete_sample_item

try:
    """
    Of the two getItem methods, you'll probably always use get_item_by_merchant_item_id instead of this one.
    Most item work is done with the item id, not the item oid. The latter is only meaningful as a primary
    key in the UltraCart databases. But here is an example of using get_item(). We take the long route here
    of retrieving the item using get_item_by_merchant_item_id to obtain the oid rather than hard-coding it.
    We do this because these samples are used in our quality control system and run repeatedly.
    """

    # Insert a sample item
    item_id = insert_sample_item()

    # Create API clients
    item_api = ItemApi(api_client())
    customer_api = CustomerApi(api_client())  # only needed for accessing reviewer information below

    # The expand variable is None in the following call. We just need the base object this time.
    api_response = item_api.get_item_by_merchant_item_id(item_id, expand=None, active=False)
    item = api_response.get_item()  # assuming this succeeded

    merchant_item_oid = item.get_merchant_item_oid()

    """
    The real devil in the getItem calls is the expansion, making sure you return everything you need without
    returning everything since these objects are extremely large.

    These are the possible expansion values:
    accounting, amember, auto_order, auto_order.steps, ccbill, channel_partner_mappings,
    chargeback, checkout, content, content.assignments, content.attributes, content.multimedia,
    content.multimedia.thumbnails, digital_delivery, ebay, email_notifications, enrollment123,
    gift_certificate, google_product_search, kit_definition, identifiers,
    instant_payment_notifications, internal, options, payment_processing, physical, pricing,
    pricing.tiers, realtime_pricing, related, reporting, restriction, reviews,
    reviews.individual_reviews, salesforce, shipping, shipping.cases, shipping.destination_markups,
    shipping.destination_restrictions, shipping.distribution_centers, shipping.methods,
    shipping.package_requirements, tax, third_party_email_marketing, variations, wishlist_member
    """
    # Expand reviews to illustrate accessing product reviews
    expand = "reviews,reviews.individual_reviews"
    api_response = item_api.get_item(merchant_item_oid, expand=expand, active=False)
    item = api_response.get_item()

    item_reviews = item.get_reviews()
    individual_reviews = item_reviews.get_individual_reviews()

    # Iterate through individual reviews
    for individual_review in individual_reviews:
        # Access rating names and scores (configurable by merchant)
        # See Home -> Configuration -> Items -> Reviews -> Settings
        # Or this URL: https://secure.ultracart.com/merchant/item/review/reviewSettingsLoad.do
        rating_name1 = individual_review.get_rating_name1()  # Not the full question, but a key string
        rating_score1 = individual_review.get_rating_score1()

        # Retrieve reviewer information (careful: can result in many API calls)
        # Consider adding sleep calls and caching results daily or weekly
        customer_response = customer_api.get_customer(
            individual_review.get_customer_profile_oid(),
            expand="reviewer"
        )
        customer = customer_response.get_customer()
        reviewer = customer.get_reviewer()

    print('The following item was retrieved via get_item():')
    print(item)

    # Delete the sample item
    delete_sample_item(merchant_item_oid)

except Exception as e:
    print('An exception occurred. Please review the following error:')
    print(e)
    raise
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
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_item, delete_sample_item

try:
    """
    Most item work is done with the item id, not the item oid. 
    The latter is only meaningful as a primary key in the UltraCart databases.
    """

    # Insert a sample item
    item_id = insert_sample_item()

    # Create Item API client
    item_api = ItemApi(api_client())

    """
    Possible expansion values include:
    accounting, amember, auto_order, auto_order.steps, ccbill, channel_partner_mappings,
    chargeback, checkout, content, content.assignments, content.attributes, 
    content.multimedia, content.multimedia.thumbnails, digital_delivery, ebay, 
    email_notifications, enrollment123, gift_certificate, google_product_search, 
    kit_definition, identifiers, instant_payment_notifications, internal, options, 
    payment_processing, physical, pricing, pricing.tiers, realtime_pricing, related, 
    reporting, restriction, reviews, salesforce, shipping, shipping.cases, 
    shipping.destination_markups, shipping.destination_restrictions, 
    shipping.distribution_centers, shipping.methods, shipping.package_requirements, 
    tax, third_party_email_marketing, variations, wishlist_member
    """
    expand = "kit_definition,options,shipping,tax,variations"
    api_response = item_api.get_item_by_merchant_item_id(item_id, expand=expand, active=False)
    item = api_response.get_item()

    print('The following item was retrieved via get_item_by_merchant_item_id():')
    print(item)

    delete_sample_item(item_id)

except Exception as e:
    print('An exception occurred. Please review the following error:')
    print(e)
    raise
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

# **get_item_shipping_distribution_center_by_code**
> ItemShippingDistributionCenterResponse get_item_shipping_distribution_center_by_code(merchant_item_oid, distribution_center_code)

Retrieve an item shipping distribution center

Retrieve an item shipping distribution center. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid to retrieve. |
 **distribution_center_code** | **str**|  |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**ItemShippingDistributionCenterResponse**](ItemShippingDistributionCenterResponse.md)

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
import sys
from ultracart.apis import ItemApi
from samples import api_client


def get_item_chunk(item_api, offset, limit):
    """
    Retrieve a chunk of items with specified expansion.

    Possible expansion values include:
    accounting, amember, auto_order, auto_order.steps, ccbill, channel_partner_mappings,
    chargeback, checkout, content, content.assignments, content.attributes,
    content.multimedia, content.multimedia.thumbnails, digital_delivery, ebay,
    email_notifications, enrollment123, gift_certificate, google_product_search,
    kit_definition, identifiers, instant_payment_notifications, internal, options,
    payment_processing, physical, pricing, pricing.tiers, realtime_pricing, related,
    reporting, restriction, reviews, salesforce, shipping, shipping.cases,
    shipping.destination_markups, shipping.destination_restrictions,
    shipping.distribution_centers, shipping.methods, shipping.package_requirements,
    tax, third_party_email_marketing, variations, wishlist_member
    """
    # Expansion of commonly needed item details
    expand = "kit_definition,options,shipping,tax,variations"

    # Retrieve items with no category filtering
    api_response = item_api.get_items(
        parent_category_id=None,
        parent_category_path=None,
        limit=limit,
        offset=offset,
        since=None,
        sort=None,
        expand=expand,
        active=False
    )

    return api_response.get_items() or []


def main():
    """
    Retrieve all items in chunks.

    Note: Categories in UltraCart are essentially folders to organize items.
    They do not impact checkout or storefront display.
    """
    # Create Item API client
    item_api = ItemApi(api_client())

    items = []
    iteration = 1
    offset = 0
    limit = 200
    more_records_to_fetch = True

    try:
        while more_records_to_fetch:
            print(f"Executing iteration {iteration}")

            chunk_of_items = get_item_chunk(item_api, offset, limit)
            items.extend(chunk_of_items)

            offset += limit
            more_records_to_fetch = len(chunk_of_items) == limit
            iteration += 1

    except Exception as e:
        print(f'Exception occurred on iteration {iteration}')
        print(e)
        sys.exit(1)

    # Print all retrieved items (will be verbose)
    print(items)


if __name__ == "__main__":
    main()
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
from ultracart.apis import ItemApi
from samples import api_client

try:
    """
    Possible expansion values for PricingTier object:
    - approval_notification
    - signup_notification
    """
    item_api = ItemApi(api_client())

    expand = "approval_notification,signup_notification"
    api_response = item_api.get_pricing_tiers(expand=expand)

except Exception as e:
    print('Exception occurred.')
    print(e)
    raise

print(api_response.get_pricing_tiers())
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
from ultracart.apis import ItemApi
from samples import api_client

"""
Retrieves a specific user review for an item. This would most likely be used by a merchant 
who has cached all reviews on a separate site and then wishes to update a particular review. 
It's always best to "get" the object, make changes to it, then call the update instead of 
trying to recreate the object from scratch.

The merchant_item_oid is a unique identifier used by UltraCart. If you do not know your 
item's oid, call ItemApi.get_item_by_merchant_item_id() to retrieve the item, and then 
get its oid via $item.get_merchant_item_oid()

The review_oid is a unique identifier used by UltraCart. If you do not know a review's oid, 
call ItemApi.get_reviews() to get all reviews where you can then grab the oid from an item.
"""

# Create Item API client
item_api = ItemApi(api_client())

# Example OIDs (replace with actual values)
merchant_item_oid = 123456
review_oid = 987654

# Retrieve the specific review
api_response = item_api.get_review(review_oid, merchant_item_oid)

# Check for errors
if api_response.get_error() is not None:
    error = api_response.get_error()
    print(f"Developer Message: {error.get_developer_message()}")
    print(f"User Message: {error.get_user_message()}")
    raise Exception("Review retrieval failed")

# Get the review
review = api_response.get_review()

# Print the review
print(review)
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
from samples import api_client
from ultracart.apis import ItemApi

"""
Retrieves all user reviews for an item.

The merchant_item_oid is a unique identifier used by UltraCart.  If you do not know your item's oid, call
ItemApi.getItemByMerchantItemId() to retrieve the item, and then it's oid $item->getMerchantItemOid()
"""

# Initialize the Item API
item_api = ItemApi(api_client())

# Specify the merchant item OID
merchant_item_oid = 123456

# Retrieve reviews
api_response = item_api.get_item_reviews(merchant_item_oid)

# Check for errors
if api_response.error is not None:
    print(f"Developer Message: {api_response.error.developer_message}")
    print(f"User Message: {api_response.error.user_message}")
    exit()

# Process and print reviews
reviews = api_response.reviews
for review in reviews:
    print(review)
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
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_digital_item
from ultracart.exceptions import ApiException

"""
Please Note!
Digital Items are not normal items you sell on your site.  They are digital files that you may add to
a library and then attach to a normal item as an accessory or the main item itself.
See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1376485/Digital+Items

Retrieves a group of digital items (file information) from the account that are not yet associated with any
actual items.  If no parameters are specified, all digital items will be returned.  Be aware that these are
not normal items that can be added to a shopping cart. Rather, they are digital files that may be associated
with normal items.  You will need to make multiple API calls in order to retrieve the entire result set since
this API performs result set pagination.

Default sort order: original_filename
Possible sort orders: original_filename, description, file_size
"""

try:
    # Create an unassociated digital item
    digital_item_oid = insert_sample_digital_item()

    # Initialize Item API
    item_api = ItemApi(api_client())

    # Set up parameters for retrieving unassociated digital items
    limit = 100
    offset = 0
    since = None  # digital items do not use since.  leave as None
    sort = None  # if None, use default of original_filename
    expand = None  # digital items have no expansion.  leave as None
    placeholders = None  # digital items have no placeholders. leave as None

    # Retrieve unassociated digital items
    api_response = item_api.get_unassociated_digital_items(
        limit=limit,
        offset=offset,
        since=since,
        sort=sort,
        expand=expand,
        placeholders=placeholders
    )

    # Extract digital items from the response
    digital_items = api_response.digital_items

    # Print retrieved digital items
    print('The following items were retrieved via get_unassociated_digital_items():')
    for digital_item in digital_items:
        print(digital_item)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)
    exit(1)
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
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_digital_item, delete_sample_digital_item
from ultracart.exceptions import ApiException

try:
    # Create and then delete a sample digital item
    digital_item_oid = insert_sample_digital_item()
    delete_sample_digital_item(digital_item_oid)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)
    exit(1)
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
from item_functions import insert_sample_item, delete_sample_item
from ultracart.exceptions import ApiException

try:
    item_id = insert_sample_item()
    delete_sample_item(item_id)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)
    exit(1)
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
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_item
from ultracart.exceptions import ApiException
from ultracart.models import ItemReviews, ItemReview

try:
    # Create a sample item
    item_id = insert_sample_item()

    # Initialize Item API
    item_api = ItemApi(api_client())

    # Expand reviews to update item with review template
    expand = 'reviews'

    # Retrieve item by merchant item ID
    item_response = item_api.get_item_by_merchant_item_id(item_id, expand=expand)
    item = item_response.item
    item_oid = item.merchant_item_oid

    # Set review template
    review_template_oid = 402
    reviews = ItemReviews()
    reviews.review_template_oid = review_template_oid
    item.reviews = reviews

    # Update item with review template
    item = item_api.update_item(item_oid, item, expand=expand).item

    # Create a new review
    review = ItemReview(
        title='Best Product Ever!',
        review="I loved this product. I bought it for my wife and she was so happy she cried. blah blah blah",
        reviewed_nickname="Bob420",
        featured=True,
        rating_name1='Durability',
        rating_name2='Price',
        rating_name3='Performance',
        rating_name4='Appearance',
        rating_score1=4.5,
        rating_score2=3.5,
        rating_score3=2.5,
        rating_score4=1.5,
        overall=5.0,
        reviewer_location="Southside Chicago",
        status='approved'
    )

    # Insert the review
    review = item_api.insert_review(item_oid, review).review

    # Print the review
    print("Inserted Review:")
    print(review)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)
    exit(1)
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
from samples import api_client
from ultracart.apis import ItemApi
from ultracart.models import ItemContentAttribute

"""
While UltraCart provides a means for updating item content, it is StoreFront specific.  This method allows for
item-wide update of content, such as SEO fields. The content attribute has three fields:
1) name
2) value
3) type: boolean,color,definitionlist,html,integer,mailinglist,multiline,rgba,simplelist,string,videolist

The SEO content has the following names:
Item Meta Title = "storefrontSEOTitle"
Item Meta Description = "storefrontSEODescription"
Item Meta Keywords = "storefrontSEOKeywords"

The merchant_item_oid is a unique identifier used by UltraCart.  If you do not know your item's oid, call
ItemApi.getItemByMerchantItemId() to retrieve the item, and then it's oid $item->getMerchantItemOid()

Success will return back a status code of 204 (No Content)
"""

# Initialize Item API
item_api = ItemApi(api_client())

# Specify the merchant item OID
merchant_item_oid = 12345

# Create content attribute
attribute = ItemContentAttribute(
    name="storefrontSEOKeywords",
    value='dog,cat,fish',
    type="string"
)

# Insert or update the content attribute
item_api.insert_update_item_content_attribute(merchant_item_oid, attribute)
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
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_digital_item, delete_sample_digital_item
from ultracart.exceptions import ApiException

try:
    digital_item_oid = insert_sample_digital_item()

    item_api = ItemApi(api_client())
    api_response = item_api.get_digital_item(digital_item_oid)
    digital_item = api_response.digital_item

    digital_item.description = "I have updated the description to this sentence."
    digital_item.click_wrap_agreement = "You hereby agree that the earth is round. No debate."

    item_api.update_digital_item(digital_item_oid, digital_item)

    delete_sample_digital_item(digital_item_oid)

except ApiException as e:
    print('An ApiException occurred. Please review the following error:')
    print(e)
    exit(1)
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
from flask import Flask
from ultracart import ApiException
from ultracart.apis import ItemApi
from samples import api_client
from item_functions import insert_sample_item, delete_sample_item

app = Flask(__name__)


@app.route('/update_item')
def update_item():
    try:
        # Insert a sample item
        item_id = insert_sample_item()

        # Create Item API client
        item_api = ItemApi(api_client())

        # Expand pricing information
        expand = "pricing"

        # Get the item by merchant item ID
        api_response = item_api.get_item_by_merchant_item_id(item_id, expand=expand, _expand=False)
        item = api_response.get_item()

        # Store original price
        original_price = item.get_pricing().get_cost()

        # Update the item's price
        item_pricing = item.get_pricing()
        item_pricing.set_cost(12.99)

        # Update the item
        api_response = item_api.update_item(item.get_merchant_item_oid(), item, expand=expand, _expand=False)
        updated_item = api_response.get_item()

        # Print price changes
        print(f'Original Price: {original_price}')
        print(f'Updated Price: {updated_item.get_pricing().get_cost()}')

        # Delete the sample item
        delete_sample_item(item_id)

        return "Item update successful"

    except ApiException as e:
        print('An ApiException occurred. Please review the following error:')
        print(e)
        return "Error updating item", 500


if __name__ == '__main__':
    app.run(debug=True)
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

# **update_item_shipping_distribution_center_by_code**
> update_item_shipping_distribution_center_by_code(merchant_item_oid, distribution_center_code, item_shipping_distribution_center)

Update an item shipping distribution center

Update an item shipping distribution center 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_oid** | **int**| The item oid to update. |
 **distribution_center_code** | **str**|  |
 **item_shipping_distribution_center** | [**ItemShippingDistributionCenter**](ItemShippingDistributionCenter.md)| Item shipping distribution center |

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

# **update_items**
> ItemsResponse update_items(items_request)

Update multiple items

Update multiple item on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from flask import Flask
from ultracart import ApiException
from ultracart.apis import ItemApi
from ultracart.models import ItemsRequest
from samples import api_client
from item_functions import insert_sample_item, delete_sample_item

app = Flask(__name__)

@app.route('/update_multiple_items')
def update_multiple_items():
    try:
        # Insert two sample items
        item_id1 = insert_sample_item()
        item_id2 = insert_sample_item()

        # Create Item API client
        item_api = ItemApi(api_client())

        # Expand pricing information
        expand = "pricing"

        # Get items by merchant item IDs
        api_response = item_api.get_item_by_merchant_item_id(item_id1, expand=expand, _expand=False)
        item1 = api_response.get_item()
        api_response = item_api.get_item_by_merchant_item_id(item_id2, expand=expand, _expand=False)
        item2 = api_response.get_item()

        # Update prices of items
        item1.get_pricing().set_cost(12.99)
        item2.get_pricing().set_cost(14.99)

        # Create items request
        update_items_request = ItemsRequest()
        items = [item1, item2]
        update_items_request.items = items

        # Update multiple items
        item_api.update_items(update_items_request, expand=expand, _expand=False, _async=False)

        # Delete sample items
        delete_sample_item(item_id1)
        delete_sample_item(item_id2)

        return "Multiple items updated successfully"

    except ApiException as e:
        print('An ApiException occurred. Please review the following error:')
        print(e)
        return "Error updating items", 500

if __name__ == '__main__':
    app.run(debug=True)
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


(No example for this operation).



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
import io
import pprint

from ultracart import ApiException
from ultracart.apis import ItemApi
from ultracart.model.item_content import ItemContent
from ultracart.model.item_content_multimedia import ItemContentMultimedia

from samples import api_client
from item_functions import insert_sample_item


def update_item():
    try:
        # Insert a sample item
        item_id = insert_sample_item()
        # Create Item API client
        item_api = ItemApi(api_client())

        with open('./ultracart_icon.png', 'rb') as file:


            file_blob = io.BytesIO(file.read())
            file_blob.name = 'ultracart_icon.png'

            # upload the file and get the resultant oid
            upload_response = item_api.upload_temporary_multimedia(file = file_blob)
            pprint.pprint(upload_response)

            temp_oid = upload_response['temp_multimedia']['temp_multimedia_oid']

            # Expand pricing information
            expand = "content.multimedia"
            get_response = item_api.get_item_by_merchant_item_id(merchant_item_id = item_id, expand = expand)
            item = get_response['item']

            content = item['content']
            if content is None:
                content = ItemContent()
                item['content'] = content

            multimedia = content['multimedia']
            if multimedia is None:
                multimedia = []
                content['multimedia'] = multimedia

            a_multimedia = ItemContentMultimedia()
            a_multimedia.file_name = 'ultracart_icon.png'
            a_multimedia.description = 'ultracart icon'
            a_multimedia.temp_multimedia_oid = temp_oid
            multimedia.append(a_multimedia)

            # this DOES work
            b_multimedia = ItemContentMultimedia()
            b_multimedia.file_name = 'universe.png'
            b_multimedia.code = 'universe'
            b_multimedia.description = 'some random NASA picture'
            b_multimedia.url = 'https://www.nasa.gov/wp-content/uploads/2022/07/web_first_images_release.png?resize=2000,1158'
            multimedia.append(b_multimedia)

            update_response = item_api.update_item(merchant_item_oid = item.merchant_item_oid, item = item, expand = expand)

            pprint.pprint(update_response)



    except ApiException as e:
        print('An ApiException occurred. Please review the following error:')
        print(e)
        return "Error updating item", 500


if __name__ == '__main__':
    update_item()

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

