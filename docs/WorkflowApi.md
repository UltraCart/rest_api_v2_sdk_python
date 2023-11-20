# ultracart.WorkflowApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_assignment_groups**](WorkflowApi.md#get_workflow_assignment_groups) | **GET** /workflow/assignment_groups | Retrieve a list of groups that workflow tasks can be assigned to
[**get_workflow_assignment_users**](WorkflowApi.md#get_workflow_assignment_users) | **GET** /workflow/assignment_users | Retrieve a list of users that workflow tasks can be assigned to
[**get_workflow_task**](WorkflowApi.md#get_workflow_task) | **GET** /workflow/tasks/{task_uuid} | Retrieve a workflow task
[**get_workflow_task_attachment_upload_url**](WorkflowApi.md#get_workflow_task_attachment_upload_url) | **GET** /workflow/tasks/attachments/{extension} | Get a presigned workflow task attachment upload URL
[**get_workflow_task_by_object_type**](WorkflowApi.md#get_workflow_task_by_object_type) | **GET** /workflow/tasks/by/{object_type}/{object_id} | Retrieve a workflow task by object type and id
[**get_workflow_tasks**](WorkflowApi.md#get_workflow_tasks) | **POST** /workflow/tasks/search | Search workflow tasks
[**insert_workflow_task**](WorkflowApi.md#insert_workflow_task) | **POST** /workflow/tasks | Insert a workflow task
[**update_workflow_task**](WorkflowApi.md#update_workflow_task) | **PUT** /workflow/tasks/{task_uuid} | Update a workflow task


# **get_workflow_assignment_groups**
> WorkflowGroupsResponse get_workflow_assignment_groups(limit=limit, offset=offset)

Retrieve a list of groups that workflow tasks can be assigned to

Retrieve a list of groups that workflow tasks can be assigned to 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)

try:
    # Retrieve a list of groups that workflow tasks can be assigned to
    api_response = api_instance.get_workflow_assignment_groups(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowApi->get_workflow_assignment_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]

### Return type

[**WorkflowGroupsResponse**](WorkflowGroupsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_assignment_users**
> WorkflowUsersResponse get_workflow_assignment_users(limit=limit, offset=offset)

Retrieve a list of users that workflow tasks can be assigned to

Retrieve a list of users that workflow tasks can be assigned to 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)

try:
    # Retrieve a list of users that workflow tasks can be assigned to
    api_response = api_instance.get_workflow_assignment_users(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowApi->get_workflow_assignment_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]

### Return type

[**WorkflowUsersResponse**](WorkflowUsersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_task**
> WorkflowTaskResponse get_workflow_task(task_uuid)

Retrieve a workflow task

Retrieve a workflow task 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

task_uuid = 'task_uuid_example' # str | 

try:
    # Retrieve a workflow task
    api_response = api_instance.get_workflow_task(task_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_task_attachment_upload_url**
> WorkflowAttachmentUploadUrlResponse get_workflow_task_attachment_upload_url(extension)

Get a presigned workflow task attachment upload URL

Get a presigned workflow task attachment upload URL 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

extension = 'extension_example' # str | 

try:
    # Get a presigned workflow task attachment upload URL
    api_response = api_instance.get_workflow_task_attachment_upload_url(extension)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_task_by_object_type**
> WorkflowTasksResponse get_workflow_task_by_object_type(object_type, object_id)

Retrieve a workflow task by object type and id

Retrieve a workflow task by object type and id 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

object_type = 'object_type_example' # str | 
object_id = 'object_id_example' # str | 

try:
    # Retrieve a workflow task by object type and id
    api_response = api_instance.get_workflow_task_by_object_type(object_type, object_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_tasks**
> WorkflowTasksResponse get_workflow_tasks(workflow_tasks_query, limit=limit, offset=offset, sort=sort)

Search workflow tasks

Retrieves a set of workflow tasks from the account based on a query object. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

workflow_tasks_query = ultracart.WorkflowTasksRequest() # WorkflowTasksRequest | Workflow tasks query
limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Search workflow tasks
    api_response = api_instance.get_workflow_tasks(workflow_tasks_query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowApi->get_workflow_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_tasks_query** | [**WorkflowTasksRequest**](WorkflowTasksRequest.md)| Workflow tasks query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**WorkflowTasksResponse**](WorkflowTasksResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_workflow_task**
> WorkflowTaskResponse insert_workflow_task(workflow_task)

Insert a workflow task

Insert a workflow task 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

workflow_task = ultracart.WorkflowTask() # WorkflowTask | workflow task

try:
    # Insert a workflow task
    api_response = api_instance.insert_workflow_task(workflow_task)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_task**
> WorkflowTaskResponse update_workflow_task(task_uuid, workflow_task)

Update a workflow task

Update a workflow task 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.WorkflowApi.fromApiKey(simple_key, False, True)

task_uuid = 'task_uuid_example' # str | 
workflow_task = ultracart.WorkflowTask() # WorkflowTask | Workflow task

try:
    # Update a workflow task
    api_response = api_instance.update_workflow_task(task_uuid, workflow_task)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

