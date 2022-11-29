# ultracart.ConversationApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_keep_alive**](ConversationApi.md#get_agent_keep_alive) | **GET** /conversation/agent/keepalive | Agent keep alive
[**get_agent_websocket_authorization**](ConversationApi.md#get_agent_websocket_authorization) | **PUT** /conversation/agent/auth | Get agent websocket authorization
[**get_conversation**](ConversationApi.md#get_conversation) | **GET** /conversation/conversations/{conversation_uuid} | Retrieve a conversation
[**get_conversation_context**](ConversationApi.md#get_conversation_context) | **PUT** /conversation/conversations/{conversation_uuid}/context | Get a webchat conversation context
[**get_conversation_messages**](ConversationApi.md#get_conversation_messages) | **GET** /conversation/conversations/{conversation_uuid}/messages/{since} | Retrieve conversation messages
[**get_conversation_multimedia_upload_url**](ConversationApi.md#get_conversation_multimedia_upload_url) | **GET** /conversation/upload_url/{extension} | Get a presigned conersation multimedia upload URL
[**get_conversation_webchat_queue_statuses**](ConversationApi.md#get_conversation_webchat_queue_statuses) | **GET** /conversation/conversations/queues/statuses | Retrieve a conversation webchat queue statuses
[**get_conversations**](ConversationApi.md#get_conversations) | **GET** /conversation/conversations | Retrieve a list of conversation summaries newest to oldest
[**join_conversation**](ConversationApi.md#join_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/join | Join a conversation
[**leave_conversation**](ConversationApi.md#leave_conversation) | **DELETE** /conversation/conversations/{conversation_uuid}/leave | Leave a conversation
[**mark_read_conversation**](ConversationApi.md#mark_read_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/markread | Mark a conversation as read
[**start_conversation**](ConversationApi.md#start_conversation) | **PUT** /conversation/conversations | Start a conversation
[**update_conversation_webchat_queue_status**](ConversationApi.md#update_conversation_webchat_queue_status) | **PUT** /conversation/conversations/queues/{queue_name}/status | Update status within the queue


# **get_agent_keep_alive**
> get_agent_keep_alive()

Agent keep alive

Called periodically by the conversation API to keep the session alive. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)


try:
    # Agent keep alive
    api_instance.get_agent_keep_alive()
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_keep_alive: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_websocket_authorization**
> ConversationAgentAuthResponse get_agent_websocket_authorization()

Get agent websocket authorization

Retrieve a JWT to authorize an agent to make a websocket connection. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)


try:
    # Get agent websocket authorization
    api_response = api_instance.get_agent_websocket_authorization()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_websocket_authorization: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationAgentAuthResponse**](ConversationAgentAuthResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation**
> ConversationResponse get_conversation(conversation_uuid, limit=limit)

Retrieve a conversation

Retrieve a conversation including the participants and messages 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

conversation_uuid = 'conversation_uuid_example' # str | 
limit = 56 # int |  (optional)

try:
    # Retrieve a conversation
    api_response = api_instance.get_conversation(conversation_uuid, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_context**
> ConversationWebchatContext get_conversation_context(conversation_uuid)

Get a webchat conversation context

Get a webchat conversation context 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

conversation_uuid = 'conversation_uuid_example' # str | 

try:
    # Get a webchat conversation context
    api_response = api_instance.get_conversation_context(conversation_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **str**|  | 

### Return type

[**ConversationWebchatContext**](ConversationWebchatContext.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_messages**
> ConversationMessagesResponse get_conversation_messages(conversation_uuid, since, limit=limit)

Retrieve conversation messages

Retrieve conversation messages since a particular time 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

conversation_uuid = 'conversation_uuid_example' # str | 
since = 789 # int | 
limit = 56 # int |  (optional)

try:
    # Retrieve conversation messages
    api_response = api_instance.get_conversation_messages(conversation_uuid, since, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **str**|  | 
 **since** | **int**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**ConversationMessagesResponse**](ConversationMessagesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_multimedia_upload_url**
> ConversationMultimediaUploadUrlResponse get_conversation_multimedia_upload_url(extension)

Get a presigned conersation multimedia upload URL

Get a presigned conersation multimedia upload URL 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

extension = 'extension_example' # str | 

try:
    # Get a presigned conersation multimedia upload URL
    api_response = api_instance.get_conversation_multimedia_upload_url(extension)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_multimedia_upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**|  | 

### Return type

[**ConversationMultimediaUploadUrlResponse**](ConversationMultimediaUploadUrlResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_webchat_queue_statuses**
> ConversationWebchatQueueStatusesResponse get_conversation_webchat_queue_statuses()

Retrieve a conversation webchat queue statuses

Retrieve a conversation webchat queue statuses including agent status and queue entries 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)


try:
    # Retrieve a conversation webchat queue statuses
    api_response = api_instance.get_conversation_webchat_queue_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_webchat_queue_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationWebchatQueueStatusesResponse**](ConversationWebchatQueueStatusesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversations**
> ConversationsResponse get_conversations(medium=medium, before=before, limit=limit, offset=offset)

Retrieve a list of conversation summaries newest to oldest

Retrieve a list of conversation summaries that are ordered newest to oldest, include the most recent message and whether its been read. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

medium = 'medium_example' # str |  (optional)
before = 'before_example' # str |  (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)

try:
    # Retrieve a list of conversation summaries newest to oldest
    api_response = api_instance.get_conversations(medium=medium, before=before, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium** | **str**|  | [optional] 
 **before** | **str**|  | [optional] 
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]

### Return type

[**ConversationsResponse**](ConversationsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_conversation**
> join_conversation(conversation_uuid)

Join a conversation

Join a conversation 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

conversation_uuid = 'conversation_uuid_example' # str | 

try:
    # Join a conversation
    api_instance.join_conversation(conversation_uuid)
except ApiException as e:
    print("Exception when calling ConversationApi->join_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_conversation**
> leave_conversation(conversation_uuid)

Leave a conversation

Leave a conversation 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

conversation_uuid = 'conversation_uuid_example' # str | 

try:
    # Leave a conversation
    api_instance.leave_conversation(conversation_uuid)
except ApiException as e:
    print("Exception when calling ConversationApi->leave_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_read_conversation**
> mark_read_conversation(conversation_uuid)

Mark a conversation as read

Mark a conversation as read 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

conversation_uuid = 'conversation_uuid_example' # str | 

try:
    # Mark a conversation as read
    api_instance.mark_read_conversation(conversation_uuid)
except ApiException as e:
    print("Exception when calling ConversationApi->mark_read_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_conversation**
> ConversationStartResponse start_conversation(start_request)

Start a conversation

Start a new conversation 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

start_request = ultracart.ConversationStartRequest() # ConversationStartRequest | Start request

try:
    # Start a conversation
    api_response = api_instance.start_conversation(start_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->start_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_request** | [**ConversationStartRequest**](ConversationStartRequest.md)| Start request | 

### Return type

[**ConversationStartResponse**](ConversationStartResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conversation_webchat_queue_status**
> update_conversation_webchat_queue_status(queue_name, status_request)

Update status within the queue

Update status within the queue 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.ConversationApi.fromApiKey(simple_key, False, True)

queue_name = 'queue_name_example' # str | 
status_request = ultracart.ConversationWebchatQueueStatusUpdateRequest() # ConversationWebchatQueueStatusUpdateRequest | Status request

try:
    # Update status within the queue
    api_instance.update_conversation_webchat_queue_status(queue_name, status_request)
except ApiException as e:
    print("Exception when calling ConversationApi->update_conversation_webchat_queue_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_name** | **str**|  | 
 **status_request** | [**ConversationWebchatQueueStatusUpdateRequest**](ConversationWebchatQueueStatusUpdateRequest.md)| Status request | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

