# ultracart.CouponApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_coupon**](CouponApi.md#delete_coupon) | **DELETE** /coupon/coupons/{coupon_oid} | Delete a coupon
[**generate_coupon_codes**](CouponApi.md#generate_coupon_codes) | **POST** /coupon/coupons/{coupon_oid}/generate_codes | Generates one time codes for a coupon
[**generate_one_time_codes_by_merchant_code**](CouponApi.md#generate_one_time_codes_by_merchant_code) | **POST** /coupon/coupons/merchant_code/{merchant_code}/generate_codes | Generates one time codes by merchant code
[**get_coupon**](CouponApi.md#get_coupon) | **GET** /coupon/coupons/{coupon_oid} | Retrieve a coupon
[**get_coupon_by_merchant_code**](CouponApi.md#get_coupon_by_merchant_code) | **GET** /coupon/coupons/merchant_code/{merchant_code} | Retrieve a coupon by merchant code
[**get_coupons**](CouponApi.md#get_coupons) | **GET** /coupon/coupons | Retrieve coupons
[**get_coupons_by_query**](CouponApi.md#get_coupons_by_query) | **GET** /coupon/coupons/query | Retrieve coupons by query
[**get_editor_values**](CouponApi.md#get_editor_values) | **GET** /coupon/editor_values | Retrieve values needed for a coupon editor
[**insert_coupon**](CouponApi.md#insert_coupon) | **POST** /coupon/coupons | Insert a coupon
[**update_coupon**](CouponApi.md#update_coupon) | **PUT** /coupon/coupons/{coupon_oid} | Update a coupon


# **delete_coupon**
> CouponResponse delete_coupon(coupon_oid)

Delete a coupon

Delete a coupon on the UltraCart account. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
coupon_oid = 56 # int | The coupon_oid to delete.

try: 
    # Delete a coupon
    api_response = api_instance.delete_coupon(coupon_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponApi->delete_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_oid** | **int**| The coupon_oid to delete. | 

### Return type

[**CouponResponse**](CouponResponse.md)

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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))

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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.CouponApi(ultracart.ApiClient(configuration))
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

