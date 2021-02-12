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
[**get_coupons_by_query**](CouponApi.md#get_coupons_by_query) | **GET** /coupon/coupons/query | Retrieve coupons by query
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
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon_oid = 56 # int | The coupon_oid to delete.

try:
    # Delete a coupon
    api_instance.delete_coupon(coupon_oid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupons_by_code**
> delete_coupons_by_code(coupon_delete_request)

Deletes multiple coupons

Delete coupons on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon_delete_request = ultracart.CouponDeletesRequest() # CouponDeletesRequest | Coupon oids to delete

try:
    # Deletes multiple coupons
    api_instance.delete_coupons_by_code(coupon_delete_request)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupons_by_oid**
> delete_coupons_by_oid(coupon_delete_request)

Deletes multiple coupons

Delete coupons on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon_delete_request = ultracart.CouponDeletesRequest() # CouponDeletesRequest | Coupon oids to delete

try:
    # Deletes multiple coupons
    api_instance.delete_coupons_by_oid(coupon_delete_request)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **does_coupon_code_exist**
> CouponExistsResponse does_coupon_code_exist(merchant_code)

Determines if a coupon merchant code already exists

Determines if a coupon merchant code already exists. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

merchant_code = 'merchant_code_example' # str | The coupon merchant code to examine.

try:
    # Determines if a coupon merchant code already exists
    api_response = api_instance.does_coupon_code_exist(merchant_code)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_coupon_codes**
> CouponCodesResponse generate_coupon_codes(coupon_oid, coupon_codes_request)

Generates one time codes for a coupon

Generate one time codes for a coupon 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon_oid = 56 # int | The coupon oid to generate codes.
coupon_codes_request = ultracart.CouponCodesRequest() # CouponCodesRequest | Coupon code generation parameters

try:
    # Generates one time codes for a coupon
    api_response = api_instance.generate_coupon_codes(coupon_oid, coupon_codes_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_one_time_codes_by_merchant_code**
> CouponCodesResponse generate_one_time_codes_by_merchant_code(merchant_code, coupon_codes_request)

Generates one time codes by merchant code

Generate one time codes by merchant code 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

merchant_code = 'merchant_code_example' # str | The merchant code to generate one time codes.
coupon_codes_request = ultracart.CouponCodesRequest() # CouponCodesRequest | Coupon code generation parameters

try:
    # Generates one time codes by merchant code
    api_response = api_instance.generate_one_time_codes_by_merchant_code(merchant_code, coupon_codes_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_apply**
> CouponAutoApplyConditions get_auto_apply()

Retrieve auto apply rules and conditions

Retrieve auto apply rules and conditions 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve auto apply rules and conditions
    api_response = api_instance.get_auto_apply()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponApi->get_auto_apply: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CouponAutoApplyConditions**](CouponAutoApplyConditions.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon**
> CouponResponse get_coupon(coupon_oid, expand=expand)

Retrieve a coupon

Retrieves a single coupon using the specified coupon profile oid. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon_oid = 56 # int | The coupon oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve a coupon
    api_response = api_instance.get_coupon(coupon_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_by_merchant_code**
> CouponResponse get_coupon_by_merchant_code(merchant_code, expand=expand)

Retrieve a coupon by merchant code

Retrieves a single coupon using the specified merchant code. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

merchant_code = 'merchant_code_example' # str | The coupon merchant code to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve a coupon by merchant code
    api_response = api_instance.get_coupon_by_merchant_code(merchant_code, expand=expand)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupons**
> CouponsResponse get_coupons(merchant_code=merchant_code, description=description, coupon_type=coupon_type, start_date_begin=start_date_begin, start_date_end=start_date_end, expiration_date_begin=expiration_date_begin, expiration_date_end=expiration_date_end, affiliate_oid=affiliate_oid, exclude_expired=exclude_expired, limit=limit, offset=offset, sort=sort, expand=expand)

Retrieve coupons

Retrieves coupons for this account.  If no parameters are specified, all coupons will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

merchant_code = 'merchant_code_example' # str | Merchant code (optional)
description = 'description_example' # str | Description (optional)
coupon_type = 'coupon_type_example' # str | Coupon type (optional)
start_date_begin = 'start_date_begin_example' # str | Start date begin (optional)
start_date_end = 'start_date_end_example' # str | Start date end (optional)
expiration_date_begin = 'expiration_date_begin_example' # str | Expiration date begin (optional)
expiration_date_end = 'expiration_date_end_example' # str | Expiration date end (optional)
affiliate_oid = 56 # int | Affiliate oid (optional)
exclude_expired = true # bool | Exclude expired (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve coupons
    api_response = api_instance.get_coupons(merchant_code=merchant_code, description=description, coupon_type=coupon_type, start_date_begin=start_date_begin, start_date_end=start_date_end, expiration_date_begin=expiration_date_begin, expiration_date_end=expiration_date_end, affiliate_oid=affiliate_oid, exclude_expired=exclude_expired, limit=limit, offset=offset, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
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
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CouponsResponse**](CouponsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupons_by_query**
> CouponsResponse get_coupons_by_query(coupon_query, limit=limit, offset=offset, sort=sort, expand=expand)

Retrieve coupons by query

Retrieves coupons from the account.  If no parameters are specified, all coupons will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon_query = ultracart.CouponQuery() # CouponQuery | Coupon query
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve coupons by query
    api_response = api_instance.get_coupons_by_query(coupon_query, limit=limit, offset=offset, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponApi->get_coupons_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_query** | [**CouponQuery**](CouponQuery.md)| Coupon query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the coupons.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CouponsResponse**](CouponsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editor_values**
> CouponEditorValues get_editor_values()

Retrieve values needed for a coupon editor

Retrieve values needed for a coupon editor 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve values needed for a coupon editor
    api_response = api_instance.get_editor_values()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponApi->get_editor_values: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CouponEditorValues**](CouponEditorValues.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_coupon**
> CouponResponse insert_coupon(coupon, expand=expand)

Insert a coupon

Insert a coupon on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon = ultracart.Coupon() # Coupon | Coupon to insert
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Insert a coupon
    api_response = api_instance.insert_coupon(coupon, expand=expand)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_coupons**
> CouponsResponse insert_coupons(coupons_request, expand=expand, placeholders=placeholders)

Insert multiple coupons

Insert multiple coupon on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupons_request = ultracart.CouponsRequest() # CouponsRequest | Coupons to insert (maximum 20)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)

try:
    # Insert multiple coupons
    api_response = api_instance.insert_coupons(coupons_request, expand=expand, placeholders=placeholders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponApi->insert_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupons_request** | [**CouponsRequest**](CouponsRequest.md)| Coupons to insert (maximum 20) | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 
 **placeholders** | **bool**| Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. | [optional] 

### Return type

[**CouponsResponse**](CouponsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_items**
> CouponItemSearchResultsResponse search_items(s=s, m=m)

Searches for items to display within a coupon editor and assign to coupons

Searches for items to display within a coupon editor and assign to coupons 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

s = 's_example' # str |  (optional)
m = 56 # int |  (optional)

try:
    # Searches for items to display within a coupon editor and assign to coupons
    api_response = api_instance.search_items(s=s, m=m)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_apply**
> update_auto_apply(conditions)

Update auto apply rules and conditions

Update auto apply rules and conditions 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

conditions = ultracart.CouponAutoApplyConditions() # CouponAutoApplyConditions | Conditions

try:
    # Update auto apply rules and conditions
    api_instance.update_auto_apply(conditions)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon**
> CouponResponse update_coupon(coupon, coupon_oid, expand=expand)

Update a coupon

Update a coupon on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon = ultracart.Coupon() # Coupon | Coupon to update
coupon_oid = 56 # int | The coupon_oid to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Update a coupon
    api_response = api_instance.update_coupon(coupon, coupon_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponApi->update_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon** | [**Coupon**](Coupon.md)| Coupon to update | 
 **coupon_oid** | **int**| The coupon_oid to update. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CouponResponse**](CouponResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupons**
> CouponsResponse update_coupons(coupons_request, expand=expand, placeholders=placeholders, _async=_async)

Update multiple coupons

Update multiple coupon on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupons_request = ultracart.CouponsRequest() # CouponsRequest | Coupons to update (synchronous maximum 50 / asynchronous maximum 100)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)
placeholders = true # bool | Whether or not placeholder values should be returned in the result.  Useful for UIs that consume this REST API. (optional)
_async = true # bool | True if the operation should be run async.  No result returned (optional)

try:
    # Update multiple coupons
    api_response = api_instance.update_coupons(coupons_request, expand=expand, placeholders=placeholders, _async=_async)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_coupon_codes**
> UploadCouponCodesResponse upload_coupon_codes(coupon_oid, upload_coupon_codes_request)

Upload one-time codes for a coupon

Upload one-time codes for a coupon 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.CouponApi.fromApiKey(simple_key, False, True)

coupon_oid = 56 # int | The coupon oid to associate with the provided one-time codes.
upload_coupon_codes_request = ultracart.UploadCouponCodesRequest() # UploadCouponCodesRequest | One-time coupon codes

try:
    # Upload one-time codes for a coupon
    api_response = api_instance.upload_coupon_codes(coupon_oid, upload_coupon_codes_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

