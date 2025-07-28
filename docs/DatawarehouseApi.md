# ultracart.DatawarehouseApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_report**](DatawarehouseApi.md#delete_custom_report) | **DELETE** /datawarehouse/custom_reports/{custom_report_oid} | Delete a custom report
[**delete_report**](DatawarehouseApi.md#delete_report) | **DELETE** /datawarehouse/reports/{report_oid} | Delete a report
[**dry_run_report_queries**](DatawarehouseApi.md#dry_run_report_queries) | **PUT** /datawarehouse/reports/dryrun | Dry run the report queries
[**execute_custom_report**](DatawarehouseApi.md#execute_custom_report) | **PUT** /datawarehouse/custom_reports/{custom_report_oid}/execute | Execute a custom report
[**execute_report_queries**](DatawarehouseApi.md#execute_report_queries) | **PUT** /datawarehouse/reports/execute | Execute the report queries
[**get_custom_report**](DatawarehouseApi.md#get_custom_report) | **GET** /datawarehouse/custom_reports/{custom_report_oid} | Get a custom report
[**get_custom_report_account_config**](DatawarehouseApi.md#get_custom_report_account_config) | **GET** /datawarehouse/custom_reports/account_config | Get custom report account configuration
[**get_custom_reports**](DatawarehouseApi.md#get_custom_reports) | **GET** /datawarehouse/custom_reports | Get custom reports
[**get_report**](DatawarehouseApi.md#get_report) | **GET** /datawarehouse/reports/{report_oid} | Get a report
[**get_report_data_set**](DatawarehouseApi.md#get_report_data_set) | **GET** /datawarehouse/reports/dataset/{dataset_uuid} | Get a report data set
[**get_report_data_set_page**](DatawarehouseApi.md#get_report_data_set_page) | **GET** /datawarehouse/reports/dataset/{dataset_uuid}/pages/{page_number} | Get a report data set page
[**get_report_websocket_authorization**](DatawarehouseApi.md#get_report_websocket_authorization) | **PUT** /datawarehouse/reports/auth | Get report websocket authorization
[**get_reports**](DatawarehouseApi.md#get_reports) | **GET** /datawarehouse/reports | Get list of reports available
[**insert_custom_report**](DatawarehouseApi.md#insert_custom_report) | **POST** /datawarehouse/custom_reports | Create a custom report
[**insert_report**](DatawarehouseApi.md#insert_report) | **POST** /datawarehouse/reports | Create a report
[**update_custom_report**](DatawarehouseApi.md#update_custom_report) | **PUT** /datawarehouse/custom_reports/{custom_report_oid} | Update a custom report
[**update_custom_report_account_config**](DatawarehouseApi.md#update_custom_report_account_config) | **PUT** /datawarehouse/custom_reports/account_config | Update custom report account config
[**update_report**](DatawarehouseApi.md#update_report) | **PUT** /datawarehouse/reports/{report_oid} | Update a report


# **delete_custom_report**
> delete_custom_report(custom_report_oid)

Delete a custom report

Delete a custom report on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

custom_report_oid = 56 # int | The report oid to delete.

try:
    # Delete a custom report
    api_instance.delete_custom_report(custom_report_oid)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->delete_custom_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_report_oid** | **int**| The report oid to delete. | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report**
> delete_report(report_oid)

Delete a report

Delete a report on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

report_oid = 56 # int | The report oid to delete.

try:
    # Delete a report
    api_instance.delete_report(report_oid)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->delete_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_oid** | **int**| The report oid to delete. | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_report_queries**
> ReportDryRunQueriesResponse dry_run_report_queries(query_request)

Dry run the report queries

Dry run the report queries 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

query_request = ultracart.ReportDryRunQueriesRequest() # ReportDryRunQueriesRequest | Dry run request

try:
    # Dry run the report queries
    api_response = api_instance.dry_run_report_queries(query_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->dry_run_report_queries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**ReportDryRunQueriesRequest**](ReportDryRunQueriesRequest.md)| Dry run request | 

### Return type

[**ReportDryRunQueriesResponse**](ReportDryRunQueriesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_custom_report**
> CustomReportResponse execute_custom_report(execution_request, custom_report_oid)

Execute a custom report

Execute a custom report on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

execution_request = ultracart.CustomReportExecutionRequest() # CustomReportExecutionRequest | Request to execute custom report
custom_report_oid = 56 # int | The report oid to execute.

try:
    # Execute a custom report
    api_response = api_instance.execute_custom_report(execution_request, custom_report_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->execute_custom_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_request** | [**CustomReportExecutionRequest**](CustomReportExecutionRequest.md)| Request to execute custom report | 
 **custom_report_oid** | **int**| The report oid to execute. | 

### Return type

[**CustomReportResponse**](CustomReportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_report_queries**
> execute_report_queries(query_request)

Execute the report queries

Execute the report queries 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

query_request = ultracart.ReportExecuteQueriesRequest() # ReportExecuteQueriesRequest | Query request

try:
    # Execute the report queries
    api_instance.execute_report_queries(query_request)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->execute_report_queries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**ReportExecuteQueriesRequest**](ReportExecuteQueriesRequest.md)| Query request | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_report**
> CustomReportResponse get_custom_report(custom_report_oid)

Get a custom report

Retrieve a custom report 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

custom_report_oid = 56 # int | 

try:
    # Get a custom report
    api_response = api_instance.get_custom_report(custom_report_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_custom_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_report_oid** | **int**|  | 

### Return type

[**CustomReportResponse**](CustomReportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_report_account_config**
> CustomReportAccountConfigResponse get_custom_report_account_config()

Get custom report account configuration

Retrieve a custom report account configuration 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)


try:
    # Get custom report account configuration
    api_response = api_instance.get_custom_report_account_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_custom_report_account_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomReportAccountConfigResponse**](CustomReportAccountConfigResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_reports**
> CustomReportsResponse get_custom_reports()

Get custom reports

Retrieve a custom reports 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)


try:
    # Get custom reports
    api_response = api_instance.get_custom_reports()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_custom_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomReportsResponse**](CustomReportsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportResponse get_report(report_oid)

Get a report

Retrieve a report 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

report_oid = 56 # int | 

try:
    # Get a report
    api_response = api_instance.get_report(report_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_oid** | **int**|  | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_data_set**
> ReportDataSetResponse get_report_data_set(dataset_uuid)

Get a report data set

Retrieve a report data set 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

dataset_uuid = 'dataset_uuid_example' # str | 

try:
    # Get a report data set
    api_response = api_instance.get_report_data_set(dataset_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_report_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uuid** | **str**|  | 

### Return type

[**ReportDataSetResponse**](ReportDataSetResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_data_set_page**
> ReportDataSetPageResponse get_report_data_set_page(dataset_uuid, page_number)

Get a report data set page

Retrieve a report data set page 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

dataset_uuid = 'dataset_uuid_example' # str | 
page_number = 56 # int | 

try:
    # Get a report data set page
    api_response = api_instance.get_report_data_set_page(dataset_uuid, page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_report_data_set_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uuid** | **str**|  | 
 **page_number** | **int**|  | 

### Return type

[**ReportDataSetPageResponse**](ReportDataSetPageResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_websocket_authorization**
> ReportAuthResponse get_report_websocket_authorization()

Get report websocket authorization

Retrieve a JWT to authorize a report to make a websocket connection. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)


try:
    # Get report websocket authorization
    api_response = api_instance.get_report_websocket_authorization()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_report_websocket_authorization: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportAuthResponse**](ReportAuthResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> ReportsResponse get_reports()

Get list of reports available

Retrieve a list of reports available 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)


try:
    # Get list of reports available
    api_response = api_instance.get_reports()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->get_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_custom_report**
> CustomReportResponse insert_custom_report(report)

Create a custom report

Create a new custom report on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

report = ultracart.CustomReport() # CustomReport | Report to create

try:
    # Create a custom report
    api_response = api_instance.insert_custom_report(report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->insert_custom_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report** | [**CustomReport**](CustomReport.md)| Report to create | 

### Return type

[**CustomReportResponse**](CustomReportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_report**
> ReportResponse insert_report(report)

Create a report

Create a new report on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

report = ultracart.Report() # Report | Report to create

try:
    # Create a report
    api_response = api_instance.insert_report(report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->insert_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report** | [**Report**](Report.md)| Report to create | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_report**
> CustomReportResponse update_custom_report(report, custom_report_oid)

Update a custom report

Update a custom report on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

report = ultracart.CustomReport() # CustomReport | Report to custom update
custom_report_oid = 56 # int | The report oid to custom update.

try:
    # Update a custom report
    api_response = api_instance.update_custom_report(report, custom_report_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->update_custom_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report** | [**CustomReport**](CustomReport.md)| Report to custom update | 
 **custom_report_oid** | **int**| The report oid to custom update. | 

### Return type

[**CustomReportResponse**](CustomReportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_report_account_config**
> CustomReportAccountConfigResponse update_custom_report_account_config(account_config)

Update custom report account config

Update custom report account config. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

account_config = ultracart.CustomReportAccountConfig() # CustomReportAccountConfig | Account config to update

try:
    # Update custom report account config
    api_response = api_instance.update_custom_report_account_config(account_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->update_custom_report_account_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_config** | [**CustomReportAccountConfig**](CustomReportAccountConfig.md)| Account config to update | 

### Return type

[**CustomReportAccountConfigResponse**](CustomReportAccountConfigResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report**
> ReportResponse update_report(report, report_oid)

Update a report

Update a report on the UltraCart account. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.DatawarehouseApi.fromApiKey(simple_key, False, True)

report = ultracart.Report() # Report | Report to update
report_oid = 56 # int | The report oid to update.

try:
    # Update a report
    api_response = api_instance.update_report(report, report_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatawarehouseApi->update_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report** | [**Report**](Report.md)| Report to update | 
 **report_oid** | **int**| The report oid to update. | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

