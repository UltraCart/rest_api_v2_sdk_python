# ultracart.AffiliateApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clicks_by_query**](AffiliateApi.md#get_clicks_by_query) | **POST** /affiliate/clicks/query | Retrieve clicks
[**get_ledgers_by_query**](AffiliateApi.md#get_ledgers_by_query) | **POST** /affiliate/ledgers/query | Retrieve ledger entries


# **get_clicks_by_query**
> AffiliateClicksResponse get_clicks_by_query(click_query)

Retrieve clicks

Retrieves a group of clicks from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the clicks returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import affiliate_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.affiliate_clicks_response import AffiliateClicksResponse
from ultracart.model.affiliate_click_query import AffiliateClickQuery
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
    api_instance = affiliate_api.AffiliateApi(api_client)
    click_query = AffiliateClickQuery(
        affiliate_link_oid=1,
        affiliate_oid=1,
        click_dts_begin="click_dts_begin_example",
        click_dts_end="click_dts_end_example",
        ip_address="ip_address_example",
        sub_id="sub_id_example",
    ) # AffiliateClickQuery | Click query
    limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) if omitted the server will use the default value of 10000
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    expand = "_expand_example" # str | The object expansion to perform on the result.  Only option is link. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve clicks
        api_response = api_instance.get_clicks_by_query(click_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling AffiliateApi->get_clicks_by_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve clicks
        api_response = api_instance.get_clicks_by_query(click_query, limit=limit, offset=offset, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling AffiliateApi->get_clicks_by_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **click_query** | [**AffiliateClickQuery**](AffiliateClickQuery.md)| Click query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] if omitted the server will use the default value of 10000
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **expand** | **str**| The object expansion to perform on the result.  Only option is link. | [optional]

### Return type

[**AffiliateClicksResponse**](AffiliateClicksResponse.md)

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

# **get_ledgers_by_query**
> AffiliateLedgersResponse get_ledgers_by_query(ledger_query)

Retrieve ledger entries

Retrieves a group of ledger entries from the account based on a query object.  If no parameters are specified, the API call will fail with a bad request error.  Always specify some parameters to limit the scope of the ledgers returned to ones you are truly interested in.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import affiliate_api
from ultracart.model.affiliate_ledger_query import AffiliateLedgerQuery
from ultracart.model.affiliate_ledgers_response import AffiliateLedgersResponse
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
    api_instance = affiliate_api.AffiliateApi(api_client)
    ledger_query = AffiliateLedgerQuery(
        affiliate_oid=1,
        item_id="item_id_example",
        order_id="order_id_example",
        sub_id="sub_id_example",
        transaction_dts_begin="transaction_dts_begin_example",
        transaction_dts_end="transaction_dts_end_example",
    ) # AffiliateLedgerQuery | Ledger query
    limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    expand = "_expand_example" # str | The object expansion to perform on the result.  Only option is link. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve ledger entries
        api_response = api_instance.get_ledgers_by_query(ledger_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling AffiliateApi->get_ledgers_by_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve ledger entries
        api_response = api_instance.get_ledgers_by_query(ledger_query, limit=limit, offset=offset, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling AffiliateApi->get_ledgers_by_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_query** | [**AffiliateLedgerQuery**](AffiliateLedgerQuery.md)| Ledger query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **expand** | **str**| The object expansion to perform on the result.  Only option is link. | [optional]

### Return type

[**AffiliateLedgersResponse**](AffiliateLedgersResponse.md)

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

