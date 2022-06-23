# ultracart.GiftCertificateApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_gift_certificate_ledger_entry**](GiftCertificateApi.md#add_gift_certificate_ledger_entry) | **POST** /gift_certificate/gift_certificates/{gift_certificate_oid}/ledger_entry | Add a gift certificate ledger entry
[**create_gift_certificate**](GiftCertificateApi.md#create_gift_certificate) | **POST** /gift_certificate/gift_certificates | Create a gift certificate
[**delete_gift_certificate**](GiftCertificateApi.md#delete_gift_certificate) | **DELETE** /gift_certificate/gift_certificates/{gift_certificate_oid} | Delete a gift certificate
[**get_gift_certificate_by_code**](GiftCertificateApi.md#get_gift_certificate_by_code) | **POST** /gift_certificate/gift_certificates/by_code/{code} | Retrieve gift certificate by code
[**get_gift_certificate_by_oid**](GiftCertificateApi.md#get_gift_certificate_by_oid) | **POST** /gift_certificate/gift_certificates/{gift_certificate_oid} | Retrieve gift certificate by oid
[**get_gift_certificates_by_email**](GiftCertificateApi.md#get_gift_certificates_by_email) | **POST** /gift_certificate/gift_certificates/by_email/{email} | Retrieve gift certificate by email
[**get_gift_certificates_by_query**](GiftCertificateApi.md#get_gift_certificates_by_query) | **POST** /gift_certificate/gift_certificates/query | Retrieve gift certificates by query
[**update_gift_certificate**](GiftCertificateApi.md#update_gift_certificate) | **PUT** /gift_certificate/gift_certificates/{gift_certificate_oid} | Update a gift certificate


# **add_gift_certificate_ledger_entry**
> GiftCertificateResponse add_gift_certificate_ledger_entry(gift_certificate_oid, gift_certificate_ledger_entry)

Add a gift certificate ledger entry

Adds a ledger entry for this gift certificate. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.gift_certificate_response import GiftCertificateResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.gift_certificate_ledger_entry import GiftCertificateLedgerEntry
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    gift_certificate_oid = 1 # int | 
    gift_certificate_ledger_entry = GiftCertificateLedgerEntry(
        amount=3.14,
        description="description_example",
        entry_dts="entry_dts_example",
        gift_certificate_ledger_oid=1,
        gift_certificate_oid=1,
        reference_order_id="reference_order_id_example",
    ) # GiftCertificateLedgerEntry | Gift certificate ledger entry

    # example passing only required values which don't have defaults set
    try:
        # Add a gift certificate ledger entry
        api_response = api_instance.add_gift_certificate_ledger_entry(gift_certificate_oid, gift_certificate_ledger_entry)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->add_gift_certificate_ledger_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_certificate_oid** | **int**|  |
 **gift_certificate_ledger_entry** | [**GiftCertificateLedgerEntry**](GiftCertificateLedgerEntry.md)| Gift certificate ledger entry |

### Return type

[**GiftCertificateResponse**](GiftCertificateResponse.md)

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

# **create_gift_certificate**
> GiftCertificateResponse create_gift_certificate(gift_certificate_create_request)

Create a gift certificate

Creates a gift certificate for this merchant account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.gift_certificate_response import GiftCertificateResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.gift_certificate_create_request import GiftCertificateCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    gift_certificate_create_request = GiftCertificateCreateRequest(
        amount=3.14,
        email="email_example",
        expiration_dts="expiration_dts_example",
        initial_ledger_description="initial_ledger_description_example",
        merchant_note="merchant_note_example",
    ) # GiftCertificateCreateRequest | Gift certificate create request

    # example passing only required values which don't have defaults set
    try:
        # Create a gift certificate
        api_response = api_instance.create_gift_certificate(gift_certificate_create_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->create_gift_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_certificate_create_request** | [**GiftCertificateCreateRequest**](GiftCertificateCreateRequest.md)| Gift certificate create request |

### Return type

[**GiftCertificateResponse**](GiftCertificateResponse.md)

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

# **delete_gift_certificate**
> delete_gift_certificate(gift_certificate_oid)

Delete a gift certificate

Deletes a gift certificate for this merchant account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    gift_certificate_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a gift certificate
        api_instance.delete_gift_certificate(gift_certificate_oid)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->delete_gift_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_certificate_oid** | **int**|  |

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

# **get_gift_certificate_by_code**
> GiftCertificateResponse get_gift_certificate_by_code(code)

Retrieve gift certificate by code

Retrieves a gift certificate from the account based on the code (the value the customer enters at checkout time). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.gift_certificate_response import GiftCertificateResponse
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    code = "code_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve gift certificate by code
        api_response = api_instance.get_gift_certificate_by_code(code)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->get_gift_certificate_by_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  |

### Return type

[**GiftCertificateResponse**](GiftCertificateResponse.md)

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

# **get_gift_certificate_by_oid**
> GiftCertificateResponse get_gift_certificate_by_oid(gift_certificate_oid)

Retrieve gift certificate by oid

Retrieves a gift certificate from the account based on the internal primary key. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.gift_certificate_response import GiftCertificateResponse
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    gift_certificate_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve gift certificate by oid
        api_response = api_instance.get_gift_certificate_by_oid(gift_certificate_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->get_gift_certificate_by_oid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_certificate_oid** | **int**|  |

### Return type

[**GiftCertificateResponse**](GiftCertificateResponse.md)

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

# **get_gift_certificates_by_email**
> GiftCertificatesResponse get_gift_certificates_by_email(email)

Retrieve gift certificate by email

Retrieves all gift certificates from the account based on customer email. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.gift_certificates_response import GiftCertificatesResponse
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    email = "email_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve gift certificate by email
        api_response = api_instance.get_gift_certificates_by_email(email)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->get_gift_certificates_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  |

### Return type

[**GiftCertificatesResponse**](GiftCertificatesResponse.md)

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

# **get_gift_certificates_by_query**
> GiftCertificatesResponse get_gift_certificates_by_query(gift_certificate_query)

Retrieve gift certificates by query

Retrieves gift certificates from the account.  If no parameters are specified, all gift certificates will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.gift_certificate_query import GiftCertificateQuery
from ultracart.model.gift_certificates_response import GiftCertificatesResponse
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    gift_certificate_query = GiftCertificateQuery(
        code="code_example",
        email="email_example",
        expiration_dts_end="expiration_dts_end_example",
        expiration_dts_start="expiration_dts_start_example",
        original_balance_end=3.14,
        original_balance_start=3.14,
        reference_order_id="reference_order_id_example",
        remaining_balance_end=3.14,
        remaining_balance_start=3.14,
    ) # GiftCertificateQuery | Gift certificates query
    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    since = "_since_example" # str | Fetch customers that have been created/modified since this date/time. (optional)
    sort = "_sort_example" # str | The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve gift certificates by query
        api_response = api_instance.get_gift_certificates_by_query(gift_certificate_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->get_gift_certificates_by_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve gift certificates by query
        api_response = api_instance.get_gift_certificates_by_query(gift_certificate_query, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->get_gift_certificates_by_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_certificate_query** | [**GiftCertificateQuery**](GiftCertificateQuery.md)| Gift certificates query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**GiftCertificatesResponse**](GiftCertificatesResponse.md)

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

# **update_gift_certificate**
> GiftCertificateResponse update_gift_certificate(gift_certificate_oid, gift_certificate)

Update a gift certificate

Update a gift certificate for this merchant account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import gift_certificate_api
from ultracart.model.gift_certificate import GiftCertificate
from ultracart.model.gift_certificate_response import GiftCertificateResponse
from ultracart.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://secure.ultracart.com/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: ultraCartOauth
configuration = ultracart.Configuration(
    host = "https://secure.ultracart.com/rest/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ultraCartSimpleApiKey
configuration.api_key['ultraCartSimpleApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ultraCartSimpleApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with ultracart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gift_certificate_api.GiftCertificateApi(api_client)
    gift_certificate_oid = 1 # int | 
    gift_certificate = GiftCertificate(
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
    ) # GiftCertificate | Gift certificate

    # example passing only required values which don't have defaults set
    try:
        # Update a gift certificate
        api_response = api_instance.update_gift_certificate(gift_certificate_oid, gift_certificate)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling GiftCertificateApi->update_gift_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_certificate_oid** | **int**|  |
 **gift_certificate** | [**GiftCertificate**](GiftCertificate.md)| Gift certificate |

### Return type

[**GiftCertificateResponse**](GiftCertificateResponse.md)

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

