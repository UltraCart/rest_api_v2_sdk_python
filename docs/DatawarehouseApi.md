# ultracart.DatawarehouseApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_report**](DatawarehouseApi.md#delete_report) | **DELETE** /datawarehouse/reports/{report_oid} | Delete a report
[**dry_run_report_queries**](DatawarehouseApi.md#dry_run_report_queries) | **PUT** /datawarehouse/reports/dryrun | Dry run the report queries
[**execute_report_queries**](DatawarehouseApi.md#execute_report_queries) | **PUT** /datawarehouse/reports/execute | Execute the report queries
[**get_report**](DatawarehouseApi.md#get_report) | **GET** /datawarehouse/reports/{report_oid} | Get a report
[**get_report_data_set**](DatawarehouseApi.md#get_report_data_set) | **GET** /datawarehouse/reports/dataset/{dataset_uuid} | Get a report data set
[**get_report_data_set_page**](DatawarehouseApi.md#get_report_data_set_page) | **GET** /datawarehouse/reports/dataset/{dataset_uuid}/pages/{page_number} | Get a report data set page
[**get_report_websocket_authorization**](DatawarehouseApi.md#get_report_websocket_authorization) | **PUT** /datawarehouse/reports/auth | Get report websocket authorization
[**get_reports**](DatawarehouseApi.md#get_reports) | **GET** /datawarehouse/reports | Get list of reports available
[**insert_report**](DatawarehouseApi.md#insert_report) | **POST** /datawarehouse/reports | Create a report
[**update_report**](DatawarehouseApi.md#update_report) | **PUT** /datawarehouse/reports/{report_oid} | Update a report


# **delete_report**
> delete_report(report_oid)

Delete a report

Delete a report on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    report_oid = 1 # int | The report oid to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a report
        api_instance.delete_report(report_oid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_report_queries**
> ReportDryRunQueriesResponse dry_run_report_queries(query_request)

Dry run the report queries

Dry run the report queries 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.report_dry_run_queries_response import ReportDryRunQueriesResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.report_dry_run_queries_request import ReportDryRunQueriesRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    query_request = ReportDryRunQueriesRequest(
        connection_id="connection_id_example",
        default_dataset_id="default_dataset_id_example",
        default_project_id="default_project_id_example",
        merchant_id="merchant_id_example",
        queries=[
            ReportDataSetQuery(
                comparison_results=True,
                data_set_query_uuid="data_set_query_uuid_example",
                data_source=ReportDataSource(
                    name="name_example",
                    partition_date_column="partition_date_column_example",
                    partition_date_safety_days=1,
                    partition_date_strategy="partition_date_strategy_example",
                    schema=[
                        ReportDataSourceSchema(
                            dimension=True,
                            name="name_example",
                            type="BIGNUMERIC",
                        ),
                    ],
                    sql="sql_example",
                ),
                dimensions=[
                    ReportPageVisualizationDimension(
                        _as="_as_example",
                        cast="cast_example",
                        column="column_example",
                        datetime_timezone="datetime_timezone_example",
                        datetime_trunc="datetime_trunc_example",
                        extract="extract_example",
                        function="function_example",
                    ),
                ],
                filter=ReportFilter(
                    connections=[
                        ReportFilterConnection(
                            column="column_example",
                            data_source_name="data_source_name_example",
                        ),
                    ],
                    name="name_example",
                    timezone="timezone_example",
                    type="date range",
                    uuid="uuid_example",
                    values=[
                        "values_example",
                    ],
                ),
                for_object_id="for_object_id_example",
                for_object_type="schema",
                metrics=[
                    ReportPageVisualizationMetric(
                        aggregation="sum",
                        _as="_as_example",
                        column="column_example",
                        round=1,
                    ),
                ],
                page_size=1,
                selected_filters=[
                    ReportFilter(
                        connections=[
                            ReportFilterConnection(
                                column="column_example",
                                data_source_name="data_source_name_example",
                            ),
                        ],
                        name="name_example",
                        timezone="timezone_example",
                        type="date range",
                        uuid="uuid_example",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
                skip_cache=True,
                user_data="user_data_example",
            ),
        ],
        security_level="security_level_example",
    ) # ReportDryRunQueriesRequest | Dry run request

    # example passing only required values which don't have defaults set
    try:
        # Dry run the report queries
        api_response = api_instance.dry_run_report_queries(query_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **execute_report_queries**
> execute_report_queries(query_request)

Execute the report queries

Execute the report queries 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.report_execute_queries_request import ReportExecuteQueriesRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    query_request = ReportExecuteQueriesRequest(
        client_uuid="client_uuid_example",
        connection_id="connection_id_example",
        default_dataset_id="default_dataset_id_example",
        default_project_id="default_project_id_example",
        merchant_id="merchant_id_example",
        queries=[
            ReportDataSetQuery(
                comparison_results=True,
                data_set_query_uuid="data_set_query_uuid_example",
                data_source=ReportDataSource(
                    name="name_example",
                    partition_date_column="partition_date_column_example",
                    partition_date_safety_days=1,
                    partition_date_strategy="partition_date_strategy_example",
                    schema=[
                        ReportDataSourceSchema(
                            dimension=True,
                            name="name_example",
                            type="BIGNUMERIC",
                        ),
                    ],
                    sql="sql_example",
                ),
                dimensions=[
                    ReportPageVisualizationDimension(
                        _as="_as_example",
                        cast="cast_example",
                        column="column_example",
                        datetime_timezone="datetime_timezone_example",
                        datetime_trunc="datetime_trunc_example",
                        extract="extract_example",
                        function="function_example",
                    ),
                ],
                filter=ReportFilter(
                    connections=[
                        ReportFilterConnection(
                            column="column_example",
                            data_source_name="data_source_name_example",
                        ),
                    ],
                    name="name_example",
                    timezone="timezone_example",
                    type="date range",
                    uuid="uuid_example",
                    values=[
                        "values_example",
                    ],
                ),
                for_object_id="for_object_id_example",
                for_object_type="schema",
                metrics=[
                    ReportPageVisualizationMetric(
                        aggregation="sum",
                        _as="_as_example",
                        column="column_example",
                        round=1,
                    ),
                ],
                page_size=1,
                selected_filters=[
                    ReportFilter(
                        connections=[
                            ReportFilterConnection(
                                column="column_example",
                                data_source_name="data_source_name_example",
                            ),
                        ],
                        name="name_example",
                        timezone="timezone_example",
                        type="date range",
                        uuid="uuid_example",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
                skip_cache=True,
                user_data="user_data_example",
            ),
        ],
        security_level="standard",
    ) # ReportExecuteQueriesRequest | Query request

    # example passing only required values which don't have defaults set
    try:
        # Execute the report queries
        api_instance.execute_report_queries(query_request)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportResponse get_report(report_oid)

Get a report

Retrieve a report 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.report_response import ReportResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    report_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get a report
        api_response = api_instance.get_report(report_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_report_data_set**
> ReportDataSetResponse get_report_data_set(dataset_uuid)

Get a report data set

Retrieve a report data set 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.report_data_set_response import ReportDataSetResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    dataset_uuid = "dataset_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a report data set
        api_response = api_instance.get_report_data_set(dataset_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_report_data_set_page**
> ReportDataSetPageResponse get_report_data_set_page(dataset_uuid, page_number)

Get a report data set page

Retrieve a report data set page 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.report_data_set_page_response import ReportDataSetPageResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    dataset_uuid = "dataset_uuid_example" # str | 
    page_number = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get a report data set page
        api_response = api_instance.get_report_data_set_page(dataset_uuid, page_number)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_report_websocket_authorization**
> ReportAuthResponse get_report_websocket_authorization()

Get report websocket authorization

Retrieve a JWT to authorize a report to make a websocket connection. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.report_auth_response import ReportAuthResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get report websocket authorization
        api_response = api_instance.get_report_websocket_authorization()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling DatawarehouseApi->get_report_websocket_authorization: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportAuthResponse**](ReportAuthResponse.md)

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

# **get_reports**
> ReportsResponse get_reports()

Get list of reports available

Retrieve a list of reports available 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.reports_response import ReportsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get list of reports available
        api_response = api_instance.get_reports()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling DatawarehouseApi->get_reports: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportsResponse**](ReportsResponse.md)

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

# **insert_report**
> ReportResponse insert_report(report)

Create a report

Create a new report on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.report import Report
from ultracart.model.report_response import ReportResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    report = Report(
        active=True,
        data_sources=[
            ReportDataSource(
                name="name_example",
                partition_date_column="partition_date_column_example",
                partition_date_safety_days=1,
                partition_date_strategy="partition_date_strategy_example",
                schema=[
                    ReportDataSourceSchema(
                        dimension=True,
                        name="name_example",
                        type="BIGNUMERIC",
                    ),
                ],
                sql="sql_example",
            ),
        ],
        default_dataset_id="default_dataset_id_example",
        default_project_id="default_project_id_example",
        filters=[
            ReportFilter(
                connections=[
                    ReportFilterConnection(
                        column="column_example",
                        data_source_name="data_source_name_example",
                    ),
                ],
                name="name_example",
                timezone="timezone_example",
                type="date range",
                uuid="uuid_example",
                values=[
                    "values_example",
                ],
            ),
        ],
        merchant_id="merchant_id_example",
        name="name_example",
        pages=[
            ReportPage(
                height=3.14,
                title="title_example",
                visualizations=[
                    ReportPageVisualization(
                        config="config_example",
                        data_source_name="data_source_name_example",
                        dimensions=[
                            ReportPageVisualizationDimension(
                                _as="_as_example",
                                cast="cast_example",
                                column="column_example",
                                datetime_timezone="datetime_timezone_example",
                                datetime_trunc="datetime_trunc_example",
                                extract="extract_example",
                                function="function_example",
                            ),
                        ],
                        metrics=[
                            ReportPageVisualizationMetric(
                                aggregation="sum",
                                _as="_as_example",
                                column="column_example",
                                round=1,
                            ),
                        ],
                        name="name_example",
                        show_comparison=True,
                        styles="styles_example",
                        type="score card",
                        visualization_uuid="visualization_uuid_example",
                    ),
                ],
                width=3.14,
            ),
        ],
        report_oid=1,
        security_level="standard",
    ) # Report | Report to create

    # example passing only required values which don't have defaults set
    try:
        # Create a report
        api_response = api_instance.insert_report(report)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **update_report**
> ReportResponse update_report(report_oid, report)

Update a report

Update a report on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import datawarehouse_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.report import Report
from ultracart.model.report_response import ReportResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    report_oid = 1 # int | The report oid to update.
    report = Report(
        active=True,
        data_sources=[
            ReportDataSource(
                name="name_example",
                partition_date_column="partition_date_column_example",
                partition_date_safety_days=1,
                partition_date_strategy="partition_date_strategy_example",
                schema=[
                    ReportDataSourceSchema(
                        dimension=True,
                        name="name_example",
                        type="BIGNUMERIC",
                    ),
                ],
                sql="sql_example",
            ),
        ],
        default_dataset_id="default_dataset_id_example",
        default_project_id="default_project_id_example",
        filters=[
            ReportFilter(
                connections=[
                    ReportFilterConnection(
                        column="column_example",
                        data_source_name="data_source_name_example",
                    ),
                ],
                name="name_example",
                timezone="timezone_example",
                type="date range",
                uuid="uuid_example",
                values=[
                    "values_example",
                ],
            ),
        ],
        merchant_id="merchant_id_example",
        name="name_example",
        pages=[
            ReportPage(
                height=3.14,
                title="title_example",
                visualizations=[
                    ReportPageVisualization(
                        config="config_example",
                        data_source_name="data_source_name_example",
                        dimensions=[
                            ReportPageVisualizationDimension(
                                _as="_as_example",
                                cast="cast_example",
                                column="column_example",
                                datetime_timezone="datetime_timezone_example",
                                datetime_trunc="datetime_trunc_example",
                                extract="extract_example",
                                function="function_example",
                            ),
                        ],
                        metrics=[
                            ReportPageVisualizationMetric(
                                aggregation="sum",
                                _as="_as_example",
                                column="column_example",
                                round=1,
                            ),
                        ],
                        name="name_example",
                        show_comparison=True,
                        styles="styles_example",
                        type="score card",
                        visualization_uuid="visualization_uuid_example",
                    ),
                ],
                width=3.14,
            ),
        ],
        report_oid=1,
        security_level="standard",
    ) # Report | Report to update

    # example passing only required values which don't have defaults set
    try:
        # Update a report
        api_response = api_instance.update_report(report_oid, report)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling DatawarehouseApi->update_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_oid** | **int**| The report oid to update. |
 **report** | [**Report**](Report.md)| Report to update |

### Return type

[**ReportResponse**](ReportResponse.md)

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

