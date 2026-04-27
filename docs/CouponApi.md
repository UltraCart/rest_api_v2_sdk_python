# ultracart.CouponApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_coupon**](CouponApi.md#delete_coupon) | **DELETE** /coupon/coupons/{coupon_oid} | Delete a coupon
[**delete_coupons_by_code**](CouponApi.md#delete_coupons_by_code) | **DELETE** /coupon/coupons/by_code | Deletes multiple coupons
[**delete_coupons_by_oid**](CouponApi.md#delete_coupons_by_oid) | **DELETE** /coupon/coupons/by_oid | Deletes multiple coupons
[**does_coupon_code_exist**](CouponApi.md#does_coupon_code_exist) | **GET** /coupon/coupons/merchant_code/{merchant_code}/exists | Determines if a coupon merchant code already exists
[**generate_coupon_codes**](CouponApi.md#generate_coupon_codes) | **POST** /coupon/coupons/{coupon_oid}/generate_codes | Generates one time codes for a coupon
[**generate_one_time_codes_by_merchant_code**](CouponApi.md#generate_one_time_codes_by_merchant_code) | **POST** /coupon/coupons/merchant_code/{merchant_code}/generate_codes | Generates one time codes by merchant code
[**get_auto_apply**](CouponApi.md#get_auto_apply) | **GET** /coupon/auto_apply | Retrieve auto apply rules and conditions
[**get_coupon**](CouponApi.md#get_coupon) | **GET** /coupon/coupons/{coupon_oid} | Retrieve a coupon
[**get_coupon_by_merchant_code**](CouponApi.md#get_coupon_by_merchant_code) | **GET** /coupon/coupons/merchant_code/{merchant_code} | Retrieve a coupon by merchant code
[**get_coupons**](CouponApi.md#get_coupons) | **GET** /coupon/coupons | Retrieve coupons
[**get_coupons_by_query**](CouponApi.md#get_coupons_by_query) | **POST** /coupon/coupons/query | Retrieve coupons by query
[**get_editor_values**](CouponApi.md#get_editor_values) | **GET** /coupon/editor_values | Retrieve values needed for a coupon editor
[**insert_coupon**](CouponApi.md#insert_coupon) | **POST** /coupon/coupons | Insert a coupon
[**insert_coupons**](CouponApi.md#insert_coupons) | **POST** /coupon/coupons/batch | Insert multiple coupons
[**search_items**](CouponApi.md#search_items) | **GET** /coupon/searchItems | Searches for items to display within a coupon editor and assign to coupons
[**update_auto_apply**](CouponApi.md#update_auto_apply) | **POST** /coupon/auto_apply | Update auto apply rules and conditions
[**update_coupon**](CouponApi.md#update_coupon) | **PUT** /coupon/coupons/{coupon_oid} | Update a coupon
[**update_coupons**](CouponApi.md#update_coupons) | **PUT** /coupon/coupons/batch | Update multiple coupons
[**upload_coupon_codes**](CouponApi.md#upload_coupon_codes) | **POST** /coupon/coupons/{coupon_oid}/upload_codes | Upload one-time codes for a coupon


# **delete_coupon**
> delete_coupon(coupon_oid)

Delete a coupon

Delete a coupon on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from samples import api_client

coupon_api = CouponApi(api_client())
coupon_oid = 123456789

coupon_api.delete_coupon(coupon_oid)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_oid** | **int**| The coupon_oid to delete. |

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

# **delete_coupons_by_code**
> delete_coupons_by_code(coupon_delete_request)

Deletes multiple coupons

Delete coupons on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponDeletesRequest
from samples import api_client

coupon_api = CouponApi(api_client())
merchant_code = '10OFF'
delete_request = CouponDeletesRequest()
delete_request.coupon_codes = [merchant_code]

coupon_api.delete_coupons_by_code(delete_request)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_delete_request** | [**CouponDeletesRequest**](CouponDeletesRequest.md)| Coupon oids to delete |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_coupons_by_oid**
> delete_coupons_by_oid(coupon_delete_request)

Deletes multiple coupons

Delete coupons on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponDeletesRequest
from samples import api_client

# This method is useful if you have the coupons stored in your own system along with their coupon_oids.  If not,
# just use delete_coupons_by_code()

coupon_api = CouponApi(api_client())
delete_request = CouponDeletesRequest()
delete_request.coupon_oids = [1234567, 2345678, 3456789]

coupon_api.delete_coupons_by_oid(delete_request)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_delete_request** | [**CouponDeletesRequest**](CouponDeletesRequest.md)| Coupon oids to delete |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **does_coupon_code_exist**
> CouponExistsResponse does_coupon_code_exist(merchant_code)

Determines if a coupon merchant code already exists

Determines if a coupon merchant code already exists. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from samples import api_client

coupon_api = CouponApi(api_client())
merchant_code = '10OFF'

api_response = coupon_api.does_coupon_code_exist(merchant_code)
coupon_exists = api_response.exists

print(api_response)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_code** | **str**| The coupon merchant code to examine. |

### Return type

[**CouponExistsResponse**](CouponExistsResponse.md)

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

# **generate_coupon_codes**
> CouponCodesResponse generate_coupon_codes(coupon_oid, coupon_codes_request)

Generates one time codes for a coupon

Generate one time codes for a coupon 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponCodesRequest
from samples import api_client
from datetime import datetime, timedelta

coupon_api = CouponApi(api_client())
coupon_oid = 12345678  # if you don't know your coupon_oid, use generate_one_time_codes_by_merchant_code.  same results

codes_request = CouponCodesRequest()
codes_request.quantity = 100  # give me 100 codes.
expiration_date = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%dT00:00:00+00:00')
codes_request.expiration_dts = expiration_date  # do you want the codes to expire?
# codes_request.expiration_seconds = None  # also an option for short-lived coupons

api_response = coupon_api.generate_coupon_codes(coupon_oid, codes_request)
coupon_codes = api_response.coupon_codes
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_oid** | **int**| The coupon oid to generate codes. |
 **coupon_codes_request** | [**CouponCodesRequest**](CouponCodesRequest.md)| Coupon code generation parameters |

### Return type

[**CouponCodesResponse**](CouponCodesResponse.md)

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

# **generate_one_time_codes_by_merchant_code**
> CouponCodesResponse generate_one_time_codes_by_merchant_code(merchant_code, coupon_codes_request)

Generates one time codes by merchant code

Generate one time codes by merchant code 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponCodesRequest
from samples import api_client
from datetime import datetime, timedelta

coupon_api = CouponApi(api_client())
merchant_code = '10OFF'

codes_request = CouponCodesRequest()
codes_request.quantity = 100  # give me 100 codes.
expiration_date = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%dT00:00:00+00:00')
codes_request.expiration_dts = expiration_date  # do you want the codes to expire?
# codes_request.expiration_seconds = None  # also an option for short-lived coupons

api_response = coupon_api.generate_one_time_codes_by_merchant_code(merchant_code, codes_request)
coupon_codes = api_response.coupon_codes
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_code** | **str**| The merchant code to generate one time codes. |
 **coupon_codes_request** | [**CouponCodesRequest**](CouponCodesRequest.md)| Coupon code generation parameters |

### Return type

[**CouponCodesResponse**](CouponCodesResponse.md)

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

# **get_auto_apply**
> CouponAutoApplyConditions get_auto_apply()

Retrieve auto apply rules and conditions

Retrieve auto apply rules and conditions 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
"""
getAutoApply returns back the items and subtotals that trigger "auto coupons", i.e. coupons that are automatically
added to a shopping cart.  The manual configuration of auto coupons is at the bottom of the main coupons screen.
See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/1376525/Coupons#Coupons-Navigation
"""

from ultracart.apis import CouponApi
from samples import api_client

coupon_api = CouponApi(api_client())
api_response = coupon_api.get_auto_apply()

print('These are the subtotal levels:')
for subtotal_level in api_response.subtotal_levels:
    print(subtotal_level)
    print()

print('These are the item triggers:')
for required_item in api_response.required_items:
    print(required_item)
    print()
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CouponAutoApplyConditions**](CouponAutoApplyConditions.md)

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

# **get_coupon**
> CouponResponse get_coupon(coupon_oid)

Retrieve a coupon

Retrieves a single coupon using the specified coupon profile oid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from samples import api_client

coupon_api = CouponApi(api_client())
coupon_oid = 123456789

expand = None  # coupons do not have expansions
api_response = coupon_api.get_coupon(coupon_oid, expand=expand)

print(api_response)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_oid** | **int**| The coupon oid to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CouponResponse**](CouponResponse.md)

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

# **get_coupon_by_merchant_code**
> CouponResponse get_coupon_by_merchant_code(merchant_code)

Retrieve a coupon by merchant code

Retrieves a single coupon using the specified merchant code. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from samples import api_client

coupon_api = CouponApi(api_client())
api_response = coupon_api.get_coupon_by_merchant_code('10OFF')

print(api_response)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_code** | **str**| The coupon merchant code to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CouponResponse**](CouponResponse.md)

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

# **get_coupons**
> CouponsResponse get_coupons()

Retrieve coupons

Retrieves coupons for this account.  If no parameters are specified, all coupons will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
# Error help: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/39077885/Troubleshooting+API+Errors
# Additional Docs: https://www.ultracart.com/api/#introduction.html

# This is an old example.  Please see get_coupons_by_query as they do essentially the same thing, but
# get_coupons_by_query is easier to use.

from ultracart.apis import CouponApi
from ultracart.exceptions import ApiException
from ultracart.models import Coupon
from typing import List
from samples import api_client


def get_coupons_chunk(coupon_api: CouponApi, offset: int = 0, limit: int = 200) -> List[Coupon]:
    """
    Returns a block of customers

    Args:
        coupon_api: CouponApi instance
        offset: pagination variable
        limit: pagination variable. max server will allow is 200

    Returns:
        List of Coupon objects

    Raises:
        ApiException
    """

    # TODO: consider using get_coupons_by_query() as it does not require all search parameters
    merchant_code = None
    description = None
    coupon_type = None
    start_date_begin = None
    start_date_end = None
    expiration_date_begin = None
    expiration_date_end = None
    affiliate_oid = None
    exclude_expired = None

    limit = limit
    offset = offset
    sort = None
    expand = None  # getCoupons doesn't have any expansions. full record is always returned.

    get_response = coupon_api.get_coupons(merchant_code, description, coupon_type, start_date_begin, start_date_end,
                                          expiration_date_begin, expiration_date_end, affiliate_oid, exclude_expired,
                                          limit=limit, offset=offset, sort=sort, expand=expand)
    if get_response.success:
        return get_response.coupons

    return []


def main():
    coupon_api = CouponApi(api_client())
    coupons = []

    try:
        iteration = 1
        offset = 0
        limit = 200
        need_more_records = True

        while need_more_records:
            print(f"executing iteration #{iteration}")
            iteration += 1

            block_of_customers = get_coupons_chunk(coupon_api, offset, limit)
            coupons.extend(block_of_customers)

            offset += limit
            need_more_records = len(block_of_customers) == limit
            # time.sleep(1)  # I'm testing rate limiter headers. this should probably be uncommented. maybe.

    except ApiException as e:
        print('API Exception when calling CouponApi->get_coupons:', e.message)
        print(e.response_body)
    except Exception as e:
        print('Exception when calling CouponApi->get_coupons:', str(e))

    print(coupons)


if __name__ == '__main__':
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_code** | **str**| Merchant code | [optional]
 **description** | **str**| Description | [optional]
 **coupon_type** | **str**| Coupon type | [optional]
 **start_date_begin** | **str**| Start date begin | [optional]
 **start_date_end** | **str**| Start date end | [optional]
 **expiration_date_begin** | **str**| Expiration date begin | [optional]
 **expiration_date_end** | **str**| Expiration date end | [optional]
 **affiliate_oid** | **int**| Affiliate oid | [optional]
 **exclude_expired** | **bool**| Exclude expired | [optional]
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CouponsResponse**](CouponsResponse.md)

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

# **get_coupons_by_query**
> CouponsResponse get_coupons_by_query(coupon_query)

Retrieve coupons by query

Retrieves coupons from the account.  If no parameters are specified, all coupons will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponQuery
from samples import api_client

# Initialize the API
coupon_api = CouponApi(api_client())


def get_coupon_chunk(coupon_api: CouponApi, offset: int, limit: int) -> list:
    """
    Retrieve a chunk of coupons based on the specified query parameters.

    Args:
        coupon_api: The CouponApi instance
        offset: Starting position for the query
        limit: Maximum number of records to return

    Returns:
        List of coupon objects
    """
    query = CouponQuery()
    query.merchant_code = '10OFF'  # supports partial matching
    query.description = 'Saturday'  # supports partial matching
    # query.coupon_type = None  # see the note at the top of the sample
    # query.start_dts_begin = (datetime.now() - timedelta(days=2000)).strftime('%Y-%m-%dT00:00:00+00:00')
    # query.start_dts_end = datetime.now().strftime('%Y-%m-%dT00:00:00+00:00')
    # query.expiration_dts_begin = None
    # query.expiration_dts_end = None
    # query.affiliate_oid = 0  # this requires an affiliate_oid. Contact support for help finding an affiliate's oid
    query.exclude_expired = True

    expand = None  # coupons do not have expansions
    sort = "merchant_code"  # Possible sorts: "coupon_type", "merchant_code", "description", "start_dts", "expiration_dts", "quickbooks_code"

    api_response = coupon_api.get_coupons_by_query(query, limit=limit, offset=offset, sort=sort, expand=expand)
    return api_response.coupons if api_response.coupons is not None else []


def main():
    coupons = []
    iteration = 1
    offset = 0
    limit = 200
    more_records_to_fetch = True

    while more_records_to_fetch:
        print(f"executing iteration {iteration}")
        chunk_of_coupons = get_coupon_chunk(coupon_api, offset, limit)
        coupons.extend(chunk_of_coupons)
        offset += limit
        more_records_to_fetch = len(chunk_of_coupons) == limit
        iteration += 1

    print(coupons)  # This could get verbose...


if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_query** | [**CouponQuery**](CouponQuery.md)| Coupon query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CouponsResponse**](CouponsResponse.md)

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

# **get_editor_values**
> CouponEditorValues get_editor_values()

Retrieve values needed for a coupon editor

Retrieve values needed for a coupon editor 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is an internal method used by our Coupon management screen.  It returns back all the static data needed
# for our dropdown lists, such as coupon constants.  You can call it if you like, but the data won't be
# of much use.
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CouponEditorValues**](CouponEditorValues.md)

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

# **insert_coupon**
> CouponResponse insert_coupon(coupon)

Insert a coupon

Insert a coupon on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import Coupon, CouponAmountOffSubtotal
from samples import api_client

# Initialize the API
coupon_api = CouponApi(api_client())

# Create the main coupon object
coupon = Coupon()
coupon.merchant_code = '11OFF'
coupon.description = "Eleven dollars off subtotal"

# Each coupon must have a 'type' defined by creating a child object directly beneath the main Coupon object.
# This is complex and there are a LOT of coupon types. See the backend (secure.ultracart.com) coupon screens
# to get an idea of what functionality each coupon possesses. If you're not sure, contact UltraCart support.
coupon.amount_off_subtotal = CouponAmountOffSubtotal()
coupon.amount_off_subtotal.discount_amount = 11

# Here are the different coupon types, but beware that new coupons are added frequently.
# CouponAmountOffItems
# CouponAmountOffShipping
# CouponAmountOffShippingWithItemsPurchase
# CouponAmountOffSubtotal
# CouponAmountOffSubtotalAndShipping
# CouponAmountOffSubtotalFreeShippingWithPurchase
# CouponAmountOffSubtotalWithBlockPurchase
# CouponAmountOffSubtotalWithItemsPurchase
# CouponAmountOffSubtotalWithPurchase
# CouponAmountShippingWithSubtotal
# CouponDiscountItems
# CouponDiscountItemWithItemPurchase
# CouponFreeItemAndShippingWithSubtotal
# CouponFreeItemsWithItemPurchase
# CouponFreeItemsWithMixMatchPurchase
# CouponFreeItemWithItemPurchase
# CouponFreeItemWithItemPurchaseAndFreeShipping
# CouponFreeItemWithSubtotal
# CouponFreeShipping
# CouponFreeShippingSpecificItems
# CouponFreeShippingWithItemsPurchase
# CouponFreeShippingWithSubtotal
# CouponMoreLoyaltyCashback
# CouponMoreLoyaltyPoints
# CouponMultipleAmountsOffItems
# CouponNoDiscount
# CouponPercentMoreLoyaltyCashback
# CouponPercentMoreLoyaltyPoints
# CouponPercentOffItems
# CouponPercentOffItemsAndFreeShipping
# CouponPercentOffItemsWithItemsPurchase
# CouponPercentOffItemWithItemsQuantityPurchase
# CouponPercentOffMsrpItems
# CouponPercentOffRetailPriceItems
# CouponPercentOffShipping
# CouponPercentOffSubtotal
# CouponPercentOffSubtotalAndFreeShipping
# CouponPercentOffSubtotalLimit
# CouponPercentOffSubtotalWithItemsPurchase
# CouponPercentOffSubtotalWithSubtotal
# CouponTieredAmountOffItems
# CouponTieredAmountOffSubtotal
# CouponTieredPercentOffItems
# CouponTieredPercentOffShipping
# CouponTieredPercentOffSubtotal
# CouponTieredPercentOffSubtotalBasedOnMSRP
# CouponTierItemDiscount
# CouponTierPercent
# CouponTierQuantityAmount
# CouponTierQuantityPercent

expand = None  # coupons do not have expansions
api_response = coupon_api.insert_coupon(coupon, expand=expand)
print(api_response)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon** | [**Coupon**](Coupon.md)| Coupon to insert |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CouponResponse**](CouponResponse.md)

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

# **insert_coupons**
> CouponsResponse insert_coupons(coupons_request)

Insert multiple coupons

Insert multiple coupon on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponsRequest
from samples import api_client

"""
Similar to insert_coupon except this method takes a request object containing up to 50 coupons.
Please see insert_coupon for a detailed example on creating a coupon. It is not repeated here.
"""

# Initialize the API
coupon_api = CouponApi(api_client())

# Create the request object
coupons_request = CouponsRequest()
coupons = []
# TODO: add Coupon() objects to this list (see insert_coupon sample for help)
coupons_request.coupons = coupons

expand = None  # coupons do not have expansions
placeholders = None  # coupons do not have placeholders

api_response = coupon_api.insert_coupons(coupons_request, expand=expand, placeholders=placeholders)
print(api_response)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupons_request** | [**CouponsRequest**](CouponsRequest.md)| Coupons to insert (maximum 50) |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]

### Return type

[**CouponsResponse**](CouponsResponse.md)

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

# **search_items**
> CouponItemSearchResultsResponse search_items()

Searches for items to display within a coupon editor and assign to coupons

Searches for items to display within a coupon editor and assign to coupons 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is an internal method used by our Coupon management screen.  It searches merchant items to display in
# some of the coupon editor dropdowns.  See ItemApi.getItemsByQuery if you need to search items.  This method
# is inflexible and geared toward our UI.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | **str**|  | [optional]
 **m** | **int**|  | [optional]

### Return type

[**CouponItemSearchResultsResponse**](CouponItemSearchResultsResponse.md)

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

# **update_auto_apply**
> update_auto_apply(conditions)

Update auto apply rules and conditions

Update auto apply rules and conditions 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponAutoApplyCondition, CouponAutoApplyConditions
from samples import api_client

coupon_api = CouponApi(api_client())

auto_apply = CouponAutoApplyConditions()

item_condition = CouponAutoApplyCondition()
item_condition.required_item_id = 'ITEM_ABC'
item_condition.coupon_code = '10OFF'
item_conditions = [item_condition]

subtotal_condition = CouponAutoApplyCondition()
subtotal_condition.minimum_subtotal = 50  # must spend fifty dollars
subtotal_condition.coupon_code = '5OFF'  # Fixed bug: was setting on item_condition in PHP
subtotal_conditions = [subtotal_condition]

auto_apply.required_items = item_conditions
auto_apply.subtotal_levels = subtotal_conditions

coupon_api.update_auto_apply(auto_apply)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conditions** | [**CouponAutoApplyConditions**](CouponAutoApplyConditions.md)| Conditions |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_coupon**
> CouponResponse update_coupon(coupon_oid, coupon)

Update a coupon

Update a coupon on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from samples import api_client
from datetime import datetime, timedelta

coupon_api = CouponApi(api_client())
coupon_oid = 123456789

expand = None  # coupons do not have expansions
api_response = coupon_api.get_coupon(coupon_oid, expand=expand)
coupon = api_response.coupon

# update the coupon.  this can be difficult given the complexity of coupons.  see insertCoupon sample for details.
expiration_date = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%dT00:00:00+00:00')
coupon.expiration_dts = expiration_date

api_response = coupon_api.update_coupon(coupon_oid, coupon, expand=expand)
updated_coupon = api_response.coupon

print(updated_coupon)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_oid** | **int**| The coupon_oid to update. |
 **coupon** | [**Coupon**](Coupon.md)| Coupon to update |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CouponResponse**](CouponResponse.md)

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

# **update_coupons**
> CouponsResponse update_coupons(coupons_request)

Update multiple coupons

Update multiple coupon on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import CouponsRequest
from samples import api_client
from datetime import datetime, timedelta

coupon_api = CouponApi(api_client())
coupon_oid = 123456789

expand = None  # coupons do not have expansions
placeholders = None  # coupons do not use placeholders

api_response = coupon_api.get_coupon(coupon_oid, expand=expand)
coupon = api_response.coupon

# update the coupon.  this can be difficult given the complexity of coupons.  see insertCoupon sample for details.
expiration_date = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%dT00:00:00+00:00')
coupon.expiration_dts = expiration_date

# This example only has one coupon.  But it's a trivial matter to add more coupons
coupons_request = CouponsRequest()
coupons_request.coupons = [coupon]

api_response = coupon_api.update_coupons(coupons_request, expand=expand, placeholders=placeholders)
updated_coupons = api_response.coupons

print(updated_coupons)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupons_request** | [**CouponsRequest**](CouponsRequest.md)| Coupons to update (synchronous maximum 50 / asynchronous maximum 100) |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional]
 **_async** | **bool**| True if the operation should be run async.  No result returned | [optional]

### Return type

[**CouponsResponse**](CouponsResponse.md)

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

# **upload_coupon_codes**
> UploadCouponCodesResponse upload_coupon_codes(coupon_oid, upload_coupon_codes_request)

Upload one-time codes for a coupon

Upload one-time codes for a coupon 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CouponApi
from ultracart.models import UploadCouponCodesRequest
from samples import api_client

"""
uploadCouponCodes allows a merchant to upload one-time use codes and associate them with a merchant code (i.e. a coupon).
UltraCart has methods for generating one-time codes, and they work well, but this method exists when the merchant generates
them themselves.  This frequently occurs when a merchant sends out a mailer with unique coupon codes on the mailer.  The
merchant can then upload those codes with this method.
"""

coupon_api = CouponApi(api_client())
coupon_oid = 12345678  # if you don't know your coupon_oid, use generateOneTimeCodesByMerchantCode.  same results

codes_request = UploadCouponCodesRequest()
codes_request.coupon_codes = ['code1', 'code2', 'code3']

api_response = coupon_api.upload_coupon_codes(coupon_oid, codes_request)
print('Uploaded codes:')
print(api_response.uploaded_codes)
print('Duplicated codes:')
print(api_response.duplicate_codes)
print('Rejected codes:')
print(api_response.rejected_codes)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_oid** | **int**| The coupon oid to associate with the provided one-time codes. |
 **upload_coupon_codes_request** | [**UploadCouponCodesRequest**](UploadCouponCodesRequest.md)| One-time coupon codes |

### Return type

[**UploadCouponCodesResponse**](UploadCouponCodesResponse.md)

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

