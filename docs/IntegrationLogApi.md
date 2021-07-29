# ultracart.IntegrationLogApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_integration_log**](IntegrationLogApi.md#get_integration_log) | **GET** /integration_log/query/{pk}/{sk} | Retrieve an integration log
[**get_integration_log_file**](IntegrationLogApi.md#get_integration_log_file) | **GET** /integration_log/query/{pk}/{sk}/{uuid} | Retrieve an integration log file
[**get_integration_log_summaries_query**](IntegrationLogApi.md#get_integration_log_summaries_query) | **POST** /integration_log/summary/query | Retrieve integration log summaries
[**get_integration_logs_query**](IntegrationLogApi.md#get_integration_logs_query) | **POST** /integration_log/query | Retrieve integration logs


# **get_integration_log**
> IntegrationLogResponse get_integration_log(pk, sk)

Retrieve an integration log

Retrieve an integration logs from the account based identifiers 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.IntegrationLogApi.fromApiKey(simple_key, False, True)

pk = 'pk_example' # str | 
sk = 'sk_example' # str | 

try:
    # Retrieve an integration log
    api_response = api_instance.get_integration_log(pk, sk)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_log_file**
> file get_integration_log_file(pk, sk, uuid)

Retrieve an integration log file

Retrieve an integration log file from the account based identifiers 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.IntegrationLogApi.fromApiKey(simple_key, False, True)

pk = 'pk_example' # str | 
sk = 'sk_example' # str | 
uuid = 'uuid_example' # str | 

try:
    # Retrieve an integration log file
    api_response = api_instance.get_integration_log_file(pk, sk, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationLogApi->get_integration_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **str**|  | 
 **sk** | **str**|  | 
 **uuid** | **str**|  | 

### Return type

[**file**](file.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_log_summaries_query**
> IntegrationLogSummaryQueryResponse get_integration_log_summaries_query(integration_log_summaries_query)

Retrieve integration log summaries

Retrieves a set of integration log summaries from the account based on a query object. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.IntegrationLogApi.fromApiKey(simple_key, False, True)

integration_log_summaries_query = ultracart.IntegrationLogSummaryQueryRequest() # IntegrationLogSummaryQueryRequest | Integration log summaries query

try:
    # Retrieve integration log summaries
    api_response = api_instance.get_integration_log_summaries_query(integration_log_summaries_query)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_logs_query**
> IntegrationLogQueryResponse get_integration_logs_query(integration_log_query, limit=limit, offset=offset, sort=sort)

Retrieve integration logs

Retrieves a set of integration logs from the account based on a query object. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.IntegrationLogApi.fromApiKey(simple_key, False, True)

integration_log_query = ultracart.IntegrationLogQueryRequest() # IntegrationLogQueryRequest | Integration log query
limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Retrieve integration logs
    api_response = api_instance.get_integration_logs_query(integration_log_query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationLogApi->get_integration_logs_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_log_query** | [**IntegrationLogQueryRequest**](IntegrationLogQueryRequest.md)| Integration log query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**IntegrationLogQueryResponse**](IntegrationLogQueryResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

