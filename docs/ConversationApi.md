# ultracart.ConversationApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_conversation_canned_message**](ConversationApi.md#delete_conversation_canned_message) | **DELETE** /conversation/canned_messages/{conversation_canned_message_oid} | Delete a conversation canned message
[**delete_department**](ConversationApi.md#delete_department) | **DELETE** /conversation/departments/{conversation_department_oid} | Delete a conversation department
[**delete_engagement**](ConversationApi.md#delete_engagement) | **DELETE** /conversation/engagements/{conversation_engagement_oid} | Delete a conversation engagement
[**delete_pbx_agent**](ConversationApi.md#delete_pbx_agent) | **DELETE** /conversation/pbx/agent/{conversationPbxAgentUuid} | Delete pbx agent
[**delete_pbx_agent_voicemail**](ConversationApi.md#delete_pbx_agent_voicemail) | **DELETE** /conversation/pbx/agent/voicemails/{recording_sid} | Delete Agent Voicemail
[**delete_pbx_audio**](ConversationApi.md#delete_pbx_audio) | **DELETE** /conversation/pbx/audio/{conversationPbxAudioUuid} | Delete pbx audio
[**delete_pbx_menu**](ConversationApi.md#delete_pbx_menu) | **DELETE** /conversation/pbx/menu/{conversationPbxMenuUuid} | Delete pbx menu
[**delete_pbx_phone_number**](ConversationApi.md#delete_pbx_phone_number) | **DELETE** /conversation/pbx/phone_number/{conversationPbxPhoneNumberUuid} | Delete pbx phoneNumber
[**delete_pbx_queue**](ConversationApi.md#delete_pbx_queue) | **DELETE** /conversation/pbx/queue/{conversationPbxQueueUuid} | Delete pbx queue
[**delete_pbx_queue_voicemail**](ConversationApi.md#delete_pbx_queue_voicemail) | **DELETE** /conversation/pbx/queues/{queue_uuid}/voicemails/{recording_sid} | Delete Queue Voicemail
[**delete_pbx_time_based**](ConversationApi.md#delete_pbx_time_based) | **DELETE** /conversation/pbx/time_based/{conversationPbxTimeBasedUuid} | Delete pbx timeBased
[**delete_pbx_time_range**](ConversationApi.md#delete_pbx_time_range) | **DELETE** /conversation/pbx/time_range/{conversationPbxTimeRangeUuid} | Delete pbx timeRange
[**delete_pbx_voicemail_mailbox**](ConversationApi.md#delete_pbx_voicemail_mailbox) | **DELETE** /conversation/pbx/voicemail_mailbox/{conversationPbxVoicemailMailboxUuid} | Delete pbx voicemailMailbox
[**get_agent_keep_alive**](ConversationApi.md#get_agent_keep_alive) | **GET** /conversation/agent/keepalive | Agent keep alive
[**get_agent_profile**](ConversationApi.md#get_agent_profile) | **GET** /conversation/agent/profile | Get agent profile
[**get_agent_websocket_authorization**](ConversationApi.md#get_agent_websocket_authorization) | **PUT** /conversation/agent/auth | Get agent websocket authorization
[**get_conversation**](ConversationApi.md#get_conversation) | **GET** /conversation/conversations/{conversation_uuid} | Retrieve a conversation
[**get_conversation_canned_messages**](ConversationApi.md#get_conversation_canned_messages) | **GET** /conversation/canned_messages | Retrieve a list of canned messages ordered by short_code
[**get_conversation_context**](ConversationApi.md#get_conversation_context) | **PUT** /conversation/conversations/{conversation_uuid}/context | Get a webchat conversation context
[**get_conversation_department_member_list**](ConversationApi.md#get_conversation_department_member_list) | **GET** /conversation/department_members | Retrieve a list of possible department members
[**get_conversation_departments**](ConversationApi.md#get_conversation_departments) | **GET** /conversation/departments | Retrieve a list of departments ordered by name
[**get_conversation_engagement**](ConversationApi.md#get_conversation_engagement) | **GET** /conversation/engagements/{conversation_engagement_oid} | Retrieve an engagement
[**get_conversation_engagements**](ConversationApi.md#get_conversation_engagements) | **GET** /conversation/engagements | Retrieve a list of engagements ordered by name
[**get_conversation_messages**](ConversationApi.md#get_conversation_messages) | **GET** /conversation/conversations/{conversation_uuid}/messages/{since} | Retrieve conversation messages
[**get_conversation_multimedia_upload_url**](ConversationApi.md#get_conversation_multimedia_upload_url) | **GET** /conversation/upload_url/{extension} | Get a presigned conversation multimedia upload URL
[**get_conversation_pbx_audio_upload_url**](ConversationApi.md#get_conversation_pbx_audio_upload_url) | **GET** /conversation/pbx/audio/upload_url/{extension} | Get a pre-signed conversation multimedia upload URL
[**get_conversation_pbx_customer_snapshot**](ConversationApi.md#get_conversation_pbx_customer_snapshot) | **POST** /conversation/pbx/customer_snapshot | Get orders and customer information for a phone number
[**get_conversation_permissions**](ConversationApi.md#get_conversation_permissions) | **GET** /conversation/permissions | Retrieve conversation permissions
[**get_conversation_webchat_queue_statuses**](ConversationApi.md#get_conversation_webchat_queue_statuses) | **GET** /conversation/conversations/queues/statuses | Retrieve a conversation webchat queue statuses
[**get_conversations**](ConversationApi.md#get_conversations) | **GET** /conversation/conversations | Retrieve a list of conversation summaries newest to oldest
[**get_conversations_autocomplete**](ConversationApi.md#get_conversations_autocomplete) | **POST** /conversation/conversations/autocomplete | Retrieve a list of matching terms for a search field
[**get_conversations_search**](ConversationApi.md#get_conversations_search) | **POST** /conversation/conversations/search | Search conversations
[**get_locations_for_engagement**](ConversationApi.md#get_locations_for_engagement) | **POST** /conversation/locations | Get location data for engagement configuration
[**get_pbx_agent**](ConversationApi.md#get_pbx_agent) | **GET** /conversation/pbx/agent/{conversationPbxAgentUuid} | Get pbx agent
[**get_pbx_agent_voicemail**](ConversationApi.md#get_pbx_agent_voicemail) | **GET** /conversation/pbx/agent/voicemails/{recording_sid} | Get Agent Voicemail
[**get_pbx_agent_voicemails**](ConversationApi.md#get_pbx_agent_voicemails) | **GET** /conversation/pbx/agent/voicemails | Get Agent Voicemails
[**get_pbx_agents**](ConversationApi.md#get_pbx_agents) | **GET** /conversation/pbx/agent | Get pbx agents
[**get_pbx_audio**](ConversationApi.md#get_pbx_audio) | **GET** /conversation/pbx/audio/{conversationPbxAudioUuid} | Get pbx audio
[**get_pbx_audio_usage**](ConversationApi.md#get_pbx_audio_usage) | **GET** /conversation/pbx/audio/{conversationPbxAudioUuid}/usage | Get pbx audio usage
[**get_pbx_audios**](ConversationApi.md#get_pbx_audios) | **GET** /conversation/pbx/audio | Get pbx audios
[**get_pbx_menu**](ConversationApi.md#get_pbx_menu) | **GET** /conversation/pbx/menu/{conversationPbxMenuUuid} | Get pbx menu
[**get_pbx_menus**](ConversationApi.md#get_pbx_menus) | **GET** /conversation/pbx/menu | Get pbx menus
[**get_pbx_phone_number**](ConversationApi.md#get_pbx_phone_number) | **GET** /conversation/pbx/phone_number/{conversationPbxPhoneNumberUuid} | Get pbx phoneNumber
[**get_pbx_phone_numbers**](ConversationApi.md#get_pbx_phone_numbers) | **GET** /conversation/pbx/phone_number | Get pbx phoneNumbers
[**get_pbx_queue**](ConversationApi.md#get_pbx_queue) | **GET** /conversation/pbx/queue/{conversationPbxQueueUuid} | Get pbx queue
[**get_pbx_queue_voicemail**](ConversationApi.md#get_pbx_queue_voicemail) | **GET** /conversation/pbx/queues/{queue_uuid}/voicemails/{recording_sid} | Get Queue Voicemail
[**get_pbx_queue_voicemails**](ConversationApi.md#get_pbx_queue_voicemails) | **GET** /conversation/pbx/queues/{queue_uuid}/voicemails | Get Queue Voicemails
[**get_pbx_queues**](ConversationApi.md#get_pbx_queues) | **GET** /conversation/pbx/queue | Get pbx queues
[**get_pbx_time_based**](ConversationApi.md#get_pbx_time_based) | **GET** /conversation/pbx/time_based/{conversationPbxTimeBasedUuid} | Get pbx timeBased
[**get_pbx_time_baseds**](ConversationApi.md#get_pbx_time_baseds) | **GET** /conversation/pbx/time_based | Get pbx timeBaseds
[**get_pbx_time_range**](ConversationApi.md#get_pbx_time_range) | **GET** /conversation/pbx/time_range/{conversationPbxTimeRangeUuid} | Get pbx timeRange
[**get_pbx_time_ranges**](ConversationApi.md#get_pbx_time_ranges) | **GET** /conversation/pbx/time_range | Get pbx timeRanges
[**get_pbx_voicemail_mailbox**](ConversationApi.md#get_pbx_voicemail_mailbox) | **GET** /conversation/pbx/voicemail_mailbox/{conversationPbxVoicemailMailboxUuid} | Get pbx voicemailMailbox
[**get_pbx_voicemail_mailboxes**](ConversationApi.md#get_pbx_voicemail_mailboxes) | **GET** /conversation/pbx/voicemail_mailbox | Get pbx voicemailMailboxes
[**insert_conversation_canned_message**](ConversationApi.md#insert_conversation_canned_message) | **POST** /conversation/canned_messages | Insert a canned message
[**insert_conversation_department**](ConversationApi.md#insert_conversation_department) | **POST** /conversation/departments | Insert a department
[**insert_conversation_engagement**](ConversationApi.md#insert_conversation_engagement) | **POST** /conversation/engagements | Insert a engagement
[**insert_pbx_agent**](ConversationApi.md#insert_pbx_agent) | **POST** /conversation/pbx/agent | Insert pbx agent
[**insert_pbx_audio**](ConversationApi.md#insert_pbx_audio) | **POST** /conversation/pbx/audio | Insert pbx audio
[**insert_pbx_menu**](ConversationApi.md#insert_pbx_menu) | **POST** /conversation/pbx/menu | Insert pbx menu
[**insert_pbx_phone_number**](ConversationApi.md#insert_pbx_phone_number) | **POST** /conversation/pbx/phone_number | Insert pbx phoneNumber
[**insert_pbx_queue**](ConversationApi.md#insert_pbx_queue) | **POST** /conversation/pbx/queue | Insert pbx queue
[**insert_pbx_time_based**](ConversationApi.md#insert_pbx_time_based) | **POST** /conversation/pbx/time_based | Insert pbx timeBased
[**insert_pbx_time_range**](ConversationApi.md#insert_pbx_time_range) | **POST** /conversation/pbx/time_range | Insert pbx timeRange
[**insert_pbx_voicemail_mailbox**](ConversationApi.md#insert_pbx_voicemail_mailbox) | **POST** /conversation/pbx/voicemail_mailbox | Insert pbx voicemailMailbox
[**join_conversation**](ConversationApi.md#join_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/join | Join a conversation
[**leave_conversation**](ConversationApi.md#leave_conversation) | **DELETE** /conversation/conversations/{conversation_uuid}/leave | Leave a conversation
[**listened_pbx_agent_voicemail**](ConversationApi.md#listened_pbx_agent_voicemail) | **GET** /conversation/pbx/agent/voicemails/{recording_sid}/listened | Listened Agent Voicemail
[**listened_pbx_queue_voicemail**](ConversationApi.md#listened_pbx_queue_voicemail) | **GET** /conversation/pbx/queues/{queue_uuid}/voicemails/{recording_sid}/listened | Listened Queue Voicemail
[**mark_read_conversation**](ConversationApi.md#mark_read_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/markread | Mark a conversation as read
[**reset_conversation_pbx_queue_statistics**](ConversationApi.md#reset_conversation_pbx_queue_statistics) | **POST** /conversation/pbx/queues/{queue_uuid}/reset_statistics | reset statistics within the queue
[**search_conversation_canned_messages**](ConversationApi.md#search_conversation_canned_messages) | **POST** /conversation/canned_messages/search | Search for canned messages by short_code
[**sms_unsubscribe_conversation**](ConversationApi.md#sms_unsubscribe_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/sms_unsubscribe | Unsubscribe any SMS participants in this conversation
[**start_conversation**](ConversationApi.md#start_conversation) | **PUT** /conversation/conversations | Start a conversation
[**update_agent_profile**](ConversationApi.md#update_agent_profile) | **PUT** /conversation/agent/profile | Update agent profile
[**update_conversation_canned_message**](ConversationApi.md#update_conversation_canned_message) | **PUT** /conversation/canned_messages/{conversation_canned_message_oid} | Update a canned message
[**update_conversation_department**](ConversationApi.md#update_conversation_department) | **PUT** /conversation/departments/{conversation_department_oid} | Update a department
[**update_conversation_engagement**](ConversationApi.md#update_conversation_engagement) | **PUT** /conversation/engagements/{conversation_engagement_oid} | Update a engagement
[**update_conversation_webchat_queue_status**](ConversationApi.md#update_conversation_webchat_queue_status) | **PUT** /conversation/conversations/queues/{queue_name}/status | Update status within the queue
[**update_pbx_agent**](ConversationApi.md#update_pbx_agent) | **PUT** /conversation/pbx/agent/{conversationPbxAgentUuid} | Update pbx agent
[**update_pbx_audio**](ConversationApi.md#update_pbx_audio) | **PUT** /conversation/pbx/audio/{conversationPbxAudioUuid} | Update pbx audio
[**update_pbx_menu**](ConversationApi.md#update_pbx_menu) | **PUT** /conversation/pbx/menu/{conversationPbxMenuUuid} | Update pbx menu
[**update_pbx_phone_number**](ConversationApi.md#update_pbx_phone_number) | **PUT** /conversation/pbx/phone_number/{conversationPbxPhoneNumberUuid} | Update pbx phoneNumber
[**update_pbx_queue**](ConversationApi.md#update_pbx_queue) | **PUT** /conversation/pbx/queue/{conversationPbxQueueUuid} | Update pbx queue
[**update_pbx_time_based**](ConversationApi.md#update_pbx_time_based) | **PUT** /conversation/pbx/time_based/{conversationPbxTimeBasedUuid} | Update pbx timeBased
[**update_pbx_time_range**](ConversationApi.md#update_pbx_time_range) | **PUT** /conversation/pbx/time_range/{conversationPbxTimeRangeUuid} | Update pbx timeRange
[**update_pbx_voicemail_mailbox**](ConversationApi.md#update_pbx_voicemail_mailbox) | **PUT** /conversation/pbx/voicemail_mailbox/{conversationPbxVoicemailMailboxUuid} | Update pbx voicemailMailbox


# **delete_conversation_canned_message**
> delete_conversation_canned_message(conversation_canned_message_oid)

Delete a conversation canned message

Delete a conversation canned message 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_canned_message_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a conversation canned message
        api_instance.delete_conversation_canned_message(conversation_canned_message_oid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_conversation_canned_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_canned_message_oid** | **int**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_department**
> delete_department(conversation_department_oid)

Delete a conversation department

Delete a conversation department 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_department_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a conversation department
        api_instance.delete_department(conversation_department_oid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_department: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_department_oid** | **int**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_engagement**
> delete_engagement(conversation_engagement_oid)

Delete a conversation engagement

Delete a conversation engagement 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_engagement_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a conversation engagement
        api_instance.delete_engagement(conversation_engagement_oid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_engagement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_engagement_oid** | **int**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_agent**
> ConversationPbxAgentResponse delete_pbx_agent(conversation_pbx_agent_uuid)

Delete pbx agent

Delete a pbx agent 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_agent_response import ConversationPbxAgentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_agent_uuid = "conversationPbxAgentUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx agent
        api_response = api_instance.delete_pbx_agent(conversation_pbx_agent_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_agent_uuid** | **str**|  |

### Return type

[**ConversationPbxAgentResponse**](ConversationPbxAgentResponse.md)

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

# **delete_pbx_agent_voicemail**
> delete_pbx_agent_voicemail(recording_sid)

Delete Agent Voicemail

Delete pbx agent Voicemail 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    recording_sid = "recording_sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Agent Voicemail
        api_instance.delete_pbx_agent_voicemail(recording_sid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_agent_voicemail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_sid** | **str**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_audio**
> ConversationPbxAudioResponse delete_pbx_audio(conversation_pbx_audio_uuid)

Delete pbx audio

Delete a pbx audio 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_audio_response import ConversationPbxAudioResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_audio_uuid = "conversationPbxAudioUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx audio
        api_response = api_instance.delete_pbx_audio(conversation_pbx_audio_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_audio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_audio_uuid** | **str**|  |

### Return type

[**ConversationPbxAudioResponse**](ConversationPbxAudioResponse.md)

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

# **delete_pbx_menu**
> ConversationPbxMenuResponse delete_pbx_menu(conversation_pbx_menu_uuid)

Delete pbx menu

Delete a pbx menu 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_menu_response import ConversationPbxMenuResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_menu_uuid = "conversationPbxMenuUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx menu
        api_response = api_instance.delete_pbx_menu(conversation_pbx_menu_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_menu_uuid** | **str**|  |

### Return type

[**ConversationPbxMenuResponse**](ConversationPbxMenuResponse.md)

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

# **delete_pbx_phone_number**
> ConversationPbxPhoneNumberResponse delete_pbx_phone_number(conversation_pbx_phone_number_uuid)

Delete pbx phoneNumber

Delete a pbx phoneNumber 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_phone_number_response import ConversationPbxPhoneNumberResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_phone_number_uuid = "conversationPbxPhoneNumberUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx phoneNumber
        api_response = api_instance.delete_pbx_phone_number(conversation_pbx_phone_number_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_phone_number_uuid** | **str**|  |

### Return type

[**ConversationPbxPhoneNumberResponse**](ConversationPbxPhoneNumberResponse.md)

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

# **delete_pbx_queue**
> ConversationPbxQueueResponse delete_pbx_queue(conversation_pbx_queue_uuid)

Delete pbx queue

Delete a pbx queue 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_queue_response import ConversationPbxQueueResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_queue_uuid = "conversationPbxQueueUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx queue
        api_response = api_instance.delete_pbx_queue(conversation_pbx_queue_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_queue_uuid** | **str**|  |

### Return type

[**ConversationPbxQueueResponse**](ConversationPbxQueueResponse.md)

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

# **delete_pbx_queue_voicemail**
> delete_pbx_queue_voicemail(queue_uuid, recording_sid)

Delete Queue Voicemail

Delete pbx queue Voicemail 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    queue_uuid = "queue_uuid_example" # str | 
    recording_sid = "recording_sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Queue Voicemail
        api_instance.delete_pbx_queue_voicemail(queue_uuid, recording_sid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_queue_voicemail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  |
 **recording_sid** | **str**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_time_based**
> ConversationPbxTimeBasedResponse delete_pbx_time_based(conversation_pbx_time_based_uuid)

Delete pbx timeBased

Delete a pbx timeBased 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_based_response import ConversationPbxTimeBasedResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_time_based_uuid = "conversationPbxTimeBasedUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx timeBased
        api_response = api_instance.delete_pbx_time_based(conversation_pbx_time_based_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_time_based: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_time_based_uuid** | **str**|  |

### Return type

[**ConversationPbxTimeBasedResponse**](ConversationPbxTimeBasedResponse.md)

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

# **delete_pbx_time_range**
> ConversationPbxTimeRangeResponse delete_pbx_time_range(conversation_pbx_time_range_uuid)

Delete pbx timeRange

Delete a pbx timeRange 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_range_response import ConversationPbxTimeRangeResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_time_range_uuid = "conversationPbxTimeRangeUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx timeRange
        api_response = api_instance.delete_pbx_time_range(conversation_pbx_time_range_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_time_range: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_time_range_uuid** | **str**|  |

### Return type

[**ConversationPbxTimeRangeResponse**](ConversationPbxTimeRangeResponse.md)

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

# **delete_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse delete_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)

Delete pbx voicemailMailbox

Delete a pbx voicemailMailbox 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_voicemail_mailbox_response import ConversationPbxVoicemailMailboxResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_voicemail_mailbox_uuid = "conversationPbxVoicemailMailboxUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete pbx voicemailMailbox
        api_response = api_instance.delete_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->delete_pbx_voicemail_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_voicemail_mailbox_uuid** | **str**|  |

### Return type

[**ConversationPbxVoicemailMailboxResponse**](ConversationPbxVoicemailMailboxResponse.md)

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

# **get_agent_keep_alive**
> get_agent_keep_alive()

Agent keep alive

Called periodically by the conversation API to keep the session alive. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Agent keep alive
        api_instance.get_agent_keep_alive()
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_agent_keep_alive: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_profile**
> ConversationAgentProfileResponse get_agent_profile()

Get agent profile

Retrieve the agents profile 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_agent_profile_response import ConversationAgentProfileResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get agent profile
        api_response = api_instance.get_agent_profile()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_agent_profile: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationAgentProfileResponse**](ConversationAgentProfileResponse.md)

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

# **get_agent_websocket_authorization**
> ConversationAgentAuthResponse get_agent_websocket_authorization()

Get agent websocket authorization

Retrieve a JWT to authorize an agent to make a websocket connection. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_agent_auth_response import ConversationAgentAuthResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get agent websocket authorization
        api_response = api_instance.get_agent_websocket_authorization()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_agent_websocket_authorization: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationAgentAuthResponse**](ConversationAgentAuthResponse.md)

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

# **get_conversation**
> ConversationResponse get_conversation(conversation_uuid)

Retrieve a conversation

Retrieve a conversation including the participants and messages 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_response import ConversationResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_uuid = "conversation_uuid_example" # str | 
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a conversation
        api_response = api_instance.get_conversation(conversation_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a conversation
        api_response = api_instance.get_conversation(conversation_uuid, limit=limit)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_conversation_canned_messages**
> ConversationCannedMessagesResponse get_conversation_canned_messages()

Retrieve a list of canned messages ordered by short_code

Retrieve a list of canned messages ordered by short_code 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_canned_messages_response import ConversationCannedMessagesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of canned messages ordered by short_code
        api_response = api_instance.get_conversation_canned_messages()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_canned_messages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationCannedMessagesResponse**](ConversationCannedMessagesResponse.md)

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

# **get_conversation_context**
> ConversationWebchatContext get_conversation_context(conversation_uuid)

Get a webchat conversation context

Get a webchat conversation context 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_webchat_context import ConversationWebchatContext
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_uuid = "conversation_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a webchat conversation context
        api_response = api_instance.get_conversation_context(conversation_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_conversation_department_member_list**
> ConversationDepartmentMembersResponse get_conversation_department_member_list()

Retrieve a list of possible department members

Retrieve a list of possible department members 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_department_members_response import ConversationDepartmentMembersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of possible department members
        api_response = api_instance.get_conversation_department_member_list()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_department_member_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationDepartmentMembersResponse**](ConversationDepartmentMembersResponse.md)

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

# **get_conversation_departments**
> ConversationDepartmentsResponse get_conversation_departments()

Retrieve a list of departments ordered by name

Retrieve a list of departments ordered by name 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_departments_response import ConversationDepartmentsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of departments ordered by name
        api_response = api_instance.get_conversation_departments()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_departments: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationDepartmentsResponse**](ConversationDepartmentsResponse.md)

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

# **get_conversation_engagement**
> ConversationEngagementResponse get_conversation_engagement(conversation_engagement_oid)

Retrieve an engagement

Retrieve an engagement 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_engagement_response import ConversationEngagementResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_engagement_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an engagement
        api_response = api_instance.get_conversation_engagement(conversation_engagement_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_engagement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_engagement_oid** | **int**|  |

### Return type

[**ConversationEngagementResponse**](ConversationEngagementResponse.md)

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

# **get_conversation_engagements**
> ConversationEngagementsResponse get_conversation_engagements()

Retrieve a list of engagements ordered by name

Retrieve a list of engagements ordered by name 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_engagements_response import ConversationEngagementsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of engagements ordered by name
        api_response = api_instance.get_conversation_engagements()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_engagements: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationEngagementsResponse**](ConversationEngagementsResponse.md)

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

# **get_conversation_messages**
> ConversationMessagesResponse get_conversation_messages(conversation_uuid, since)

Retrieve conversation messages

Retrieve conversation messages since a particular time 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_messages_response import ConversationMessagesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_uuid = "conversation_uuid_example" # str | 
    since = 1 # int | 
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve conversation messages
        api_response = api_instance.get_conversation_messages(conversation_uuid, since)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve conversation messages
        api_response = api_instance.get_conversation_messages(conversation_uuid, since, limit=limit)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_conversation_multimedia_upload_url**
> ConversationMultimediaUploadUrlResponse get_conversation_multimedia_upload_url(extension)

Get a presigned conversation multimedia upload URL

Get a presigned conversation multimedia upload URL 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_multimedia_upload_url_response import ConversationMultimediaUploadUrlResponse
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
        # Get a presigned conversation multimedia upload URL
        api_response = api_instance.get_conversation_multimedia_upload_url(extension)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **get_conversation_pbx_audio_upload_url**
> ConversationPbxAudioUploadUrlResponse get_conversation_pbx_audio_upload_url(extension)

Get a pre-signed conversation multimedia upload URL

Get a pre-signed conversation multimedia upload URL 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_audio_upload_url_response import ConversationPbxAudioUploadUrlResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    extension = "extension_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a pre-signed conversation multimedia upload URL
        api_response = api_instance.get_conversation_pbx_audio_upload_url(extension)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_pbx_audio_upload_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**|  |

### Return type

[**ConversationPbxAudioUploadUrlResponse**](ConversationPbxAudioUploadUrlResponse.md)

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

# **get_conversation_pbx_customer_snapshot**
> ConversationPbxCustomerSnapshotResponse get_conversation_pbx_customer_snapshot(pbx_customer_snapshot_request)

Get orders and customer information for a phone number

Retrieves all the orders, auto orders, and customer profile for a given phone number 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_customer_snapshot_request import ConversationPbxCustomerSnapshotRequest
from ultracart.model.conversation_pbx_customer_snapshot_response import ConversationPbxCustomerSnapshotResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_customer_snapshot_request = ConversationPbxCustomerSnapshotRequest(
        auto_order_expand="auto_order_expand_example",
        customer_expand="customer_expand_example",
        error=Error(
            developer_message="developer_message_example",
            error_code="error_code_example",
            more_info="more_info_example",
            object_id="object_id_example",
            user_message="user_message_example",
        ),
        metadata=ResponseMetadata(
            payload_name="payload_name_example",
            result_set=ResultSet(
                count=1,
                limit=1,
                more=True,
                next_offset=1,
                offset=1,
                total_records=1,
            ),
        ),
        order_expand="order_expand_example",
        phone_number="phone_number_example",
        success=True,
        warning=Warning(
            more_info="more_info_example",
            warning_message="warning_message_example",
        ),
    ) # ConversationPbxCustomerSnapshotRequest | Conversation pbx customer snapshot request

    # example passing only required values which don't have defaults set
    try:
        # Get orders and customer information for a phone number
        api_response = api_instance.get_conversation_pbx_customer_snapshot(pbx_customer_snapshot_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_pbx_customer_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_customer_snapshot_request** | [**ConversationPbxCustomerSnapshotRequest**](ConversationPbxCustomerSnapshotRequest.md)| Conversation pbx customer snapshot request |

### Return type

[**ConversationPbxCustomerSnapshotResponse**](ConversationPbxCustomerSnapshotResponse.md)

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

# **get_conversation_permissions**
> ConversationPermissionsResponse get_conversation_permissions()

Retrieve conversation permissions

Retrieve conversation permissions 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_permissions_response import ConversationPermissionsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve conversation permissions
        api_response = api_instance.get_conversation_permissions()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_permissions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPermissionsResponse**](ConversationPermissionsResponse.md)

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

# **get_conversation_webchat_queue_statuses**
> ConversationWebchatQueueStatusesResponse get_conversation_webchat_queue_statuses()

Retrieve a conversation webchat queue statuses

Retrieve a conversation webchat queue statuses including agent status and queue entries 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_webchat_queue_statuses_response import ConversationWebchatQueueStatusesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a conversation webchat queue statuses
        api_response = api_instance.get_conversation_webchat_queue_statuses()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversation_webchat_queue_statuses: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationWebchatQueueStatusesResponse**](ConversationWebchatQueueStatusesResponse.md)

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

# **get_conversations**
> ConversationsResponse get_conversations()

Retrieve a list of conversation summaries newest to oldest

Retrieve a list of conversation summaries that are ordered newest to oldest, include the most recent message and whether its been read. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversations_response import ConversationsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    medium = "medium_example" # str |  (optional)
    before = "before_example" # str |  (optional)
    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of conversation summaries newest to oldest
        api_response = api_instance.get_conversations(medium=medium, before=before, limit=limit, offset=offset)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium** | **str**|  | [optional]
 **before** | **str**|  | [optional]
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0

### Return type

[**ConversationsResponse**](ConversationsResponse.md)

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

# **get_conversations_autocomplete**
> ConversationAutocompleteResponse get_conversations_autocomplete(autocomplete_request)

Retrieve a list of matching terms for a search field

Retrieve a list of matching terms for a search field 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_autocomplete_response import ConversationAutocompleteResponse
from ultracart.model.conversation_autocomplete_request import ConversationAutocompleteRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    autocomplete_request = ConversationAutocompleteRequest(
        field="field_example",
        term="term_example",
    ) # ConversationAutocompleteRequest | Autocomplete Request

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of matching terms for a search field
        api_response = api_instance.get_conversations_autocomplete(autocomplete_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversations_autocomplete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autocomplete_request** | [**ConversationAutocompleteRequest**](ConversationAutocompleteRequest.md)| Autocomplete Request |

### Return type

[**ConversationAutocompleteResponse**](ConversationAutocompleteResponse.md)

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

# **get_conversations_search**
> ConversationSearchResponse get_conversations_search(search_request)

Search conversations

Search conversations 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_search_response import ConversationSearchResponse
from ultracart.model.conversation_search_request import ConversationSearchRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    search_request = ConversationSearchRequest(
        date_end="date_end_example",
        date_start="date_start_example",
        email_filter="email_filter_example",
        language_filter="language_filter_example",
        medium_filter="medium_filter_example",
        order_by_newest=True,
        order_by_oldest=True,
        range_begin=1,
        range_end=1,
        sms_phone_number_filter="sms_phone_number_filter_example",
        text_search="text_search_example",
        visible_filter=True,
    ) # ConversationSearchRequest | Search Request

    # example passing only required values which don't have defaults set
    try:
        # Search conversations
        api_response = api_instance.get_conversations_search(search_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_conversations_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**ConversationSearchRequest**](ConversationSearchRequest.md)| Search Request |

### Return type

[**ConversationSearchResponse**](ConversationSearchResponse.md)

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

# **get_locations_for_engagement**
> ConversationLocationsResponse get_locations_for_engagement()

Get location data for engagement configuration

Get location data for engagement configuration 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_locations_response import ConversationLocationsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get location data for engagement configuration
        api_response = api_instance.get_locations_for_engagement()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_locations_for_engagement: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationLocationsResponse**](ConversationLocationsResponse.md)

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

# **get_pbx_agent**
> ConversationPbxAgentResponse get_pbx_agent(conversation_pbx_agent_uuid)

Get pbx agent

Retrieve a pbx agent 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_agent_response import ConversationPbxAgentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_agent_uuid = "conversationPbxAgentUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx agent
        api_response = api_instance.get_pbx_agent(conversation_pbx_agent_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_agent_uuid** | **str**|  |

### Return type

[**ConversationPbxAgentResponse**](ConversationPbxAgentResponse.md)

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

# **get_pbx_agent_voicemail**
> ConversationPbxVoicemailMessageResponse get_pbx_agent_voicemail(recording_sid)

Get Agent Voicemail

Retrieve pbx agent Voicemail 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_voicemail_message_response import ConversationPbxVoicemailMessageResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    recording_sid = "recording_sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Agent Voicemail
        api_response = api_instance.get_pbx_agent_voicemail(recording_sid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_agent_voicemail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_sid** | **str**|  |

### Return type

[**ConversationPbxVoicemailMessageResponse**](ConversationPbxVoicemailMessageResponse.md)

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

# **get_pbx_agent_voicemails**
> ConversationPbxVoicemailMessageSummariesResponse get_pbx_agent_voicemails()

Get Agent Voicemails

Retrieve pbx agent Voicemails 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_voicemail_message_summaries_response import ConversationPbxVoicemailMessageSummariesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get Agent Voicemails
        api_response = api_instance.get_pbx_agent_voicemails()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_agent_voicemails: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxVoicemailMessageSummariesResponse**](ConversationPbxVoicemailMessageSummariesResponse.md)

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

# **get_pbx_agents**
> ConversationPbxAgentsResponse get_pbx_agents()

Get pbx agents

Retrieve pbx agents 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_agents_response import ConversationPbxAgentsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx agents
        api_response = api_instance.get_pbx_agents()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_agents: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxAgentsResponse**](ConversationPbxAgentsResponse.md)

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

# **get_pbx_audio**
> ConversationPbxAudioResponse get_pbx_audio(conversation_pbx_audio_uuid)

Get pbx audio

Retrieve a pbx audio 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_audio_response import ConversationPbxAudioResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_audio_uuid = "conversationPbxAudioUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx audio
        api_response = api_instance.get_pbx_audio(conversation_pbx_audio_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_audio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_audio_uuid** | **str**|  |

### Return type

[**ConversationPbxAudioResponse**](ConversationPbxAudioResponse.md)

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

# **get_pbx_audio_usage**
> ConversationPbxAudioUsageResponse get_pbx_audio_usage(conversation_pbx_audio_uuid)

Get pbx audio usage

Retrieve a pbx audio usage 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_audio_usage_response import ConversationPbxAudioUsageResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_audio_uuid = "conversationPbxAudioUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx audio usage
        api_response = api_instance.get_pbx_audio_usage(conversation_pbx_audio_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_audio_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_audio_uuid** | **str**|  |

### Return type

[**ConversationPbxAudioUsageResponse**](ConversationPbxAudioUsageResponse.md)

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

# **get_pbx_audios**
> ConversationPbxAudiosResponse get_pbx_audios()

Get pbx audios

Retrieve pbx audios 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_audios_response import ConversationPbxAudiosResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx audios
        api_response = api_instance.get_pbx_audios()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_audios: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxAudiosResponse**](ConversationPbxAudiosResponse.md)

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

# **get_pbx_menu**
> ConversationPbxMenuResponse get_pbx_menu(conversation_pbx_menu_uuid)

Get pbx menu

Retrieve a pbx menu 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_menu_response import ConversationPbxMenuResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_menu_uuid = "conversationPbxMenuUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx menu
        api_response = api_instance.get_pbx_menu(conversation_pbx_menu_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_menu_uuid** | **str**|  |

### Return type

[**ConversationPbxMenuResponse**](ConversationPbxMenuResponse.md)

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

# **get_pbx_menus**
> ConversationPbxMenusResponse get_pbx_menus()

Get pbx menus

Retrieve pbx menus 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_menus_response import ConversationPbxMenusResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx menus
        api_response = api_instance.get_pbx_menus()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_menus: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxMenusResponse**](ConversationPbxMenusResponse.md)

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

# **get_pbx_phone_number**
> ConversationPbxPhoneNumberResponse get_pbx_phone_number(conversation_pbx_phone_number_uuid)

Get pbx phoneNumber

Retrieve a pbx phoneNumber 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_phone_number_response import ConversationPbxPhoneNumberResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_phone_number_uuid = "conversationPbxPhoneNumberUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx phoneNumber
        api_response = api_instance.get_pbx_phone_number(conversation_pbx_phone_number_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_phone_number_uuid** | **str**|  |

### Return type

[**ConversationPbxPhoneNumberResponse**](ConversationPbxPhoneNumberResponse.md)

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

# **get_pbx_phone_numbers**
> ConversationPbxPhoneNumbersResponse get_pbx_phone_numbers()

Get pbx phoneNumbers

Retrieve pbx phoneNumbers 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_phone_numbers_response import ConversationPbxPhoneNumbersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx phoneNumbers
        api_response = api_instance.get_pbx_phone_numbers()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_phone_numbers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxPhoneNumbersResponse**](ConversationPbxPhoneNumbersResponse.md)

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

# **get_pbx_queue**
> ConversationPbxQueueResponse get_pbx_queue(conversation_pbx_queue_uuid)

Get pbx queue

Retrieve a pbx queue 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_queue_response import ConversationPbxQueueResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_queue_uuid = "conversationPbxQueueUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx queue
        api_response = api_instance.get_pbx_queue(conversation_pbx_queue_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_queue_uuid** | **str**|  |

### Return type

[**ConversationPbxQueueResponse**](ConversationPbxQueueResponse.md)

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

# **get_pbx_queue_voicemail**
> ConversationPbxVoicemailMessageResponse get_pbx_queue_voicemail(queue_uuid, recording_sid)

Get Queue Voicemail

Retrieve pbx queue Voicemail 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_voicemail_message_response import ConversationPbxVoicemailMessageResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    queue_uuid = "queue_uuid_example" # str | 
    recording_sid = "recording_sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Queue Voicemail
        api_response = api_instance.get_pbx_queue_voicemail(queue_uuid, recording_sid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_queue_voicemail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  |
 **recording_sid** | **str**|  |

### Return type

[**ConversationPbxVoicemailMessageResponse**](ConversationPbxVoicemailMessageResponse.md)

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

# **get_pbx_queue_voicemails**
> ConversationPbxVoicemailMessageSummariesResponse get_pbx_queue_voicemails(queue_uuid)

Get Queue Voicemails

Retrieve pbx queue voicemails 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_voicemail_message_summaries_response import ConversationPbxVoicemailMessageSummariesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    queue_uuid = "queue_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Queue Voicemails
        api_response = api_instance.get_pbx_queue_voicemails(queue_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_queue_voicemails: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  |

### Return type

[**ConversationPbxVoicemailMessageSummariesResponse**](ConversationPbxVoicemailMessageSummariesResponse.md)

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

# **get_pbx_queues**
> ConversationPbxQueuesResponse get_pbx_queues()

Get pbx queues

Retrieve pbx queues 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_queues_response import ConversationPbxQueuesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx queues
        api_response = api_instance.get_pbx_queues()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_queues: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxQueuesResponse**](ConversationPbxQueuesResponse.md)

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

# **get_pbx_time_based**
> ConversationPbxTimeBasedResponse get_pbx_time_based(conversation_pbx_time_based_uuid)

Get pbx timeBased

Retrieve a pbx timeBased 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_based_response import ConversationPbxTimeBasedResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_time_based_uuid = "conversationPbxTimeBasedUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx timeBased
        api_response = api_instance.get_pbx_time_based(conversation_pbx_time_based_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_time_based: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_time_based_uuid** | **str**|  |

### Return type

[**ConversationPbxTimeBasedResponse**](ConversationPbxTimeBasedResponse.md)

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

# **get_pbx_time_baseds**
> ConversationPbxTimeBasedsResponse get_pbx_time_baseds()

Get pbx timeBaseds

Retrieve pbx timeBaseds 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_baseds_response import ConversationPbxTimeBasedsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx timeBaseds
        api_response = api_instance.get_pbx_time_baseds()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_time_baseds: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxTimeBasedsResponse**](ConversationPbxTimeBasedsResponse.md)

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

# **get_pbx_time_range**
> ConversationPbxTimeRangeResponse get_pbx_time_range(conversation_pbx_time_range_uuid)

Get pbx timeRange

Retrieve a pbx timeRange 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_range_response import ConversationPbxTimeRangeResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_time_range_uuid = "conversationPbxTimeRangeUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx timeRange
        api_response = api_instance.get_pbx_time_range(conversation_pbx_time_range_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_time_range: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_time_range_uuid** | **str**|  |

### Return type

[**ConversationPbxTimeRangeResponse**](ConversationPbxTimeRangeResponse.md)

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

# **get_pbx_time_ranges**
> ConversationPbxTimeRangesResponse get_pbx_time_ranges()

Get pbx timeRanges

Retrieve pbx timeRanges 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_time_ranges_response import ConversationPbxTimeRangesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx timeRanges
        api_response = api_instance.get_pbx_time_ranges()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_time_ranges: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxTimeRangesResponse**](ConversationPbxTimeRangesResponse.md)

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

# **get_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse get_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)

Get pbx voicemailMailbox

Retrieve a pbx voicemailMailbox 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_voicemail_mailbox_response import ConversationPbxVoicemailMailboxResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_voicemail_mailbox_uuid = "conversationPbxVoicemailMailboxUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get pbx voicemailMailbox
        api_response = api_instance.get_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_voicemail_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_voicemail_mailbox_uuid** | **str**|  |

### Return type

[**ConversationPbxVoicemailMailboxResponse**](ConversationPbxVoicemailMailboxResponse.md)

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

# **get_pbx_voicemail_mailboxes**
> ConversationPbxVoicemailMailboxesResponse get_pbx_voicemail_mailboxes()

Get pbx voicemailMailboxes

Retrieve pbx voicemailMailboxes 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_voicemail_mailboxes_response import ConversationPbxVoicemailMailboxesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get pbx voicemailMailboxes
        api_response = api_instance.get_pbx_voicemail_mailboxes()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->get_pbx_voicemail_mailboxes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxVoicemailMailboxesResponse**](ConversationPbxVoicemailMailboxesResponse.md)

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

# **insert_conversation_canned_message**
> ConversationCannedMessageResponse insert_conversation_canned_message(canned_message)

Insert a canned message

Insert a canned message 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_canned_message import ConversationCannedMessage
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_canned_message_response import ConversationCannedMessageResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    canned_message = ConversationCannedMessage(
        canned_message="canned_message_example",
        conversation_canned_message_oid=1,
        conversation_department_oids=[
            1,
        ],
        short_code="short_code_example",
    ) # ConversationCannedMessage | Canned message

    # example passing only required values which don't have defaults set
    try:
        # Insert a canned message
        api_response = api_instance.insert_conversation_canned_message(canned_message)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_conversation_canned_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canned_message** | [**ConversationCannedMessage**](ConversationCannedMessage.md)| Canned message |

### Return type

[**ConversationCannedMessageResponse**](ConversationCannedMessageResponse.md)

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

# **insert_conversation_department**
> ConversationDepartmentResponse insert_conversation_department(department)

Insert a department

Insert a department 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_department import ConversationDepartment
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_department_response import ConversationDepartmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    department = ConversationDepartment(
        conversation_department_oid=1,
        department_name="department_name_example",
        members=[
            ConversationDepartmentMember(
                member=True,
                name="name_example",
                user_id=1,
            ),
        ],
        merchant_id="merchant_id_example",
        settings={},
    ) # ConversationDepartment | Department

    # example passing only required values which don't have defaults set
    try:
        # Insert a department
        api_response = api_instance.insert_conversation_department(department)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_conversation_department: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department** | [**ConversationDepartment**](ConversationDepartment.md)| Department |

### Return type

[**ConversationDepartmentResponse**](ConversationDepartmentResponse.md)

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

# **insert_conversation_engagement**
> ConversationEngagementResponse insert_conversation_engagement(engagement)

Insert a engagement

Insert a engagement 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_engagement_response import ConversationEngagementResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_engagement import ConversationEngagement
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    engagement = ConversationEngagement(
        active=True,
        conversation_engagement_oid=1,
        customer_greeting="customer_greeting_example",
        customer_initiated=True,
        department_oids=[
            1,
        ],
        engagement_name="engagement_name_example",
        equation=ConversationEngagementEquation(
            groups=[
                ConversationEngagementEquationGroup(
                    functions=[
                        ConversationEngagementEquationFunction(
                            any_page_url_logic="contains",
                            any_page_url_value="any_page_url_value_example",
                            current_page_url_logic="contains",
                            current_page_url_value="current_page_url_value_example",
                            customers_browsing_time_logic="is at least",
                            customers_browsing_time_seconds=1,
                            customers_location_country="customers_location_country_example",
                            customers_location_logic="is",
                            customers_location_state="customers_location_state_example",
                            number_of_viewed_pages_logic="is at least",
                            number_of_viewed_pages_value=1,
                            referring_website_logic="contains",
                            referring_website_value="referring_website_value_example",
                            type="current page url",
                        ),
                    ],
                ),
            ],
        ),
        time_on_page=1,
        visitor_type="all",
    ) # ConversationEngagement | Engagement

    # example passing only required values which don't have defaults set
    try:
        # Insert a engagement
        api_response = api_instance.insert_conversation_engagement(engagement)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_conversation_engagement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engagement** | [**ConversationEngagement**](ConversationEngagement.md)| Engagement |

### Return type

[**ConversationEngagementResponse**](ConversationEngagementResponse.md)

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

# **insert_pbx_agent**
> ConversationPbxAgentResponse insert_pbx_agent(pbx_agent)

Insert pbx agent

Insert a pbx agent 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_agent import ConversationPbxAgent
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_agent_response import ConversationPbxAgentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_agent = ConversationPbxAgent(
        cellphone="cellphone_example",
        conversation_pbx_agent_uuid="conversation_pbx_agent_uuid_example",
        conversation_pbx_voicemail_mailbox_uuid="conversation_pbx_voicemail_mailbox_uuid_example",
        forward_calls_to_cellphone=True,
        merchant_id="merchant_id_example",
        record_outgoing_automatically=True,
        twilio_taskrouter_worker_id="twilio_taskrouter_worker_id_example",
        user_id=1,
        voicemail=True,
    ) # ConversationPbxAgent | Pbx Agent

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx agent
        api_response = api_instance.insert_pbx_agent(pbx_agent)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_agent** | [**ConversationPbxAgent**](ConversationPbxAgent.md)| Pbx Agent |

### Return type

[**ConversationPbxAgentResponse**](ConversationPbxAgentResponse.md)

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

# **insert_pbx_audio**
> ConversationPbxAudioResponse insert_pbx_audio(pbx_audio)

Insert pbx audio

Insert a pbx audio 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_audio import ConversationPbxAudio
from ultracart.model.conversation_pbx_audio_response import ConversationPbxAudioResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_audio = ConversationPbxAudio(
        audio_s3_listing_key="audio_s3_listing_key_example",
        conversation_pbx_audio_uuid="conversation_pbx_audio_uuid_example",
        default_hold_music=True,
        description="description_example",
        filename="filename_example",
        merchant_id="merchant_id_example",
        mime_type="mime_type_example",
        url="url_example",
        user_id=1,
        version=1,
    ) # ConversationPbxAudio | Pbx Audio

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx audio
        api_response = api_instance.insert_pbx_audio(pbx_audio)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_audio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_audio** | [**ConversationPbxAudio**](ConversationPbxAudio.md)| Pbx Audio |

### Return type

[**ConversationPbxAudioResponse**](ConversationPbxAudioResponse.md)

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

# **insert_pbx_menu**
> ConversationPbxMenuResponse insert_pbx_menu(pbx_menu)

Insert pbx menu

Insert a pbx menu 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_menu import ConversationPbxMenu
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_menu_response import ConversationPbxMenuResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_menu = ConversationPbxMenu(
        allow_direct_extensions=True,
        conversation_pbx_menu_uuid="conversation_pbx_menu_uuid_example",
        default_action="default_action_example",
        default_action_target="default_action_target_example",
        mappings=[
            ConversationPbxMenuMapping(
                action="action_example",
                action_target="action_target_example",
                digits=1,
                speech="speech_example",
            ),
        ],
        merchant_id="merchant_id_example",
        name="name_example",
        play_audio_uuid="play_audio_uuid_example",
        say="say_example",
        timeout=1,
    ) # ConversationPbxMenu | Pbx Menu

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx menu
        api_response = api_instance.insert_pbx_menu(pbx_menu)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_menu** | [**ConversationPbxMenu**](ConversationPbxMenu.md)| Pbx Menu |

### Return type

[**ConversationPbxMenuResponse**](ConversationPbxMenuResponse.md)

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

# **insert_pbx_phone_number**
> ConversationPbxPhoneNumberResponse insert_pbx_phone_number(pbx_phone_number)

Insert pbx phoneNumber

Insert a pbx phoneNumber 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_phone_number import ConversationPbxPhoneNumber
from ultracart.model.conversation_pbx_phone_number_response import ConversationPbxPhoneNumberResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_phone_number = ConversationPbxPhoneNumber(
        action="action_example",
        action_target="action_target_example",
        conversation_pbx_time_range_uuid="conversation_pbx_time_range_uuid_example",
        merchant_id="merchant_id_example",
        phone_number="phone_number_example",
    ) # ConversationPbxPhoneNumber | Pbx PhoneNumber

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx phoneNumber
        api_response = api_instance.insert_pbx_phone_number(pbx_phone_number)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_phone_number** | [**ConversationPbxPhoneNumber**](ConversationPbxPhoneNumber.md)| Pbx PhoneNumber |

### Return type

[**ConversationPbxPhoneNumberResponse**](ConversationPbxPhoneNumberResponse.md)

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

# **insert_pbx_queue**
> ConversationPbxQueueResponse insert_pbx_queue(pbx_queue)

Insert pbx queue

Insert a pbx queue 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_queue import ConversationPbxQueue
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_queue_response import ConversationPbxQueueResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_queue = ConversationPbxQueue(
        announce_queue_position=True,
        conversation_pbx_queue_uuid="conversation_pbx_queue_uuid_example",
        conversation_voicemail_mailbox_uuid="conversation_voicemail_mailbox_uuid_example",
        hold_conversation_pbx_audio_uuid="hold_conversation_pbx_audio_uuid_example",
        max_hold_seconds=1,
        members=ConversationPbxQueueMembers(
            groups=[
                1,
            ],
            users=[
                1,
            ],
        ),
        merchant_id="merchant_id_example",
        name="name_example",
        no_agent_available_play_audio_uuid="no_agent_available_play_audio_uuid_example",
        no_agent_available_say="no_agent_available_say_example",
        no_agent_available_say_voice="no_agent_available_say_voice_example",
        play_audio_uuid="play_audio_uuid_example",
        record_call=True,
        say="say_example",
        say_voice="say_voice_example",
        twilio_taskrouter_workflow_sid="twilio_taskrouter_workflow_sid_example",
        twilio_workspace_queue_sid="twilio_workspace_queue_sid_example",
        voicemail=True,
        wait_critical_seconds=1,
        wait_warning_seconds=1,
        wrap_up_seconds=1,
    ) # ConversationPbxQueue | Pbx Queue

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx queue
        api_response = api_instance.insert_pbx_queue(pbx_queue)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_queue** | [**ConversationPbxQueue**](ConversationPbxQueue.md)| Pbx Queue |

### Return type

[**ConversationPbxQueueResponse**](ConversationPbxQueueResponse.md)

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

# **insert_pbx_time_based**
> ConversationPbxTimeBasedResponse insert_pbx_time_based(pbx_time_based)

Insert pbx timeBased

Insert a pbx timeBased 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_time_based import ConversationPbxTimeBased
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_based_response import ConversationPbxTimeBasedResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_time_based = ConversationPbxTimeBased(
        conversation_pbx_time_based_uuid="conversation_pbx_time_based_uuid_example",
        mapping_config=ConversationPbxTimeBasedMappingConfig(
            default=ConversationPbxTimeBasedMapping(
                action="action_example",
                action_target="action_target_example",
                name="name_example",
                time_range_uuid="time_range_uuid_example",
            ),
            mappings=[
                ConversationPbxTimeBasedMapping(
                    action="action_example",
                    action_target="action_target_example",
                    name="name_example",
                    time_range_uuid="time_range_uuid_example",
                ),
            ],
        ),
        merchant_id="merchant_id_example",
        time_based_name="time_based_name_example",
    ) # ConversationPbxTimeBased | Pbx TimeBased

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx timeBased
        api_response = api_instance.insert_pbx_time_based(pbx_time_based)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_time_based: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_time_based** | [**ConversationPbxTimeBased**](ConversationPbxTimeBased.md)| Pbx TimeBased |

### Return type

[**ConversationPbxTimeBasedResponse**](ConversationPbxTimeBasedResponse.md)

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

# **insert_pbx_time_range**
> ConversationPbxTimeRangeResponse insert_pbx_time_range(pbx_time_range)

Insert pbx timeRange

Insert a pbx timeRange 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_time_range import ConversationPbxTimeRange
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_range_response import ConversationPbxTimeRangeResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_time_range = ConversationPbxTimeRange(
        configs=[
            ConversationPbxTimeRangeConfig(
                end_date="end_date_example",
                end_day_of_week=1,
                end_time="end_time_example",
                start_date="start_date_example",
                start_day_of_week=1,
                start_time="start_time_example",
            ),
        ],
        conversation_pbx_time_range_uuid="conversation_pbx_time_range_uuid_example",
        merchant_id="merchant_id_example",
        time_range_name="time_range_name_example",
        timezone="timezone_example",
    ) # ConversationPbxTimeRange | Pbx TimeRange

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx timeRange
        api_response = api_instance.insert_pbx_time_range(pbx_time_range)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_time_range: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_time_range** | [**ConversationPbxTimeRange**](ConversationPbxTimeRange.md)| Pbx TimeRange |

### Return type

[**ConversationPbxTimeRangeResponse**](ConversationPbxTimeRangeResponse.md)

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

# **insert_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse insert_pbx_voicemail_mailbox(pbx_voicemail_mailbox)

Insert pbx voicemailMailbox

Insert a pbx voicemailMailbox 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_voicemail_mailbox_response import ConversationPbxVoicemailMailboxResponse
from ultracart.model.conversation_pbx_voicemail_mailbox import ConversationPbxVoicemailMailbox
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    pbx_voicemail_mailbox = ConversationPbxVoicemailMailbox(
        conversation_pbx_voicemail_mailbox_uuid="conversation_pbx_voicemail_mailbox_uuid_example",
        merchant_id="merchant_id_example",
        send_notices_to_email="send_notices_to_email_example",
        user_id=1,
        voicemail_follow_play_audio_uuid="voicemail_follow_play_audio_uuid_example",
        voicemail_followup_say="voicemail_followup_say_example",
        voicemail_mailbox_id="voicemail_mailbox_id_example",
        voicemail_mailbox_type="agent",
        voicemail_prompt_play_audio_uuid="voicemail_prompt_play_audio_uuid_example",
        voicemail_prompt_say="voicemail_prompt_say_example",
        voicemail_say_voice="voicemail_say_voice_example",
    ) # ConversationPbxVoicemailMailbox | Pbx VoicemailMailbox

    # example passing only required values which don't have defaults set
    try:
        # Insert pbx voicemailMailbox
        api_response = api_instance.insert_pbx_voicemail_mailbox(pbx_voicemail_mailbox)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->insert_pbx_voicemail_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_voicemail_mailbox** | [**ConversationPbxVoicemailMailbox**](ConversationPbxVoicemailMailbox.md)| Pbx VoicemailMailbox |

### Return type

[**ConversationPbxVoicemailMailboxResponse**](ConversationPbxVoicemailMailboxResponse.md)

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

# **join_conversation**
> join_conversation(conversation_uuid)

Join a conversation

Join a conversation 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_join_request import ConversationJoinRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_uuid = "conversation_uuid_example" # str | 
    join_request = ConversationJoinRequest(
        participant_language_iso_code="participant_language_iso_code_example",
    ) # ConversationJoinRequest | Join request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Join a conversation
        api_instance.join_conversation(conversation_uuid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->join_conversation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Join a conversation
        api_instance.join_conversation(conversation_uuid, join_request=join_request)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->join_conversation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **str**|  |
 **join_request** | [**ConversationJoinRequest**](ConversationJoinRequest.md)| Join request | [optional]

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

# **leave_conversation**
> leave_conversation(conversation_uuid)

Leave a conversation

Leave a conversation 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_uuid = "conversation_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Leave a conversation
        api_instance.leave_conversation(conversation_uuid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
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

# **listened_pbx_agent_voicemail**
> listened_pbx_agent_voicemail(recording_sid)

Listened Agent Voicemail

Listened pbx agent Voicemail 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    recording_sid = "recording_sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Listened Agent Voicemail
        api_instance.listened_pbx_agent_voicemail(recording_sid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->listened_pbx_agent_voicemail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_sid** | **str**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listened_pbx_queue_voicemail**
> listened_pbx_queue_voicemail(queue_uuid, recording_sid)

Listened Queue Voicemail

Listened pbx queue Voicemail 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    queue_uuid = "queue_uuid_example" # str | 
    recording_sid = "recording_sid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Listened Queue Voicemail
        api_instance.listened_pbx_queue_voicemail(queue_uuid, recording_sid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->listened_pbx_queue_voicemail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  |
 **recording_sid** | **str**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_read_conversation**
> mark_read_conversation(conversation_uuid)

Mark a conversation as read

Mark a conversation as read 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_uuid = "conversation_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Mark a conversation as read
        api_instance.mark_read_conversation(conversation_uuid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
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

# **reset_conversation_pbx_queue_statistics**
> reset_conversation_pbx_queue_statistics(queue_uuid)

reset statistics within the queue

reset statistics within the queue 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    queue_uuid = "queue_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # reset statistics within the queue
        api_instance.reset_conversation_pbx_queue_statistics(queue_uuid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->reset_conversation_pbx_queue_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  |

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
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_conversation_canned_messages**
> ConversationCannedMessagesResponse search_conversation_canned_messages(search_request)

Search for canned messages by short_code

Search for canned messages by short_code 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_canned_messages_search import ConversationCannedMessagesSearch
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_canned_messages_response import ConversationCannedMessagesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    search_request = ConversationCannedMessagesSearch(
        max_results=1,
        short_code="short_code_example",
    ) # ConversationCannedMessagesSearch | Search request

    # example passing only required values which don't have defaults set
    try:
        # Search for canned messages by short_code
        api_response = api_instance.search_conversation_canned_messages(search_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->search_conversation_canned_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**ConversationCannedMessagesSearch**](ConversationCannedMessagesSearch.md)| Search request |

### Return type

[**ConversationCannedMessagesResponse**](ConversationCannedMessagesResponse.md)

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

# **sms_unsubscribe_conversation**
> sms_unsubscribe_conversation(conversation_uuid)

Unsubscribe any SMS participants in this conversation

Unsubscribe any SMS participants in this conversation 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_uuid = "conversation_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unsubscribe any SMS participants in this conversation
        api_instance.sms_unsubscribe_conversation(conversation_uuid)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->sms_unsubscribe_conversation: %s\n" % e)
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

 - **Content-Type**: Not defined
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

# **start_conversation**
> ConversationStartResponse start_conversation(start_request)

Start a conversation

Start a new conversation 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_start_response import ConversationStartResponse
from ultracart.model.conversation_start_request import ConversationStartRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    start_request = ConversationStartRequest(
        add_conversation_participant_arns=[
            "add_conversation_participant_arns_example",
        ],
        conversation_arn="conversation_arn_example",
        conversation_webchat_queue_uuid="conversation_webchat_queue_uuid_example",
    ) # ConversationStartRequest | Start request

    # example passing only required values which don't have defaults set
    try:
        # Start a conversation
        api_response = api_instance.start_conversation(start_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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

# **update_agent_profile**
> ConversationAgentProfileResponse update_agent_profile(profile_request)

Update agent profile

Update agent profile 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_agent_profile import ConversationAgentProfile
from ultracart.model.conversation_agent_profile_response import ConversationAgentProfileResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    profile_request = ConversationAgentProfile(
        chat_limit=1,
        default_language_iso_code="default_language_iso_code_example",
        default_status="available",
        display_name="display_name_example",
        name="name_example",
        profile_image_upload_key="profile_image_upload_key_example",
        profile_image_url="profile_image_url_example",
    ) # ConversationAgentProfile | Profile request

    # example passing only required values which don't have defaults set
    try:
        # Update agent profile
        api_response = api_instance.update_agent_profile(profile_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_agent_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_request** | [**ConversationAgentProfile**](ConversationAgentProfile.md)| Profile request |

### Return type

[**ConversationAgentProfileResponse**](ConversationAgentProfileResponse.md)

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

# **update_conversation_canned_message**
> ConversationCannedMessageResponse update_conversation_canned_message(conversation_canned_message_oid, canned_message)

Update a canned message

Update a canned message 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_canned_message import ConversationCannedMessage
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_canned_message_response import ConversationCannedMessageResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_canned_message_oid = 1 # int | 
    canned_message = ConversationCannedMessage(
        canned_message="canned_message_example",
        conversation_canned_message_oid=1,
        conversation_department_oids=[
            1,
        ],
        short_code="short_code_example",
    ) # ConversationCannedMessage | Canned message

    # example passing only required values which don't have defaults set
    try:
        # Update a canned message
        api_response = api_instance.update_conversation_canned_message(conversation_canned_message_oid, canned_message)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_conversation_canned_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_canned_message_oid** | **int**|  |
 **canned_message** | [**ConversationCannedMessage**](ConversationCannedMessage.md)| Canned message |

### Return type

[**ConversationCannedMessageResponse**](ConversationCannedMessageResponse.md)

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

# **update_conversation_department**
> ConversationDepartmentResponse update_conversation_department(conversation_department_oid, department)

Update a department

Update a department 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_department import ConversationDepartment
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_department_response import ConversationDepartmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_department_oid = 1 # int | 
    department = ConversationDepartment(
        conversation_department_oid=1,
        department_name="department_name_example",
        members=[
            ConversationDepartmentMember(
                member=True,
                name="name_example",
                user_id=1,
            ),
        ],
        merchant_id="merchant_id_example",
        settings={},
    ) # ConversationDepartment | Department

    # example passing only required values which don't have defaults set
    try:
        # Update a department
        api_response = api_instance.update_conversation_department(conversation_department_oid, department)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_conversation_department: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_department_oid** | **int**|  |
 **department** | [**ConversationDepartment**](ConversationDepartment.md)| Department |

### Return type

[**ConversationDepartmentResponse**](ConversationDepartmentResponse.md)

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

# **update_conversation_engagement**
> ConversationEngagementResponse update_conversation_engagement(conversation_engagement_oid, engagement)

Update a engagement

Update a engagement 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_engagement_response import ConversationEngagementResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_engagement import ConversationEngagement
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_engagement_oid = 1 # int | 
    engagement = ConversationEngagement(
        active=True,
        conversation_engagement_oid=1,
        customer_greeting="customer_greeting_example",
        customer_initiated=True,
        department_oids=[
            1,
        ],
        engagement_name="engagement_name_example",
        equation=ConversationEngagementEquation(
            groups=[
                ConversationEngagementEquationGroup(
                    functions=[
                        ConversationEngagementEquationFunction(
                            any_page_url_logic="contains",
                            any_page_url_value="any_page_url_value_example",
                            current_page_url_logic="contains",
                            current_page_url_value="current_page_url_value_example",
                            customers_browsing_time_logic="is at least",
                            customers_browsing_time_seconds=1,
                            customers_location_country="customers_location_country_example",
                            customers_location_logic="is",
                            customers_location_state="customers_location_state_example",
                            number_of_viewed_pages_logic="is at least",
                            number_of_viewed_pages_value=1,
                            referring_website_logic="contains",
                            referring_website_value="referring_website_value_example",
                            type="current page url",
                        ),
                    ],
                ),
            ],
        ),
        time_on_page=1,
        visitor_type="all",
    ) # ConversationEngagement | Engagement

    # example passing only required values which don't have defaults set
    try:
        # Update a engagement
        api_response = api_instance.update_conversation_engagement(conversation_engagement_oid, engagement)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_conversation_engagement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_engagement_oid** | **int**|  |
 **engagement** | [**ConversationEngagement**](ConversationEngagement.md)| Engagement |

### Return type

[**ConversationEngagementResponse**](ConversationEngagementResponse.md)

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

# **update_conversation_webchat_queue_status**
> update_conversation_webchat_queue_status(queue_name, status_request)

Update status within the queue

Update status within the queue 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_webchat_queue_status_update_request import ConversationWebchatQueueStatusUpdateRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    queue_name = "queue_name_example" # str | 
    status_request = ConversationWebchatQueueStatusUpdateRequest(
        agent_status="available",
    ) # ConversationWebchatQueueStatusUpdateRequest | Status request

    # example passing only required values which don't have defaults set
    try:
        # Update status within the queue
        api_instance.update_conversation_webchat_queue_status(queue_name, status_request)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_agent**
> ConversationPbxAgentResponse update_pbx_agent(conversation_pbx_agent_uuid, pbx_agent)

Update pbx agent

Update a pbx agent 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_agent import ConversationPbxAgent
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_agent_response import ConversationPbxAgentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_agent_uuid = "conversationPbxAgentUuid_example" # str | 
    pbx_agent = ConversationPbxAgent(
        cellphone="cellphone_example",
        conversation_pbx_agent_uuid="conversation_pbx_agent_uuid_example",
        conversation_pbx_voicemail_mailbox_uuid="conversation_pbx_voicemail_mailbox_uuid_example",
        forward_calls_to_cellphone=True,
        merchant_id="merchant_id_example",
        record_outgoing_automatically=True,
        twilio_taskrouter_worker_id="twilio_taskrouter_worker_id_example",
        user_id=1,
        voicemail=True,
    ) # ConversationPbxAgent | Pbx Agent

    # example passing only required values which don't have defaults set
    try:
        # Update pbx agent
        api_response = api_instance.update_pbx_agent(conversation_pbx_agent_uuid, pbx_agent)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_agent_uuid** | **str**|  |
 **pbx_agent** | [**ConversationPbxAgent**](ConversationPbxAgent.md)| Pbx Agent |

### Return type

[**ConversationPbxAgentResponse**](ConversationPbxAgentResponse.md)

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

# **update_pbx_audio**
> ConversationPbxAudioResponse update_pbx_audio(conversation_pbx_audio_uuid, pbx_audio)

Update pbx audio

Update a pbx audio 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_audio import ConversationPbxAudio
from ultracart.model.conversation_pbx_audio_response import ConversationPbxAudioResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_audio_uuid = "conversationPbxAudioUuid_example" # str | 
    pbx_audio = ConversationPbxAudio(
        audio_s3_listing_key="audio_s3_listing_key_example",
        conversation_pbx_audio_uuid="conversation_pbx_audio_uuid_example",
        default_hold_music=True,
        description="description_example",
        filename="filename_example",
        merchant_id="merchant_id_example",
        mime_type="mime_type_example",
        url="url_example",
        user_id=1,
        version=1,
    ) # ConversationPbxAudio | Pbx Audio

    # example passing only required values which don't have defaults set
    try:
        # Update pbx audio
        api_response = api_instance.update_pbx_audio(conversation_pbx_audio_uuid, pbx_audio)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_audio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_audio_uuid** | **str**|  |
 **pbx_audio** | [**ConversationPbxAudio**](ConversationPbxAudio.md)| Pbx Audio |

### Return type

[**ConversationPbxAudioResponse**](ConversationPbxAudioResponse.md)

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

# **update_pbx_menu**
> ConversationPbxMenuResponse update_pbx_menu(conversation_pbx_menu_uuid, pbx_menu)

Update pbx menu

Update a pbx menu 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_menu import ConversationPbxMenu
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_menu_response import ConversationPbxMenuResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_menu_uuid = "conversationPbxMenuUuid_example" # str | 
    pbx_menu = ConversationPbxMenu(
        allow_direct_extensions=True,
        conversation_pbx_menu_uuid="conversation_pbx_menu_uuid_example",
        default_action="default_action_example",
        default_action_target="default_action_target_example",
        mappings=[
            ConversationPbxMenuMapping(
                action="action_example",
                action_target="action_target_example",
                digits=1,
                speech="speech_example",
            ),
        ],
        merchant_id="merchant_id_example",
        name="name_example",
        play_audio_uuid="play_audio_uuid_example",
        say="say_example",
        timeout=1,
    ) # ConversationPbxMenu | Pbx Menu

    # example passing only required values which don't have defaults set
    try:
        # Update pbx menu
        api_response = api_instance.update_pbx_menu(conversation_pbx_menu_uuid, pbx_menu)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_menu_uuid** | **str**|  |
 **pbx_menu** | [**ConversationPbxMenu**](ConversationPbxMenu.md)| Pbx Menu |

### Return type

[**ConversationPbxMenuResponse**](ConversationPbxMenuResponse.md)

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

# **update_pbx_phone_number**
> ConversationPbxPhoneNumberResponse update_pbx_phone_number(conversation_pbx_phone_number_uuid, pbx_phone_number)

Update pbx phoneNumber

Update a pbx phoneNumber 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_phone_number import ConversationPbxPhoneNumber
from ultracart.model.conversation_pbx_phone_number_response import ConversationPbxPhoneNumberResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_phone_number_uuid = "conversationPbxPhoneNumberUuid_example" # str | 
    pbx_phone_number = ConversationPbxPhoneNumber(
        action="action_example",
        action_target="action_target_example",
        conversation_pbx_time_range_uuid="conversation_pbx_time_range_uuid_example",
        merchant_id="merchant_id_example",
        phone_number="phone_number_example",
    ) # ConversationPbxPhoneNumber | Pbx PhoneNumber

    # example passing only required values which don't have defaults set
    try:
        # Update pbx phoneNumber
        api_response = api_instance.update_pbx_phone_number(conversation_pbx_phone_number_uuid, pbx_phone_number)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_phone_number_uuid** | **str**|  |
 **pbx_phone_number** | [**ConversationPbxPhoneNumber**](ConversationPbxPhoneNumber.md)| Pbx PhoneNumber |

### Return type

[**ConversationPbxPhoneNumberResponse**](ConversationPbxPhoneNumberResponse.md)

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

# **update_pbx_queue**
> ConversationPbxQueueResponse update_pbx_queue(conversation_pbx_queue_uuid, pbx_queue)

Update pbx queue

Update a pbx queue 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_queue import ConversationPbxQueue
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_queue_response import ConversationPbxQueueResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_queue_uuid = "conversationPbxQueueUuid_example" # str | 
    pbx_queue = ConversationPbxQueue(
        announce_queue_position=True,
        conversation_pbx_queue_uuid="conversation_pbx_queue_uuid_example",
        conversation_voicemail_mailbox_uuid="conversation_voicemail_mailbox_uuid_example",
        hold_conversation_pbx_audio_uuid="hold_conversation_pbx_audio_uuid_example",
        max_hold_seconds=1,
        members=ConversationPbxQueueMembers(
            groups=[
                1,
            ],
            users=[
                1,
            ],
        ),
        merchant_id="merchant_id_example",
        name="name_example",
        no_agent_available_play_audio_uuid="no_agent_available_play_audio_uuid_example",
        no_agent_available_say="no_agent_available_say_example",
        no_agent_available_say_voice="no_agent_available_say_voice_example",
        play_audio_uuid="play_audio_uuid_example",
        record_call=True,
        say="say_example",
        say_voice="say_voice_example",
        twilio_taskrouter_workflow_sid="twilio_taskrouter_workflow_sid_example",
        twilio_workspace_queue_sid="twilio_workspace_queue_sid_example",
        voicemail=True,
        wait_critical_seconds=1,
        wait_warning_seconds=1,
        wrap_up_seconds=1,
    ) # ConversationPbxQueue | Pbx Queue

    # example passing only required values which don't have defaults set
    try:
        # Update pbx queue
        api_response = api_instance.update_pbx_queue(conversation_pbx_queue_uuid, pbx_queue)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_queue_uuid** | **str**|  |
 **pbx_queue** | [**ConversationPbxQueue**](ConversationPbxQueue.md)| Pbx Queue |

### Return type

[**ConversationPbxQueueResponse**](ConversationPbxQueueResponse.md)

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

# **update_pbx_time_based**
> ConversationPbxTimeBasedResponse update_pbx_time_based(conversation_pbx_time_based_uuid, pbx_time_based)

Update pbx timeBased

Update a pbx timeBased 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_time_based import ConversationPbxTimeBased
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_based_response import ConversationPbxTimeBasedResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_time_based_uuid = "conversationPbxTimeBasedUuid_example" # str | 
    pbx_time_based = ConversationPbxTimeBased(
        conversation_pbx_time_based_uuid="conversation_pbx_time_based_uuid_example",
        mapping_config=ConversationPbxTimeBasedMappingConfig(
            default=ConversationPbxTimeBasedMapping(
                action="action_example",
                action_target="action_target_example",
                name="name_example",
                time_range_uuid="time_range_uuid_example",
            ),
            mappings=[
                ConversationPbxTimeBasedMapping(
                    action="action_example",
                    action_target="action_target_example",
                    name="name_example",
                    time_range_uuid="time_range_uuid_example",
                ),
            ],
        ),
        merchant_id="merchant_id_example",
        time_based_name="time_based_name_example",
    ) # ConversationPbxTimeBased | Pbx TimeBased

    # example passing only required values which don't have defaults set
    try:
        # Update pbx timeBased
        api_response = api_instance.update_pbx_time_based(conversation_pbx_time_based_uuid, pbx_time_based)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_time_based: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_time_based_uuid** | **str**|  |
 **pbx_time_based** | [**ConversationPbxTimeBased**](ConversationPbxTimeBased.md)| Pbx TimeBased |

### Return type

[**ConversationPbxTimeBasedResponse**](ConversationPbxTimeBasedResponse.md)

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

# **update_pbx_time_range**
> ConversationPbxTimeRangeResponse update_pbx_time_range(conversation_pbx_time_range_uuid, pbx_time_range)

Update pbx timeRange

Update a pbx timeRange 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_time_range import ConversationPbxTimeRange
from ultracart.model.error_response import ErrorResponse
from ultracart.model.conversation_pbx_time_range_response import ConversationPbxTimeRangeResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_time_range_uuid = "conversationPbxTimeRangeUuid_example" # str | 
    pbx_time_range = ConversationPbxTimeRange(
        configs=[
            ConversationPbxTimeRangeConfig(
                end_date="end_date_example",
                end_day_of_week=1,
                end_time="end_time_example",
                start_date="start_date_example",
                start_day_of_week=1,
                start_time="start_time_example",
            ),
        ],
        conversation_pbx_time_range_uuid="conversation_pbx_time_range_uuid_example",
        merchant_id="merchant_id_example",
        time_range_name="time_range_name_example",
        timezone="timezone_example",
    ) # ConversationPbxTimeRange | Pbx TimeRange

    # example passing only required values which don't have defaults set
    try:
        # Update pbx timeRange
        api_response = api_instance.update_pbx_time_range(conversation_pbx_time_range_uuid, pbx_time_range)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_time_range: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_time_range_uuid** | **str**|  |
 **pbx_time_range** | [**ConversationPbxTimeRange**](ConversationPbxTimeRange.md)| Pbx TimeRange |

### Return type

[**ConversationPbxTimeRangeResponse**](ConversationPbxTimeRangeResponse.md)

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

# **update_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse update_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid, pbx_voicemail_mailbox)

Update pbx voicemailMailbox

Update a pbx voicemailMailbox 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import conversation_api
from ultracart.model.conversation_pbx_voicemail_mailbox_response import ConversationPbxVoicemailMailboxResponse
from ultracart.model.conversation_pbx_voicemail_mailbox import ConversationPbxVoicemailMailbox
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    conversation_pbx_voicemail_mailbox_uuid = "conversationPbxVoicemailMailboxUuid_example" # str | 
    pbx_voicemail_mailbox = ConversationPbxVoicemailMailbox(
        conversation_pbx_voicemail_mailbox_uuid="conversation_pbx_voicemail_mailbox_uuid_example",
        merchant_id="merchant_id_example",
        send_notices_to_email="send_notices_to_email_example",
        user_id=1,
        voicemail_follow_play_audio_uuid="voicemail_follow_play_audio_uuid_example",
        voicemail_followup_say="voicemail_followup_say_example",
        voicemail_mailbox_id="voicemail_mailbox_id_example",
        voicemail_mailbox_type="agent",
        voicemail_prompt_play_audio_uuid="voicemail_prompt_play_audio_uuid_example",
        voicemail_prompt_say="voicemail_prompt_say_example",
        voicemail_say_voice="voicemail_say_voice_example",
    ) # ConversationPbxVoicemailMailbox | Pbx VoicemailMailbox

    # example passing only required values which don't have defaults set
    try:
        # Update pbx voicemailMailbox
        api_response = api_instance.update_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid, pbx_voicemail_mailbox)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling ConversationApi->update_pbx_voicemail_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_voicemail_mailbox_uuid** | **str**|  |
 **pbx_voicemail_mailbox** | [**ConversationPbxVoicemailMailbox**](ConversationPbxVoicemailMailbox.md)| Pbx VoicemailMailbox |

### Return type

[**ConversationPbxVoicemailMailboxResponse**](ConversationPbxVoicemailMailboxResponse.md)

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

