# ultracart.CustomerApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_store_credit**](CustomerApi.md#add_customer_store_credit) | **POST** /customer/customers/{customer_profile_oid}/store_credit | Adds store credit to a customer
[**adjust_internal_certificate**](CustomerApi.md#adjust_internal_certificate) | **POST** /customer/customers/{customer_profile_oid}/adjust_cashback_balance | Updates the cashback balance for a customer by updating the internal gift certificate used, creating the gift certificate if needed.
[**delete_customer**](CustomerApi.md#delete_customer) | **DELETE** /customer/customers/{customer_profile_oid} | Delete a customer
[**delete_wish_list_item**](CustomerApi.md#delete_wish_list_item) | **DELETE** /customer/customers/{customer_profile_oid}/wishlist/{customer_wishlist_item_oid} | Delete a customer wishlist item
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customer/customers/{customer_profile_oid} | Retrieve a customer
[**get_customer_by_email**](CustomerApi.md#get_customer_by_email) | **GET** /customer/customers/by_email/{email} | Retrieve a customer by Email
[**get_customer_editor_values**](CustomerApi.md#get_customer_editor_values) | **GET** /customer/editor_values | Retrieve values needed for a customer profile editor
[**get_customer_email_lists**](CustomerApi.md#get_customer_email_lists) | **GET** /customer/email_lists | Retrieve all email lists across all storefronts
[**get_customer_store_credit**](CustomerApi.md#get_customer_store_credit) | **GET** /customer/customers/{customer_profile_oid}/store_credit | Retrieve the customer store credit accumulated through loyalty programs
[**get_customer_wish_list**](CustomerApi.md#get_customer_wish_list) | **GET** /customer/customers/{customer_profile_oid}/wishlist | Retrieve wishlist items for customer
[**get_customer_wish_list_item**](CustomerApi.md#get_customer_wish_list_item) | **GET** /customer/customers/{customer_profile_oid}/wishlist/{customer_wishlist_item_oid} | Retrieve wishlist item for customer
[**get_customers**](CustomerApi.md#get_customers) | **GET** /customer/customers | Retrieve customers
[**get_customers_by_query**](CustomerApi.md#get_customers_by_query) | **POST** /customer/customers/query | Retrieve customers by query
[**get_customers_for_data_tables**](CustomerApi.md#get_customers_for_data_tables) | **POST** /customer/customers/dataTables | Retrieve customers for DataTables plugin
[**get_email_verification_token**](CustomerApi.md#get_email_verification_token) | **POST** /customer/customers/email_verify/get_token | Create a token that can be used to verify a customer email address
[**get_magic_link**](CustomerApi.md#get_magic_link) | **PUT** /customer/customers/{customer_profile_oid}/magic_link/{storefront_host_name} | getMagicLink
[**insert_customer**](CustomerApi.md#insert_customer) | **POST** /customer/customers | Insert a customer
[**insert_wish_list_item**](CustomerApi.md#insert_wish_list_item) | **POST** /customer/customers/{customer_profile_oid}/wishlist | Insert a customer wishlist item
[**merge_customer**](CustomerApi.md#merge_customer) | **PUT** /customer/customers/{customer_profile_oid}/merge | Merge customer into this customer
[**search_customer_profile_values**](CustomerApi.md#search_customer_profile_values) | **POST** /customer/search | Searches for all matching values (using POST)
[**update_customer**](CustomerApi.md#update_customer) | **PUT** /customer/customers/{customer_profile_oid} | Update a customer
[**update_customer_email_lists**](CustomerApi.md#update_customer_email_lists) | **POST** /customer/customers/{customer_profile_oid}/email_lists | Update email list subscriptions for a customer
[**update_wish_list_item**](CustomerApi.md#update_wish_list_item) | **PUT** /customer/customers/{customer_profile_oid}/wishlist/{customer_wishlist_item_oid} | Update a customer wishlist item
[**validate_email_verification_token**](CustomerApi.md#validate_email_verification_token) | **POST** /customer/customers/email_verify/validate_token | Validate a token that can be used to verify a customer email address


# **add_customer_store_credit**
> BaseResponse add_customer_store_credit(customer_profile_oid, store_credit_request)

Adds store credit to a customer

Adds store credit to a customer 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customer_store_credit_add_request import CustomerStoreCreditAddRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid to credit.
    store_credit_request = CustomerStoreCreditAddRequest(
        amount=3.14,
        description="description_example",
        expiration_days=1,
        vesting_days=1,
    ) # CustomerStoreCreditAddRequest | Store credit to add

    # example passing only required values which don't have defaults set
    try:
        # Adds store credit to a customer
        api_response = api_instance.add_customer_store_credit(customer_profile_oid, store_credit_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->add_customer_store_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid to credit. |
 **store_credit_request** | [**CustomerStoreCreditAddRequest**](CustomerStoreCreditAddRequest.md)| Store credit to add |

### Return type

[**BaseResponse**](BaseResponse.md)

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

# **adjust_internal_certificate**
> AdjustInternalCertificateResponse adjust_internal_certificate(customer_profile_oid, adjust_internal_certificate_request)

Updates the cashback balance for a customer by updating the internal gift certificate used, creating the gift certificate if needed.

Updates the cashback balance for a customer by updating the internal gift certificate used, creating the gift certificate if needed. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.adjust_internal_certificate_request import AdjustInternalCertificateRequest
from ultracart.model.adjust_internal_certificate_response import AdjustInternalCertificateResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer profile oid
    adjust_internal_certificate_request = AdjustInternalCertificateRequest(
        adjustment_amount=3.14,
        description="description_example",
        entry_dts="entry_dts_example",
        expiration_days=1,
        order_id="order_id_example",
        vesting_days=1,
    ) # AdjustInternalCertificateRequest | adjustInternalCertificateRequest

    # example passing only required values which don't have defaults set
    try:
        # Updates the cashback balance for a customer by updating the internal gift certificate used, creating the gift certificate if needed.
        api_response = api_instance.adjust_internal_certificate(customer_profile_oid, adjust_internal_certificate_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->adjust_internal_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer profile oid |
 **adjust_internal_certificate_request** | [**AdjustInternalCertificateRequest**](AdjustInternalCertificateRequest.md)| adjustInternalCertificateRequest |

### Return type

[**AdjustInternalCertificateResponse**](AdjustInternalCertificateResponse.md)

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

# **delete_customer**
> delete_customer(customer_profile_oid)

Delete a customer

Delete a customer on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer_profile_oid to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a customer
        api_instance.delete_customer(customer_profile_oid)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->delete_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid to delete. |

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

# **delete_wish_list_item**
> CustomerWishListItem delete_wish_list_item(customer_profile_oid, customer_wishlist_item_oid)

Delete a customer wishlist item

Delete a customer wishlist item 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_wish_list_item import CustomerWishListItem
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid for this wishlist.
    customer_wishlist_item_oid = 1 # int | The wishlist oid for this wishlist item to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a customer wishlist item
        api_response = api_instance.delete_wish_list_item(customer_profile_oid, customer_wishlist_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->delete_wish_list_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **customer_wishlist_item_oid** | **int**| The wishlist oid for this wishlist item to delete. |

### Return type

[**CustomerWishListItem**](CustomerWishListItem.md)

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

# **get_customer**
> CustomerResponse get_customer(customer_profile_oid)

Retrieve a customer

Retrieves a single customer using the specified customer profile oid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_response import CustomerResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid to retrieve.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a customer
        api_response = api_instance.get_customer(customer_profile_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a customer
        api_response = api_instance.get_customer(customer_profile_oid, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **get_customer_by_email**
> CustomerResponse get_customer_by_email(email)

Retrieve a customer by Email

Retrieves a single customer using the specified customer email address. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_response import CustomerResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    email = "email_example" # str | The email address of the customer to retrieve.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a customer by Email
        api_response = api_instance.get_customer_by_email(email)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer_by_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a customer by Email
        api_response = api_instance.get_customer_by_email(email, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the customer to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **get_customer_editor_values**
> CustomerEditorValues get_customer_editor_values()

Retrieve values needed for a customer profile editor

Retrieve values needed for a customer profile editor. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_editor_values import CustomerEditorValues
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve values needed for a customer profile editor
        api_response = api_instance.get_customer_editor_values()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer_editor_values: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerEditorValues**](CustomerEditorValues.md)

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

# **get_customer_email_lists**
> EmailListsResponse get_customer_email_lists()

Retrieve all email lists across all storefronts

Retrieve all email lists across all storefronts 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_lists_response import EmailListsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve all email lists across all storefronts
        api_response = api_instance.get_customer_email_lists()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer_email_lists: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailListsResponse**](EmailListsResponse.md)

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

# **get_customer_store_credit**
> CustomerStoreCreditResponse get_customer_store_credit(customer_profile_oid)

Retrieve the customer store credit accumulated through loyalty programs

Retrieve the customer store credit accumulated through loyalty programs 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customer_store_credit_response import CustomerStoreCreditResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the customer store credit accumulated through loyalty programs
        api_response = api_instance.get_customer_store_credit(customer_profile_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer_store_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid to retrieve. |

### Return type

[**CustomerStoreCreditResponse**](CustomerStoreCreditResponse.md)

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

# **get_customer_wish_list**
> CustomerWishListItemsResponse get_customer_wish_list(customer_profile_oid)

Retrieve wishlist items for customer

Retrieve wishlist items for customer. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customer_wish_list_items_response import CustomerWishListItemsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid for this wishlist.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve wishlist items for customer
        api_response = api_instance.get_customer_wish_list(customer_profile_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer_wish_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |

### Return type

[**CustomerWishListItemsResponse**](CustomerWishListItemsResponse.md)

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

# **get_customer_wish_list_item**
> CustomerWishListItemResponse get_customer_wish_list_item(customer_profile_oid, customer_wishlist_item_oid)

Retrieve wishlist item for customer

Retrieve wishlist item for customer. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_wish_list_item_response import CustomerWishListItemResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid for this wishlist.
    customer_wishlist_item_oid = 1 # int | The wishlist oid for this wishlist item.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve wishlist item for customer
        api_response = api_instance.get_customer_wish_list_item(customer_profile_oid, customer_wishlist_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customer_wish_list_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **customer_wishlist_item_oid** | **int**| The wishlist oid for this wishlist item. |

### Return type

[**CustomerWishListItemResponse**](CustomerWishListItemResponse.md)

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

# **get_customers**
> CustomersResponse get_customers()

Retrieve customers

Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customers_response import CustomersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    email = "email_example" # str | Email (optional)
    qb_class = "qb_class_example" # str | Quickbooks class (optional)
    quickbooks_code = "quickbooks_code_example" # str | Quickbooks code (optional)
    last_modified_dts_start = "last_modified_dts_start_example" # str | Last modified date start (optional)
    last_modified_dts_end = "last_modified_dts_end_example" # str | Last modified date end (optional)
    signup_dts_start = "signup_dts_start_example" # str | Signup date start (optional)
    signup_dts_end = "signup_dts_end_example" # str | Signup date end (optional)
    billing_first_name = "billing_first_name_example" # str | Billing first name (optional)
    billing_last_name = "billing_last_name_example" # str | Billing last name (optional)
    billing_company = "billing_company_example" # str | Billing company (optional)
    billing_city = "billing_city_example" # str | Billing city (optional)
    billing_state = "billing_state_example" # str | Billing state (optional)
    billing_postal_code = "billing_postal_code_example" # str | Billing postal code (optional)
    billing_country_code = "billing_country_code_example" # str | Billing country code (optional)
    billing_day_phone = "billing_day_phone_example" # str | Billing day phone (optional)
    billing_evening_phone = "billing_evening_phone_example" # str | Billing evening phone (optional)
    shipping_first_name = "shipping_first_name_example" # str | Shipping first name (optional)
    shipping_last_name = "shipping_last_name_example" # str | Shipping last name (optional)
    shipping_company = "shipping_company_example" # str | Shipping company (optional)
    shipping_city = "shipping_city_example" # str | Shipping city (optional)
    shipping_state = "shipping_state_example" # str | Shipping state (optional)
    shipping_postal_code = "shipping_postal_code_example" # str | Shipping postal code (optional)
    shipping_country_code = "shipping_country_code_example" # str | Shipping country code (optional)
    shipping_day_phone = "shipping_day_phone_example" # str | Shipping day phone (optional)
    shipping_evening_phone = "shipping_evening_phone_example" # str | Shipping evening phone (optional)
    pricing_tier_oid = 1 # int | Pricing tier oid (optional)
    pricing_tier_name = "pricing_tier_name_example" # str | Pricing tier name (optional)
    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    since = "_since_example" # str | Fetch customers that have been created/modified since this date/time. (optional)
    sort = "_sort_example" # str | The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve customers
        api_response = api_instance.get_customers(email=email, qb_class=qb_class, quickbooks_code=quickbooks_code, last_modified_dts_start=last_modified_dts_start, last_modified_dts_end=last_modified_dts_end, signup_dts_start=signup_dts_start, signup_dts_end=signup_dts_end, billing_first_name=billing_first_name, billing_last_name=billing_last_name, billing_company=billing_company, billing_city=billing_city, billing_state=billing_state, billing_postal_code=billing_postal_code, billing_country_code=billing_country_code, billing_day_phone=billing_day_phone, billing_evening_phone=billing_evening_phone, shipping_first_name=shipping_first_name, shipping_last_name=shipping_last_name, shipping_company=shipping_company, shipping_city=shipping_city, shipping_state=shipping_state, shipping_postal_code=shipping_postal_code, shipping_country_code=shipping_country_code, shipping_day_phone=shipping_day_phone, shipping_evening_phone=shipping_evening_phone, pricing_tier_oid=pricing_tier_oid, pricing_tier_name=pricing_tier_name, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email | [optional]
 **qb_class** | **str**| Quickbooks class | [optional]
 **quickbooks_code** | **str**| Quickbooks code | [optional]
 **last_modified_dts_start** | **str**| Last modified date start | [optional]
 **last_modified_dts_end** | **str**| Last modified date end | [optional]
 **signup_dts_start** | **str**| Signup date start | [optional]
 **signup_dts_end** | **str**| Signup date end | [optional]
 **billing_first_name** | **str**| Billing first name | [optional]
 **billing_last_name** | **str**| Billing last name | [optional]
 **billing_company** | **str**| Billing company | [optional]
 **billing_city** | **str**| Billing city | [optional]
 **billing_state** | **str**| Billing state | [optional]
 **billing_postal_code** | **str**| Billing postal code | [optional]
 **billing_country_code** | **str**| Billing country code | [optional]
 **billing_day_phone** | **str**| Billing day phone | [optional]
 **billing_evening_phone** | **str**| Billing evening phone | [optional]
 **shipping_first_name** | **str**| Shipping first name | [optional]
 **shipping_last_name** | **str**| Shipping last name | [optional]
 **shipping_company** | **str**| Shipping company | [optional]
 **shipping_city** | **str**| Shipping city | [optional]
 **shipping_state** | **str**| Shipping state | [optional]
 **shipping_postal_code** | **str**| Shipping postal code | [optional]
 **shipping_country_code** | **str**| Shipping country code | [optional]
 **shipping_day_phone** | **str**| Shipping day phone | [optional]
 **shipping_evening_phone** | **str**| Shipping evening phone | [optional]
 **pricing_tier_oid** | **int**| Pricing tier oid | [optional]
 **pricing_tier_name** | **str**| Pricing tier name | [optional]
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomersResponse**](CustomersResponse.md)

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

# **get_customers_by_query**
> CustomersResponse get_customers_by_query(customer_query)

Retrieve customers by query

Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customers_response import CustomersResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_query import CustomerQuery
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_query = CustomerQuery(
        all_tags=[
            "all_tags_example",
        ],
        any_tags=[
            "any_tags_example",
        ],
        billing_city="billing_city_example",
        billing_company="billing_company_example",
        billing_country_code="billing_country_code_example",
        billing_day_phone="billing_day_phone_example",
        billing_evening_phone="billing_evening_phone_example",
        billing_first_name="billing_first_name_example",
        billing_last_name="billing_last_name_example",
        billing_postal_code="billing_postal_code_example",
        billing_state="billing_state_example",
        email="email_example",
        last_modified_dts_end="last_modified_dts_end_example",
        last_modified_dts_start="last_modified_dts_start_example",
        pricing_tier_name="pricing_tier_name_example",
        pricing_tier_oid=1,
        qb_class="qb_class_example",
        quickbooks_code="quickbooks_code_example",
        shipping_city="shipping_city_example",
        shipping_company="shipping_company_example",
        shipping_country_code="shipping_country_code_example",
        shipping_day_phone="shipping_day_phone_example",
        shipping_evening_phone="shipping_evening_phone_example",
        shipping_first_name="shipping_first_name_example",
        shipping_last_name="shipping_last_name_example",
        shipping_postal_code="shipping_postal_code_example",
        shipping_state="shipping_state_example",
        signup_dts_end="signup_dts_end_example",
        signup_dts_start="signup_dts_start_example",
    ) # CustomerQuery | Customer query
    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    since = "_since_example" # str | Fetch customers that have been created/modified since this date/time. (optional)
    sort = "_sort_example" # str | The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve customers by query
        api_response = api_instance.get_customers_by_query(customer_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customers_by_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve customers by query
        api_response = api_instance.get_customers_by_query(customer_query, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customers_by_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_query** | [**CustomerQuery**](CustomerQuery.md)| Customer query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomersResponse**](CustomersResponse.md)

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

# **get_customers_for_data_tables**
> DataTablesServerSideResponse get_customers_for_data_tables()

Retrieve customers for DataTables plugin

Retrieves customers from the account.  If no searches are specified, all customers will be returned. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.data_tables_server_side_response import DataTablesServerSideResponse
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
        # Retrieve customers for DataTables plugin
        api_response = api_instance.get_customers_for_data_tables(expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_customers_for_data_tables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**DataTablesServerSideResponse**](DataTablesServerSideResponse.md)

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

# **get_email_verification_token**
> EmailVerifyTokenResponse get_email_verification_token(token_request)

Create a token that can be used to verify a customer email address

Create a token that can be used to verify a customer email address.  The implementation of how a customer interacts with this token is left to the merchant. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.email_verify_token_request import EmailVerifyTokenRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_verify_token_response import EmailVerifyTokenResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    token_request = EmailVerifyTokenRequest(
        email="email_example",
        password="password_example",
    ) # EmailVerifyTokenRequest | Token request

    # example passing only required values which don't have defaults set
    try:
        # Create a token that can be used to verify a customer email address
        api_response = api_instance.get_email_verification_token(token_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_email_verification_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**EmailVerifyTokenRequest**](EmailVerifyTokenRequest.md)| Token request |

### Return type

[**EmailVerifyTokenResponse**](EmailVerifyTokenResponse.md)

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

# **get_magic_link**
> CustomerMagicLinkResponse get_magic_link(customer_profile_oid, storefront_host_name)

getMagicLink

Retrieves a magic link to allow a merchant to login as a customer.  This method is a PUT call intentionally. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customer_magic_link_response import CustomerMagicLinkResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer_profile_oid of the customer.
    storefront_host_name = "storefront_host_name_example" # str | The storefront to log into.

    # example passing only required values which don't have defaults set
    try:
        # getMagicLink
        api_response = api_instance.get_magic_link(customer_profile_oid, storefront_host_name)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->get_magic_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid of the customer. |
 **storefront_host_name** | **str**| The storefront to log into. |

### Return type

[**CustomerMagicLinkResponse**](CustomerMagicLinkResponse.md)

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

# **insert_customer**
> CustomerResponse insert_customer(customer)

Insert a customer

Insert a customer on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer import Customer
from ultracart.model.customer_response import CustomerResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer = Customer(
        activity=CustomerActivity(
            activities=[
                Activity(
                    action="action_example",
                    channel="channel_example",
                    metric="metric_example",
                    storefront_oid=1,
                    subject="subject_example",
                    ts=1,
                    type="type_example",
                    uuid="uuid_example",
                ),
            ],
            global_unsubscribed=True,
            global_unsubscribed_dts="global_unsubscribed_dts_example",
            memberships=[
                ListSegmentMembership(
                    name="name_example",
                    type="type_example",
                    uuid="uuid_example",
                ),
            ],
            metrics=[
                Metric(
                    all_time=3.14,
                    all_time_formatted="all_time_formatted_example",
                    last_30=3.14,
                    last_30_formatted="last_30_formatted_example",
                    name="name_example",
                    prior_30=3.14,
                    prior_30_formatted="prior_30_formatted_example",
                    type="type_example",
                ),
            ],
            properties_list=[
                ModelProperty(
                    name="name_example",
                    value="value_example",
                ),
            ],
            spam_complaint=True,
            spam_complaint_dts="spam_complaint_dts_example",
        ),
        affiliate_oid=1,
        allow_3rd_party_billing=True,
        allow_cod=True,
        allow_drop_shipping=True,
        allow_purchase_order=True,
        allow_quote_request=True,
        allow_selection_of_address_type=True,
        attachments=[
            CustomerAttachment(
                customer_profile_attachment_oid=1,
                description="description_example",
                file_name="file_name_example",
                mime_type="mime_type_example",
                upload_dts="upload_dts_example",
            ),
        ],
        auto_approve_cod=True,
        auto_approve_purchase_order=True,
        automatic_merchant_notes="automatic_merchant_notes_example",
        billing=[
            CustomerBilling(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                customer_billing_oid=1,
                customer_profile_oid=1,
                day_phone="day_phone_example",
                default_billing=True,
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                last_used_dts="last_used_dts_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                tax_county="tax_county_example",
                title="title_example",
            ),
        ],
        business_notes="business_notes_example",
        cards=[
            CustomerCard(
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_type="card_type_example",
                customer_profile_credit_card_id=1,
                customer_profile_oid=1,
                last_used_dts="last_used_dts_example",
            ),
        ],
        cc_emails=[
            CustomerEmail(
                customer_profile_email_oid=1,
                email="email_example",
                label="label_example",
                receipt_notification=True,
                refund_notification=True,
                shipment_notification=True,
            ),
        ],
        customer_profile_oid=1,
        dhl_account_number="dhl_account_number_example",
        dhl_duty_account_number="dhl_duty_account_number_example",
        do_not_send_mail=True,
        edi=CustomerEDI(
            channel_partner_oid=1,
            distribution_center_number="distribution_center_number_example",
            store_number="store_number_example",
        ),
        email="email_example",
        exempt_shipping_handling_charge=True,
        fedex_account_number="fedex_account_number_example",
        free_shipping=True,
        free_shipping_minimum=3.14,
        last_modified_by="last_modified_by_example",
        last_modified_dts="last_modified_dts_example",
        loyalty=CustomerLoyalty(
            current_points=1,
            internal_gift_certificate=GiftCertificate(
                activated=True,
                code="code_example",
                customer_profile_oid=1,
                deleted=True,
                email="email_example",
                expiration_dts="expiration_dts_example",
                gift_certificate_oid=1,
                internal=True,
                ledger_entries=[
                    GiftCertificateLedgerEntry(
                        amount=3.14,
                        description="description_example",
                        entry_dts="entry_dts_example",
                        gift_certificate_ledger_oid=1,
                        gift_certificate_oid=1,
                        reference_order_id="reference_order_id_example",
                    ),
                ],
                merchant_id="merchant_id_example",
                merchant_note="merchant_note_example",
                original_balance=3.14,
                reference_order_id="reference_order_id_example",
                remaining_balance=3.14,
            ),
            internal_gift_certificate_balance="internal_gift_certificate_balance_example",
            internal_gift_certificate_oid=1,
            ledger_entries=[
                CustomerLoyaltyLedger(
                    created_by="created_by_example",
                    created_dts="created_dts_example",
                    description="description_example",
                    email="email_example",
                    item_id="item_id_example",
                    item_index=1,
                    ledger_dts="ledger_dts_example",
                    loyalty_campaign_oid=1,
                    loyalty_ledger_oid=1,
                    loyalty_points=1,
                    modified_by="modified_by_example",
                    modified_dts="modified_dts_example",
                    order_id="order_id_example",
                    quantity=1,
                    vesting_dts="vesting_dts_example",
                ),
            ],
            pending_points=1,
            redemptions=[
                CustomerLoyaltyRedemption(
                    coupon_code="coupon_code_example",
                    coupon_code_oid=1,
                    coupon_used=True,
                    description_for_customer="description_for_customer_example",
                    expiration_dts="expiration_dts_example",
                    gift_certificate_code="gift_certificate_code_example",
                    gift_certificate_oid=1,
                    loyalty_ledger_oid=1,
                    loyalty_points=1,
                    loyalty_redemption_oid=1,
                    order_id="order_id_example",
                    redemption_dts="redemption_dts_example",
                    remaining_balance=3.14,
                ),
            ],
        ),
        maximum_item_count=1,
        merchant_id="merchant_id_example",
        minimum_item_count=1,
        minimum_subtotal=3.14,
        no_coupons=True,
        no_free_shipping=True,
        no_realtime_charge=True,
        orders=[
            Order(
                affiliates=[
                    OrderAffiliate(
                        affiliate_oid=1,
                        ledger_entries=[
                            OrderAffiliateLedger(
                                assigned_by_user="assigned_by_user_example",
                                item_id="item_id_example",
                                tier_number=1,
                                transaction_amount=3.14,
                                transaction_amount_paid=3.14,
                                transaction_dts="transaction_dts_example",
                                transaction_memo="transaction_memo_example",
                                transaction_percentage=3.14,
                                transaction_state="Pending",
                            ),
                        ],
                        sub_id="sub_id_example",
                    ),
                ],
                auto_order=OrderAutoOrder(
                    auto_order_code="auto_order_code_example",
                    auto_order_oid=1,
                    cancel_after_next_x_orders=1,
                    cancel_downgrade=True,
                    cancel_reason="cancel_reason_example",
                    cancel_upgrade=True,
                    canceled_by_user="canceled_by_user_example",
                    canceled_dts="canceled_dts_example",
                    completed=True,
                    credit_card_attempt=1,
                    disabled_dts="disabled_dts_example",
                    enabled=True,
                    failure_reason="failure_reason_example",
                    items=[
                        AutoOrderItem(
                            arbitrary_item_id="arbitrary_item_id_example",
                            arbitrary_percentage_discount=3.14,
                            arbitrary_quantity=3.14,
                            arbitrary_schedule_days=1,
                            arbitrary_unit_cost=3.14,
                            arbitrary_unit_cost_remaining_orders=1,
                            auto_order_item_oid=1,
                            calculated_next_shipment_dts="calculated_next_shipment_dts_example",
                            first_order_dts="first_order_dts_example",
                            frequency="Weekly",
                            future_schedules=[
                                AutoOrderItemFutureSchedule(
                                    item_id="item_id_example",
                                    rebill_count=1,
                                    shipment_dts="shipment_dts_example",
                                    unit_cost=3.14,
                                ),
                            ],
                            last_order_dts="last_order_dts_example",
                            life_time_value=3.14,
                            next_item_id="next_item_id_example",
                            next_preshipment_notice_dts="next_preshipment_notice_dts_example",
                            next_shipment_dts="next_shipment_dts_example",
                            no_order_after_dts="no_order_after_dts_example",
                            number_of_rebills=1,
                            options=[
                                AutoOrderItemOption(
                                    label="label_example",
                                    value="value_example",
                                ),
                            ],
                            original_item_id="original_item_id_example",
                            original_quantity=3.14,
                            paused=True,
                            paypal_payer_id="paypal_payer_id_example",
                            paypal_recurring_payment_profile_id="paypal_recurring_payment_profile_id_example",
                            preshipment_notice_sent=True,
                            rebill_value=3.14,
                            remaining_repeat_count=1,
                            simple_schedule=AutoOrderItemSimpleSchedule(
                                frequency="Weekly",
                                item_id="item_id_example",
                                repeat_count=1,
                            ),
                        ),
                    ],
                    next_attempt="next_attempt_example",
                    original_order_id="original_order_id_example",
                    override_affiliate_id=1,
                    rebill_orders=[
                        Order(),
                    ],
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    status="active",
                ),
                billing=OrderBilling(
                    address1="address1_example",
                    address2="address2_example",
                    cc_emails=[
                        "cc_emails_example",
                    ],
                    cell_phone="cell_phone_example",
                    cell_phone_e164="cell_phone_e164_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    email="email_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    title="title_example",
                ),
                buysafe=OrderBuysafe(
                    buysafe_bond_available=True,
                    buysafe_bond_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_free=True,
                    buysafe_bond_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_wanted=True,
                    buysafe_shopping_cart_id="buysafe_shopping_cart_id_example",
                ),
                channel_partner=OrderChannelPartner(
                    auto_approve_purchase_order=True,
                    channel_partner_code="channel_partner_code_example",
                    channel_partner_data="channel_partner_data_example",
                    channel_partner_oid=1,
                    channel_partner_order_id="channel_partner_order_id_example",
                    ignore_invalid_shipping_method=True,
                    no_realtime_payment_processing=True,
                    skip_payment_processing=True,
                    store_completed=True,
                    store_if_payment_declines=True,
                    treat_warnings_as_errors=True,
                ),
                checkout=OrderCheckout(
                    browser=Browser(
                        device=BrowserDevice(
                            family="family_example",
                        ),
                        os=BrowserOS(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                            patch_minor="patch_minor_example",
                        ),
                        user_agent=BrowserUserAgent(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                        ),
                    ),
                    comments="comments_example",
                    custom_field1="custom_field1_example",
                    custom_field10="custom_field10_example",
                    custom_field2="custom_field2_example",
                    custom_field3="custom_field3_example",
                    custom_field4="custom_field4_example",
                    custom_field5="custom_field5_example",
                    custom_field6="custom_field6_example",
                    custom_field7="custom_field7_example",
                    custom_field8="custom_field8_example",
                    custom_field9="custom_field9_example",
                    customer_ip_address="customer_ip_address_example",
                    screen_branding_theme_code="screen_branding_theme_code_example",
                    screen_size="screen_size_example",
                    storefront_host_name="storefront_host_name_example",
                    upsell_path_code="upsell_path_code_example",
                ),
                coupons=[
                    OrderCoupon(
                        accounting_code="accounting_code_example",
                        automatically_applied=True,
                        base_coupon_code="base_coupon_code_example",
                        coupon_code="coupon_code_example",
                        hdie_from_customer=True,
                    ),
                ],
                creation_dts="creation_dts_example",
                currency_code="currency_code_example",
                current_stage="Accounts Receivable",
                customer_profile=Customer(),
                digital_order=OrderDigitalOrder(
                    creation_dts="creation_dts_example",
                    expiration_dts="expiration_dts_example",
                    items=[
                        OrderDigitalItem(
                            file_size=1,
                            last_download="last_download_example",
                            last_download_ip_address="last_download_ip_address_example",
                            original_filename="original_filename_example",
                            product_code="product_code_example",
                            product_description="product_description_example",
                            remaining_downloads=1,
                            url="url_example",
                        ),
                    ],
                    url="url_example",
                    url_id="url_id_example",
                ),
                edi=OrderEdi(
                    bill_to_edi_code="bill_to_edi_code_example",
                    edi_department="edi_department_example",
                    edi_internal_vendor_number="edi_internal_vendor_number_example",
                    ship_to_edi_code="ship_to_edi_code_example",
                ),
                exchange_rate=3.14,
                fraud_score=OrderFraudScore(
                    anonymous_proxy=True,
                    bin_match="NA",
                    carder_email=True,
                    country_code="country_code_example",
                    country_match=True,
                    customer_phone_in_billing_location="customer_phone_in_billing_location_example",
                    distance_km=1,
                    free_email=True,
                    high_risk_country=True,
                    ip_city="ip_city_example",
                    ip_isp="ip_isp_example",
                    ip_latitude="ip_latitude_example",
                    ip_longitude="ip_longitude_example",
                    ip_org="ip_org_example",
                    ip_region="ip_region_example",
                    proxy_score=3.14,
                    score=3.14,
                    ship_forwarder=True,
                    spam_score=3.14,
                    transparent_proxy=True,
                ),
                gift=OrderGift(
                    gift=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_charge_accounting_code="gift_charge_accounting_code_example",
                    gift_charge_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_email="gift_email_example",
                    gift_message="gift_message_example",
                    gift_wrap_accounting_code="gift_wrap_accounting_code_example",
                    gift_wrap_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_title="gift_wrap_title_example",
                ),
                gift_certificate=OrderGiftCertificate(
                    gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_certificate_code="gift_certificate_code_example",
                    gift_certificate_oid=1,
                ),
                internal=OrderInternal(
                    exported_to_accounting=True,
                    merchant_notes="merchant_notes_example",
                    placed_by_user="placed_by_user_example",
                    refund_by_user="refund_by_user_example",
                    sales_rep_code="sales_rep_code_example",
                    transactional_merchant_notes=[
                        OrderTransactionalMerchantNote(
                            ip_address="ip_address_example",
                            note="note_example",
                            note_dts="note_dts_example",
                            user="user_example",
                        ),
                    ],
                ),
                items=[
                    OrderItem(
                        accounting_code="accounting_code_example",
                        activation_codes=[
                            "activation_codes_example",
                        ],
                        arbitrary_unit_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                        auto_order_schedule="auto_order_schedule_example",
                        barcode="barcode_example",
                        barcode_gtin12="barcode_gtin12_example",
                        barcode_gtin14="barcode_gtin14_example",
                        barcode_upc11="barcode_upc11_example",
                        barcode_upc12="barcode_upc12_example",
                        channel_partner_item_id="channel_partner_item_id_example",
                        cogs=3.14,
                        component_unit_value=3.14,
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        country_code_of_origin="country_code_of_origin_example",
                        customs_description="customs_description_example",
                        description="description_example",
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discount_quantity=3.14,
                        discount_shipping_weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        distribution_center_code="distribution_center_code_example",
                        edi=OrderItemEdi(
                            identifications=[
                                OrderItemEdiIdentification(
                                    identification="identification_example",
                                    quantity=1,
                                ),
                            ],
                            lots=[
                                OrderItemEdiLot(
                                    lot_expiration="lot_expiration_example",
                                    lot_number="lot_number_example",
                                    lot_quantity=1,
                                ),
                            ],
                        ),
                        exclude_coupon=True,
                        free_shipping=True,
                        hazmat=True,
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        item_index=1,
                        item_reference_oid=1,
                        kit=True,
                        kit_component=True,
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        manufacturer_sku="manufacturer_sku_example",
                        max_days_time_in_transit=1,
                        merchant_item_id="merchant_item_id_example",
                        mix_and_match_group_name="mix_and_match_group_name_example",
                        mix_and_match_group_oid=1,
                        no_shipping_discount=True,
                        options=[
                            OrderItemOption(
                                additional_dimension_application="none",
                                cost_change=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                file_attachment=OrderItemOptionFileAttachment(
                                    expiration_dts="expiration_dts_example",
                                    file_name="file_name_example",
                                    mime_type="mime_type_example",
                                    size=1,
                                ),
                                height=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                hidden=True,
                                label="label_example",
                                length=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                one_time_fee=True,
                                value="value_example",
                                weight_change=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                width=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                            ),
                        ],
                        packed_by_user="packed_by_user_example",
                        parent_item_index=1,
                        parent_merchant_item_id="parent_merchant_item_id_example",
                        perishable_class="perishable_class_example",
                        pricing_tier_name="pricing_tier_name_example",
                        properties=[
                            OrderItemProperty(
                                display=True,
                                expiration_dts="expiration_dts_example",
                                name="name_example",
                                value="value_example",
                            ),
                        ],
                        quantity=3.14,
                        quantity_refunded=3.14,
                        quickbooks_class="quickbooks_class_example",
                        refund_reason="refund_reason_example",
                        return_reason="return_reason_example",
                        ship_separately=True,
                        shipped_by_user="shipped_by_user_example",
                        shipped_dts="shipped_dts_example",
                        shipping_status="shipping_status_example",
                        special_product_type="special_product_type_example",
                        tags=[
                            OrderItemTag(
                                tag_value="tag_value_example",
                            ),
                        ],
                        tax_free=True,
                        tax_product_type="",
                        taxable_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_refunded=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        transmitted_to_distribution_center_dts="transmitted_to_distribution_center_dts_example",
                        unit_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        upsell=True,
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
                language_iso_code="language_iso_code_example",
                linked_shipment=OrderLinkedShipment(
                    has_linked_shipment=True,
                    linked_shipment=True,
                    linked_shipment_channel_partner_order_ids=[
                        "linked_shipment_channel_partner_order_ids_example",
                    ],
                    linked_shipment_order_ids=[
                        "linked_shipment_order_ids_example",
                    ],
                    linked_shipment_to_order_id="linked_shipment_to_order_id_example",
                ),
                marketing=OrderMarketing(
                    advertising_source="advertising_source_example",
                    cell_phone_opt_in=True,
                    mailing_list=True,
                    referral_code="referral_code_example",
                ),
                merchant_id="merchant_id_example",
                order_id="order_id_example",
                payment=OrderPayment(
                    check=OrderPaymentCheck(
                        check_number="check_number_example",
                    ),
                    credit_card=OrderPaymentCreditCard(
                        card_auth_ticket="card_auth_ticket_example",
                        card_authorization_amount=3.14,
                        card_authorization_dts="card_authorization_dts_example",
                        card_authorization_reference_number="card_authorization_reference_number_example",
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_number_token="card_number_token_example",
                        card_number_truncated=True,
                        card_type="AMEX",
                        card_verification_number_token="card_verification_number_token_example",
                        dual_vaulted=OrderPaymentCreditCardDualVaulted(
                            gateway_name="gateway_name_example",
                            properties=[
                                OrderPaymentCreditCardDualVaultedProperty(
                                    name="name_example",
                                    value="value_example",
                                ),
                            ],
                            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                        ),
                    ),
                    echeck=OrderPaymentECheck(
                        bank_aba_code="bank_aba_code_example",
                        bank_account_name="bank_account_name_example",
                        bank_account_number="bank_account_number_example",
                        bank_account_type="Checking",
                        bank_name="bank_name_example",
                        bank_owner_type="Personal",
                        customer_tax_id="customer_tax_id_example",
                        drivers_license_dob="drivers_license_dob_example",
                        drivers_license_number="drivers_license_number_example",
                        drivers_license_state="drivers_license_state_example",
                    ),
                    health_benefit_card=OrderPaymentHealthBenefitCard(
                        health_benefit_card_expiration_month=1,
                        health_benefit_card_expiration_year=1,
                        health_benefit_card_number="health_benefit_card_number_example",
                        health_benefit_card_number_token="health_benefit_card_number_token_example",
                        health_benefit_card_number_truncated=True,
                        health_benefit_card_verification_number_token="health_benefit_card_verification_number_token_example",
                    ),
                    hold_for_fraud_review=True,
                    insurance=OrderPaymentInsurance(
                        application_id="application_id_example",
                        claim_id="claim_id_example",
                        insurance_type="insurance_type_example",
                        refund_claim_id="refund_claim_id_example",
                    ),
                    payment_dts="payment_dts_example",
                    payment_method="Affirm",
                    payment_method_accounting_code="payment_method_accounting_code_example",
                    payment_method_deposit_to_account="payment_method_deposit_to_account_example",
                    payment_status="Unprocessed",
                    purchase_order=OrderPaymentPurchaseOrder(
                        purchase_order_number="purchase_order_number_example",
                    ),
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    surcharge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    surcharge_accounting_code="surcharge_accounting_code_example",
                    surcharge_transaction_fee=3.14,
                    surcharge_transaction_percentage=3.14,
                    test_order=True,
                    transactions=[
                        OrderPaymentTransaction(
                            details=[
                                OrderPaymentTransactionDetail(
                                    name="name_example",
                                    type="type_example",
                                    value="value_example",
                                ),
                            ],
                            successful=True,
                            transaction_gateway="transaction_gateway_example",
                            transaction_id=1,
                            transaction_timestamp="transaction_timestamp_example",
                        ),
                    ],
                ),
                point_of_sale=OrderPointOfSale(
                    location=PointOfSaleLocation(
                        adddress2="adddress2_example",
                        address1="address1_example",
                        city="city_example",
                        country="country_example",
                        distribution_center_code="distribution_center_code_example",
                        external_id="external_id_example",
                        merchant_id="merchant_id_example",
                        pos_location_oid=1,
                        postal_code="postal_code_example",
                        state_province="state_province_example",
                    ),
                    reader=PointOfSaleReader(
                        device_type="device_type_example",
                        label="label_example",
                        merchant_id="merchant_id_example",
                        payment_provider="stripe",
                        pos_reader_id=1,
                        pos_register_oid=1,
                        serial_number="serial_number_example",
                        stripe_account_id="stripe_account_id_example",
                        stripe_reader_id="stripe_reader_id_example",
                    ),
                    register=PointOfSaleRegister(
                        merchant_id="merchant_id_example",
                        name="name_example",
                        pos_location_oid=1,
                        pos_register_oid=1,
                    ),
                ),
                properties=[
                    OrderProperty(
                        display=True,
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quote=OrderQuote(
                    quote_expiration_dts="quote_expiration_dts_example",
                    quoted_by="quoted_by_example",
                    quoted_dts="quoted_dts_example",
                ),
                refund_dts="refund_dts_example",
                refund_reason="refund_reason_example",
                reject_dts="reject_dts_example",
                reject_reason="reject_reason_example",
                salesforce=OrderSalesforce(
                    salesforce_opportunity_id="salesforce_opportunity_id_example",
                ),
                shipping=OrderShipping(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    delivery_date="delivery_date_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    least_cost_route=True,
                    least_cost_route_shipping_methods=[
                        "least_cost_route_shipping_methods_example",
                    ],
                    lift_gate=True,
                    pickup_dts="pickup_dts_example",
                    postal_code="postal_code_example",
                    rma="rma_example",
                    ship_on_date="ship_on_date_example",
                    ship_to_residential=True,
                    shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                    shipping_date="shipping_date_example",
                    shipping_department_status="shipping_department_status_example",
                    shipping_method="shipping_method_example",
                    shipping_method_accounting_code="shipping_method_accounting_code_example",
                    special_instructions="special_instructions_example",
                    state_region="state_region_example",
                    title="title_example",
                    tracking_number_details=[
                        OrderTrackingNumberDetails(
                            actual_delivery_date="actual_delivery_date_example",
                            actual_delivery_date_formatted="actual_delivery_date_formatted_example",
                            details=[
                                OrderTrackingNumberDetail(
                                    city="city_example",
                                    event_dts="event_dts_example",
                                    event_local_date="event_local_date_example",
                                    event_local_time="event_local_time_example",
                                    event_timezone_id="event_timezone_id_example",
                                    state="state_example",
                                    subtag="subtag_example",
                                    subtag_message="subtag_message_example",
                                    tag="tag_example",
                                    tag_description="tag_description_example",
                                    tag_icon="tag_icon_example",
                                    zip="zip_example",
                                ),
                            ],
                            easypost_tracker_id="easypost_tracker_id_example",
                            expected_delivery_date="expected_delivery_date_example",
                            expected_delivery_date_formatted="expected_delivery_date_formatted_example",
                            map_url="map_url_example",
                            order_placed_date="order_placed_date_example",
                            order_placed_date_formatted="order_placed_date_formatted_example",
                            payment_processed_date="payment_processed_date_example",
                            payment_processed_date_formatted="payment_processed_date_formatted_example",
                            shipped_date="shipped_date_example",
                            shipped_date_formatted="shipped_date_formatted_example",
                            shipping_method="shipping_method_example",
                            status="status_example",
                            status_description="status_description_example",
                            tracking_number="tracking_number_example",
                            tracking_url="tracking_url_example",
                        ),
                    ],
                    tracking_numbers=[
                        "tracking_numbers_example",
                    ],
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                ),
                summary=OrderSummary(
                    actual_fulfillment=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_payment_processing=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_shipping=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    arbitrary_shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    other_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ),
                tags=[
                    OrderTag(
                        tag_value="tag_value_example",
                    ),
                ],
                taxes=OrderTaxes(
                    arbitrary_tax=3.14,
                    arbitrary_tax_rate=3.14,
                    arbitrary_taxable_subtotal=3.14,
                    tax_city_accounting_code="tax_city_accounting_code_example",
                    tax_country_accounting_code="tax_country_accounting_code_example",
                    tax_county="tax_county_example",
                    tax_county_accounting_code="tax_county_accounting_code_example",
                    tax_gift_charge=True,
                    tax_postal_code_accounting_code="tax_postal_code_accounting_code_example",
                    tax_rate=3.14,
                    tax_rate_city=3.14,
                    tax_rate_country=3.14,
                    tax_rate_county=3.14,
                    tax_rate_postal_code=3.14,
                    tax_rate_state=3.14,
                    tax_shipping=True,
                    tax_state_accounting_code="tax_state_accounting_code_example",
                ),
                utms=[
                    OrderUtm(
                        attribution_first_click_subtotal=3.14,
                        attribution_first_click_total=3.14,
                        attribution_last_click_subtotal=3.14,
                        attribution_last_click_total=3.14,
                        attribution_linear_subtotal=3.14,
                        attribution_linear_total=3.14,
                        attribution_position_based_subtotal=3.14,
                        attribution_position_based_total=3.14,
                        click_dts="click_dts_example",
                        facebook_ad_id="facebook_ad_id_example",
                        fbclid="fbclid_example",
                        gbraid="gbraid_example",
                        glcid="glcid_example",
                        itm_campaign="itm_campaign_example",
                        itm_content="itm_content_example",
                        itm_id="itm_id_example",
                        itm_medium="itm_medium_example",
                        itm_source="itm_source_example",
                        itm_term="itm_term_example",
                        msclkid="msclkid_example",
                        ttclid="ttclid_example",
                        uc_message_id="uc_message_id_example",
                        utm_campaign="utm_campaign_example",
                        utm_content="utm_content_example",
                        utm_id="utm_id_example",
                        utm_medium="utm_medium_example",
                        utm_source="utm_source_example",
                        utm_term="utm_term_example",
                        vmcid="vmcid_example",
                        wbraid="wbraid_example",
                    ),
                ],
            ),
        ],
        orders_summary=CustomerOrdersSummary(
            first_order_dts="first_order_dts_example",
            last_order_dts="last_order_dts_example",
            order_count=1,
            total=3.14,
        ),
        password="password_example",
        pricing_tiers=[
            CustomerPricingTier(
                name="name_example",
                pricing_tier_oid=1,
            ),
        ],
        privacy=CustomerPrivacy(
            last_update_dts="last_update_dts_example",
            marketing=True,
            preference=True,
            statistics=True,
        ),
        properties=[
            CustomerProperty(
                customer_profile_property_oid=1,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        qb_class="qb_class_example",
        qb_code="qb_code_example",
        qb_tax_exemption_reason_code=1,
        quotes=[
            Order(
                affiliates=[
                    OrderAffiliate(
                        affiliate_oid=1,
                        ledger_entries=[
                            OrderAffiliateLedger(
                                assigned_by_user="assigned_by_user_example",
                                item_id="item_id_example",
                                tier_number=1,
                                transaction_amount=3.14,
                                transaction_amount_paid=3.14,
                                transaction_dts="transaction_dts_example",
                                transaction_memo="transaction_memo_example",
                                transaction_percentage=3.14,
                                transaction_state="Pending",
                            ),
                        ],
                        sub_id="sub_id_example",
                    ),
                ],
                auto_order=OrderAutoOrder(
                    auto_order_code="auto_order_code_example",
                    auto_order_oid=1,
                    cancel_after_next_x_orders=1,
                    cancel_downgrade=True,
                    cancel_reason="cancel_reason_example",
                    cancel_upgrade=True,
                    canceled_by_user="canceled_by_user_example",
                    canceled_dts="canceled_dts_example",
                    completed=True,
                    credit_card_attempt=1,
                    disabled_dts="disabled_dts_example",
                    enabled=True,
                    failure_reason="failure_reason_example",
                    items=[
                        AutoOrderItem(
                            arbitrary_item_id="arbitrary_item_id_example",
                            arbitrary_percentage_discount=3.14,
                            arbitrary_quantity=3.14,
                            arbitrary_schedule_days=1,
                            arbitrary_unit_cost=3.14,
                            arbitrary_unit_cost_remaining_orders=1,
                            auto_order_item_oid=1,
                            calculated_next_shipment_dts="calculated_next_shipment_dts_example",
                            first_order_dts="first_order_dts_example",
                            frequency="Weekly",
                            future_schedules=[
                                AutoOrderItemFutureSchedule(
                                    item_id="item_id_example",
                                    rebill_count=1,
                                    shipment_dts="shipment_dts_example",
                                    unit_cost=3.14,
                                ),
                            ],
                            last_order_dts="last_order_dts_example",
                            life_time_value=3.14,
                            next_item_id="next_item_id_example",
                            next_preshipment_notice_dts="next_preshipment_notice_dts_example",
                            next_shipment_dts="next_shipment_dts_example",
                            no_order_after_dts="no_order_after_dts_example",
                            number_of_rebills=1,
                            options=[
                                AutoOrderItemOption(
                                    label="label_example",
                                    value="value_example",
                                ),
                            ],
                            original_item_id="original_item_id_example",
                            original_quantity=3.14,
                            paused=True,
                            paypal_payer_id="paypal_payer_id_example",
                            paypal_recurring_payment_profile_id="paypal_recurring_payment_profile_id_example",
                            preshipment_notice_sent=True,
                            rebill_value=3.14,
                            remaining_repeat_count=1,
                            simple_schedule=AutoOrderItemSimpleSchedule(
                                frequency="Weekly",
                                item_id="item_id_example",
                                repeat_count=1,
                            ),
                        ),
                    ],
                    next_attempt="next_attempt_example",
                    original_order_id="original_order_id_example",
                    override_affiliate_id=1,
                    rebill_orders=[
                        Order(),
                    ],
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    status="active",
                ),
                billing=OrderBilling(
                    address1="address1_example",
                    address2="address2_example",
                    cc_emails=[
                        "cc_emails_example",
                    ],
                    cell_phone="cell_phone_example",
                    cell_phone_e164="cell_phone_e164_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    email="email_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    title="title_example",
                ),
                buysafe=OrderBuysafe(
                    buysafe_bond_available=True,
                    buysafe_bond_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_free=True,
                    buysafe_bond_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_wanted=True,
                    buysafe_shopping_cart_id="buysafe_shopping_cart_id_example",
                ),
                channel_partner=OrderChannelPartner(
                    auto_approve_purchase_order=True,
                    channel_partner_code="channel_partner_code_example",
                    channel_partner_data="channel_partner_data_example",
                    channel_partner_oid=1,
                    channel_partner_order_id="channel_partner_order_id_example",
                    ignore_invalid_shipping_method=True,
                    no_realtime_payment_processing=True,
                    skip_payment_processing=True,
                    store_completed=True,
                    store_if_payment_declines=True,
                    treat_warnings_as_errors=True,
                ),
                checkout=OrderCheckout(
                    browser=Browser(
                        device=BrowserDevice(
                            family="family_example",
                        ),
                        os=BrowserOS(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                            patch_minor="patch_minor_example",
                        ),
                        user_agent=BrowserUserAgent(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                        ),
                    ),
                    comments="comments_example",
                    custom_field1="custom_field1_example",
                    custom_field10="custom_field10_example",
                    custom_field2="custom_field2_example",
                    custom_field3="custom_field3_example",
                    custom_field4="custom_field4_example",
                    custom_field5="custom_field5_example",
                    custom_field6="custom_field6_example",
                    custom_field7="custom_field7_example",
                    custom_field8="custom_field8_example",
                    custom_field9="custom_field9_example",
                    customer_ip_address="customer_ip_address_example",
                    screen_branding_theme_code="screen_branding_theme_code_example",
                    screen_size="screen_size_example",
                    storefront_host_name="storefront_host_name_example",
                    upsell_path_code="upsell_path_code_example",
                ),
                coupons=[
                    OrderCoupon(
                        accounting_code="accounting_code_example",
                        automatically_applied=True,
                        base_coupon_code="base_coupon_code_example",
                        coupon_code="coupon_code_example",
                        hdie_from_customer=True,
                    ),
                ],
                creation_dts="creation_dts_example",
                currency_code="currency_code_example",
                current_stage="Accounts Receivable",
                customer_profile=Customer(),
                digital_order=OrderDigitalOrder(
                    creation_dts="creation_dts_example",
                    expiration_dts="expiration_dts_example",
                    items=[
                        OrderDigitalItem(
                            file_size=1,
                            last_download="last_download_example",
                            last_download_ip_address="last_download_ip_address_example",
                            original_filename="original_filename_example",
                            product_code="product_code_example",
                            product_description="product_description_example",
                            remaining_downloads=1,
                            url="url_example",
                        ),
                    ],
                    url="url_example",
                    url_id="url_id_example",
                ),
                edi=OrderEdi(
                    bill_to_edi_code="bill_to_edi_code_example",
                    edi_department="edi_department_example",
                    edi_internal_vendor_number="edi_internal_vendor_number_example",
                    ship_to_edi_code="ship_to_edi_code_example",
                ),
                exchange_rate=3.14,
                fraud_score=OrderFraudScore(
                    anonymous_proxy=True,
                    bin_match="NA",
                    carder_email=True,
                    country_code="country_code_example",
                    country_match=True,
                    customer_phone_in_billing_location="customer_phone_in_billing_location_example",
                    distance_km=1,
                    free_email=True,
                    high_risk_country=True,
                    ip_city="ip_city_example",
                    ip_isp="ip_isp_example",
                    ip_latitude="ip_latitude_example",
                    ip_longitude="ip_longitude_example",
                    ip_org="ip_org_example",
                    ip_region="ip_region_example",
                    proxy_score=3.14,
                    score=3.14,
                    ship_forwarder=True,
                    spam_score=3.14,
                    transparent_proxy=True,
                ),
                gift=OrderGift(
                    gift=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_charge_accounting_code="gift_charge_accounting_code_example",
                    gift_charge_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_email="gift_email_example",
                    gift_message="gift_message_example",
                    gift_wrap_accounting_code="gift_wrap_accounting_code_example",
                    gift_wrap_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_title="gift_wrap_title_example",
                ),
                gift_certificate=OrderGiftCertificate(
                    gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_certificate_code="gift_certificate_code_example",
                    gift_certificate_oid=1,
                ),
                internal=OrderInternal(
                    exported_to_accounting=True,
                    merchant_notes="merchant_notes_example",
                    placed_by_user="placed_by_user_example",
                    refund_by_user="refund_by_user_example",
                    sales_rep_code="sales_rep_code_example",
                    transactional_merchant_notes=[
                        OrderTransactionalMerchantNote(
                            ip_address="ip_address_example",
                            note="note_example",
                            note_dts="note_dts_example",
                            user="user_example",
                        ),
                    ],
                ),
                items=[
                    OrderItem(
                        accounting_code="accounting_code_example",
                        activation_codes=[
                            "activation_codes_example",
                        ],
                        arbitrary_unit_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                        auto_order_schedule="auto_order_schedule_example",
                        barcode="barcode_example",
                        barcode_gtin12="barcode_gtin12_example",
                        barcode_gtin14="barcode_gtin14_example",
                        barcode_upc11="barcode_upc11_example",
                        barcode_upc12="barcode_upc12_example",
                        channel_partner_item_id="channel_partner_item_id_example",
                        cogs=3.14,
                        component_unit_value=3.14,
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        country_code_of_origin="country_code_of_origin_example",
                        customs_description="customs_description_example",
                        description="description_example",
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discount_quantity=3.14,
                        discount_shipping_weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        distribution_center_code="distribution_center_code_example",
                        edi=OrderItemEdi(
                            identifications=[
                                OrderItemEdiIdentification(
                                    identification="identification_example",
                                    quantity=1,
                                ),
                            ],
                            lots=[
                                OrderItemEdiLot(
                                    lot_expiration="lot_expiration_example",
                                    lot_number="lot_number_example",
                                    lot_quantity=1,
                                ),
                            ],
                        ),
                        exclude_coupon=True,
                        free_shipping=True,
                        hazmat=True,
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        item_index=1,
                        item_reference_oid=1,
                        kit=True,
                        kit_component=True,
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        manufacturer_sku="manufacturer_sku_example",
                        max_days_time_in_transit=1,
                        merchant_item_id="merchant_item_id_example",
                        mix_and_match_group_name="mix_and_match_group_name_example",
                        mix_and_match_group_oid=1,
                        no_shipping_discount=True,
                        options=[
                            OrderItemOption(
                                additional_dimension_application="none",
                                cost_change=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                file_attachment=OrderItemOptionFileAttachment(
                                    expiration_dts="expiration_dts_example",
                                    file_name="file_name_example",
                                    mime_type="mime_type_example",
                                    size=1,
                                ),
                                height=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                hidden=True,
                                label="label_example",
                                length=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                one_time_fee=True,
                                value="value_example",
                                weight_change=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                width=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                            ),
                        ],
                        packed_by_user="packed_by_user_example",
                        parent_item_index=1,
                        parent_merchant_item_id="parent_merchant_item_id_example",
                        perishable_class="perishable_class_example",
                        pricing_tier_name="pricing_tier_name_example",
                        properties=[
                            OrderItemProperty(
                                display=True,
                                expiration_dts="expiration_dts_example",
                                name="name_example",
                                value="value_example",
                            ),
                        ],
                        quantity=3.14,
                        quantity_refunded=3.14,
                        quickbooks_class="quickbooks_class_example",
                        refund_reason="refund_reason_example",
                        return_reason="return_reason_example",
                        ship_separately=True,
                        shipped_by_user="shipped_by_user_example",
                        shipped_dts="shipped_dts_example",
                        shipping_status="shipping_status_example",
                        special_product_type="special_product_type_example",
                        tags=[
                            OrderItemTag(
                                tag_value="tag_value_example",
                            ),
                        ],
                        tax_free=True,
                        tax_product_type="",
                        taxable_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_refunded=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        transmitted_to_distribution_center_dts="transmitted_to_distribution_center_dts_example",
                        unit_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        upsell=True,
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
                language_iso_code="language_iso_code_example",
                linked_shipment=OrderLinkedShipment(
                    has_linked_shipment=True,
                    linked_shipment=True,
                    linked_shipment_channel_partner_order_ids=[
                        "linked_shipment_channel_partner_order_ids_example",
                    ],
                    linked_shipment_order_ids=[
                        "linked_shipment_order_ids_example",
                    ],
                    linked_shipment_to_order_id="linked_shipment_to_order_id_example",
                ),
                marketing=OrderMarketing(
                    advertising_source="advertising_source_example",
                    cell_phone_opt_in=True,
                    mailing_list=True,
                    referral_code="referral_code_example",
                ),
                merchant_id="merchant_id_example",
                order_id="order_id_example",
                payment=OrderPayment(
                    check=OrderPaymentCheck(
                        check_number="check_number_example",
                    ),
                    credit_card=OrderPaymentCreditCard(
                        card_auth_ticket="card_auth_ticket_example",
                        card_authorization_amount=3.14,
                        card_authorization_dts="card_authorization_dts_example",
                        card_authorization_reference_number="card_authorization_reference_number_example",
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_number_token="card_number_token_example",
                        card_number_truncated=True,
                        card_type="AMEX",
                        card_verification_number_token="card_verification_number_token_example",
                        dual_vaulted=OrderPaymentCreditCardDualVaulted(
                            gateway_name="gateway_name_example",
                            properties=[
                                OrderPaymentCreditCardDualVaultedProperty(
                                    name="name_example",
                                    value="value_example",
                                ),
                            ],
                            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                        ),
                    ),
                    echeck=OrderPaymentECheck(
                        bank_aba_code="bank_aba_code_example",
                        bank_account_name="bank_account_name_example",
                        bank_account_number="bank_account_number_example",
                        bank_account_type="Checking",
                        bank_name="bank_name_example",
                        bank_owner_type="Personal",
                        customer_tax_id="customer_tax_id_example",
                        drivers_license_dob="drivers_license_dob_example",
                        drivers_license_number="drivers_license_number_example",
                        drivers_license_state="drivers_license_state_example",
                    ),
                    health_benefit_card=OrderPaymentHealthBenefitCard(
                        health_benefit_card_expiration_month=1,
                        health_benefit_card_expiration_year=1,
                        health_benefit_card_number="health_benefit_card_number_example",
                        health_benefit_card_number_token="health_benefit_card_number_token_example",
                        health_benefit_card_number_truncated=True,
                        health_benefit_card_verification_number_token="health_benefit_card_verification_number_token_example",
                    ),
                    hold_for_fraud_review=True,
                    insurance=OrderPaymentInsurance(
                        application_id="application_id_example",
                        claim_id="claim_id_example",
                        insurance_type="insurance_type_example",
                        refund_claim_id="refund_claim_id_example",
                    ),
                    payment_dts="payment_dts_example",
                    payment_method="Affirm",
                    payment_method_accounting_code="payment_method_accounting_code_example",
                    payment_method_deposit_to_account="payment_method_deposit_to_account_example",
                    payment_status="Unprocessed",
                    purchase_order=OrderPaymentPurchaseOrder(
                        purchase_order_number="purchase_order_number_example",
                    ),
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    surcharge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    surcharge_accounting_code="surcharge_accounting_code_example",
                    surcharge_transaction_fee=3.14,
                    surcharge_transaction_percentage=3.14,
                    test_order=True,
                    transactions=[
                        OrderPaymentTransaction(
                            details=[
                                OrderPaymentTransactionDetail(
                                    name="name_example",
                                    type="type_example",
                                    value="value_example",
                                ),
                            ],
                            successful=True,
                            transaction_gateway="transaction_gateway_example",
                            transaction_id=1,
                            transaction_timestamp="transaction_timestamp_example",
                        ),
                    ],
                ),
                point_of_sale=OrderPointOfSale(
                    location=PointOfSaleLocation(
                        adddress2="adddress2_example",
                        address1="address1_example",
                        city="city_example",
                        country="country_example",
                        distribution_center_code="distribution_center_code_example",
                        external_id="external_id_example",
                        merchant_id="merchant_id_example",
                        pos_location_oid=1,
                        postal_code="postal_code_example",
                        state_province="state_province_example",
                    ),
                    reader=PointOfSaleReader(
                        device_type="device_type_example",
                        label="label_example",
                        merchant_id="merchant_id_example",
                        payment_provider="stripe",
                        pos_reader_id=1,
                        pos_register_oid=1,
                        serial_number="serial_number_example",
                        stripe_account_id="stripe_account_id_example",
                        stripe_reader_id="stripe_reader_id_example",
                    ),
                    register=PointOfSaleRegister(
                        merchant_id="merchant_id_example",
                        name="name_example",
                        pos_location_oid=1,
                        pos_register_oid=1,
                    ),
                ),
                properties=[
                    OrderProperty(
                        display=True,
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quote=OrderQuote(
                    quote_expiration_dts="quote_expiration_dts_example",
                    quoted_by="quoted_by_example",
                    quoted_dts="quoted_dts_example",
                ),
                refund_dts="refund_dts_example",
                refund_reason="refund_reason_example",
                reject_dts="reject_dts_example",
                reject_reason="reject_reason_example",
                salesforce=OrderSalesforce(
                    salesforce_opportunity_id="salesforce_opportunity_id_example",
                ),
                shipping=OrderShipping(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    delivery_date="delivery_date_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    least_cost_route=True,
                    least_cost_route_shipping_methods=[
                        "least_cost_route_shipping_methods_example",
                    ],
                    lift_gate=True,
                    pickup_dts="pickup_dts_example",
                    postal_code="postal_code_example",
                    rma="rma_example",
                    ship_on_date="ship_on_date_example",
                    ship_to_residential=True,
                    shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                    shipping_date="shipping_date_example",
                    shipping_department_status="shipping_department_status_example",
                    shipping_method="shipping_method_example",
                    shipping_method_accounting_code="shipping_method_accounting_code_example",
                    special_instructions="special_instructions_example",
                    state_region="state_region_example",
                    title="title_example",
                    tracking_number_details=[
                        OrderTrackingNumberDetails(
                            actual_delivery_date="actual_delivery_date_example",
                            actual_delivery_date_formatted="actual_delivery_date_formatted_example",
                            details=[
                                OrderTrackingNumberDetail(
                                    city="city_example",
                                    event_dts="event_dts_example",
                                    event_local_date="event_local_date_example",
                                    event_local_time="event_local_time_example",
                                    event_timezone_id="event_timezone_id_example",
                                    state="state_example",
                                    subtag="subtag_example",
                                    subtag_message="subtag_message_example",
                                    tag="tag_example",
                                    tag_description="tag_description_example",
                                    tag_icon="tag_icon_example",
                                    zip="zip_example",
                                ),
                            ],
                            easypost_tracker_id="easypost_tracker_id_example",
                            expected_delivery_date="expected_delivery_date_example",
                            expected_delivery_date_formatted="expected_delivery_date_formatted_example",
                            map_url="map_url_example",
                            order_placed_date="order_placed_date_example",
                            order_placed_date_formatted="order_placed_date_formatted_example",
                            payment_processed_date="payment_processed_date_example",
                            payment_processed_date_formatted="payment_processed_date_formatted_example",
                            shipped_date="shipped_date_example",
                            shipped_date_formatted="shipped_date_formatted_example",
                            shipping_method="shipping_method_example",
                            status="status_example",
                            status_description="status_description_example",
                            tracking_number="tracking_number_example",
                            tracking_url="tracking_url_example",
                        ),
                    ],
                    tracking_numbers=[
                        "tracking_numbers_example",
                    ],
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                ),
                summary=OrderSummary(
                    actual_fulfillment=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_payment_processing=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_shipping=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    arbitrary_shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    other_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ),
                tags=[
                    OrderTag(
                        tag_value="tag_value_example",
                    ),
                ],
                taxes=OrderTaxes(
                    arbitrary_tax=3.14,
                    arbitrary_tax_rate=3.14,
                    arbitrary_taxable_subtotal=3.14,
                    tax_city_accounting_code="tax_city_accounting_code_example",
                    tax_country_accounting_code="tax_country_accounting_code_example",
                    tax_county="tax_county_example",
                    tax_county_accounting_code="tax_county_accounting_code_example",
                    tax_gift_charge=True,
                    tax_postal_code_accounting_code="tax_postal_code_accounting_code_example",
                    tax_rate=3.14,
                    tax_rate_city=3.14,
                    tax_rate_country=3.14,
                    tax_rate_county=3.14,
                    tax_rate_postal_code=3.14,
                    tax_rate_state=3.14,
                    tax_shipping=True,
                    tax_state_accounting_code="tax_state_accounting_code_example",
                ),
                utms=[
                    OrderUtm(
                        attribution_first_click_subtotal=3.14,
                        attribution_first_click_total=3.14,
                        attribution_last_click_subtotal=3.14,
                        attribution_last_click_total=3.14,
                        attribution_linear_subtotal=3.14,
                        attribution_linear_total=3.14,
                        attribution_position_based_subtotal=3.14,
                        attribution_position_based_total=3.14,
                        click_dts="click_dts_example",
                        facebook_ad_id="facebook_ad_id_example",
                        fbclid="fbclid_example",
                        gbraid="gbraid_example",
                        glcid="glcid_example",
                        itm_campaign="itm_campaign_example",
                        itm_content="itm_content_example",
                        itm_id="itm_id_example",
                        itm_medium="itm_medium_example",
                        itm_source="itm_source_example",
                        itm_term="itm_term_example",
                        msclkid="msclkid_example",
                        ttclid="ttclid_example",
                        uc_message_id="uc_message_id_example",
                        utm_campaign="utm_campaign_example",
                        utm_content="utm_content_example",
                        utm_id="utm_id_example",
                        utm_medium="utm_medium_example",
                        utm_source="utm_source_example",
                        utm_term="utm_term_example",
                        vmcid="vmcid_example",
                        wbraid="wbraid_example",
                    ),
                ],
            ),
        ],
        quotes_summary=CustomerQuotesSummary(
            first_quote_dts="first_quote_dts_example",
            last_quote_dts="last_quote_dts_example",
            quote_count=1,
            total=3.14,
        ),
        referral_source="referral_source_example",
        reviewer=CustomerReviewer(
            auto_approve=True,
            average_overall_rating=3.14,
            expert=True,
            first_review="first_review_example",
            last_review="last_review_example",
            location="location_example",
            nickname="nickname_example",
            number_helpful_review_votes=1,
            rank=1,
            reviews_contributed=1,
        ),
        sales_rep_code="sales_rep_code_example",
        send_signup_notification=True,
        shipping=[
            CustomerShipping(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                customer_profile_oid=1,
                customer_shipping_oid=1,
                day_phone="day_phone_example",
                default_shipping=True,
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                last_used_dts="last_used_dts_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                tax_county="tax_county_example",
                title="title_example",
            ),
        ],
        signup_dts="signup_dts_example",
        software_entitlements=[
            CustomerSoftwareEntitlement(
                activation_code="activation_code_example",
                activation_dts="activation_dts_example",
                customer_software_entitlement_oid=1,
                expiration_dts="expiration_dts_example",
                purchased_via_item_description="purchased_via_item_description_example",
                purchased_via_item_id="purchased_via_item_id_example",
                purchased_via_order_id="purchased_via_order_id_example",
                software_sku="software_sku_example",
            ),
        ],
        suppress_buysafe=True,
        tags=[
            CustomerTag(
                tag_value="tag_value_example",
            ),
        ],
        tax_codes=CustomerTaxCodes(
            avalara_customer_code="avalara_customer_code_example",
            avalara_entity_use_code="avalara_entity_use_code_example",
            sovos_customer_code="sovos_customer_code_example",
            taxjar_customer_id="taxjar_customer_id_example",
            taxjar_exemption_type="taxjar_exemption_type_example",
        ),
        tax_exempt=True,
        tax_id="tax_id_example",
        terms="terms_example",
        track_separately=True,
        unapproved=True,
        ups_account_number="ups_account_number_example",
        website_url="website_url_example",
    ) # Customer | Customer to insert
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert a customer
        api_response = api_instance.insert_customer(customer)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->insert_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert a customer
        api_response = api_instance.insert_customer(customer, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->insert_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](Customer.md)| Customer to insert |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **insert_wish_list_item**
> CustomerWishListItem insert_wish_list_item(customer_profile_oid, wishlist_item)

Insert a customer wishlist item

Insert a customer wishlist item 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_wish_list_item import CustomerWishListItem
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid for this wishlist.
    wishlist_item = CustomerWishListItem(
        add_dts="add_dts_example",
        comments="comments_example",
        customer_profile_oid=1,
        customer_wishlist_item_oid=1,
        merchant_item_oid=1,
        position=1,
        priority=1,
    ) # CustomerWishListItem | Wishlist item to insert

    # example passing only required values which don't have defaults set
    try:
        # Insert a customer wishlist item
        api_response = api_instance.insert_wish_list_item(customer_profile_oid, wishlist_item)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->insert_wish_list_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **wishlist_item** | [**CustomerWishListItem**](CustomerWishListItem.md)| Wishlist item to insert |

### Return type

[**CustomerWishListItem**](CustomerWishListItem.md)

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

# **merge_customer**
> merge_customer(customer_profile_oid, customer)

Merge customer into this customer

Merge customer into this customer. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customer_merge_request import CustomerMergeRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer_profile_oid to update.
    customer = CustomerMergeRequest(
        customer_profile_oid=1,
        email="email_example",
    ) # CustomerMergeRequest | Customer to merge into this profile.
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge customer into this customer
        api_instance.merge_customer(customer_profile_oid, customer)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->merge_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge customer into this customer
        api_instance.merge_customer(customer_profile_oid, customer, expand=expand)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->merge_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid to update. |
 **customer** | [**CustomerMergeRequest**](CustomerMergeRequest.md)| Customer to merge into this profile. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

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

# **search_customer_profile_values**
> LookupResponse search_customer_profile_values(lookup_request)

Searches for all matching values (using POST)

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.lookup_response import LookupResponse
from ultracart.model.lookup_request import LookupRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    lookup_request = LookupRequest(
        category="category_example",
        matches="matches_example",
        max_hits=1,
        storefront_host_name="storefront_host_name_example",
        storefront_oid=1,
        subcategory="subcategory_example",
    ) # LookupRequest | LookupRequest

    # example passing only required values which don't have defaults set
    try:
        # Searches for all matching values (using POST)
        api_response = api_instance.search_customer_profile_values(lookup_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->search_customer_profile_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_request** | [**LookupRequest**](LookupRequest.md)| LookupRequest |

### Return type

[**LookupResponse**](LookupResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

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

# **update_customer**
> CustomerResponse update_customer(customer_profile_oid, customer)

Update a customer

Update a customer on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer import Customer
from ultracart.model.customer_response import CustomerResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer_profile_oid to update.
    customer = Customer(
        activity=CustomerActivity(
            activities=[
                Activity(
                    action="action_example",
                    channel="channel_example",
                    metric="metric_example",
                    storefront_oid=1,
                    subject="subject_example",
                    ts=1,
                    type="type_example",
                    uuid="uuid_example",
                ),
            ],
            global_unsubscribed=True,
            global_unsubscribed_dts="global_unsubscribed_dts_example",
            memberships=[
                ListSegmentMembership(
                    name="name_example",
                    type="type_example",
                    uuid="uuid_example",
                ),
            ],
            metrics=[
                Metric(
                    all_time=3.14,
                    all_time_formatted="all_time_formatted_example",
                    last_30=3.14,
                    last_30_formatted="last_30_formatted_example",
                    name="name_example",
                    prior_30=3.14,
                    prior_30_formatted="prior_30_formatted_example",
                    type="type_example",
                ),
            ],
            properties_list=[
                ModelProperty(
                    name="name_example",
                    value="value_example",
                ),
            ],
            spam_complaint=True,
            spam_complaint_dts="spam_complaint_dts_example",
        ),
        affiliate_oid=1,
        allow_3rd_party_billing=True,
        allow_cod=True,
        allow_drop_shipping=True,
        allow_purchase_order=True,
        allow_quote_request=True,
        allow_selection_of_address_type=True,
        attachments=[
            CustomerAttachment(
                customer_profile_attachment_oid=1,
                description="description_example",
                file_name="file_name_example",
                mime_type="mime_type_example",
                upload_dts="upload_dts_example",
            ),
        ],
        auto_approve_cod=True,
        auto_approve_purchase_order=True,
        automatic_merchant_notes="automatic_merchant_notes_example",
        billing=[
            CustomerBilling(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                customer_billing_oid=1,
                customer_profile_oid=1,
                day_phone="day_phone_example",
                default_billing=True,
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                last_used_dts="last_used_dts_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                tax_county="tax_county_example",
                title="title_example",
            ),
        ],
        business_notes="business_notes_example",
        cards=[
            CustomerCard(
                card_expiration_month=1,
                card_expiration_year=1,
                card_number="card_number_example",
                card_number_token="card_number_token_example",
                card_type="card_type_example",
                customer_profile_credit_card_id=1,
                customer_profile_oid=1,
                last_used_dts="last_used_dts_example",
            ),
        ],
        cc_emails=[
            CustomerEmail(
                customer_profile_email_oid=1,
                email="email_example",
                label="label_example",
                receipt_notification=True,
                refund_notification=True,
                shipment_notification=True,
            ),
        ],
        customer_profile_oid=1,
        dhl_account_number="dhl_account_number_example",
        dhl_duty_account_number="dhl_duty_account_number_example",
        do_not_send_mail=True,
        edi=CustomerEDI(
            channel_partner_oid=1,
            distribution_center_number="distribution_center_number_example",
            store_number="store_number_example",
        ),
        email="email_example",
        exempt_shipping_handling_charge=True,
        fedex_account_number="fedex_account_number_example",
        free_shipping=True,
        free_shipping_minimum=3.14,
        last_modified_by="last_modified_by_example",
        last_modified_dts="last_modified_dts_example",
        loyalty=CustomerLoyalty(
            current_points=1,
            internal_gift_certificate=GiftCertificate(
                activated=True,
                code="code_example",
                customer_profile_oid=1,
                deleted=True,
                email="email_example",
                expiration_dts="expiration_dts_example",
                gift_certificate_oid=1,
                internal=True,
                ledger_entries=[
                    GiftCertificateLedgerEntry(
                        amount=3.14,
                        description="description_example",
                        entry_dts="entry_dts_example",
                        gift_certificate_ledger_oid=1,
                        gift_certificate_oid=1,
                        reference_order_id="reference_order_id_example",
                    ),
                ],
                merchant_id="merchant_id_example",
                merchant_note="merchant_note_example",
                original_balance=3.14,
                reference_order_id="reference_order_id_example",
                remaining_balance=3.14,
            ),
            internal_gift_certificate_balance="internal_gift_certificate_balance_example",
            internal_gift_certificate_oid=1,
            ledger_entries=[
                CustomerLoyaltyLedger(
                    created_by="created_by_example",
                    created_dts="created_dts_example",
                    description="description_example",
                    email="email_example",
                    item_id="item_id_example",
                    item_index=1,
                    ledger_dts="ledger_dts_example",
                    loyalty_campaign_oid=1,
                    loyalty_ledger_oid=1,
                    loyalty_points=1,
                    modified_by="modified_by_example",
                    modified_dts="modified_dts_example",
                    order_id="order_id_example",
                    quantity=1,
                    vesting_dts="vesting_dts_example",
                ),
            ],
            pending_points=1,
            redemptions=[
                CustomerLoyaltyRedemption(
                    coupon_code="coupon_code_example",
                    coupon_code_oid=1,
                    coupon_used=True,
                    description_for_customer="description_for_customer_example",
                    expiration_dts="expiration_dts_example",
                    gift_certificate_code="gift_certificate_code_example",
                    gift_certificate_oid=1,
                    loyalty_ledger_oid=1,
                    loyalty_points=1,
                    loyalty_redemption_oid=1,
                    order_id="order_id_example",
                    redemption_dts="redemption_dts_example",
                    remaining_balance=3.14,
                ),
            ],
        ),
        maximum_item_count=1,
        merchant_id="merchant_id_example",
        minimum_item_count=1,
        minimum_subtotal=3.14,
        no_coupons=True,
        no_free_shipping=True,
        no_realtime_charge=True,
        orders=[
            Order(
                affiliates=[
                    OrderAffiliate(
                        affiliate_oid=1,
                        ledger_entries=[
                            OrderAffiliateLedger(
                                assigned_by_user="assigned_by_user_example",
                                item_id="item_id_example",
                                tier_number=1,
                                transaction_amount=3.14,
                                transaction_amount_paid=3.14,
                                transaction_dts="transaction_dts_example",
                                transaction_memo="transaction_memo_example",
                                transaction_percentage=3.14,
                                transaction_state="Pending",
                            ),
                        ],
                        sub_id="sub_id_example",
                    ),
                ],
                auto_order=OrderAutoOrder(
                    auto_order_code="auto_order_code_example",
                    auto_order_oid=1,
                    cancel_after_next_x_orders=1,
                    cancel_downgrade=True,
                    cancel_reason="cancel_reason_example",
                    cancel_upgrade=True,
                    canceled_by_user="canceled_by_user_example",
                    canceled_dts="canceled_dts_example",
                    completed=True,
                    credit_card_attempt=1,
                    disabled_dts="disabled_dts_example",
                    enabled=True,
                    failure_reason="failure_reason_example",
                    items=[
                        AutoOrderItem(
                            arbitrary_item_id="arbitrary_item_id_example",
                            arbitrary_percentage_discount=3.14,
                            arbitrary_quantity=3.14,
                            arbitrary_schedule_days=1,
                            arbitrary_unit_cost=3.14,
                            arbitrary_unit_cost_remaining_orders=1,
                            auto_order_item_oid=1,
                            calculated_next_shipment_dts="calculated_next_shipment_dts_example",
                            first_order_dts="first_order_dts_example",
                            frequency="Weekly",
                            future_schedules=[
                                AutoOrderItemFutureSchedule(
                                    item_id="item_id_example",
                                    rebill_count=1,
                                    shipment_dts="shipment_dts_example",
                                    unit_cost=3.14,
                                ),
                            ],
                            last_order_dts="last_order_dts_example",
                            life_time_value=3.14,
                            next_item_id="next_item_id_example",
                            next_preshipment_notice_dts="next_preshipment_notice_dts_example",
                            next_shipment_dts="next_shipment_dts_example",
                            no_order_after_dts="no_order_after_dts_example",
                            number_of_rebills=1,
                            options=[
                                AutoOrderItemOption(
                                    label="label_example",
                                    value="value_example",
                                ),
                            ],
                            original_item_id="original_item_id_example",
                            original_quantity=3.14,
                            paused=True,
                            paypal_payer_id="paypal_payer_id_example",
                            paypal_recurring_payment_profile_id="paypal_recurring_payment_profile_id_example",
                            preshipment_notice_sent=True,
                            rebill_value=3.14,
                            remaining_repeat_count=1,
                            simple_schedule=AutoOrderItemSimpleSchedule(
                                frequency="Weekly",
                                item_id="item_id_example",
                                repeat_count=1,
                            ),
                        ),
                    ],
                    next_attempt="next_attempt_example",
                    original_order_id="original_order_id_example",
                    override_affiliate_id=1,
                    rebill_orders=[
                        Order(),
                    ],
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    status="active",
                ),
                billing=OrderBilling(
                    address1="address1_example",
                    address2="address2_example",
                    cc_emails=[
                        "cc_emails_example",
                    ],
                    cell_phone="cell_phone_example",
                    cell_phone_e164="cell_phone_e164_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    email="email_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    title="title_example",
                ),
                buysafe=OrderBuysafe(
                    buysafe_bond_available=True,
                    buysafe_bond_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_free=True,
                    buysafe_bond_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_wanted=True,
                    buysafe_shopping_cart_id="buysafe_shopping_cart_id_example",
                ),
                channel_partner=OrderChannelPartner(
                    auto_approve_purchase_order=True,
                    channel_partner_code="channel_partner_code_example",
                    channel_partner_data="channel_partner_data_example",
                    channel_partner_oid=1,
                    channel_partner_order_id="channel_partner_order_id_example",
                    ignore_invalid_shipping_method=True,
                    no_realtime_payment_processing=True,
                    skip_payment_processing=True,
                    store_completed=True,
                    store_if_payment_declines=True,
                    treat_warnings_as_errors=True,
                ),
                checkout=OrderCheckout(
                    browser=Browser(
                        device=BrowserDevice(
                            family="family_example",
                        ),
                        os=BrowserOS(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                            patch_minor="patch_minor_example",
                        ),
                        user_agent=BrowserUserAgent(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                        ),
                    ),
                    comments="comments_example",
                    custom_field1="custom_field1_example",
                    custom_field10="custom_field10_example",
                    custom_field2="custom_field2_example",
                    custom_field3="custom_field3_example",
                    custom_field4="custom_field4_example",
                    custom_field5="custom_field5_example",
                    custom_field6="custom_field6_example",
                    custom_field7="custom_field7_example",
                    custom_field8="custom_field8_example",
                    custom_field9="custom_field9_example",
                    customer_ip_address="customer_ip_address_example",
                    screen_branding_theme_code="screen_branding_theme_code_example",
                    screen_size="screen_size_example",
                    storefront_host_name="storefront_host_name_example",
                    upsell_path_code="upsell_path_code_example",
                ),
                coupons=[
                    OrderCoupon(
                        accounting_code="accounting_code_example",
                        automatically_applied=True,
                        base_coupon_code="base_coupon_code_example",
                        coupon_code="coupon_code_example",
                        hdie_from_customer=True,
                    ),
                ],
                creation_dts="creation_dts_example",
                currency_code="currency_code_example",
                current_stage="Accounts Receivable",
                customer_profile=Customer(),
                digital_order=OrderDigitalOrder(
                    creation_dts="creation_dts_example",
                    expiration_dts="expiration_dts_example",
                    items=[
                        OrderDigitalItem(
                            file_size=1,
                            last_download="last_download_example",
                            last_download_ip_address="last_download_ip_address_example",
                            original_filename="original_filename_example",
                            product_code="product_code_example",
                            product_description="product_description_example",
                            remaining_downloads=1,
                            url="url_example",
                        ),
                    ],
                    url="url_example",
                    url_id="url_id_example",
                ),
                edi=OrderEdi(
                    bill_to_edi_code="bill_to_edi_code_example",
                    edi_department="edi_department_example",
                    edi_internal_vendor_number="edi_internal_vendor_number_example",
                    ship_to_edi_code="ship_to_edi_code_example",
                ),
                exchange_rate=3.14,
                fraud_score=OrderFraudScore(
                    anonymous_proxy=True,
                    bin_match="NA",
                    carder_email=True,
                    country_code="country_code_example",
                    country_match=True,
                    customer_phone_in_billing_location="customer_phone_in_billing_location_example",
                    distance_km=1,
                    free_email=True,
                    high_risk_country=True,
                    ip_city="ip_city_example",
                    ip_isp="ip_isp_example",
                    ip_latitude="ip_latitude_example",
                    ip_longitude="ip_longitude_example",
                    ip_org="ip_org_example",
                    ip_region="ip_region_example",
                    proxy_score=3.14,
                    score=3.14,
                    ship_forwarder=True,
                    spam_score=3.14,
                    transparent_proxy=True,
                ),
                gift=OrderGift(
                    gift=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_charge_accounting_code="gift_charge_accounting_code_example",
                    gift_charge_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_email="gift_email_example",
                    gift_message="gift_message_example",
                    gift_wrap_accounting_code="gift_wrap_accounting_code_example",
                    gift_wrap_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_title="gift_wrap_title_example",
                ),
                gift_certificate=OrderGiftCertificate(
                    gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_certificate_code="gift_certificate_code_example",
                    gift_certificate_oid=1,
                ),
                internal=OrderInternal(
                    exported_to_accounting=True,
                    merchant_notes="merchant_notes_example",
                    placed_by_user="placed_by_user_example",
                    refund_by_user="refund_by_user_example",
                    sales_rep_code="sales_rep_code_example",
                    transactional_merchant_notes=[
                        OrderTransactionalMerchantNote(
                            ip_address="ip_address_example",
                            note="note_example",
                            note_dts="note_dts_example",
                            user="user_example",
                        ),
                    ],
                ),
                items=[
                    OrderItem(
                        accounting_code="accounting_code_example",
                        activation_codes=[
                            "activation_codes_example",
                        ],
                        arbitrary_unit_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                        auto_order_schedule="auto_order_schedule_example",
                        barcode="barcode_example",
                        barcode_gtin12="barcode_gtin12_example",
                        barcode_gtin14="barcode_gtin14_example",
                        barcode_upc11="barcode_upc11_example",
                        barcode_upc12="barcode_upc12_example",
                        channel_partner_item_id="channel_partner_item_id_example",
                        cogs=3.14,
                        component_unit_value=3.14,
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        country_code_of_origin="country_code_of_origin_example",
                        customs_description="customs_description_example",
                        description="description_example",
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discount_quantity=3.14,
                        discount_shipping_weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        distribution_center_code="distribution_center_code_example",
                        edi=OrderItemEdi(
                            identifications=[
                                OrderItemEdiIdentification(
                                    identification="identification_example",
                                    quantity=1,
                                ),
                            ],
                            lots=[
                                OrderItemEdiLot(
                                    lot_expiration="lot_expiration_example",
                                    lot_number="lot_number_example",
                                    lot_quantity=1,
                                ),
                            ],
                        ),
                        exclude_coupon=True,
                        free_shipping=True,
                        hazmat=True,
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        item_index=1,
                        item_reference_oid=1,
                        kit=True,
                        kit_component=True,
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        manufacturer_sku="manufacturer_sku_example",
                        max_days_time_in_transit=1,
                        merchant_item_id="merchant_item_id_example",
                        mix_and_match_group_name="mix_and_match_group_name_example",
                        mix_and_match_group_oid=1,
                        no_shipping_discount=True,
                        options=[
                            OrderItemOption(
                                additional_dimension_application="none",
                                cost_change=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                file_attachment=OrderItemOptionFileAttachment(
                                    expiration_dts="expiration_dts_example",
                                    file_name="file_name_example",
                                    mime_type="mime_type_example",
                                    size=1,
                                ),
                                height=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                hidden=True,
                                label="label_example",
                                length=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                one_time_fee=True,
                                value="value_example",
                                weight_change=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                width=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                            ),
                        ],
                        packed_by_user="packed_by_user_example",
                        parent_item_index=1,
                        parent_merchant_item_id="parent_merchant_item_id_example",
                        perishable_class="perishable_class_example",
                        pricing_tier_name="pricing_tier_name_example",
                        properties=[
                            OrderItemProperty(
                                display=True,
                                expiration_dts="expiration_dts_example",
                                name="name_example",
                                value="value_example",
                            ),
                        ],
                        quantity=3.14,
                        quantity_refunded=3.14,
                        quickbooks_class="quickbooks_class_example",
                        refund_reason="refund_reason_example",
                        return_reason="return_reason_example",
                        ship_separately=True,
                        shipped_by_user="shipped_by_user_example",
                        shipped_dts="shipped_dts_example",
                        shipping_status="shipping_status_example",
                        special_product_type="special_product_type_example",
                        tags=[
                            OrderItemTag(
                                tag_value="tag_value_example",
                            ),
                        ],
                        tax_free=True,
                        tax_product_type="",
                        taxable_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_refunded=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        transmitted_to_distribution_center_dts="transmitted_to_distribution_center_dts_example",
                        unit_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        upsell=True,
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
                language_iso_code="language_iso_code_example",
                linked_shipment=OrderLinkedShipment(
                    has_linked_shipment=True,
                    linked_shipment=True,
                    linked_shipment_channel_partner_order_ids=[
                        "linked_shipment_channel_partner_order_ids_example",
                    ],
                    linked_shipment_order_ids=[
                        "linked_shipment_order_ids_example",
                    ],
                    linked_shipment_to_order_id="linked_shipment_to_order_id_example",
                ),
                marketing=OrderMarketing(
                    advertising_source="advertising_source_example",
                    cell_phone_opt_in=True,
                    mailing_list=True,
                    referral_code="referral_code_example",
                ),
                merchant_id="merchant_id_example",
                order_id="order_id_example",
                payment=OrderPayment(
                    check=OrderPaymentCheck(
                        check_number="check_number_example",
                    ),
                    credit_card=OrderPaymentCreditCard(
                        card_auth_ticket="card_auth_ticket_example",
                        card_authorization_amount=3.14,
                        card_authorization_dts="card_authorization_dts_example",
                        card_authorization_reference_number="card_authorization_reference_number_example",
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_number_token="card_number_token_example",
                        card_number_truncated=True,
                        card_type="AMEX",
                        card_verification_number_token="card_verification_number_token_example",
                        dual_vaulted=OrderPaymentCreditCardDualVaulted(
                            gateway_name="gateway_name_example",
                            properties=[
                                OrderPaymentCreditCardDualVaultedProperty(
                                    name="name_example",
                                    value="value_example",
                                ),
                            ],
                            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                        ),
                    ),
                    echeck=OrderPaymentECheck(
                        bank_aba_code="bank_aba_code_example",
                        bank_account_name="bank_account_name_example",
                        bank_account_number="bank_account_number_example",
                        bank_account_type="Checking",
                        bank_name="bank_name_example",
                        bank_owner_type="Personal",
                        customer_tax_id="customer_tax_id_example",
                        drivers_license_dob="drivers_license_dob_example",
                        drivers_license_number="drivers_license_number_example",
                        drivers_license_state="drivers_license_state_example",
                    ),
                    health_benefit_card=OrderPaymentHealthBenefitCard(
                        health_benefit_card_expiration_month=1,
                        health_benefit_card_expiration_year=1,
                        health_benefit_card_number="health_benefit_card_number_example",
                        health_benefit_card_number_token="health_benefit_card_number_token_example",
                        health_benefit_card_number_truncated=True,
                        health_benefit_card_verification_number_token="health_benefit_card_verification_number_token_example",
                    ),
                    hold_for_fraud_review=True,
                    insurance=OrderPaymentInsurance(
                        application_id="application_id_example",
                        claim_id="claim_id_example",
                        insurance_type="insurance_type_example",
                        refund_claim_id="refund_claim_id_example",
                    ),
                    payment_dts="payment_dts_example",
                    payment_method="Affirm",
                    payment_method_accounting_code="payment_method_accounting_code_example",
                    payment_method_deposit_to_account="payment_method_deposit_to_account_example",
                    payment_status="Unprocessed",
                    purchase_order=OrderPaymentPurchaseOrder(
                        purchase_order_number="purchase_order_number_example",
                    ),
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    surcharge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    surcharge_accounting_code="surcharge_accounting_code_example",
                    surcharge_transaction_fee=3.14,
                    surcharge_transaction_percentage=3.14,
                    test_order=True,
                    transactions=[
                        OrderPaymentTransaction(
                            details=[
                                OrderPaymentTransactionDetail(
                                    name="name_example",
                                    type="type_example",
                                    value="value_example",
                                ),
                            ],
                            successful=True,
                            transaction_gateway="transaction_gateway_example",
                            transaction_id=1,
                            transaction_timestamp="transaction_timestamp_example",
                        ),
                    ],
                ),
                point_of_sale=OrderPointOfSale(
                    location=PointOfSaleLocation(
                        adddress2="adddress2_example",
                        address1="address1_example",
                        city="city_example",
                        country="country_example",
                        distribution_center_code="distribution_center_code_example",
                        external_id="external_id_example",
                        merchant_id="merchant_id_example",
                        pos_location_oid=1,
                        postal_code="postal_code_example",
                        state_province="state_province_example",
                    ),
                    reader=PointOfSaleReader(
                        device_type="device_type_example",
                        label="label_example",
                        merchant_id="merchant_id_example",
                        payment_provider="stripe",
                        pos_reader_id=1,
                        pos_register_oid=1,
                        serial_number="serial_number_example",
                        stripe_account_id="stripe_account_id_example",
                        stripe_reader_id="stripe_reader_id_example",
                    ),
                    register=PointOfSaleRegister(
                        merchant_id="merchant_id_example",
                        name="name_example",
                        pos_location_oid=1,
                        pos_register_oid=1,
                    ),
                ),
                properties=[
                    OrderProperty(
                        display=True,
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quote=OrderQuote(
                    quote_expiration_dts="quote_expiration_dts_example",
                    quoted_by="quoted_by_example",
                    quoted_dts="quoted_dts_example",
                ),
                refund_dts="refund_dts_example",
                refund_reason="refund_reason_example",
                reject_dts="reject_dts_example",
                reject_reason="reject_reason_example",
                salesforce=OrderSalesforce(
                    salesforce_opportunity_id="salesforce_opportunity_id_example",
                ),
                shipping=OrderShipping(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    delivery_date="delivery_date_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    least_cost_route=True,
                    least_cost_route_shipping_methods=[
                        "least_cost_route_shipping_methods_example",
                    ],
                    lift_gate=True,
                    pickup_dts="pickup_dts_example",
                    postal_code="postal_code_example",
                    rma="rma_example",
                    ship_on_date="ship_on_date_example",
                    ship_to_residential=True,
                    shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                    shipping_date="shipping_date_example",
                    shipping_department_status="shipping_department_status_example",
                    shipping_method="shipping_method_example",
                    shipping_method_accounting_code="shipping_method_accounting_code_example",
                    special_instructions="special_instructions_example",
                    state_region="state_region_example",
                    title="title_example",
                    tracking_number_details=[
                        OrderTrackingNumberDetails(
                            actual_delivery_date="actual_delivery_date_example",
                            actual_delivery_date_formatted="actual_delivery_date_formatted_example",
                            details=[
                                OrderTrackingNumberDetail(
                                    city="city_example",
                                    event_dts="event_dts_example",
                                    event_local_date="event_local_date_example",
                                    event_local_time="event_local_time_example",
                                    event_timezone_id="event_timezone_id_example",
                                    state="state_example",
                                    subtag="subtag_example",
                                    subtag_message="subtag_message_example",
                                    tag="tag_example",
                                    tag_description="tag_description_example",
                                    tag_icon="tag_icon_example",
                                    zip="zip_example",
                                ),
                            ],
                            easypost_tracker_id="easypost_tracker_id_example",
                            expected_delivery_date="expected_delivery_date_example",
                            expected_delivery_date_formatted="expected_delivery_date_formatted_example",
                            map_url="map_url_example",
                            order_placed_date="order_placed_date_example",
                            order_placed_date_formatted="order_placed_date_formatted_example",
                            payment_processed_date="payment_processed_date_example",
                            payment_processed_date_formatted="payment_processed_date_formatted_example",
                            shipped_date="shipped_date_example",
                            shipped_date_formatted="shipped_date_formatted_example",
                            shipping_method="shipping_method_example",
                            status="status_example",
                            status_description="status_description_example",
                            tracking_number="tracking_number_example",
                            tracking_url="tracking_url_example",
                        ),
                    ],
                    tracking_numbers=[
                        "tracking_numbers_example",
                    ],
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                ),
                summary=OrderSummary(
                    actual_fulfillment=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_payment_processing=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_shipping=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    arbitrary_shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    other_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ),
                tags=[
                    OrderTag(
                        tag_value="tag_value_example",
                    ),
                ],
                taxes=OrderTaxes(
                    arbitrary_tax=3.14,
                    arbitrary_tax_rate=3.14,
                    arbitrary_taxable_subtotal=3.14,
                    tax_city_accounting_code="tax_city_accounting_code_example",
                    tax_country_accounting_code="tax_country_accounting_code_example",
                    tax_county="tax_county_example",
                    tax_county_accounting_code="tax_county_accounting_code_example",
                    tax_gift_charge=True,
                    tax_postal_code_accounting_code="tax_postal_code_accounting_code_example",
                    tax_rate=3.14,
                    tax_rate_city=3.14,
                    tax_rate_country=3.14,
                    tax_rate_county=3.14,
                    tax_rate_postal_code=3.14,
                    tax_rate_state=3.14,
                    tax_shipping=True,
                    tax_state_accounting_code="tax_state_accounting_code_example",
                ),
                utms=[
                    OrderUtm(
                        attribution_first_click_subtotal=3.14,
                        attribution_first_click_total=3.14,
                        attribution_last_click_subtotal=3.14,
                        attribution_last_click_total=3.14,
                        attribution_linear_subtotal=3.14,
                        attribution_linear_total=3.14,
                        attribution_position_based_subtotal=3.14,
                        attribution_position_based_total=3.14,
                        click_dts="click_dts_example",
                        facebook_ad_id="facebook_ad_id_example",
                        fbclid="fbclid_example",
                        gbraid="gbraid_example",
                        glcid="glcid_example",
                        itm_campaign="itm_campaign_example",
                        itm_content="itm_content_example",
                        itm_id="itm_id_example",
                        itm_medium="itm_medium_example",
                        itm_source="itm_source_example",
                        itm_term="itm_term_example",
                        msclkid="msclkid_example",
                        ttclid="ttclid_example",
                        uc_message_id="uc_message_id_example",
                        utm_campaign="utm_campaign_example",
                        utm_content="utm_content_example",
                        utm_id="utm_id_example",
                        utm_medium="utm_medium_example",
                        utm_source="utm_source_example",
                        utm_term="utm_term_example",
                        vmcid="vmcid_example",
                        wbraid="wbraid_example",
                    ),
                ],
            ),
        ],
        orders_summary=CustomerOrdersSummary(
            first_order_dts="first_order_dts_example",
            last_order_dts="last_order_dts_example",
            order_count=1,
            total=3.14,
        ),
        password="password_example",
        pricing_tiers=[
            CustomerPricingTier(
                name="name_example",
                pricing_tier_oid=1,
            ),
        ],
        privacy=CustomerPrivacy(
            last_update_dts="last_update_dts_example",
            marketing=True,
            preference=True,
            statistics=True,
        ),
        properties=[
            CustomerProperty(
                customer_profile_property_oid=1,
                expiration_dts="expiration_dts_example",
                name="name_example",
                value="value_example",
            ),
        ],
        qb_class="qb_class_example",
        qb_code="qb_code_example",
        qb_tax_exemption_reason_code=1,
        quotes=[
            Order(
                affiliates=[
                    OrderAffiliate(
                        affiliate_oid=1,
                        ledger_entries=[
                            OrderAffiliateLedger(
                                assigned_by_user="assigned_by_user_example",
                                item_id="item_id_example",
                                tier_number=1,
                                transaction_amount=3.14,
                                transaction_amount_paid=3.14,
                                transaction_dts="transaction_dts_example",
                                transaction_memo="transaction_memo_example",
                                transaction_percentage=3.14,
                                transaction_state="Pending",
                            ),
                        ],
                        sub_id="sub_id_example",
                    ),
                ],
                auto_order=OrderAutoOrder(
                    auto_order_code="auto_order_code_example",
                    auto_order_oid=1,
                    cancel_after_next_x_orders=1,
                    cancel_downgrade=True,
                    cancel_reason="cancel_reason_example",
                    cancel_upgrade=True,
                    canceled_by_user="canceled_by_user_example",
                    canceled_dts="canceled_dts_example",
                    completed=True,
                    credit_card_attempt=1,
                    disabled_dts="disabled_dts_example",
                    enabled=True,
                    failure_reason="failure_reason_example",
                    items=[
                        AutoOrderItem(
                            arbitrary_item_id="arbitrary_item_id_example",
                            arbitrary_percentage_discount=3.14,
                            arbitrary_quantity=3.14,
                            arbitrary_schedule_days=1,
                            arbitrary_unit_cost=3.14,
                            arbitrary_unit_cost_remaining_orders=1,
                            auto_order_item_oid=1,
                            calculated_next_shipment_dts="calculated_next_shipment_dts_example",
                            first_order_dts="first_order_dts_example",
                            frequency="Weekly",
                            future_schedules=[
                                AutoOrderItemFutureSchedule(
                                    item_id="item_id_example",
                                    rebill_count=1,
                                    shipment_dts="shipment_dts_example",
                                    unit_cost=3.14,
                                ),
                            ],
                            last_order_dts="last_order_dts_example",
                            life_time_value=3.14,
                            next_item_id="next_item_id_example",
                            next_preshipment_notice_dts="next_preshipment_notice_dts_example",
                            next_shipment_dts="next_shipment_dts_example",
                            no_order_after_dts="no_order_after_dts_example",
                            number_of_rebills=1,
                            options=[
                                AutoOrderItemOption(
                                    label="label_example",
                                    value="value_example",
                                ),
                            ],
                            original_item_id="original_item_id_example",
                            original_quantity=3.14,
                            paused=True,
                            paypal_payer_id="paypal_payer_id_example",
                            paypal_recurring_payment_profile_id="paypal_recurring_payment_profile_id_example",
                            preshipment_notice_sent=True,
                            rebill_value=3.14,
                            remaining_repeat_count=1,
                            simple_schedule=AutoOrderItemSimpleSchedule(
                                frequency="Weekly",
                                item_id="item_id_example",
                                repeat_count=1,
                            ),
                        ),
                    ],
                    next_attempt="next_attempt_example",
                    original_order_id="original_order_id_example",
                    override_affiliate_id=1,
                    rebill_orders=[
                        Order(),
                    ],
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    status="active",
                ),
                billing=OrderBilling(
                    address1="address1_example",
                    address2="address2_example",
                    cc_emails=[
                        "cc_emails_example",
                    ],
                    cell_phone="cell_phone_example",
                    cell_phone_e164="cell_phone_e164_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    email="email_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    postal_code="postal_code_example",
                    state_region="state_region_example",
                    title="title_example",
                ),
                buysafe=OrderBuysafe(
                    buysafe_bond_available=True,
                    buysafe_bond_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_free=True,
                    buysafe_bond_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    buysafe_bond_wanted=True,
                    buysafe_shopping_cart_id="buysafe_shopping_cart_id_example",
                ),
                channel_partner=OrderChannelPartner(
                    auto_approve_purchase_order=True,
                    channel_partner_code="channel_partner_code_example",
                    channel_partner_data="channel_partner_data_example",
                    channel_partner_oid=1,
                    channel_partner_order_id="channel_partner_order_id_example",
                    ignore_invalid_shipping_method=True,
                    no_realtime_payment_processing=True,
                    skip_payment_processing=True,
                    store_completed=True,
                    store_if_payment_declines=True,
                    treat_warnings_as_errors=True,
                ),
                checkout=OrderCheckout(
                    browser=Browser(
                        device=BrowserDevice(
                            family="family_example",
                        ),
                        os=BrowserOS(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                            patch_minor="patch_minor_example",
                        ),
                        user_agent=BrowserUserAgent(
                            family="family_example",
                            major="major_example",
                            minor="minor_example",
                            patch="patch_example",
                        ),
                    ),
                    comments="comments_example",
                    custom_field1="custom_field1_example",
                    custom_field10="custom_field10_example",
                    custom_field2="custom_field2_example",
                    custom_field3="custom_field3_example",
                    custom_field4="custom_field4_example",
                    custom_field5="custom_field5_example",
                    custom_field6="custom_field6_example",
                    custom_field7="custom_field7_example",
                    custom_field8="custom_field8_example",
                    custom_field9="custom_field9_example",
                    customer_ip_address="customer_ip_address_example",
                    screen_branding_theme_code="screen_branding_theme_code_example",
                    screen_size="screen_size_example",
                    storefront_host_name="storefront_host_name_example",
                    upsell_path_code="upsell_path_code_example",
                ),
                coupons=[
                    OrderCoupon(
                        accounting_code="accounting_code_example",
                        automatically_applied=True,
                        base_coupon_code="base_coupon_code_example",
                        coupon_code="coupon_code_example",
                        hdie_from_customer=True,
                    ),
                ],
                creation_dts="creation_dts_example",
                currency_code="currency_code_example",
                current_stage="Accounts Receivable",
                customer_profile=Customer(),
                digital_order=OrderDigitalOrder(
                    creation_dts="creation_dts_example",
                    expiration_dts="expiration_dts_example",
                    items=[
                        OrderDigitalItem(
                            file_size=1,
                            last_download="last_download_example",
                            last_download_ip_address="last_download_ip_address_example",
                            original_filename="original_filename_example",
                            product_code="product_code_example",
                            product_description="product_description_example",
                            remaining_downloads=1,
                            url="url_example",
                        ),
                    ],
                    url="url_example",
                    url_id="url_id_example",
                ),
                edi=OrderEdi(
                    bill_to_edi_code="bill_to_edi_code_example",
                    edi_department="edi_department_example",
                    edi_internal_vendor_number="edi_internal_vendor_number_example",
                    ship_to_edi_code="ship_to_edi_code_example",
                ),
                exchange_rate=3.14,
                fraud_score=OrderFraudScore(
                    anonymous_proxy=True,
                    bin_match="NA",
                    carder_email=True,
                    country_code="country_code_example",
                    country_match=True,
                    customer_phone_in_billing_location="customer_phone_in_billing_location_example",
                    distance_km=1,
                    free_email=True,
                    high_risk_country=True,
                    ip_city="ip_city_example",
                    ip_isp="ip_isp_example",
                    ip_latitude="ip_latitude_example",
                    ip_longitude="ip_longitude_example",
                    ip_org="ip_org_example",
                    ip_region="ip_region_example",
                    proxy_score=3.14,
                    score=3.14,
                    ship_forwarder=True,
                    spam_score=3.14,
                    transparent_proxy=True,
                ),
                gift=OrderGift(
                    gift=True,
                    gift_charge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_charge_accounting_code="gift_charge_accounting_code_example",
                    gift_charge_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_email="gift_email_example",
                    gift_message="gift_message_example",
                    gift_wrap_accounting_code="gift_wrap_accounting_code_example",
                    gift_wrap_cost=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_wrap_title="gift_wrap_title_example",
                ),
                gift_certificate=OrderGiftCertificate(
                    gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    gift_certificate_code="gift_certificate_code_example",
                    gift_certificate_oid=1,
                ),
                internal=OrderInternal(
                    exported_to_accounting=True,
                    merchant_notes="merchant_notes_example",
                    placed_by_user="placed_by_user_example",
                    refund_by_user="refund_by_user_example",
                    sales_rep_code="sales_rep_code_example",
                    transactional_merchant_notes=[
                        OrderTransactionalMerchantNote(
                            ip_address="ip_address_example",
                            note="note_example",
                            note_dts="note_dts_example",
                            user="user_example",
                        ),
                    ],
                ),
                items=[
                    OrderItem(
                        accounting_code="accounting_code_example",
                        activation_codes=[
                            "activation_codes_example",
                        ],
                        arbitrary_unit_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        auto_order_last_rebill_dts="auto_order_last_rebill_dts_example",
                        auto_order_schedule="auto_order_schedule_example",
                        barcode="barcode_example",
                        barcode_gtin12="barcode_gtin12_example",
                        barcode_gtin14="barcode_gtin14_example",
                        barcode_upc11="barcode_upc11_example",
                        barcode_upc12="barcode_upc12_example",
                        channel_partner_item_id="channel_partner_item_id_example",
                        cogs=3.14,
                        component_unit_value=3.14,
                        cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        country_code_of_origin="country_code_of_origin_example",
                        customs_description="customs_description_example",
                        description="description_example",
                        discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        discount_quantity=3.14,
                        discount_shipping_weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        distribution_center_code="distribution_center_code_example",
                        edi=OrderItemEdi(
                            identifications=[
                                OrderItemEdiIdentification(
                                    identification="identification_example",
                                    quantity=1,
                                ),
                            ],
                            lots=[
                                OrderItemEdiLot(
                                    lot_expiration="lot_expiration_example",
                                    lot_number="lot_number_example",
                                    lot_quantity=1,
                                ),
                            ],
                        ),
                        exclude_coupon=True,
                        free_shipping=True,
                        hazmat=True,
                        height=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        item_index=1,
                        item_reference_oid=1,
                        kit=True,
                        kit_component=True,
                        length=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                        manufacturer_sku="manufacturer_sku_example",
                        max_days_time_in_transit=1,
                        merchant_item_id="merchant_item_id_example",
                        mix_and_match_group_name="mix_and_match_group_name_example",
                        mix_and_match_group_oid=1,
                        no_shipping_discount=True,
                        options=[
                            OrderItemOption(
                                additional_dimension_application="none",
                                cost_change=Currency(
                                    currency_code="currency_code_example",
                                    exchange_rate=3.14,
                                    localized=3.14,
                                    localized_formatted="localized_formatted_example",
                                    value=3.14,
                                ),
                                file_attachment=OrderItemOptionFileAttachment(
                                    expiration_dts="expiration_dts_example",
                                    file_name="file_name_example",
                                    mime_type="mime_type_example",
                                    size=1,
                                ),
                                height=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                hidden=True,
                                label="label_example",
                                length=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                                one_time_fee=True,
                                value="value_example",
                                weight_change=Weight(
                                    uom="KG",
                                    value=3.14,
                                ),
                                width=Distance(
                                    uom="IN",
                                    value=3.14,
                                ),
                            ),
                        ],
                        packed_by_user="packed_by_user_example",
                        parent_item_index=1,
                        parent_merchant_item_id="parent_merchant_item_id_example",
                        perishable_class="perishable_class_example",
                        pricing_tier_name="pricing_tier_name_example",
                        properties=[
                            OrderItemProperty(
                                display=True,
                                expiration_dts="expiration_dts_example",
                                name="name_example",
                                value="value_example",
                            ),
                        ],
                        quantity=3.14,
                        quantity_refunded=3.14,
                        quickbooks_class="quickbooks_class_example",
                        refund_reason="refund_reason_example",
                        return_reason="return_reason_example",
                        ship_separately=True,
                        shipped_by_user="shipped_by_user_example",
                        shipped_dts="shipped_dts_example",
                        shipping_status="shipping_status_example",
                        special_product_type="special_product_type_example",
                        tags=[
                            OrderItemTag(
                                tag_value="tag_value_example",
                            ),
                        ],
                        tax_free=True,
                        tax_product_type="",
                        taxable_cost=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        total_refunded=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        transmitted_to_distribution_center_dts="transmitted_to_distribution_center_dts_example",
                        unit_cost_with_discount=Currency(
                            currency_code="currency_code_example",
                            exchange_rate=3.14,
                            localized=3.14,
                            localized_formatted="localized_formatted_example",
                            value=3.14,
                        ),
                        upsell=True,
                        weight=Weight(
                            uom="KG",
                            value=3.14,
                        ),
                        width=Distance(
                            uom="IN",
                            value=3.14,
                        ),
                    ),
                ],
                language_iso_code="language_iso_code_example",
                linked_shipment=OrderLinkedShipment(
                    has_linked_shipment=True,
                    linked_shipment=True,
                    linked_shipment_channel_partner_order_ids=[
                        "linked_shipment_channel_partner_order_ids_example",
                    ],
                    linked_shipment_order_ids=[
                        "linked_shipment_order_ids_example",
                    ],
                    linked_shipment_to_order_id="linked_shipment_to_order_id_example",
                ),
                marketing=OrderMarketing(
                    advertising_source="advertising_source_example",
                    cell_phone_opt_in=True,
                    mailing_list=True,
                    referral_code="referral_code_example",
                ),
                merchant_id="merchant_id_example",
                order_id="order_id_example",
                payment=OrderPayment(
                    check=OrderPaymentCheck(
                        check_number="check_number_example",
                    ),
                    credit_card=OrderPaymentCreditCard(
                        card_auth_ticket="card_auth_ticket_example",
                        card_authorization_amount=3.14,
                        card_authorization_dts="card_authorization_dts_example",
                        card_authorization_reference_number="card_authorization_reference_number_example",
                        card_expiration_month=1,
                        card_expiration_year=1,
                        card_number="card_number_example",
                        card_number_token="card_number_token_example",
                        card_number_truncated=True,
                        card_type="AMEX",
                        card_verification_number_token="card_verification_number_token_example",
                        dual_vaulted=OrderPaymentCreditCardDualVaulted(
                            gateway_name="gateway_name_example",
                            properties=[
                                OrderPaymentCreditCardDualVaultedProperty(
                                    name="name_example",
                                    value="value_example",
                                ),
                            ],
                            rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                        ),
                    ),
                    echeck=OrderPaymentECheck(
                        bank_aba_code="bank_aba_code_example",
                        bank_account_name="bank_account_name_example",
                        bank_account_number="bank_account_number_example",
                        bank_account_type="Checking",
                        bank_name="bank_name_example",
                        bank_owner_type="Personal",
                        customer_tax_id="customer_tax_id_example",
                        drivers_license_dob="drivers_license_dob_example",
                        drivers_license_number="drivers_license_number_example",
                        drivers_license_state="drivers_license_state_example",
                    ),
                    health_benefit_card=OrderPaymentHealthBenefitCard(
                        health_benefit_card_expiration_month=1,
                        health_benefit_card_expiration_year=1,
                        health_benefit_card_number="health_benefit_card_number_example",
                        health_benefit_card_number_token="health_benefit_card_number_token_example",
                        health_benefit_card_number_truncated=True,
                        health_benefit_card_verification_number_token="health_benefit_card_verification_number_token_example",
                    ),
                    hold_for_fraud_review=True,
                    insurance=OrderPaymentInsurance(
                        application_id="application_id_example",
                        claim_id="claim_id_example",
                        insurance_type="insurance_type_example",
                        refund_claim_id="refund_claim_id_example",
                    ),
                    payment_dts="payment_dts_example",
                    payment_method="Affirm",
                    payment_method_accounting_code="payment_method_accounting_code_example",
                    payment_method_deposit_to_account="payment_method_deposit_to_account_example",
                    payment_status="Unprocessed",
                    purchase_order=OrderPaymentPurchaseOrder(
                        purchase_order_number="purchase_order_number_example",
                    ),
                    rotating_transaction_gateway_code="rotating_transaction_gateway_code_example",
                    surcharge=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    surcharge_accounting_code="surcharge_accounting_code_example",
                    surcharge_transaction_fee=3.14,
                    surcharge_transaction_percentage=3.14,
                    test_order=True,
                    transactions=[
                        OrderPaymentTransaction(
                            details=[
                                OrderPaymentTransactionDetail(
                                    name="name_example",
                                    type="type_example",
                                    value="value_example",
                                ),
                            ],
                            successful=True,
                            transaction_gateway="transaction_gateway_example",
                            transaction_id=1,
                            transaction_timestamp="transaction_timestamp_example",
                        ),
                    ],
                ),
                point_of_sale=OrderPointOfSale(
                    location=PointOfSaleLocation(
                        adddress2="adddress2_example",
                        address1="address1_example",
                        city="city_example",
                        country="country_example",
                        distribution_center_code="distribution_center_code_example",
                        external_id="external_id_example",
                        merchant_id="merchant_id_example",
                        pos_location_oid=1,
                        postal_code="postal_code_example",
                        state_province="state_province_example",
                    ),
                    reader=PointOfSaleReader(
                        device_type="device_type_example",
                        label="label_example",
                        merchant_id="merchant_id_example",
                        payment_provider="stripe",
                        pos_reader_id=1,
                        pos_register_oid=1,
                        serial_number="serial_number_example",
                        stripe_account_id="stripe_account_id_example",
                        stripe_reader_id="stripe_reader_id_example",
                    ),
                    register=PointOfSaleRegister(
                        merchant_id="merchant_id_example",
                        name="name_example",
                        pos_location_oid=1,
                        pos_register_oid=1,
                    ),
                ),
                properties=[
                    OrderProperty(
                        display=True,
                        expiration_dts="expiration_dts_example",
                        name="name_example",
                        value="value_example",
                    ),
                ],
                quote=OrderQuote(
                    quote_expiration_dts="quote_expiration_dts_example",
                    quoted_by="quoted_by_example",
                    quoted_dts="quoted_dts_example",
                ),
                refund_dts="refund_dts_example",
                refund_reason="refund_reason_example",
                reject_dts="reject_dts_example",
                reject_reason="reject_reason_example",
                salesforce=OrderSalesforce(
                    salesforce_opportunity_id="salesforce_opportunity_id_example",
                ),
                shipping=OrderShipping(
                    address1="address1_example",
                    address2="address2_example",
                    city="city_example",
                    company="company_example",
                    country_code="country_code_example",
                    day_phone="day_phone_example",
                    day_phone_e164="day_phone_e164_example",
                    delivery_date="delivery_date_example",
                    evening_phone="evening_phone_example",
                    evening_phone_e164="evening_phone_e164_example",
                    first_name="first_name_example",
                    last_name="last_name_example",
                    least_cost_route=True,
                    least_cost_route_shipping_methods=[
                        "least_cost_route_shipping_methods_example",
                    ],
                    lift_gate=True,
                    pickup_dts="pickup_dts_example",
                    postal_code="postal_code_example",
                    rma="rma_example",
                    ship_on_date="ship_on_date_example",
                    ship_to_residential=True,
                    shipping_3rd_party_account_number="shipping_3rd_party_account_number_example",
                    shipping_date="shipping_date_example",
                    shipping_department_status="shipping_department_status_example",
                    shipping_method="shipping_method_example",
                    shipping_method_accounting_code="shipping_method_accounting_code_example",
                    special_instructions="special_instructions_example",
                    state_region="state_region_example",
                    title="title_example",
                    tracking_number_details=[
                        OrderTrackingNumberDetails(
                            actual_delivery_date="actual_delivery_date_example",
                            actual_delivery_date_formatted="actual_delivery_date_formatted_example",
                            details=[
                                OrderTrackingNumberDetail(
                                    city="city_example",
                                    event_dts="event_dts_example",
                                    event_local_date="event_local_date_example",
                                    event_local_time="event_local_time_example",
                                    event_timezone_id="event_timezone_id_example",
                                    state="state_example",
                                    subtag="subtag_example",
                                    subtag_message="subtag_message_example",
                                    tag="tag_example",
                                    tag_description="tag_description_example",
                                    tag_icon="tag_icon_example",
                                    zip="zip_example",
                                ),
                            ],
                            easypost_tracker_id="easypost_tracker_id_example",
                            expected_delivery_date="expected_delivery_date_example",
                            expected_delivery_date_formatted="expected_delivery_date_formatted_example",
                            map_url="map_url_example",
                            order_placed_date="order_placed_date_example",
                            order_placed_date_formatted="order_placed_date_formatted_example",
                            payment_processed_date="payment_processed_date_example",
                            payment_processed_date_formatted="payment_processed_date_formatted_example",
                            shipped_date="shipped_date_example",
                            shipped_date_formatted="shipped_date_formatted_example",
                            shipping_method="shipping_method_example",
                            status="status_example",
                            status_description="status_description_example",
                            tracking_number="tracking_number_example",
                            tracking_url="tracking_url_example",
                        ),
                    ],
                    tracking_numbers=[
                        "tracking_numbers_example",
                    ],
                    weight=Weight(
                        uom="KG",
                        value=3.14,
                    ),
                ),
                summary=OrderSummary(
                    actual_fulfillment=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_payment_processing=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    actual_shipping=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    arbitrary_shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    health_benefit_card_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_amount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    internal_gift_certificate_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    other_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    shipping_handling_total_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_discount_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    subtotal_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    tax_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    taxable_subtotal_discount=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                    total_refunded=Currency(
                        currency_code="currency_code_example",
                        exchange_rate=3.14,
                        localized=3.14,
                        localized_formatted="localized_formatted_example",
                        value=3.14,
                    ),
                ),
                tags=[
                    OrderTag(
                        tag_value="tag_value_example",
                    ),
                ],
                taxes=OrderTaxes(
                    arbitrary_tax=3.14,
                    arbitrary_tax_rate=3.14,
                    arbitrary_taxable_subtotal=3.14,
                    tax_city_accounting_code="tax_city_accounting_code_example",
                    tax_country_accounting_code="tax_country_accounting_code_example",
                    tax_county="tax_county_example",
                    tax_county_accounting_code="tax_county_accounting_code_example",
                    tax_gift_charge=True,
                    tax_postal_code_accounting_code="tax_postal_code_accounting_code_example",
                    tax_rate=3.14,
                    tax_rate_city=3.14,
                    tax_rate_country=3.14,
                    tax_rate_county=3.14,
                    tax_rate_postal_code=3.14,
                    tax_rate_state=3.14,
                    tax_shipping=True,
                    tax_state_accounting_code="tax_state_accounting_code_example",
                ),
                utms=[
                    OrderUtm(
                        attribution_first_click_subtotal=3.14,
                        attribution_first_click_total=3.14,
                        attribution_last_click_subtotal=3.14,
                        attribution_last_click_total=3.14,
                        attribution_linear_subtotal=3.14,
                        attribution_linear_total=3.14,
                        attribution_position_based_subtotal=3.14,
                        attribution_position_based_total=3.14,
                        click_dts="click_dts_example",
                        facebook_ad_id="facebook_ad_id_example",
                        fbclid="fbclid_example",
                        gbraid="gbraid_example",
                        glcid="glcid_example",
                        itm_campaign="itm_campaign_example",
                        itm_content="itm_content_example",
                        itm_id="itm_id_example",
                        itm_medium="itm_medium_example",
                        itm_source="itm_source_example",
                        itm_term="itm_term_example",
                        msclkid="msclkid_example",
                        ttclid="ttclid_example",
                        uc_message_id="uc_message_id_example",
                        utm_campaign="utm_campaign_example",
                        utm_content="utm_content_example",
                        utm_id="utm_id_example",
                        utm_medium="utm_medium_example",
                        utm_source="utm_source_example",
                        utm_term="utm_term_example",
                        vmcid="vmcid_example",
                        wbraid="wbraid_example",
                    ),
                ],
            ),
        ],
        quotes_summary=CustomerQuotesSummary(
            first_quote_dts="first_quote_dts_example",
            last_quote_dts="last_quote_dts_example",
            quote_count=1,
            total=3.14,
        ),
        referral_source="referral_source_example",
        reviewer=CustomerReviewer(
            auto_approve=True,
            average_overall_rating=3.14,
            expert=True,
            first_review="first_review_example",
            last_review="last_review_example",
            location="location_example",
            nickname="nickname_example",
            number_helpful_review_votes=1,
            rank=1,
            reviews_contributed=1,
        ),
        sales_rep_code="sales_rep_code_example",
        send_signup_notification=True,
        shipping=[
            CustomerShipping(
                address1="address1_example",
                address2="address2_example",
                city="city_example",
                company="company_example",
                country_code="country_code_example",
                customer_profile_oid=1,
                customer_shipping_oid=1,
                day_phone="day_phone_example",
                default_shipping=True,
                evening_phone="evening_phone_example",
                first_name="first_name_example",
                last_name="last_name_example",
                last_used_dts="last_used_dts_example",
                postal_code="postal_code_example",
                state_region="state_region_example",
                tax_county="tax_county_example",
                title="title_example",
            ),
        ],
        signup_dts="signup_dts_example",
        software_entitlements=[
            CustomerSoftwareEntitlement(
                activation_code="activation_code_example",
                activation_dts="activation_dts_example",
                customer_software_entitlement_oid=1,
                expiration_dts="expiration_dts_example",
                purchased_via_item_description="purchased_via_item_description_example",
                purchased_via_item_id="purchased_via_item_id_example",
                purchased_via_order_id="purchased_via_order_id_example",
                software_sku="software_sku_example",
            ),
        ],
        suppress_buysafe=True,
        tags=[
            CustomerTag(
                tag_value="tag_value_example",
            ),
        ],
        tax_codes=CustomerTaxCodes(
            avalara_customer_code="avalara_customer_code_example",
            avalara_entity_use_code="avalara_entity_use_code_example",
            sovos_customer_code="sovos_customer_code_example",
            taxjar_customer_id="taxjar_customer_id_example",
            taxjar_exemption_type="taxjar_exemption_type_example",
        ),
        tax_exempt=True,
        tax_id="tax_id_example",
        terms="terms_example",
        track_separately=True,
        unapproved=True,
        ups_account_number="ups_account_number_example",
        website_url="website_url_example",
    ) # Customer | Customer to update
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a customer
        api_response = api_instance.update_customer(customer_profile_oid, customer)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->update_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a customer
        api_response = api_instance.update_customer(customer_profile_oid, customer, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->update_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid to update. |
 **customer** | [**Customer**](Customer.md)| Customer to update |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **update_customer_email_lists**
> CustomerEmailListChanges update_customer_email_lists(customer_profile_oid, list_changes)

Update email list subscriptions for a customer

Update email list subscriptions for a customer 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.customer_email_list_changes import CustomerEmailListChanges
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer profile oid
    list_changes = CustomerEmailListChanges(
        add_to_lists=[
            "add_to_lists_example",
        ],
        remove_from_lists=[
            "remove_from_lists_example",
        ],
    ) # CustomerEmailListChanges | List changes

    # example passing only required values which don't have defaults set
    try:
        # Update email list subscriptions for a customer
        api_response = api_instance.update_customer_email_lists(customer_profile_oid, list_changes)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->update_customer_email_lists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer profile oid |
 **list_changes** | [**CustomerEmailListChanges**](CustomerEmailListChanges.md)| List changes |

### Return type

[**CustomerEmailListChanges**](CustomerEmailListChanges.md)

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

# **update_wish_list_item**
> CustomerWishListItem update_wish_list_item(customer_profile_oid, customer_wishlist_item_oid, wishlist_item)

Update a customer wishlist item

Update a customer wishlist item 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.customer_wish_list_item import CustomerWishListItem
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    customer_profile_oid = 1 # int | The customer oid for this wishlist.
    customer_wishlist_item_oid = 1 # int | The wishlist oid for this wishlist item.
    wishlist_item = CustomerWishListItem(
        add_dts="add_dts_example",
        comments="comments_example",
        customer_profile_oid=1,
        customer_wishlist_item_oid=1,
        merchant_item_oid=1,
        position=1,
        priority=1,
    ) # CustomerWishListItem | Wishlist item to update

    # example passing only required values which don't have defaults set
    try:
        # Update a customer wishlist item
        api_response = api_instance.update_wish_list_item(customer_profile_oid, customer_wishlist_item_oid, wishlist_item)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->update_wish_list_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **customer_wishlist_item_oid** | **int**| The wishlist oid for this wishlist item. |
 **wishlist_item** | [**CustomerWishListItem**](CustomerWishListItem.md)| Wishlist item to update |

### Return type

[**CustomerWishListItem**](CustomerWishListItem.md)

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

# **validate_email_verification_token**
> EmailVerifyTokenValidateResponse validate_email_verification_token(validation_request)

Validate a token that can be used to verify a customer email address

Validate a token that can be used to verify a customer email address.  The implementation of how a customer interacts with this token is left to the merchant. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import customer_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_verify_token_validate_response import EmailVerifyTokenValidateResponse
from ultracart.model.email_verify_token_validate_request import EmailVerifyTokenValidateRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    validation_request = EmailVerifyTokenValidateRequest(
        token="token_example",
    ) # EmailVerifyTokenValidateRequest | Token validation request

    # example passing only required values which don't have defaults set
    try:
        # Validate a token that can be used to verify a customer email address
        api_response = api_instance.validate_email_verification_token(validation_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling CustomerApi->validate_email_verification_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_request** | [**EmailVerifyTokenValidateRequest**](EmailVerifyTokenValidateRequest.md)| Token validation request |

### Return type

[**EmailVerifyTokenValidateResponse**](EmailVerifyTokenValidateResponse.md)

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

