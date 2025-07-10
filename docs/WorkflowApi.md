# ultracart.WorkflowApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_agent_websocket_authorization**](WorkflowApi.md#get_workflow_agent_websocket_authorization) | **PUT** /workflow/agent/auth | Get agent websocket authorization
[**get_workflow_assignment_groups**](WorkflowApi.md#get_workflow_assignment_groups) | **GET** /workflow/assignment_groups | Retrieve a list of groups that workflow tasks can be assigned to
[**get_workflow_assignment_users**](WorkflowApi.md#get_workflow_assignment_users) | **GET** /workflow/assignment_users | Retrieve a list of users that workflow tasks can be assigned to
[**get_workflow_me**](WorkflowApi.md#get_workflow_me) | **GET** /workflow/me | Retrieve a user object for myself
[**get_workflow_task**](WorkflowApi.md#get_workflow_task) | **GET** /workflow/tasks/{task_uuid} | Retrieve a workflow task
[**get_workflow_task_attachment_upload_url**](WorkflowApi.md#get_workflow_task_attachment_upload_url) | **GET** /workflow/tasks/attachments/{extension} | Get a presigned workflow task attachment upload URL
[**get_workflow_task_by_object_type**](WorkflowApi.md#get_workflow_task_by_object_type) | **GET** /workflow/tasks/by/{object_type}/{object_id} | Retrieve a workflow task by object type and id
[**get_workflow_task_open_count**](WorkflowApi.md#get_workflow_task_open_count) | **GET** /workflow/tasks/open_count | Retrieve workflow task open count
[**get_workflow_task_tags**](WorkflowApi.md#get_workflow_task_tags) | **GET** /workflow/tasks/tags | Get a list of existing workflow task tags
[**get_workflow_tasks**](WorkflowApi.md#get_workflow_tasks) | **POST** /workflow/tasks/search | Search workflow tasks
[**insert_workflow_task**](WorkflowApi.md#insert_workflow_task) | **POST** /workflow/tasks | Insert a workflow task
[**update_workflow_task**](WorkflowApi.md#update_workflow_task) | **PUT** /workflow/tasks/{task_uuid} | Update a workflow task


# **get_workflow_agent_websocket_authorization**
> WorkflowAgentAuthResponse get_workflow_agent_websocket_authorization()

Get agent websocket authorization

Retrieve a JWT to authorize an agent to make a websocket connection. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkflowAgentAuthResponse**](WorkflowAgentAuthResponse.md)

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

# **get_workflow_assignment_groups**
> WorkflowGroupsResponse get_workflow_assignment_groups()

Retrieve a list of groups that workflow tasks can be assigned to

Retrieve a list of groups that workflow tasks can be assigned to 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0

### Return type

[**WorkflowGroupsResponse**](WorkflowGroupsResponse.md)

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

# **get_workflow_assignment_users**
> WorkflowUsersResponse get_workflow_assignment_users()

Retrieve a list of users that workflow tasks can be assigned to

Retrieve a list of users that workflow tasks can be assigned to 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0

### Return type

[**WorkflowUsersResponse**](WorkflowUsersResponse.md)

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

# **get_workflow_me**
> WorkflowUserResponse get_workflow_me()

Retrieve a user object for myself

Retrieve a user object for myself 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkflowUserResponse**](WorkflowUserResponse.md)

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

# **get_workflow_task**
> WorkflowTaskResponse get_workflow_task(task_uuid)

Retrieve a workflow task

Retrieve a workflow task 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_uuid** | **str**|  |

### Return type

[**WorkflowTaskResponse**](WorkflowTaskResponse.md)

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

# **get_workflow_task_attachment_upload_url**
> WorkflowAttachmentUploadUrlResponse get_workflow_task_attachment_upload_url(extension)

Get a presigned workflow task attachment upload URL

Get a presigned workflow task attachment upload URL 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**|  |

### Return type

[**WorkflowAttachmentUploadUrlResponse**](WorkflowAttachmentUploadUrlResponse.md)

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

# **get_workflow_task_by_object_type**
> WorkflowTasksResponse get_workflow_task_by_object_type(object_type, object_id)

Retrieve a workflow task by object type and id

Retrieve a workflow task by object type and id 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**|  |
 **object_id** | **str**|  |

### Return type

[**WorkflowTasksResponse**](WorkflowTasksResponse.md)

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

# **get_workflow_task_open_count**
> WorkflowTaskOpenCountResponse get_workflow_task_open_count()

Retrieve workflow task open count

Retrieve workflow task open count 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkflowTaskOpenCountResponse**](WorkflowTaskOpenCountResponse.md)

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

# **get_workflow_task_tags**
> WorkflowTaskTagsResponse get_workflow_task_tags()

Get a list of existing workflow task tags

Retrieves a unique list of all the existing workflow task tags. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkflowTaskTagsResponse**](WorkflowTaskTagsResponse.md)

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

# **get_workflow_tasks**
> WorkflowTasksResponse get_workflow_tasks(workflow_tasks_query)

Search workflow tasks

Retrieves a set of workflow tasks from the account based on a query object. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_tasks_query** | [**WorkflowTasksRequest**](WorkflowTasksRequest.md)| Workflow tasks query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**WorkflowTasksResponse**](WorkflowTasksResponse.md)

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

# **insert_workflow_task**
> WorkflowTaskResponse insert_workflow_task(workflow_task)

Insert a workflow task

Insert a workflow task 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task** | [**WorkflowTask**](WorkflowTask.md)| workflow task |

### Return type

[**WorkflowTaskResponse**](WorkflowTaskResponse.md)

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

# **update_workflow_task**
> WorkflowTaskResponse update_workflow_task(task_uuid, workflow_task)

Update a workflow task

Update a workflow task 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# Internal API - Please see the README.md in this directory for an explanation on why there are no samples here.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_uuid** | **str**|  |
 **workflow_task** | [**WorkflowTask**](WorkflowTask.md)| Workflow task |

### Return type

[**WorkflowTaskResponse**](WorkflowTaskResponse.md)

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

