# ultracart.BulkApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_cancel_job**](BulkApi.md#bulk_cancel_job) | **DELETE** /bulk/{object}/{job_id} | Request cancellation of a bulk job
[**bulk_generate_upload_url**](BulkApi.md#bulk_generate_upload_url) | **POST** /bulk/{object}/upload-url | Generate a presigned upload URL for a bulk payload
[**bulk_get_job**](BulkApi.md#bulk_get_job) | **GET** /bulk/{object}/{job_id} | Retrieve a bulk job&#39;s status and counts
[**bulk_get_job_records**](BulkApi.md#bulk_get_job_records) | **GET** /bulk/{object}/{job_id}/records | Paginate a bulk job&#39;s per-record results
[**bulk_list_jobs**](BulkApi.md#bulk_list_jobs) | **GET** /bulk/{object} | List bulk jobs for the calling merchant
[**bulk_submit_job**](BulkApi.md#bulk_submit_job) | **POST** /bulk/{object} | Submit a bulk job


# **bulk_cancel_job**
> bulk_cancel_job(object, job_id)

Request cancellation of a bulk job

Queued jobs cancel immediately (200). In-progress jobs finalize as cancelled between records (202); already-processed records stand. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object type |
 **job_id** | **str**| The bulk job id |

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
**200** |  |  -  |
**202** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_generate_upload_url**
> BulkUploadUrlResponse bulk_generate_upload_url(object)

Generate a presigned upload URL for a bulk payload

Returns a presigned S3 PUT URL the merchant uploads NDJSON to, plus the s3_key to pass to submit. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object type |

### Return type

[**BulkUploadUrlResponse**](BulkUploadUrlResponse.md)

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

# **bulk_get_job**
> BulkJobResponse bulk_get_job(object, job_id)

Retrieve a bulk job's status and counts

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object type |
 **job_id** | **str**| The bulk job id |

### Return type

[**BulkJobResponse**](BulkJobResponse.md)

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

# **bulk_get_job_records**
> BulkRecordsResponse bulk_get_job_records(object, job_id)

Paginate a bulk job's per-record results

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object type |
 **job_id** | **str**| The bulk job id |
 **status** | **str**| Filter by per-record result status (success, failed, duplicate) | [optional]
 **cursor** | **str**| Opaque pagination cursor | [optional]
 **limit** | **int**| Page size (default 100, max 1000) | [optional]

### Return type

[**BulkRecordsResponse**](BulkRecordsResponse.md)

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

# **bulk_list_jobs**
> BulkJobsResponse bulk_list_jobs(object)

List bulk jobs for the calling merchant

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object type |
 **status** | **str**| Filter by job status | [optional]
 **cursor** | **str**| Opaque pagination cursor | [optional]
 **limit** | **int**| Page size (default 100, max 1000) | [optional]

### Return type

[**BulkJobsResponse**](BulkJobsResponse.md)

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

# **bulk_submit_job**
> BulkJobResponse bulk_submit_job(object, bulk_job)

Submit a bulk job

Submits a job referencing a previously uploaded NDJSON object. One active job per merchant; additional submissions queue. The bulk surface is write-only (insert / upsert); it has no bulk read or export operation. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object type |
 **bulk_job** | [**BulkJobRequest**](BulkJobRequest.md)| Bulk job submission |

### Return type

[**BulkJobResponse**](BulkJobResponse.md)

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

