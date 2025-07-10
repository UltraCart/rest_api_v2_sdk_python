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
[**update_auto_orders_batch**](AutoOrderApi.md#update_auto_orders_batch) | **PUT** /auto_order/auto_orders/batch | Update multiple auto orders


# **consolidate_auto_orders**
> AutoOrderResponse consolidate_auto_orders(auto_order_oid, auto_order_consolidate)

Consolidates multiple auto orders

Consolidates mutliple auto orders on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from ultracart.models import AutoOrderConsolidate
from samples import api_client


# consolidateAutoOrders
# an auto order with no items, the original_order is used for shipping, billing, and payment information.
# Once you have your empty auto order, add items to it and call updateAutoOrder.

def consolidate_auto_orders():
    auto_order_api = AutoOrderApi(api_client())

    # see https://www.ultracart.com/api/#resource_auto_order.html for list
    expand = "items,items.future_schedules,original_order,rebill_orders"

    # set getAutoOrdersByQuery for retrieving auto orders where you can get their auto_order_oid
    target_auto_order_oid = 123456789

    consolidate_request = AutoOrderConsolidate()
    # these are the autoorder_oids you wish to consolidate into the target
    consolidate_request.source_auto_order_oids = [23456789, 3456789]

    api_response = auto_order_api.consolidate_auto_orders(
        target_auto_order_oid,
        consolidate_request,
        expand=expand
    )

    consolidated_auto_order = api_response.auto_order

    # TODO: make sure the consolidated order has all the items and history of all orders
    print(consolidated_auto_order)


if __name__ == "__main__":
    consolidate_auto_orders()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_oid** | **int**| The auto order oid to consolidate into. |
 **auto_order_consolidate** | [**AutoOrderConsolidate**](AutoOrderConsolidate.md)| Auto orders to consolidate |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

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

# **establish_auto_order_by_reference_order_id**
> AutoOrderResponse establish_auto_order_by_reference_order_id(reference_order_id)

Establish an auto order by referencing a regular order id

Establish an auto order by referencing a regular order id.  The result will be an auto order without any items.  You should add the items and perform an update call.  Orders must be less than 60 days old and use a credit card payment. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from ultracart.models import AutoOrderItem
from samples import api_client


# This method takes a normal order id and creates an empty auto order from it.  While this might seem useless having
# an auto order with no items, the original_order is used for shipping, billing, and payment information.
# Once you have your empty auto order, add items to it and call updateAutoOrder.

def establish_and_update_auto_order():
    auto_order_api = AutoOrderApi(api_client())

    # see https://www.ultracart.com/api/#resource_auto_order.html for list
    expand = "items,items.future_schedules,original_order,rebill_orders"

    original_order_id = "DEMO-123457"
    api_response = auto_order_api.establish_auto_order_by_reference_order_id(original_order_id, expand=expand)

    empty_auto_order = api_response.auto_order
    auto_order_oid = empty_auto_order.auto_order_oid

    items = []
    item = AutoOrderItem()
    item.original_item_id = "ITEM_ABC"  # This item should be configured with auto order features.
    item.original_quantity = 1
    item.arbitrary_unit_cost = 59.99

    # Valid Frequencies
    # "Weekly", "Biweekly", "Every...", "Every 10 Days", "Every 4 Weeks", "Every 6 Weeks", "Every 8 Weeks", "Every 24 Days", "Every 28 Days", "Monthly",
    # "Every 45 Days", "Every 2 Months", "Every 3 Months", "Every 4 Months", "Every 5 Months", "Every 6 Months", "Yearly"
    item.frequency = "Monthly"
    items.append(item)
    empty_auto_order.items = items

    validate_original_order = 'No'
    api_response = auto_order_api.update_auto_order(auto_order_oid, empty_auto_order, validate_original_order, expand=expand)
    updated_auto_order = api_response.auto_order
    print(updated_auto_order)


if __name__ == "__main__":
    establish_and_update_auto_order()
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

# **get_auto_order**
> AutoOrderResponse get_auto_order(auto_order_oid)

Retrieve an auto order by oid

Retrieves a single auto order using the specified auto order oid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from samples import api_client


# retrieves an auto_order given the auto_order_oid

def get_auto_order():
    auto_order_api = AutoOrderApi(api_client())

    # see https://www.ultracart.com/api/#resource_auto_order.html for list
    expand = "items,items.future_schedules,original_order,rebill_orders"

    # If you don't know the oid, use getAutoOrdersByQuery for retrieving auto orders
    auto_order_oid = 123456789
    api_response = auto_order_api.get_auto_order(auto_order_oid, expand=expand)
    auto_order = api_response.auto_order
    print(auto_order)


if __name__ == "__main__":
    get_auto_order()
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

# **get_auto_order_by_code**
> AutoOrderResponse get_auto_order_by_code(auto_order_code)

Retrieve an auto order by code

Retrieves a single auto order using the specified reference (original) order id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from samples import api_client


# This example illustrates how to query an auto order when you know the 'code'.  Each AutoOrder has a unique
# identifier used by UltraCart called an OID (Object Identifier).  AutoOrders also have a unique code which
# is (arguably) an easy way for customers to discuss a specific auto order with a merchant.
# The codes look like this: "RT2A9CBSX9"
#
# It is doubtful that an UltraCart merchant will ever make use of this method.

def get_auto_order_by_code():
    auto_order_api = AutoOrderApi(api_client())

    # These are the possible expansion values for auto orders.  This list is taken from www.ultracart.com/api/
    # and may become stale. Please review the master website when in doubt.
    # items
    # items.future_schedules
    # items.sample_schedule
    # original_order
    # original_order.affiliate
    # original_order.affiliate.ledger
    # original_order.auto_order
    # original_order.billing
    # original_order.buysafe
    # original_order.channel_partner
    # original_order.checkout
    # original_order.coupon
    # original_order.customer_profile
    # original_order.digital_order
    # original_order.edi
    # original_order.fraud_score
    # original_order.gift
    # original_order.gift_certificate
    # original_order.internal
    # original_order.item
    # original_order.linked_shipment
    # original_order.marketing
    # original_order.payment
    # original_order.payment.transaction
    # original_order.quote
    # original_order.salesforce
    # original_order.shipping
    # original_order.summary
    # original_order.taxes
    # rebill_orders
    # rebill_orders.affiliate
    # rebill_orders.affiliate.ledger
    # rebill_orders.auto_order
    # rebill_orders.billing
    # rebill_orders.buysafe
    # rebill_orders.channel_partner
    # rebill_orders.checkout
    # rebill_orders.coupon
    # rebill_orders.customer_profile
    # rebill_orders.digital_order
    # rebill_orders.edi
    # rebill_orders.fraud_score
    # rebill_orders.gift
    # rebill_orders.gift_certificate
    # rebill_orders.internal
    # rebill_orders.item
    # rebill_orders.linked_shipment
    # rebill_orders.marketing
    # rebill_orders.payment
    # rebill_orders.payment.transaction
    # rebill_orders.quote
    # rebill_orders.salesforce
    # rebill_orders.shipping
    # rebill_orders.summary
    # rebill_orders.taxes

    # contact us if you're unsure what you need
    expand = "items,items.future_schedules,original_order,rebill_orders"
    code = "RT2A9CBSX9"
    api_response = auto_order_api.get_auto_order_by_code(code, expand=expand)
    auto_order = api_response.auto_order

    # this will be verbose...
    print(auto_order)


if __name__ == "__main__":
    get_auto_order_by_code()
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

# **get_auto_order_by_reference_order_id**
> AutoOrderResponse get_auto_order_by_reference_order_id(reference_order_id)

Retrieve an auto order by order id

Retrieves a single auto order using the specified reference (original) order id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from samples import api_client


# This example illustrates how to query an auto order when you know the original order id.

def get_auto_order_by_reference_order_id():
    auto_order_api = AutoOrderApi(api_client())

    # These are the possible expansion values for auto orders.  This list is taken from www.ultracart.com/api/
    # and may become stale. Please review the master website when in doubt.
    # items
    # items.future_schedules
    # items.sample_schedule
    # original_order
    # original_order.affiliate
    # original_order.affiliate.ledger
    # original_order.auto_order
    # original_order.billing
    # original_order.buysafe
    # original_order.channel_partner
    # original_order.checkout
    # original_order.coupon
    # original_order.customer_profile
    # original_order.digital_order
    # original_order.edi
    # original_order.fraud_score
    # original_order.gift
    # original_order.gift_certificate
    # original_order.internal
    # original_order.item
    # original_order.linked_shipment
    # original_order.marketing
    # original_order.payment
    # original_order.payment.transaction
    # original_order.quote
    # original_order.salesforce
    # original_order.shipping
    # original_order.summary
    # original_order.taxes
    # rebill_orders
    # rebill_orders.affiliate
    # rebill_orders.affiliate.ledger
    # rebill_orders.auto_order
    # rebill_orders.billing
    # rebill_orders.buysafe
    # rebill_orders.channel_partner
    # rebill_orders.checkout
    # rebill_orders.coupon
    # rebill_orders.customer_profile
    # rebill_orders.digital_order
    # rebill_orders.edi
    # rebill_orders.fraud_score
    # rebill_orders.gift
    # rebill_orders.gift_certificate
    # rebill_orders.internal
    # rebill_orders.item
    # rebill_orders.linked_shipment
    # rebill_orders.marketing
    # rebill_orders.payment
    # rebill_orders.payment.transaction
    # rebill_orders.quote
    # rebill_orders.salesforce
    # rebill_orders.shipping
    # rebill_orders.summary
    # rebill_orders.taxes

    # contact us if you're unsure what you need
    expand = "items,items.future_schedules,original_order,rebill_orders"
    original_order_id = "DEMO-12345678"
    api_response = auto_order_api.get_auto_order_by_reference_order_id(original_order_id, expand=expand)
    auto_order = api_response.auto_order

    # this will be verbose...
    print(auto_order)


if __name__ == "__main__":
    get_auto_order_by_reference_order_id()
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

# **get_auto_orders**
> AutoOrdersResponse get_auto_orders()

Retrieve auto orders

Retrieves auto orders from the account.  If no parameters are specified, all auto orders will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from samples import api_client

# getAutoOrders provides a query service on AutoOrders (aka subscriptions or recurring orders) within the UltraCart
# system. It was the first query provided and the most cumbersome to use.  Please use getAutoOrdersByQuery for an
# easier query method.  If you have multiple auto_order_oids and need the corresponding objects, consider
# getAutoOrdersBatch() to reduce call count.

def get_auto_order_chunk(auto_order_api, offset, limit):
    expand = "items,original_order,rebill_orders"
    # see www.ultracart.com/api/ for all the expansion fields available (this list below may become stale)
    """
    Possible Order Expansions:

    add_ons                             items.sample_schedule	        original_order.buysafe	        original_order.payment.transaction
    items	                            original_order	                original_order.channel_partner	original_order.quote
    items.future_schedules	            original_order.affiliate	    original_order.checkout	        original_order.salesforce
    original_order.affiliate.ledger	    original_order.coupon	        original_order.shipping
    original_order.auto_order	        original_order.customer_profile	original_order.summary
    original_order.billing	            original_order.digital_order	original_order.taxes
    rebill_orders	                    original_order.edi	            rebill_orders.affiliate
    rebill_orders.affiliate.ledger	    original_order.fraud_score	    rebill_orders.auto_order
    rebill_orders.billing	            original_order.gift	            rebill_orders.buysafe
    rebill_orders.channel_partner	    original_order.gift_certificate	rebill_orders.checkout
    rebill_orders.coupon	            original_order.internal	        rebill_orders.customer_profile
    rebill_orders.digital_order	        original_order.item	            rebill_orders.edi
    rebill_orders.fraud_score	        original_order.linked_shipment	rebill_orders.gift
    rebill_orders.gift_certificate      original_order.marketing	    rebill_orders.internal
    rebill_orders.item	                original_order.payment	        rebill_orders.linked_shipment
    rebill_orders.marketing	            rebill_orders.payment	        rebill_orders.quote
    rebill_orders.payment.transaction	rebill_orders.salesforce	    rebill_orders.shipping
    rebill_orders.summary	            rebill_orders.taxes
    """

    auto_order_code = None
    original_order_id = None
    first_name = None
    last_name = None
    company = None
    city = None
    state = None
    postal_code = None
    country_code = None
    phone = None
    email = 'test@ultracart.com'  # <-- for this example, we are only filtering on email address.
    original_order_date_begin = None
    original_order_date_end = None
    next_shipment_date_begin = None
    next_shipment_date_end = None
    card_type = None
    item_id = None
    status = None
    since = None
    sort = None

    # see all these parameters?  that is why you should use getAutoOrdersByQuery() instead of getAutoOrders()
    api_response = auto_order_api.get_auto_orders(auto_order_code, original_order_id, first_name, last_name,
        company, city, state, postal_code, country_code, phone, email, original_order_date_begin,
        original_order_date_end, next_shipment_date_begin, next_shipment_date_end, card_type, item_id, status,
        limit, offset, since, sort, expand=expand)

    if api_response.auto_orders is not None:
        return api_response.auto_orders
    return []

def get_all_auto_orders():
    auto_order_api = AutoOrderApi(api_client())
    auto_orders = []

    iteration = 1
    offset = 0
    limit = 200
    more_records_to_fetch = True

    while more_records_to_fetch:
        print(f"executing iteration {iteration}")
        chunk_of_auto_orders = get_auto_order_chunk(auto_order_api, offset, limit)
        auto_orders.extend(chunk_of_auto_orders)
        offset = offset + limit
        more_records_to_fetch = len(chunk_of_auto_orders) == limit
        iteration += 1

    # this could get verbose...
    print(auto_orders)

if __name__ == "__main__":
    get_all_auto_orders()
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
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch auto orders that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the auto orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**AutoOrdersResponse**](AutoOrdersResponse.md)

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

# **get_auto_orders_batch**
> AutoOrdersResponse get_auto_orders_batch(auto_order_batch)

Retrieve auto order batch

Retrieves a group of auto orders from the account based on an array of auto order oids.  If more than 200 auto order ids are specified, the API call will fail with a bad request error. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from ultracart.models import AutoOrderQueryBatch
from samples import api_client


# This example illustrates how to retrieve auto orders when you have a list of auto_order_oid.

def get_auto_orders_batch():
    auto_order_api = AutoOrderApi(api_client())

    # These are the possible expansion values for auto orders.  This list is taken from www.ultracart.com/api/
    # and may become stale. Please review the master website when in doubt.
    # items
    # items.future_schedules
    # items.sample_schedule
    # original_order
    # original_order.affiliate
    # original_order.affiliate.ledger
    # original_order.auto_order
    # original_order.billing
    # original_order.buysafe
    # original_order.channel_partner
    # original_order.checkout
    # original_order.coupon
    # original_order.customer_profile
    # original_order.digital_order
    # original_order.edi
    # original_order.fraud_score
    # original_order.gift
    # original_order.gift_certificate
    # original_order.internal
    # original_order.item
    # original_order.linked_shipment
    # original_order.marketing
    # original_order.payment
    # original_order.payment.transaction
    # original_order.quote
    # original_order.salesforce
    # original_order.shipping
    # original_order.summary
    # original_order.taxes
    # rebill_orders
    # rebill_orders.affiliate
    # rebill_orders.affiliate.ledger
    # rebill_orders.auto_order
    # rebill_orders.billing
    # rebill_orders.buysafe
    # rebill_orders.channel_partner
    # rebill_orders.checkout
    # rebill_orders.coupon
    # rebill_orders.customer_profile
    # rebill_orders.digital_order
    # rebill_orders.edi
    # rebill_orders.fraud_score
    # rebill_orders.gift
    # rebill_orders.gift_certificate
    # rebill_orders.internal
    # rebill_orders.item
    # rebill_orders.linked_shipment
    # rebill_orders.marketing
    # rebill_orders.payment
    # rebill_orders.payment.transaction
    # rebill_orders.quote
    # rebill_orders.salesforce
    # rebill_orders.shipping
    # rebill_orders.summary
    # rebill_orders.taxes

    # contact us if you're unsure what you need
    expand = "items,items.future_schedules,original_order,rebill_orders"
    auto_order_oids = [123456, 234567, 345678, 456789]
    batch_request = AutoOrderQueryBatch()
    batch_request.auto_order_oids = auto_order_oids
    api_response = auto_order_api.get_auto_orders_batch(batch_request, expand=expand)
    auto_orders = api_response.auto_orders

    # this will be verbose...
    print(auto_orders)


if __name__ == "__main__":
    get_auto_orders_batch()
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

# **get_auto_orders_by_query**
> AutoOrdersResponse get_auto_orders_by_query(auto_order_query)

Retrieve auto orders by query

Retrieves a group of auto orders from the account based on a query object.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
from typing import List
from ultracart.apis import AutoOrderApi
from ultracart.models import AutoOrderQuery
from ultracart.exceptions import ApiException
from samples import api_client

# Initialize the API client
auto_order_api = AutoOrderApi(api_client())


def get_auto_order_chunk(auto_order_api: AutoOrderApi, offset: int, limit: int) -> List:
    """
    Retrieve a chunk of auto orders with pagination.

    Args:
        auto_order_api: The AutoOrderApi instance
        offset: Starting position for fetching records
        limit: Maximum number of records to fetch

    Returns:
        List of auto orders for the current chunk
    """
    # These expansion values are from www.ultracart.com/api/
    # Please review the master website for the most current list
    expand = "items,items.future_schedules,original_order,rebill_orders"  # contact us if you're unsure what you need

    # Available sorting fields are documented in the original PHP file
    sort = "next_shipment_dts"

    query = AutoOrderQuery()
    query.email = "support@ultracart.com"

    api_response = auto_order_api.get_auto_orders_by_query(query, limit=limit, offset=offset, sort=sort, expand=expand)

    if api_response.auto_orders is not None:
        return api_response.auto_orders
    return []


def main():
    auto_orders = []
    iteration = 1
    offset = 0
    limit = 200
    more_records_to_fetch = True

    try:
        while more_records_to_fetch:
            print(f"executing iteration {iteration}")

            chunk_of_orders = get_auto_order_chunk(auto_order_api, offset, limit)
            auto_orders.extend(chunk_of_orders)
            offset += limit
            more_records_to_fetch = len(chunk_of_orders) == limit
            iteration += 1

    except ApiException as e:
        print(f"ApiException occurred on iteration {iteration}")
        print(e)
        exit(1)

    # Print the results
    print(auto_orders)


if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_query** | [**AutoOrderQuery**](AutoOrderQuery.md)| Auto order query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the auto orders.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result. | [optional]

### Return type

[**AutoOrdersResponse**](AutoOrdersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **pause_auto_order**
> AutoOrderResponse pause_auto_order(auto_order_oid, auto_order)

Pause auto order

Completely pause an auto order 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is a convenience method created for an UltraCart merchant to pause a large number of auto orders
# due to an inventory shortage.  This is not new functionality and can be accomplished with the normal updateAutoOrder
# call.  It does the following logic to an auto order:
# for each item in the auto order:
#    if the item is not paused, pause it, setPause(true)
# save the changes by calling updateAutoOrder()
#
# Some warnings if you choose to use this method.
# There are no convenience methods to unpause auto orders.
# There are no convenience methods to query which auto orders are paused.
# We do not recommend pausing auto orders and the merchant is on their own to manage auto order state if they
# choose to begin pausing orders.  Keep good track of what you're doing.

from ultracart.apis import AutoOrderApi
from samples import api_client

auto_order_api = AutoOrderApi(api_client())

expand = "items"  # see https://www.ultracart.com/api/#resource_auto_order.html for list
auto_order_oid = 123456789  # get an auto order and update it.  There are many ways to retrieve an auto order.
get_response = auto_order_api.get_auto_order(auto_order_oid, expand=expand)
auto_order = get_response.auto_order

pause_response = auto_order_api.pause_auto_order(auto_order_oid, auto_order)
paused_auto_order = pause_response.auto_order
print(paused_auto_order)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_oid** | **int**| The auto order oid to pause. |
 **auto_order** | [**AutoOrder**](AutoOrder.md)| Auto order to pause |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

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

# **update_auto_order**
> AutoOrderResponse update_auto_order(auto_order_oid, auto_order)

Update an auto order

Update an auto order on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from samples import api_client

"""
This script demonstrates updating an auto order.
Warning: Take great care editing auto orders. They are complex.
Sometimes you must change the original_order to affect the auto_order. If you have questions about what fields
to update to achieve your desired change, contact UltraCart support. Better to ask and get it right than to
make a bad assumption and corrupt a thousand auto orders. UltraCart support is ready to assist.
"""

# Initialize the API client
auto_order_api = AutoOrderApi(api_client())

# See https://www.ultracart.com/api/#resource_auto_order.html for complete list
expand = "items,items.future_schedules,original_order,rebill_orders"

# Get an auto order and update it. There are many ways to retrieve an auto order.
auto_order_oid = 123456789

# Retrieve the auto order
api_response = auto_order_api.get_auto_order(auto_order_oid)
auto_order = api_response.auto_order
validate_original_order = 'No'

# For this example, the customer supplied the wrong postal code when ordering.
# So to change the postal code for all subsequent auto orders, we change the original order.
auto_order.original_order.billing.postal_code = '44233'

# Update the auto order
api_response = auto_order_api.update_auto_order(auto_order_oid, auto_order,
                                                validate_original_order=validate_original_order, expand=expand)
updated_auto_order = api_response.auto_order
print(updated_auto_order)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_order_oid** | **int**| The auto order oid to update. |
 **auto_order** | [**AutoOrder**](AutoOrder.md)| Auto order to update |
 **validate_original_order** | **str**| Validate original order before updating | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**AutoOrderResponse**](AutoOrderResponse.md)

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

# **update_auto_orders_batch**
> AutoOrdersResponse update_auto_orders_batch(auto_orders_request)

Update multiple auto orders

Update multiple auto orders on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import AutoOrderApi
from ultracart.models import AutoOrdersRequest
from samples import api_client

"""
This script demonstrates updating multiple auto orders in a batch.
Warning: Take great care editing auto orders. They are complex.
Sometimes you must change the original_order to affect the auto_order. If you have questions about what fields
to update to achieve your desired change, contact UltraCart support. Better to ask and get it right than to
make a bad assumption and corrupt a thousand auto orders. UltraCart support is ready to assist.
"""

# Initialize the API client
auto_order_api = AutoOrderApi(api_client())

# The async parameter is what it seems. True if async.
# The max records allowed depends on the async flag. Sync max is 20, Async max is 100.
async_flag = True  # if true, success returns back a 204 No Content. False returns back the updated orders.

# Since we're async, nothing is returned, so we don't care about expansions.
# If you are doing a synchronous operation, then set your expand appropriately.
# See getAutoOrders() sample for expansion samples.
expand = None

# Mostly used for UI, not needed for a pure scripting operation
placeholders = False

# TODO: This should be an array of auto orders that have been updated.
# See any getAutoOrders method for retrieval.
auto_orders = []

# Create the request object and set the auto orders
auto_orders_request = AutoOrdersRequest()
auto_orders_request.auto_orders = auto_orders

# Perform the batch update
api_response = auto_order_api.update_auto_orders_batch(auto_orders_request, expand=expand, placeholders=placeholders,
                                                       async_flag=async_flag)

if api_response is not None:
    # Something went wrong if we have a response
    print(api_response)
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

