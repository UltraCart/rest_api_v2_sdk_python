# ultracart.IntegrationLogApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_integration_log**](IntegrationLogApi.md#get_integration_log) | **GET** /integration_log/query/{pk}/{sk} | Retrieve an integration log
[**get_integration_log_file**](IntegrationLogApi.md#get_integration_log_file) | **GET** /integration_log/query/{pk}/{sk}/{uuid} | Retrieve an integration log file
[**get_integration_log_file_pdf**](IntegrationLogApi.md#get_integration_log_file_pdf) | **GET** /integration_log/query/{pk}/{sk}/{uuid}/pdf | Retrieve an integration log file converted to PDF
[**get_integration_log_summaries_query**](IntegrationLogApi.md#get_integration_log_summaries_query) | **POST** /integration_log/summary/query | Retrieve integration log summaries
[**get_integration_logs_query**](IntegrationLogApi.md#get_integration_logs_query) | **POST** /integration_log/query | Retrieve integration logs


# **get_integration_log**
> IntegrationLogResponse get_integration_log(pk, sk)

Retrieve an integration log

Retrieve an integration logs from the account based identifiers 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import integration_log_api
from ultracart.model.integration_log_response import IntegrationLogResponse
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
    api_instance = integration_log_api.IntegrationLogApi(api_client)
    pk = "pk_example" # str | 
    sk = "sk_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an integration log
        api_response = api_instance.get_integration_log(pk, sk)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling IntegrationLogApi->get_integration_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  |
 **sk** | **str**|  |

### Return type

[**IntegrationLogResponse**](IntegrationLogResponse.md)

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

# **get_integration_log_file**
> file_type get_integration_log_file(pk, sk, uuid)

Retrieve an integration log file

Retrieve an integration log file from the account based identifiers 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import integration_log_api
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
    api_instance = integration_log_api.IntegrationLogApi(api_client)
    pk = "pk_example" # str | 
    sk = "sk_example" # str | 
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an integration log file
        api_response = api_instance.get_integration_log_file(pk, sk, uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling IntegrationLogApi->get_integration_log_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  |
 **sk** | **str**|  |
 **uuid** | **str**|  |

### Return type

**file_type**

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


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

# **get_integration_log_file_pdf**
> file_type get_integration_log_file_pdf(pk, sk, uuid)

Retrieve an integration log file converted to PDF

Retrieve an integration log file from the account based identifiers 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import integration_log_api
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
    api_instance = integration_log_api.IntegrationLogApi(api_client)
    pk = "pk_example" # str | 
    sk = "sk_example" # str | 
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an integration log file converted to PDF
        api_response = api_instance.get_integration_log_file_pdf(pk, sk, uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling IntegrationLogApi->get_integration_log_file_pdf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  |
 **sk** | **str**|  |
 **uuid** | **str**|  |

### Return type

**file_type**

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


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

# **get_integration_log_summaries_query**
> IntegrationLogSummaryQueryResponse get_integration_log_summaries_query(integration_log_summaries_query)

Retrieve integration log summaries

Retrieves a set of integration log summaries from the account based on a query object. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import integration_log_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.integration_log_summary_query_request import IntegrationLogSummaryQueryRequest
from ultracart.model.integration_log_summary_query_response import IntegrationLogSummaryQueryResponse
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
    api_instance = integration_log_api.IntegrationLogApi(api_client)
    integration_log_summaries_query = IntegrationLogSummaryQueryRequest(
        log_dts_begin="log_dts_begin_example",
        log_dts_end="log_dts_end_example",
    ) # IntegrationLogSummaryQueryRequest | Integration log summaries query

    # example passing only required values which don't have defaults set
    try:
        # Retrieve integration log summaries
        api_response = api_instance.get_integration_log_summaries_query(integration_log_summaries_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling IntegrationLogApi->get_integration_log_summaries_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_log_summaries_query** | [**IntegrationLogSummaryQueryRequest**](IntegrationLogSummaryQueryRequest.md)| Integration log summaries query |

### Return type

[**IntegrationLogSummaryQueryResponse**](IntegrationLogSummaryQueryResponse.md)

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

# **get_integration_logs_query**
> IntegrationLogQueryResponse get_integration_logs_query(integration_log_query)

Retrieve integration logs

Retrieves a set of integration logs from the account based on a query object. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import integration_log_api
from ultracart.model.integration_log_query_request import IntegrationLogQueryRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.integration_log_query_response import IntegrationLogQueryResponse
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
    api_instance = integration_log_api.IntegrationLogApi(api_client)
    integration_log_query = IntegrationLogQueryRequest(
        action="action_example",
        direction="direction_example",
        email="email_example",
        file_names=[
            "file_names_example",
        ],
        item_id="item_id_example",
        item_ipn_oid=1,
        log_dts_begin="log_dts_begin_example",
        log_dts_end="log_dts_end_example",
        log_type="log_type_example",
        logger_id="logger_id_example",
        logger_name="logger_name_example",
        order_ids=[
            "order_ids_example",
        ],
        status="status_example",
    ) # IntegrationLogQueryRequest | Integration log query
    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve integration logs
        api_response = api_instance.get_integration_logs_query(integration_log_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling IntegrationLogApi->get_integration_logs_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve integration logs
        api_response = api_instance.get_integration_logs_query(integration_log_query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling IntegrationLogApi->get_integration_logs_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_log_query** | [**IntegrationLogQueryRequest**](IntegrationLogQueryRequest.md)| Integration log query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**IntegrationLogQueryResponse**](IntegrationLogQueryResponse.md)

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

