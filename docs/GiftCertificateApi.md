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
#  add a gift certificate ledger entry.  this is how you affect the remaining balance.
from ultracart.apis import GiftCertificateApi
from ultracart.model.gift_certificate_ledger_entry import GiftCertificateLedgerEntry
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client
from datetime import datetime

api_instance = GiftCertificateApi(api_client())

try:

    amount = -65.35  # this is the change in the gc.  this is not a balance.  it will be subtracted from it.
    description = "Customer bought something."
    entry_dts = datetime.now().astimezone().isoformat('T', 'milliseconds')
    gift_certificate_oid = 676713  # this is an existing gift certificate oid.  I created it using create_gift_certificate.py
    reference_order_id = 'BLAH-12345'  # if this ledger entry is related to an order, add it here, else use null.
    ledger_entry = GiftCertificateLedgerEntry(amount=amount,
                                              description=description,
                                              entry_dts=entry_dts,
                                              gift_certificate_oid=gift_certificate_oid,
                                              reference_order_id=reference_order_id)

    # create does not take an expansion variable.  it will return the entire object by default.
    gc_response = api_instance.add_gift_certificate_ledger_entry(gift_certificate_oid, ledger_entry)
    gift_certificate = gc_response.gift_certificate

    pprint(gift_certificate)

except ApiException as e:
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
# create a gift certificate
from ultracart.apis import GiftCertificateApi
from ultracart.model.gift_certificate_create_request import GiftCertificateCreateRequest
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client
from datetime import datetime, timedelta

api_instance = GiftCertificateApi(api_client())

try:

    amount = 150.75
    expiration_dts = datetime.now() + timedelta(days=180)
    expiration_dts_iso8601 = expiration_dts.astimezone().isoformat('T', 'milliseconds')
    initial_ledger_description = "Issued instead of refund"
    merchant_note = 'Problem Order: blah-12345\nIssued gift certificate due to stale product.' \
                    '\nIssued By: Customer Service Rep Joe Smith'
    email = 'support@ultracart.com'
    gc_create_request = GiftCertificateCreateRequest(amount=amount,
                                                     email=email,
                                                     expiration_dts_iso8601=expiration_dts_iso8601,
                                                     initial_ledger_description=initial_ledger_description,
                                                     merchant_note=merchant_note)

    # create does not take an expansion variable.  it will return the entire object by default.
    gc_response = api_instance.create_gift_certificate(gc_create_request)
    gift_certificate = gc_response.gift_certificate

    pprint(gift_certificate)

except ApiException as e:
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
# delete a gift certificate

from ultracart.apis import GiftCertificateApi
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client

api_instance = GiftCertificateApi(api_client())

try:

    gift_certificate_oid = 676777

    # by_code does not take an expansion variable.  it will return the entire object by default.
    api_instance.delete_gift_certificate(gift_certificate_oid)

    # if I query the gift certificate now, it will still return to me, but the deleted property will be True
    gc_response = api_instance.get_gift_certificate_by_oid(gift_certificate_oid)
    gift_certificate = gc_response.gift_certificate

    pprint(gift_certificate)

except ApiException as e:
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
# get a gift certificate by code.

from ultracart.apis import GiftCertificateApi
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client

api_instance = GiftCertificateApi(api_client())

try:

    code = 'NRQPHPCFVK'

    # by_code does not take an expansion variable.  it will return the entire object by default.
    gc_response = api_instance.get_gift_certificate_by_code(code)
    gift_certificate = gc_response.gift_certificate

    pprint(gift_certificate)

except ApiException as e:
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
# get a gift certificate by gift_certificate_oid.

from ultracart.apis import GiftCertificateApi
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client


api_instance = GiftCertificateApi(api_client())

try:

    gift_certificate_oid = 676713

    # by_oid does not take an expansion variable.  it will return the entire object by default.
    gc_response = api_instance.get_gift_certificate_by_oid(gift_certificate_oid)
    gift_certificate = gc_response.gift_certificate

    pprint(gift_certificate)

except ApiException as e:
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
# get a gift certificate by gift_certificate_oid.

from ultracart.apis import GiftCertificateApi
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client

api_instance = GiftCertificateApi(api_client())

try:

    email = "support@ultracart.com"

    # by_email does not take an expansion variable.  it will return the entire object by default.
    gc_response = api_instance.get_gift_certificates_by_email(email)
    gift_certificates = gc_response.gift_certificates

    pprint(gift_certificates)

except ApiException as e:
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
# retrieve all items using chunking if necessary

from ultracart.apis import GiftCertificateApi
from ultracart.model.gift_certificate_query import GiftCertificateQuery
from ultracart.rest import ApiException
from samples import api_client
import time

api_instance = GiftCertificateApi(api_client())

expand = 'ledger'


def get_gift_certificates_chunk(_offset=0, _limit=200):
    gc_query = GiftCertificateQuery()
    gc_response = api_instance.get_gift_certificates_by_query(gc_query, offset=_offset, limit=_limit, expand=expand)
    if gc_response.success:
        return gc_response.gift_certificates
    # if unsuccessful, return empty array
    return []


gift_certificates = []
try:

    iteration = 1
    offset = 0
    limit = 200
    need_more_records = True

    while need_more_records:
        print("executing iteration " + str(iteration))
        block_of_certs = get_gift_certificates_chunk(offset, limit)
        gift_certificates.extend(block_of_certs)
        offset = offset + limit
        need_more_records = len(block_of_certs) == limit
        iteration = iteration + 1
        time.sleep(3)  # pace your calls or the rate limiter was slam down on your script.

    # pprint(gift_certificates)
    rec_num = 1
    for gc in gift_certificates:
        print(rec_num, ") oid: ", gc.gift_certificate_oid, ", code: ", gc.code)
        rec_num = rec_num + 1

except ApiException as e:
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
# update a gift certificate

from ultracart.apis import GiftCertificateApi
from ultracart.rest import ApiException
from pprint import pprint
from samples import api_client

api_instance = GiftCertificateApi(api_client())

try:

    gift_certificate_oid = 676713

    # by_oid does not take an expansion variable.  it will return the entire object by default.
    gc_response = api_instance.get_gift_certificate_by_oid(gift_certificate_oid)
    gift_certificate = gc_response.gift_certificate

    gift_certificate.email = 'support@ultracart.com'

    gc_response = api_instance.update_gift_certificate(gift_certificate_oid, gift_certificate)
    gift_certificate = gc_response.gift_certificate

    pprint(gift_certificate)

except ApiException as e:
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

