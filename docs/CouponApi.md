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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_oid = 1 # int | The coupon_oid to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a coupon
        api_instance.delete_coupon(coupon_oid)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->delete_coupon: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.coupon_deletes_request import CouponDeletesRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_delete_request = CouponDeletesRequest(
        coupon_codes=[
            "coupon_codes_example",
        ],
        coupon_oids=[
            1,
        ],
    ) # CouponDeletesRequest | Coupon oids to delete

    # example passing only required values which don't have defaults set
    try:
        # Deletes multiple coupons
        api_instance.delete_coupons_by_code(coupon_delete_request)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->delete_coupons_by_code: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.coupon_deletes_request import CouponDeletesRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_delete_request = CouponDeletesRequest(
        coupon_codes=[
            "coupon_codes_example",
        ],
        coupon_oids=[
            1,
        ],
    ) # CouponDeletesRequest | Coupon oids to delete

    # example passing only required values which don't have defaults set
    try:
        # Deletes multiple coupons
        api_instance.delete_coupons_by_oid(coupon_delete_request)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->delete_coupons_by_oid: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_exists_response import CouponExistsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_code = "merchant_code_example" # str | The coupon merchant code to examine.

    # example passing only required values which don't have defaults set
    try:
        # Determines if a coupon merchant code already exists
        api_response = api_instance.does_coupon_code_exist(merchant_code)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->does_coupon_code_exist: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_codes_response import CouponCodesResponse
from ultracart.model.coupon_codes_request import CouponCodesRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_oid = 1 # int | The coupon oid to generate codes.
    coupon_codes_request = CouponCodesRequest(
        error=Error(
            developer_message="developer_message_example",
            error_code="error_code_example",
            more_info="more_info_example",
            object_id="object_id_example",
            user_message="user_message_example",
        ),
        expiration_dts="expiration_dts_example",
        expiration_seconds=1,
        metadata=ResponseMetadata(
            payload_name="payload_name_example",
            result_set=ResultSet(
                count=1,
                limit=1,
                more=True,
                next_offset=1,
                offset=1,
                total_records=1,
            ),
        ),
        quantity=1,
        success=True,
        warning=Warning(
            more_info="more_info_example",
            warning_message="warning_message_example",
        ),
    ) # CouponCodesRequest | Coupon code generation parameters

    # example passing only required values which don't have defaults set
    try:
        # Generates one time codes for a coupon
        api_response = api_instance.generate_coupon_codes(coupon_oid, coupon_codes_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->generate_coupon_codes: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_codes_response import CouponCodesResponse
from ultracart.model.coupon_codes_request import CouponCodesRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_code = "merchant_code_example" # str | The merchant code to generate one time codes.
    coupon_codes_request = CouponCodesRequest(
        error=Error(
            developer_message="developer_message_example",
            error_code="error_code_example",
            more_info="more_info_example",
            object_id="object_id_example",
            user_message="user_message_example",
        ),
        expiration_dts="expiration_dts_example",
        expiration_seconds=1,
        metadata=ResponseMetadata(
            payload_name="payload_name_example",
            result_set=ResultSet(
                count=1,
                limit=1,
                more=True,
                next_offset=1,
                offset=1,
                total_records=1,
            ),
        ),
        quantity=1,
        success=True,
        warning=Warning(
            more_info="more_info_example",
            warning_message="warning_message_example",
        ),
    ) # CouponCodesRequest | Coupon code generation parameters

    # example passing only required values which don't have defaults set
    try:
        # Generates one time codes by merchant code
        api_response = api_instance.generate_one_time_codes_by_merchant_code(merchant_code, coupon_codes_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->generate_one_time_codes_by_merchant_code: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_auto_apply_conditions import CouponAutoApplyConditions
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve auto apply rules and conditions
        api_response = api_instance.get_auto_apply()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_auto_apply: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_response import CouponResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_oid = 1 # int | The coupon oid to retrieve.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a coupon
        api_response = api_instance.get_coupon(coupon_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a coupon
        api_response = api_instance.get_coupon(coupon_oid, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_coupon: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_response import CouponResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_code = "merchant_code_example" # str | The coupon merchant code to retrieve.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a coupon by merchant code
        api_response = api_instance.get_coupon_by_merchant_code(merchant_code)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_coupon_by_merchant_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a coupon by merchant code
        api_response = api_instance.get_coupon_by_merchant_code(merchant_code, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_coupon_by_merchant_code: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupons_response import CouponsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    merchant_code = "merchant_code_example" # str | Merchant code (optional)
    description = "description_example" # str | Description (optional)
    coupon_type = "coupon_type_example" # str | Coupon type (optional)
    start_date_begin = "start_date_begin_example" # str | Start date begin (optional)
    start_date_end = "start_date_end_example" # str | Start date end (optional)
    expiration_date_begin = "expiration_date_begin_example" # str | Expiration date begin (optional)
    expiration_date_end = "expiration_date_end_example" # str | Expiration date end (optional)
    affiliate_oid = 1 # int | Affiliate oid (optional)
    exclude_expired = True # bool | Exclude expired (optional)
    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve coupons
        api_response = api_instance.get_coupons(merchant_code=merchant_code, description=description, coupon_type=coupon_type, start_date_begin=start_date_begin, start_date_end=start_date_end, expiration_date_begin=expiration_date_begin, expiration_date_end=expiration_date_end, affiliate_oid=affiliate_oid, exclude_expired=exclude_expired, limit=limit, offset=offset, sort=sort, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_coupons: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupons_response import CouponsResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.coupon_query import CouponQuery
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_query = CouponQuery(
        affiliate_oid=1,
        coupon_type="coupon_type_example",
        description="description_example",
        exclude_expired=True,
        expiration_dts_begin="expiration_dts_begin_example",
        expiration_dts_end="expiration_dts_end_example",
        merchant_code="merchant_code_example",
        merchant_code_or_description="merchant_code_or_description_example",
        start_dts_begin="start_dts_begin_example",
        start_dts_end="start_dts_end_example",
    ) # CouponQuery | Coupon query
    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve coupons by query
        api_response = api_instance.get_coupons_by_query(coupon_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_coupons_by_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve coupons by query
        api_response = api_instance.get_coupons_by_query(coupon_query, limit=limit, offset=offset, sort=sort, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_coupons_by_query: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.coupon_editor_values import CouponEditorValues
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve values needed for a coupon editor
        api_response = api_instance.get_editor_values()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->get_editor_values: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_response import CouponResponse
from ultracart.model.coupon import Coupon
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon = Coupon(
        affiliate_oid=1,
        allow_multiple_one_time_codes=True,
        amount_off_items=CouponAmountOffItems(
            currency_code="currency_code_example",
            discount_amount=3.14,
            items=[
                "items_example",
            ],
            limit=1,
        ),
        amount_off_shipping=CouponAmountOffShipping(
            currency_code="currency_code_example",
            discount_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        amount_off_shipping_with_items_purchase=CouponAmountOffShippingWithItemsPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            items=[
                "items_example",
            ],
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        amount_off_subtotal=CouponAmountOffSubtotal(
            currency_code="currency_code_example",
            discount_amount=3.14,
        ),
        amount_off_subtotal_and_free_shipping=CouponAmountOffSubtotalFreeShippingWithPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            purchase_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        amount_off_subtotal_and_shipping=CouponAmountOffSubtotalAndShipping(
            currency_code="currency_code_example",
            discount_amount=3.14,
        ),
        amount_off_subtotal_with_block_purchase=CouponAmountOffSubtotalWithBlockPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            required_purchase_item="required_purchase_item_example",
            required_purchase_quantity=1,
        ),
        amount_off_subtotal_with_items_purchase=CouponAmountOffSubtotalWithItemsPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            items=[
                "items_example",
            ],
            required_purchase_quantity=1,
        ),
        amount_off_subtotal_with_purchase=CouponAmountOffSubtotalWithPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            purchase_amount=3.14,
        ),
        amount_shipping_with_subtotal=CouponAmountShippingWithSubtotal(
            currency_code="currency_code_example",
            purchase_amount=3.14,
            shipping_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        automatically_apply_coupon_codes=CouponAutomaticallyApplyCouponCodes(
            coupon_codes=[
                "coupon_codes_example",
            ],
        ),
        buy_one_get_one=CouponBuyOneGetOneLimit(
            items=[
                "items_example",
            ],
            limit=1,
        ),
        calculated_description="calculated_description_example",
        can_be_used_with_other_coupons=True,
        coupon_oid=1,
        coupon_type="coupon_type_example",
        description="description_example",
        discount_item_with_item_purchase=CouponDiscountItemWithItemPurchase(
            currency_code="currency_code_example",
            discount_item="discount_item_example",
            discount_price=3.14,
            limit=1,
            required_purchase_item="required_purchase_item_example",
        ),
        discount_items=CouponDiscountItems(
            currency_code="currency_code_example",
            discount_price=3.14,
            items=[
                "items_example",
            ],
            limit=1,
        ),
        expiration_dts="expiration_dts_example",
        free_item_and_shipping_with_subtotal=CouponFreeItemAndShippingWithSubtotal(
            currency_code="currency_code_example",
            items=[
                "items_example",
            ],
            limit=1,
            shipping_methods=[
                "shipping_methods_example",
            ],
            subtotal_amount=3.14,
        ),
        free_item_with_item_purchase=CouponFreeItemWithItemPurchase(
            items=[
                "items_example",
            ],
            limit=1,
            match_required_purchase_item_to_free_item=True,
            required_purchase_items=[
                "required_purchase_items_example",
            ],
        ),
        free_item_with_subtotal=CouponFreeItemWithSubtotal(
            currency_code="currency_code_example",
            items=[
                "items_example",
            ],
            limit=1,
            subtotal_amount=3.14,
        ),
        free_items_with_item_purchase=CouponFreeItemsWithItemPurchase(
            free_item="free_item_example",
            free_quantity=1,
            limit=1,
            required_purchase_item="required_purchase_item_example",
            required_purchase_quantity=1,
        ),
        free_items_with_mixmatch_purchase=CouponFreeItemsWithMixMatchPurchase(
            free_item="free_item_example",
            free_quantity=1,
            limit=1,
            required_purchase_mix_and_match_group="required_purchase_mix_and_match_group_example",
            required_purchase_quantity=1,
        ),
        free_shipping=CouponFreeShipping(
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        free_shipping_specific_items=CouponFreeShippingSpecificItems(
            items=[
                "items_example",
            ],
        ),
        free_shipping_with_items_purchase=CouponFreeShippingWithItemsPurchase(
            items=[
                "items_example",
            ],
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        free_shipping_with_subtotal=CouponFreeShippingWithSubtotal(
            currency_code="currency_code_example",
            purchase_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        hide_from_customer=True,
        merchant_code="merchant_code_example",
        merchant_notes="merchant_notes_example",
        more_loyalty_cashback=CouponMoreLoyaltyCashback(
            loyalty_cashback=3.14,
        ),
        more_loyalty_points=CouponMoreLoyaltyPoints(
            loyalty_points=3.14,
        ),
        multiple_amounts_off_items=CouponMultipleAmountsOffItems(
            discounts=[
                CouponTierItemDiscount(
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                ),
            ],
            limit=1,
        ),
        no_discount=CouponNoDiscount(
            ignore_this_property=True,
        ),
        percent_more_loyalty_cashback=CouponPercentMoreLoyaltyCashback(
            percent_more_loyalty_cashback=3.14,
        ),
        percent_more_loyalty_points=CouponPercentMoreLoyaltyPoints(
            percent_more_loyalty_points=3.14,
        ),
        percent_off_item_with_items_quantity_purchase=CouponPercentOffItemWithItemsQuantityPurchase(
            discount_percent=3.14,
            items=[
                "items_example",
            ],
            limit=1,
            required_purchase_items=[
                "required_purchase_items_example",
            ],
            required_purchase_quantity=1,
        ),
        percent_off_items=CouponPercentOffItems(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
            limit=1,
        ),
        percent_off_items_and_free_shipping=CouponPercentOffItemsAndFreeShipping(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
        ),
        percent_off_items_with_items_purchase=CouponPercentOffItemsWithItemsPurchase(
            discount_percent=3.14,
            items=[
                "items_example",
            ],
            limit=1,
            required_purchase_items=[
                "required_purchase_items_example",
            ],
        ),
        percent_off_msrp_items=CouponPercentOffMsrpItems(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
            limit=1,
            minimum_cumulative_msrp=3.14,
            minimum_subtotal=3.14,
        ),
        percent_off_retail_price_items=CouponPercentOffRetailPriceItems(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
            limit=1,
        ),
        percent_off_shipping=CouponPercentOffShipping(
            discount_percent=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        percent_off_subtotal=CouponPercentOffSubtotal(
            discount_percent=3.14,
        ),
        percent_off_subtotal_and_free_shipping=CouponPercentOffSubtotalAndFreeShipping(
            discount_percent=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        percent_off_subtotal_limit=CouponPercentOffSubtotalLimit(
            currency_code="currency_code_example",
            discount_percent=3.14,
            limit=3.14,
        ),
        percent_off_subtotal_with_items_purchase=CouponPercentOffSubtotalWithItemsPurchase(
            discount_percent=3.14,
            items=[
                "items_example",
            ],
        ),
        percent_off_subtotal_with_subtotal=CouponPercentOffSubtotalWithSubtotal(
            currency_code="currency_code_example",
            discount_percent=3.14,
            subtotal_amount=3.14,
        ),
        quickbooks_code="quickbooks_code_example",
        restrict_by_postal_codes=[
            "restrict_by_postal_codes_example",
        ],
        restrict_by_screen_branding_theme_codes=[
            CouponRestriction(
                invalid_for_this=True,
                name="name_example",
                valid_for_this=True,
                valid_only_for_this=True,
            ),
        ],
        restrict_by_storefronts=[
            CouponRestriction(
                invalid_for_this=True,
                name="name_example",
                valid_for_this=True,
                valid_only_for_this=True,
            ),
        ],
        skip_on_rebill=True,
        start_dts="start_dts_example",
        super_coupon=True,
        tiered_amount_off_items=CouponTieredAmountOffItems(
            items=[
                "items_example",
            ],
            limit=3.14,
            tiers=[
                CouponTierQuantityAmount(
                    discount_amount=3.14,
                    item_quantity=1,
                    quickbooks_code="quickbooks_code_example",
                ),
            ],
        ),
        tiered_amount_off_subtotal=CouponTieredAmountOffSubtotal(
            items=[
                "items_example",
            ],
            tiers=[
                CouponTierAmount(
                    discount_amount=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        tiered_percent_off_items=CouponTieredPercentOffItems(
            items=[
                "items_example",
            ],
            limit=3.14,
            tiers=[
                CouponTierQuantityPercent(
                    discount_percent=3.14,
                    item_quantity=1,
                    quickbooks_code="quickbooks_code_example",
                ),
            ],
        ),
        tiered_percent_off_shipping=CouponTieredPercentOffShipping(
            quickbooks_code="quickbooks_code_example",
            shipping_methods=[
                "shipping_methods_example",
            ],
            tiers=[
                CouponTierPercent(
                    discount_percent=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        tiered_percent_off_subtotal=CouponTieredPercentOffSubtotal(
            items=[
                "items_example",
            ],
            tiers=[
                CouponTierPercent(
                    discount_percent=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        tiered_percent_off_subtotal_based_on_msrp=CouponTieredPercentOffSubtotalBasedOnMSRP(
            items=[
                "items_example",
            ],
            tiers=[
                CouponTierPercent(
                    discount_percent=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        usable_by="Anyone",
    ) # Coupon | Coupon to insert
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert a coupon
        api_response = api_instance.insert_coupon(coupon)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->insert_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert a coupon
        api_response = api_instance.insert_coupon(coupon, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->insert_coupon: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupons_request import CouponsRequest
from ultracart.model.coupons_response import CouponsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupons_request = CouponsRequest(
        coupons=[
            Coupon(
                affiliate_oid=1,
                allow_multiple_one_time_codes=True,
                amount_off_items=CouponAmountOffItems(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                amount_off_shipping=CouponAmountOffShipping(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                amount_off_shipping_with_items_purchase=CouponAmountOffShippingWithItemsPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                amount_off_subtotal=CouponAmountOffSubtotal(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                ),
                amount_off_subtotal_and_free_shipping=CouponAmountOffSubtotalFreeShippingWithPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    purchase_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                amount_off_subtotal_and_shipping=CouponAmountOffSubtotalAndShipping(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                ),
                amount_off_subtotal_with_block_purchase=CouponAmountOffSubtotalWithBlockPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    required_purchase_item="required_purchase_item_example",
                    required_purchase_quantity=1,
                ),
                amount_off_subtotal_with_items_purchase=CouponAmountOffSubtotalWithItemsPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                    required_purchase_quantity=1,
                ),
                amount_off_subtotal_with_purchase=CouponAmountOffSubtotalWithPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    purchase_amount=3.14,
                ),
                amount_shipping_with_subtotal=CouponAmountShippingWithSubtotal(
                    currency_code="currency_code_example",
                    purchase_amount=3.14,
                    shipping_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                automatically_apply_coupon_codes=CouponAutomaticallyApplyCouponCodes(
                    coupon_codes=[
                        "coupon_codes_example",
                    ],
                ),
                buy_one_get_one=CouponBuyOneGetOneLimit(
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                calculated_description="calculated_description_example",
                can_be_used_with_other_coupons=True,
                coupon_oid=1,
                coupon_type="coupon_type_example",
                description="description_example",
                discount_item_with_item_purchase=CouponDiscountItemWithItemPurchase(
                    currency_code="currency_code_example",
                    discount_item="discount_item_example",
                    discount_price=3.14,
                    limit=1,
                    required_purchase_item="required_purchase_item_example",
                ),
                discount_items=CouponDiscountItems(
                    currency_code="currency_code_example",
                    discount_price=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                expiration_dts="expiration_dts_example",
                free_item_and_shipping_with_subtotal=CouponFreeItemAndShippingWithSubtotal(
                    currency_code="currency_code_example",
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                    subtotal_amount=3.14,
                ),
                free_item_with_item_purchase=CouponFreeItemWithItemPurchase(
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    match_required_purchase_item_to_free_item=True,
                    required_purchase_items=[
                        "required_purchase_items_example",
                    ],
                ),
                free_item_with_subtotal=CouponFreeItemWithSubtotal(
                    currency_code="currency_code_example",
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    subtotal_amount=3.14,
                ),
                free_items_with_item_purchase=CouponFreeItemsWithItemPurchase(
                    free_item="free_item_example",
                    free_quantity=1,
                    limit=1,
                    required_purchase_item="required_purchase_item_example",
                    required_purchase_quantity=1,
                ),
                free_items_with_mixmatch_purchase=CouponFreeItemsWithMixMatchPurchase(
                    free_item="free_item_example",
                    free_quantity=1,
                    limit=1,
                    required_purchase_mix_and_match_group="required_purchase_mix_and_match_group_example",
                    required_purchase_quantity=1,
                ),
                free_shipping=CouponFreeShipping(
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                free_shipping_specific_items=CouponFreeShippingSpecificItems(
                    items=[
                        "items_example",
                    ],
                ),
                free_shipping_with_items_purchase=CouponFreeShippingWithItemsPurchase(
                    items=[
                        "items_example",
                    ],
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                free_shipping_with_subtotal=CouponFreeShippingWithSubtotal(
                    currency_code="currency_code_example",
                    purchase_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                hide_from_customer=True,
                merchant_code="merchant_code_example",
                merchant_notes="merchant_notes_example",
                more_loyalty_cashback=CouponMoreLoyaltyCashback(
                    loyalty_cashback=3.14,
                ),
                more_loyalty_points=CouponMoreLoyaltyPoints(
                    loyalty_points=3.14,
                ),
                multiple_amounts_off_items=CouponMultipleAmountsOffItems(
                    discounts=[
                        CouponTierItemDiscount(
                            discount_amount=3.14,
                            items=[
                                "items_example",
                            ],
                        ),
                    ],
                    limit=1,
                ),
                no_discount=CouponNoDiscount(
                    ignore_this_property=True,
                ),
                percent_more_loyalty_cashback=CouponPercentMoreLoyaltyCashback(
                    percent_more_loyalty_cashback=3.14,
                ),
                percent_more_loyalty_points=CouponPercentMoreLoyaltyPoints(
                    percent_more_loyalty_points=3.14,
                ),
                percent_off_item_with_items_quantity_purchase=CouponPercentOffItemWithItemsQuantityPurchase(
                    discount_percent=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    required_purchase_items=[
                        "required_purchase_items_example",
                    ],
                    required_purchase_quantity=1,
                ),
                percent_off_items=CouponPercentOffItems(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                percent_off_items_and_free_shipping=CouponPercentOffItemsAndFreeShipping(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                ),
                percent_off_items_with_items_purchase=CouponPercentOffItemsWithItemsPurchase(
                    discount_percent=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    required_purchase_items=[
                        "required_purchase_items_example",
                    ],
                ),
                percent_off_msrp_items=CouponPercentOffMsrpItems(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    minimum_cumulative_msrp=3.14,
                    minimum_subtotal=3.14,
                ),
                percent_off_retail_price_items=CouponPercentOffRetailPriceItems(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                percent_off_shipping=CouponPercentOffShipping(
                    discount_percent=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                percent_off_subtotal=CouponPercentOffSubtotal(
                    discount_percent=3.14,
                ),
                percent_off_subtotal_and_free_shipping=CouponPercentOffSubtotalAndFreeShipping(
                    discount_percent=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                percent_off_subtotal_limit=CouponPercentOffSubtotalLimit(
                    currency_code="currency_code_example",
                    discount_percent=3.14,
                    limit=3.14,
                ),
                percent_off_subtotal_with_items_purchase=CouponPercentOffSubtotalWithItemsPurchase(
                    discount_percent=3.14,
                    items=[
                        "items_example",
                    ],
                ),
                percent_off_subtotal_with_subtotal=CouponPercentOffSubtotalWithSubtotal(
                    currency_code="currency_code_example",
                    discount_percent=3.14,
                    subtotal_amount=3.14,
                ),
                quickbooks_code="quickbooks_code_example",
                restrict_by_postal_codes=[
                    "restrict_by_postal_codes_example",
                ],
                restrict_by_screen_branding_theme_codes=[
                    CouponRestriction(
                        invalid_for_this=True,
                        name="name_example",
                        valid_for_this=True,
                        valid_only_for_this=True,
                    ),
                ],
                restrict_by_storefronts=[
                    CouponRestriction(
                        invalid_for_this=True,
                        name="name_example",
                        valid_for_this=True,
                        valid_only_for_this=True,
                    ),
                ],
                skip_on_rebill=True,
                start_dts="start_dts_example",
                super_coupon=True,
                tiered_amount_off_items=CouponTieredAmountOffItems(
                    items=[
                        "items_example",
                    ],
                    limit=3.14,
                    tiers=[
                        CouponTierQuantityAmount(
                            discount_amount=3.14,
                            item_quantity=1,
                            quickbooks_code="quickbooks_code_example",
                        ),
                    ],
                ),
                tiered_amount_off_subtotal=CouponTieredAmountOffSubtotal(
                    items=[
                        "items_example",
                    ],
                    tiers=[
                        CouponTierAmount(
                            discount_amount=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                tiered_percent_off_items=CouponTieredPercentOffItems(
                    items=[
                        "items_example",
                    ],
                    limit=3.14,
                    tiers=[
                        CouponTierQuantityPercent(
                            discount_percent=3.14,
                            item_quantity=1,
                            quickbooks_code="quickbooks_code_example",
                        ),
                    ],
                ),
                tiered_percent_off_shipping=CouponTieredPercentOffShipping(
                    quickbooks_code="quickbooks_code_example",
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                    tiers=[
                        CouponTierPercent(
                            discount_percent=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                tiered_percent_off_subtotal=CouponTieredPercentOffSubtotal(
                    items=[
                        "items_example",
                    ],
                    tiers=[
                        CouponTierPercent(
                            discount_percent=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                tiered_percent_off_subtotal_based_on_msrp=CouponTieredPercentOffSubtotalBasedOnMSRP(
                    items=[
                        "items_example",
                    ],
                    tiers=[
                        CouponTierPercent(
                            discount_percent=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                usable_by="Anyone",
            ),
        ],
    ) # CouponsRequest | Coupons to insert (maximum 50)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert multiple coupons
        api_response = api_instance.insert_coupons(coupons_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->insert_coupons: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert multiple coupons
        api_response = api_instance.insert_coupons(coupons_request, expand=expand, placeholders=placeholders)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->insert_coupons: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.coupon_item_search_results_response import CouponItemSearchResultsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    s = "s_example" # str |  (optional)
    m = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Searches for items to display within a coupon editor and assign to coupons
        api_response = api_instance.search_items(s=s, m=m)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->search_items: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_auto_apply_conditions import CouponAutoApplyConditions
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conditions = CouponAutoApplyConditions(
        error=Error(
            developer_message="developer_message_example",
            error_code="error_code_example",
            more_info="more_info_example",
            object_id="object_id_example",
            user_message="user_message_example",
        ),
        metadata=ResponseMetadata(
            payload_name="payload_name_example",
            result_set=ResultSet(
                count=1,
                limit=1,
                more=True,
                next_offset=1,
                offset=1,
                total_records=1,
            ),
        ),
        required_items=[
            CouponAutoApplyCondition(
                coupon_code="coupon_code_example",
                minimum_subtotal=3.14,
                required_item_id="required_item_id_example",
            ),
        ],
        subtotal_levels=[
            CouponAutoApplyCondition(
                coupon_code="coupon_code_example",
                minimum_subtotal=3.14,
                required_item_id="required_item_id_example",
            ),
        ],
        success=True,
        warning=Warning(
            more_info="more_info_example",
            warning_message="warning_message_example",
        ),
    ) # CouponAutoApplyConditions | Conditions

    # example passing only required values which don't have defaults set
    try:
        # Update auto apply rules and conditions
        api_instance.update_auto_apply(conditions)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->update_auto_apply: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupon_response import CouponResponse
from ultracart.model.coupon import Coupon
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_oid = 1 # int | The coupon_oid to update.
    coupon = Coupon(
        affiliate_oid=1,
        allow_multiple_one_time_codes=True,
        amount_off_items=CouponAmountOffItems(
            currency_code="currency_code_example",
            discount_amount=3.14,
            items=[
                "items_example",
            ],
            limit=1,
        ),
        amount_off_shipping=CouponAmountOffShipping(
            currency_code="currency_code_example",
            discount_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        amount_off_shipping_with_items_purchase=CouponAmountOffShippingWithItemsPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            items=[
                "items_example",
            ],
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        amount_off_subtotal=CouponAmountOffSubtotal(
            currency_code="currency_code_example",
            discount_amount=3.14,
        ),
        amount_off_subtotal_and_free_shipping=CouponAmountOffSubtotalFreeShippingWithPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            purchase_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        amount_off_subtotal_and_shipping=CouponAmountOffSubtotalAndShipping(
            currency_code="currency_code_example",
            discount_amount=3.14,
        ),
        amount_off_subtotal_with_block_purchase=CouponAmountOffSubtotalWithBlockPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            required_purchase_item="required_purchase_item_example",
            required_purchase_quantity=1,
        ),
        amount_off_subtotal_with_items_purchase=CouponAmountOffSubtotalWithItemsPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            items=[
                "items_example",
            ],
            required_purchase_quantity=1,
        ),
        amount_off_subtotal_with_purchase=CouponAmountOffSubtotalWithPurchase(
            currency_code="currency_code_example",
            discount_amount=3.14,
            purchase_amount=3.14,
        ),
        amount_shipping_with_subtotal=CouponAmountShippingWithSubtotal(
            currency_code="currency_code_example",
            purchase_amount=3.14,
            shipping_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        automatically_apply_coupon_codes=CouponAutomaticallyApplyCouponCodes(
            coupon_codes=[
                "coupon_codes_example",
            ],
        ),
        buy_one_get_one=CouponBuyOneGetOneLimit(
            items=[
                "items_example",
            ],
            limit=1,
        ),
        calculated_description="calculated_description_example",
        can_be_used_with_other_coupons=True,
        coupon_oid=1,
        coupon_type="coupon_type_example",
        description="description_example",
        discount_item_with_item_purchase=CouponDiscountItemWithItemPurchase(
            currency_code="currency_code_example",
            discount_item="discount_item_example",
            discount_price=3.14,
            limit=1,
            required_purchase_item="required_purchase_item_example",
        ),
        discount_items=CouponDiscountItems(
            currency_code="currency_code_example",
            discount_price=3.14,
            items=[
                "items_example",
            ],
            limit=1,
        ),
        expiration_dts="expiration_dts_example",
        free_item_and_shipping_with_subtotal=CouponFreeItemAndShippingWithSubtotal(
            currency_code="currency_code_example",
            items=[
                "items_example",
            ],
            limit=1,
            shipping_methods=[
                "shipping_methods_example",
            ],
            subtotal_amount=3.14,
        ),
        free_item_with_item_purchase=CouponFreeItemWithItemPurchase(
            items=[
                "items_example",
            ],
            limit=1,
            match_required_purchase_item_to_free_item=True,
            required_purchase_items=[
                "required_purchase_items_example",
            ],
        ),
        free_item_with_subtotal=CouponFreeItemWithSubtotal(
            currency_code="currency_code_example",
            items=[
                "items_example",
            ],
            limit=1,
            subtotal_amount=3.14,
        ),
        free_items_with_item_purchase=CouponFreeItemsWithItemPurchase(
            free_item="free_item_example",
            free_quantity=1,
            limit=1,
            required_purchase_item="required_purchase_item_example",
            required_purchase_quantity=1,
        ),
        free_items_with_mixmatch_purchase=CouponFreeItemsWithMixMatchPurchase(
            free_item="free_item_example",
            free_quantity=1,
            limit=1,
            required_purchase_mix_and_match_group="required_purchase_mix_and_match_group_example",
            required_purchase_quantity=1,
        ),
        free_shipping=CouponFreeShipping(
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        free_shipping_specific_items=CouponFreeShippingSpecificItems(
            items=[
                "items_example",
            ],
        ),
        free_shipping_with_items_purchase=CouponFreeShippingWithItemsPurchase(
            items=[
                "items_example",
            ],
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        free_shipping_with_subtotal=CouponFreeShippingWithSubtotal(
            currency_code="currency_code_example",
            purchase_amount=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        hide_from_customer=True,
        merchant_code="merchant_code_example",
        merchant_notes="merchant_notes_example",
        more_loyalty_cashback=CouponMoreLoyaltyCashback(
            loyalty_cashback=3.14,
        ),
        more_loyalty_points=CouponMoreLoyaltyPoints(
            loyalty_points=3.14,
        ),
        multiple_amounts_off_items=CouponMultipleAmountsOffItems(
            discounts=[
                CouponTierItemDiscount(
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                ),
            ],
            limit=1,
        ),
        no_discount=CouponNoDiscount(
            ignore_this_property=True,
        ),
        percent_more_loyalty_cashback=CouponPercentMoreLoyaltyCashback(
            percent_more_loyalty_cashback=3.14,
        ),
        percent_more_loyalty_points=CouponPercentMoreLoyaltyPoints(
            percent_more_loyalty_points=3.14,
        ),
        percent_off_item_with_items_quantity_purchase=CouponPercentOffItemWithItemsQuantityPurchase(
            discount_percent=3.14,
            items=[
                "items_example",
            ],
            limit=1,
            required_purchase_items=[
                "required_purchase_items_example",
            ],
            required_purchase_quantity=1,
        ),
        percent_off_items=CouponPercentOffItems(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
            limit=1,
        ),
        percent_off_items_and_free_shipping=CouponPercentOffItemsAndFreeShipping(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
        ),
        percent_off_items_with_items_purchase=CouponPercentOffItemsWithItemsPurchase(
            discount_percent=3.14,
            items=[
                "items_example",
            ],
            limit=1,
            required_purchase_items=[
                "required_purchase_items_example",
            ],
        ),
        percent_off_msrp_items=CouponPercentOffMsrpItems(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
            limit=1,
            minimum_cumulative_msrp=3.14,
            minimum_subtotal=3.14,
        ),
        percent_off_retail_price_items=CouponPercentOffRetailPriceItems(
            discount_percent=3.14,
            excluded_items=[
                "excluded_items_example",
            ],
            items=[
                "items_example",
            ],
            limit=1,
        ),
        percent_off_shipping=CouponPercentOffShipping(
            discount_percent=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        percent_off_subtotal=CouponPercentOffSubtotal(
            discount_percent=3.14,
        ),
        percent_off_subtotal_and_free_shipping=CouponPercentOffSubtotalAndFreeShipping(
            discount_percent=3.14,
            shipping_methods=[
                "shipping_methods_example",
            ],
        ),
        percent_off_subtotal_limit=CouponPercentOffSubtotalLimit(
            currency_code="currency_code_example",
            discount_percent=3.14,
            limit=3.14,
        ),
        percent_off_subtotal_with_items_purchase=CouponPercentOffSubtotalWithItemsPurchase(
            discount_percent=3.14,
            items=[
                "items_example",
            ],
        ),
        percent_off_subtotal_with_subtotal=CouponPercentOffSubtotalWithSubtotal(
            currency_code="currency_code_example",
            discount_percent=3.14,
            subtotal_amount=3.14,
        ),
        quickbooks_code="quickbooks_code_example",
        restrict_by_postal_codes=[
            "restrict_by_postal_codes_example",
        ],
        restrict_by_screen_branding_theme_codes=[
            CouponRestriction(
                invalid_for_this=True,
                name="name_example",
                valid_for_this=True,
                valid_only_for_this=True,
            ),
        ],
        restrict_by_storefronts=[
            CouponRestriction(
                invalid_for_this=True,
                name="name_example",
                valid_for_this=True,
                valid_only_for_this=True,
            ),
        ],
        skip_on_rebill=True,
        start_dts="start_dts_example",
        super_coupon=True,
        tiered_amount_off_items=CouponTieredAmountOffItems(
            items=[
                "items_example",
            ],
            limit=3.14,
            tiers=[
                CouponTierQuantityAmount(
                    discount_amount=3.14,
                    item_quantity=1,
                    quickbooks_code="quickbooks_code_example",
                ),
            ],
        ),
        tiered_amount_off_subtotal=CouponTieredAmountOffSubtotal(
            items=[
                "items_example",
            ],
            tiers=[
                CouponTierAmount(
                    discount_amount=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        tiered_percent_off_items=CouponTieredPercentOffItems(
            items=[
                "items_example",
            ],
            limit=3.14,
            tiers=[
                CouponTierQuantityPercent(
                    discount_percent=3.14,
                    item_quantity=1,
                    quickbooks_code="quickbooks_code_example",
                ),
            ],
        ),
        tiered_percent_off_shipping=CouponTieredPercentOffShipping(
            quickbooks_code="quickbooks_code_example",
            shipping_methods=[
                "shipping_methods_example",
            ],
            tiers=[
                CouponTierPercent(
                    discount_percent=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        tiered_percent_off_subtotal=CouponTieredPercentOffSubtotal(
            items=[
                "items_example",
            ],
            tiers=[
                CouponTierPercent(
                    discount_percent=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        tiered_percent_off_subtotal_based_on_msrp=CouponTieredPercentOffSubtotalBasedOnMSRP(
            items=[
                "items_example",
            ],
            tiers=[
                CouponTierPercent(
                    discount_percent=3.14,
                    quickbooks_code="quickbooks_code_example",
                    subtotal_amount=3.14,
                ),
            ],
        ),
        usable_by="Anyone",
    ) # Coupon | Coupon to update
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a coupon
        api_response = api_instance.update_coupon(coupon_oid, coupon)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->update_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a coupon
        api_response = api_instance.update_coupon(coupon_oid, coupon, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->update_coupon: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.coupons_request import CouponsRequest
from ultracart.model.coupons_response import CouponsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupons_request = CouponsRequest(
        coupons=[
            Coupon(
                affiliate_oid=1,
                allow_multiple_one_time_codes=True,
                amount_off_items=CouponAmountOffItems(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                amount_off_shipping=CouponAmountOffShipping(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                amount_off_shipping_with_items_purchase=CouponAmountOffShippingWithItemsPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                amount_off_subtotal=CouponAmountOffSubtotal(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                ),
                amount_off_subtotal_and_free_shipping=CouponAmountOffSubtotalFreeShippingWithPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    purchase_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                amount_off_subtotal_and_shipping=CouponAmountOffSubtotalAndShipping(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                ),
                amount_off_subtotal_with_block_purchase=CouponAmountOffSubtotalWithBlockPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    required_purchase_item="required_purchase_item_example",
                    required_purchase_quantity=1,
                ),
                amount_off_subtotal_with_items_purchase=CouponAmountOffSubtotalWithItemsPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    items=[
                        "items_example",
                    ],
                    required_purchase_quantity=1,
                ),
                amount_off_subtotal_with_purchase=CouponAmountOffSubtotalWithPurchase(
                    currency_code="currency_code_example",
                    discount_amount=3.14,
                    purchase_amount=3.14,
                ),
                amount_shipping_with_subtotal=CouponAmountShippingWithSubtotal(
                    currency_code="currency_code_example",
                    purchase_amount=3.14,
                    shipping_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                automatically_apply_coupon_codes=CouponAutomaticallyApplyCouponCodes(
                    coupon_codes=[
                        "coupon_codes_example",
                    ],
                ),
                buy_one_get_one=CouponBuyOneGetOneLimit(
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                calculated_description="calculated_description_example",
                can_be_used_with_other_coupons=True,
                coupon_oid=1,
                coupon_type="coupon_type_example",
                description="description_example",
                discount_item_with_item_purchase=CouponDiscountItemWithItemPurchase(
                    currency_code="currency_code_example",
                    discount_item="discount_item_example",
                    discount_price=3.14,
                    limit=1,
                    required_purchase_item="required_purchase_item_example",
                ),
                discount_items=CouponDiscountItems(
                    currency_code="currency_code_example",
                    discount_price=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                expiration_dts="expiration_dts_example",
                free_item_and_shipping_with_subtotal=CouponFreeItemAndShippingWithSubtotal(
                    currency_code="currency_code_example",
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                    subtotal_amount=3.14,
                ),
                free_item_with_item_purchase=CouponFreeItemWithItemPurchase(
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    match_required_purchase_item_to_free_item=True,
                    required_purchase_items=[
                        "required_purchase_items_example",
                    ],
                ),
                free_item_with_subtotal=CouponFreeItemWithSubtotal(
                    currency_code="currency_code_example",
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    subtotal_amount=3.14,
                ),
                free_items_with_item_purchase=CouponFreeItemsWithItemPurchase(
                    free_item="free_item_example",
                    free_quantity=1,
                    limit=1,
                    required_purchase_item="required_purchase_item_example",
                    required_purchase_quantity=1,
                ),
                free_items_with_mixmatch_purchase=CouponFreeItemsWithMixMatchPurchase(
                    free_item="free_item_example",
                    free_quantity=1,
                    limit=1,
                    required_purchase_mix_and_match_group="required_purchase_mix_and_match_group_example",
                    required_purchase_quantity=1,
                ),
                free_shipping=CouponFreeShipping(
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                free_shipping_specific_items=CouponFreeShippingSpecificItems(
                    items=[
                        "items_example",
                    ],
                ),
                free_shipping_with_items_purchase=CouponFreeShippingWithItemsPurchase(
                    items=[
                        "items_example",
                    ],
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                free_shipping_with_subtotal=CouponFreeShippingWithSubtotal(
                    currency_code="currency_code_example",
                    purchase_amount=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                hide_from_customer=True,
                merchant_code="merchant_code_example",
                merchant_notes="merchant_notes_example",
                more_loyalty_cashback=CouponMoreLoyaltyCashback(
                    loyalty_cashback=3.14,
                ),
                more_loyalty_points=CouponMoreLoyaltyPoints(
                    loyalty_points=3.14,
                ),
                multiple_amounts_off_items=CouponMultipleAmountsOffItems(
                    discounts=[
                        CouponTierItemDiscount(
                            discount_amount=3.14,
                            items=[
                                "items_example",
                            ],
                        ),
                    ],
                    limit=1,
                ),
                no_discount=CouponNoDiscount(
                    ignore_this_property=True,
                ),
                percent_more_loyalty_cashback=CouponPercentMoreLoyaltyCashback(
                    percent_more_loyalty_cashback=3.14,
                ),
                percent_more_loyalty_points=CouponPercentMoreLoyaltyPoints(
                    percent_more_loyalty_points=3.14,
                ),
                percent_off_item_with_items_quantity_purchase=CouponPercentOffItemWithItemsQuantityPurchase(
                    discount_percent=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    required_purchase_items=[
                        "required_purchase_items_example",
                    ],
                    required_purchase_quantity=1,
                ),
                percent_off_items=CouponPercentOffItems(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                percent_off_items_and_free_shipping=CouponPercentOffItemsAndFreeShipping(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                ),
                percent_off_items_with_items_purchase=CouponPercentOffItemsWithItemsPurchase(
                    discount_percent=3.14,
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    required_purchase_items=[
                        "required_purchase_items_example",
                    ],
                ),
                percent_off_msrp_items=CouponPercentOffMsrpItems(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                    limit=1,
                    minimum_cumulative_msrp=3.14,
                    minimum_subtotal=3.14,
                ),
                percent_off_retail_price_items=CouponPercentOffRetailPriceItems(
                    discount_percent=3.14,
                    excluded_items=[
                        "excluded_items_example",
                    ],
                    items=[
                        "items_example",
                    ],
                    limit=1,
                ),
                percent_off_shipping=CouponPercentOffShipping(
                    discount_percent=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                percent_off_subtotal=CouponPercentOffSubtotal(
                    discount_percent=3.14,
                ),
                percent_off_subtotal_and_free_shipping=CouponPercentOffSubtotalAndFreeShipping(
                    discount_percent=3.14,
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                ),
                percent_off_subtotal_limit=CouponPercentOffSubtotalLimit(
                    currency_code="currency_code_example",
                    discount_percent=3.14,
                    limit=3.14,
                ),
                percent_off_subtotal_with_items_purchase=CouponPercentOffSubtotalWithItemsPurchase(
                    discount_percent=3.14,
                    items=[
                        "items_example",
                    ],
                ),
                percent_off_subtotal_with_subtotal=CouponPercentOffSubtotalWithSubtotal(
                    currency_code="currency_code_example",
                    discount_percent=3.14,
                    subtotal_amount=3.14,
                ),
                quickbooks_code="quickbooks_code_example",
                restrict_by_postal_codes=[
                    "restrict_by_postal_codes_example",
                ],
                restrict_by_screen_branding_theme_codes=[
                    CouponRestriction(
                        invalid_for_this=True,
                        name="name_example",
                        valid_for_this=True,
                        valid_only_for_this=True,
                    ),
                ],
                restrict_by_storefronts=[
                    CouponRestriction(
                        invalid_for_this=True,
                        name="name_example",
                        valid_for_this=True,
                        valid_only_for_this=True,
                    ),
                ],
                skip_on_rebill=True,
                start_dts="start_dts_example",
                super_coupon=True,
                tiered_amount_off_items=CouponTieredAmountOffItems(
                    items=[
                        "items_example",
                    ],
                    limit=3.14,
                    tiers=[
                        CouponTierQuantityAmount(
                            discount_amount=3.14,
                            item_quantity=1,
                            quickbooks_code="quickbooks_code_example",
                        ),
                    ],
                ),
                tiered_amount_off_subtotal=CouponTieredAmountOffSubtotal(
                    items=[
                        "items_example",
                    ],
                    tiers=[
                        CouponTierAmount(
                            discount_amount=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                tiered_percent_off_items=CouponTieredPercentOffItems(
                    items=[
                        "items_example",
                    ],
                    limit=3.14,
                    tiers=[
                        CouponTierQuantityPercent(
                            discount_percent=3.14,
                            item_quantity=1,
                            quickbooks_code="quickbooks_code_example",
                        ),
                    ],
                ),
                tiered_percent_off_shipping=CouponTieredPercentOffShipping(
                    quickbooks_code="quickbooks_code_example",
                    shipping_methods=[
                        "shipping_methods_example",
                    ],
                    tiers=[
                        CouponTierPercent(
                            discount_percent=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                tiered_percent_off_subtotal=CouponTieredPercentOffSubtotal(
                    items=[
                        "items_example",
                    ],
                    tiers=[
                        CouponTierPercent(
                            discount_percent=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                tiered_percent_off_subtotal_based_on_msrp=CouponTieredPercentOffSubtotalBasedOnMSRP(
                    items=[
                        "items_example",
                    ],
                    tiers=[
                        CouponTierPercent(
                            discount_percent=3.14,
                            quickbooks_code="quickbooks_code_example",
                            subtotal_amount=3.14,
                        ),
                    ],
                ),
                usable_by="Anyone",
            ),
        ],
    ) # CouponsRequest | Coupons to update (synchronous maximum 50 / asynchronous maximum 100)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)
    placeholders = True # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)
    _async = True # bool | True if the operation should be run async.  No result returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple coupons
        api_response = api_instance.update_coupons(coupons_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->update_coupons: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple coupons
        api_response = api_instance.update_coupons(coupons_request, expand=expand, placeholders=placeholders, _async=_async)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->update_coupons: %s\n" % e)
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
import time
import ultracart
from ultracart.api import coupon_api
from ultracart.model.upload_coupon_codes_response import UploadCouponCodesResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.upload_coupon_codes_request import UploadCouponCodesRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    coupon_oid = 1 # int | The coupon oid to associate with the provided one-time codes.
    upload_coupon_codes_request = UploadCouponCodesRequest(
        coupon_codes=[
            "coupon_codes_example",
        ],
        error=Error(
            developer_message="developer_message_example",
            error_code="error_code_example",
            more_info="more_info_example",
            object_id="object_id_example",
            user_message="user_message_example",
        ),
        metadata=ResponseMetadata(
            payload_name="payload_name_example",
            result_set=ResultSet(
                count=1,
                limit=1,
                more=True,
                next_offset=1,
                offset=1,
                total_records=1,
            ),
        ),
        success=True,
        warning=Warning(
            more_info="more_info_example",
            warning_message="warning_message_example",
        ),
    ) # UploadCouponCodesRequest | One-time coupon codes

    # example passing only required values which don't have defaults set
    try:
        # Upload one-time codes for a coupon
        api_response = api_instance.upload_coupon_codes(coupon_oid, upload_coupon_codes_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CouponApi->upload_coupon_codes: %s\n" % e)
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

