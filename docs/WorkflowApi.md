# ultracart.WorkflowApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_assignment_groups**](WorkflowApi.md#get_workflow_assignment_groups) | **GET** /workflow/assignment_groups | Retrieve a list of groups that workflow tasks can be assigned to
[**get_workflow_assignment_users**](WorkflowApi.md#get_workflow_assignment_users) | **GET** /workflow/assignment_users | Retrieve a list of users that workflow tasks can be assigned to
[**get_workflow_me**](WorkflowApi.md#get_workflow_me) | **GET** /workflow/me | Retrieve a user object for myself
[**get_workflow_task**](WorkflowApi.md#get_workflow_task) | **GET** /workflow/tasks/{task_uuid} | Retrieve a workflow task
[**get_workflow_task_attachment_upload_url**](WorkflowApi.md#get_workflow_task_attachment_upload_url) | **GET** /workflow/tasks/attachments/{extension} | Get a presigned workflow task attachment upload URL
[**get_workflow_task_by_object_type**](WorkflowApi.md#get_workflow_task_by_object_type) | **GET** /workflow/tasks/by/{object_type}/{object_id} | Retrieve a workflow task by object type and id
[**get_workflow_tasks**](WorkflowApi.md#get_workflow_tasks) | **POST** /workflow/tasks/search | Search workflow tasks
[**insert_workflow_task**](WorkflowApi.md#insert_workflow_task) | **POST** /workflow/tasks | Insert a workflow task
[**update_workflow_task**](WorkflowApi.md#update_workflow_task) | **PUT** /workflow/tasks/{task_uuid} | Update a workflow task


# **get_workflow_assignment_groups**
> WorkflowGroupsResponse get_workflow_assignment_groups()

Retrieve a list of groups that workflow tasks can be assigned to

Retrieve a list of groups that workflow tasks can be assigned to 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.workflow_groups_response import WorkflowGroupsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of groups that workflow tasks can be assigned to
        api_response = api_instance.get_workflow_assignment_groups(limit=limit, offset=offset)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_assignment_groups: %s\n" % e)
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
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_users_response import WorkflowUsersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of users that workflow tasks can be assigned to
        api_response = api_instance.get_workflow_assignment_users(limit=limit, offset=offset)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_assignment_users: %s\n" % e)
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
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_user_response import WorkflowUserResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a user object for myself
        api_response = api_instance.get_workflow_me()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_me: %s\n" % e)
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
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_task_response import WorkflowTaskResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    task_uuid = "task_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a workflow task
        api_response = api_instance.get_workflow_task(task_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_task: %s\n" % e)
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
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_attachment_upload_url_response import WorkflowAttachmentUploadUrlResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    extension = "extension_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a presigned workflow task attachment upload URL
        api_response = api_instance.get_workflow_task_attachment_upload_url(extension)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_task_attachment_upload_url: %s\n" % e)
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
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_tasks_response import WorkflowTasksResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    object_type = "object_type_example" # str | 
    object_id = "object_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a workflow task by object type and id
        api_response = api_instance.get_workflow_task_by_object_type(object_type, object_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_task_by_object_type: %s\n" % e)
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

# **get_workflow_tasks**
> WorkflowTasksResponse get_workflow_tasks(workflow_tasks_query)

Search workflow tasks

Retrieves a set of workflow tasks from the account based on a query object. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_tasks_response import WorkflowTasksResponse
from ultracart.model.workflow_tasks_request import WorkflowTasksRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    workflow_tasks_query = WorkflowTasksRequest(
        assigned_to_group_id=1,
        assigned_to_me=True,
        assigned_to_user_id=1,
        created_by=WorkflowUser(
            user="user_example",
            user_icon_url="user_icon_url_example",
            user_id=1,
        ),
        created_dts_begin="created_dts_begin_example",
        created_dts_end="created_dts_end_example",
        delay_until_dts_begin="delay_until_dts_begin_example",
        delay_until_dts_end="delay_until_dts_end_example",
        due_dts_begin="due_dts_begin_example",
        due_dts_end="due_dts_end_example",
        last_update_dts_begin="last_update_dts_begin_example",
        last_update_dts_end="last_update_dts_end_example",
        object_email="object_email_example",
        object_type="order",
        priority="1 - low",
        status="open",
        unassigned=True,
    ) # WorkflowTasksRequest | Workflow tasks query
    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search workflow tasks
        api_response = api_instance.get_workflow_tasks(workflow_tasks_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_tasks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search workflow tasks
        api_response = api_instance.get_workflow_tasks(workflow_tasks_query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->get_workflow_tasks: %s\n" % e)
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
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_task import WorkflowTask
from ultracart.model.workflow_task_response import WorkflowTaskResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    workflow_task = WorkflowTask(
        assigned_to_group="assigned_to_group_example",
        assigned_to_group_id=1,
        assigned_to_user="assigned_to_user_example",
        assigned_to_user_id=1,
        attachments=[
            WorkflowAttachment(
                download_key="download_key_example",
                file_name="file_name_example",
                file_uuid="file_uuid_example",
                mime_type="mime_type_example",
                upload_key="upload_key_example",
            ),
        ],
        created_by=WorkflowUser(
            user="user_example",
            user_icon_url="user_icon_url_example",
            user_id=1,
        ),
        created_dts="created_dts_example",
        delay_until_dts="delay_until_dts_example",
        due_dts="due_dts_example",
        histories=[
            WorkflowTaskHistory(
                activity_dts="activity_dts_example",
                description="description_example",
                ip_address="ip_address_example",
                user=WorkflowUser(
                    user="user_example",
                    user_icon_url="user_icon_url_example",
                    user_id=1,
                ),
            ),
        ],
        last_update_dts="last_update_dts_example",
        merchant_id="merchant_id_example",
        notes=[
            WorkflowNote(
                attachments=[
                    WorkflowAttachment(
                        download_key="download_key_example",
                        file_name="file_name_example",
                        file_uuid="file_uuid_example",
                        mime_type="mime_type_example",
                        upload_key="upload_key_example",
                    ),
                ],
                edit_dts="edit_dts_example",
                note="note_example",
                note_dts="note_dts_example",
                original_note="original_note_example",
                user=WorkflowUser(
                    user="user_example",
                    user_icon_url="user_icon_url_example",
                    user_id=1,
                ),
            ),
        ],
        object_email="object_email_example",
        object_id="object_id_example",
        object_type="order",
        object_url="object_url_example",
        priority="1 - low",
        status="open",
        task_context="task_context_example",
        task_details="task_details_example",
        task_name="task_name_example",
        workflow_task_uuid="workflow_task_uuid_example",
    ) # WorkflowTask | workflow task

    # example passing only required values which don't have defaults set
    try:
        # Insert a workflow task
        api_response = api_instance.insert_workflow_task(workflow_task)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->insert_workflow_task: %s\n" % e)
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
import time
import ultracart
from ultracart.api import workflow_api
from ultracart.model.workflow_task import WorkflowTask
from ultracart.model.workflow_task_response import WorkflowTaskResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    task_uuid = "task_uuid_example" # str | 
    workflow_task = WorkflowTask(
        assigned_to_group="assigned_to_group_example",
        assigned_to_group_id=1,
        assigned_to_user="assigned_to_user_example",
        assigned_to_user_id=1,
        attachments=[
            WorkflowAttachment(
                download_key="download_key_example",
                file_name="file_name_example",
                file_uuid="file_uuid_example",
                mime_type="mime_type_example",
                upload_key="upload_key_example",
            ),
        ],
        created_by=WorkflowUser(
            user="user_example",
            user_icon_url="user_icon_url_example",
            user_id=1,
        ),
        created_dts="created_dts_example",
        delay_until_dts="delay_until_dts_example",
        due_dts="due_dts_example",
        histories=[
            WorkflowTaskHistory(
                activity_dts="activity_dts_example",
                description="description_example",
                ip_address="ip_address_example",
                user=WorkflowUser(
                    user="user_example",
                    user_icon_url="user_icon_url_example",
                    user_id=1,
                ),
            ),
        ],
        last_update_dts="last_update_dts_example",
        merchant_id="merchant_id_example",
        notes=[
            WorkflowNote(
                attachments=[
                    WorkflowAttachment(
                        download_key="download_key_example",
                        file_name="file_name_example",
                        file_uuid="file_uuid_example",
                        mime_type="mime_type_example",
                        upload_key="upload_key_example",
                    ),
                ],
                edit_dts="edit_dts_example",
                note="note_example",
                note_dts="note_dts_example",
                original_note="original_note_example",
                user=WorkflowUser(
                    user="user_example",
                    user_icon_url="user_icon_url_example",
                    user_id=1,
                ),
            ),
        ],
        object_email="object_email_example",
        object_id="object_id_example",
        object_type="order",
        object_url="object_url_example",
        priority="1 - low",
        status="open",
        task_context="task_context_example",
        task_details="task_details_example",
        task_name="task_name_example",
        workflow_task_uuid="workflow_task_uuid_example",
    ) # WorkflowTask | Workflow task

    # example passing only required values which don't have defaults set
    try:
        # Update a workflow task
        api_response = api_instance.update_workflow_task(task_uuid, workflow_task)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling WorkflowApi->update_workflow_task: %s\n" % e)
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

