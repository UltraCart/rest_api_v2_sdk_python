# ultracart.ConversationApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agent_profile_knowledge_base_document**](ConversationApi.md#delete_agent_profile_knowledge_base_document) | **DELETE** /conversation/agent/profiles/{user_id}/knowledge_base/{document_uuid} | Delete a knowledge base document
[**delete_agent_profile_mcp**](ConversationApi.md#delete_agent_profile_mcp) | **DELETE** /conversation/agent/profiles/{user_id}/mcps/{mcp_server_uuid} | Delete an agent MCP server
[**delete_conversation_canned_message**](ConversationApi.md#delete_conversation_canned_message) | **DELETE** /conversation/canned_messages/{conversation_canned_message_oid} | Delete a conversation canned message
[**delete_department**](ConversationApi.md#delete_department) | **DELETE** /conversation/departments/{conversation_department_oid} | Delete a conversation department
[**delete_engagement**](ConversationApi.md#delete_engagement) | **DELETE** /conversation/engagements/{conversation_engagement_oid} | Delete a conversation engagement
[**delete_pbx_address**](ConversationApi.md#delete_pbx_address) | **DELETE** /conversation/pbx/address/{conversationPbxAddressUuid} | Delete pbx address
[**delete_pbx_agent_voicemail**](ConversationApi.md#delete_pbx_agent_voicemail) | **DELETE** /conversation/pbx/agent/voicemails/{recording_sid} | Delete Agent Voicemail
[**delete_pbx_audio**](ConversationApi.md#delete_pbx_audio) | **DELETE** /conversation/pbx/audio/{conversationPbxAudioUuid} | Delete pbx audio
[**delete_pbx_class_of_service**](ConversationApi.md#delete_pbx_class_of_service) | **DELETE** /conversation/pbx/class_of_service/{classOfServiceUuid} | Delete pbx class of service
[**delete_pbx_hardware_phone**](ConversationApi.md#delete_pbx_hardware_phone) | **DELETE** /conversation/pbx/hardware_phone/{conversationPbxHardwarePhoneUuid} | Delete pbx hardware phone
[**delete_pbx_menu**](ConversationApi.md#delete_pbx_menu) | **DELETE** /conversation/pbx/menu/{conversationPbxMenuUuid} | Delete pbx menu
[**delete_pbx_phone_number**](ConversationApi.md#delete_pbx_phone_number) | **DELETE** /conversation/pbx/phone_number/{conversationPbxPhoneNumberUuid} | Delete pbx phoneNumber
[**delete_pbx_queue**](ConversationApi.md#delete_pbx_queue) | **DELETE** /conversation/pbx/queue/{conversationPbxQueueUuid} | Delete pbx queue
[**delete_pbx_queue_voicemail**](ConversationApi.md#delete_pbx_queue_voicemail) | **DELETE** /conversation/pbx/queues/{queue_uuid}/voicemails/{recording_sid} | Delete Queue Voicemail
[**delete_pbx_time_based**](ConversationApi.md#delete_pbx_time_based) | **DELETE** /conversation/pbx/time_based/{conversationPbxTimeBasedUuid} | Delete pbx timeBased
[**delete_pbx_time_range**](ConversationApi.md#delete_pbx_time_range) | **DELETE** /conversation/pbx/time_range/{conversationPbxTimeRangeUuid} | Delete pbx timeRange
[**delete_pbx_voicemail_mailbox**](ConversationApi.md#delete_pbx_voicemail_mailbox) | **DELETE** /conversation/pbx/voicemail_mailbox/{conversationPbxVoicemailMailboxUuid} | Delete pbx voicemailMailbox
[**get_agent_keep_alive**](ConversationApi.md#get_agent_keep_alive) | **GET** /conversation/agent/keepalive | Agent keep alive
[**get_agent_profile**](ConversationApi.md#get_agent_profile) | **GET** /conversation/agent/profile | Get agent profile
[**get_agent_profile_knowledge_base**](ConversationApi.md#get_agent_profile_knowledge_base) | **GET** /conversation/agent/profiles/{user_id}/knowledge_base | Get the list of knowledge base documents associated with this agent profile
[**get_agent_profile_mcp**](ConversationApi.md#get_agent_profile_mcp) | **GET** /conversation/agent/profiles/{user_id}/mcps/{mcp_server_uuid} | Get an MCP server associated with this agent
[**get_agent_profile_mcp_tools**](ConversationApi.md#get_agent_profile_mcp_tools) | **GET** /conversation/agent/profiles/{user_id}/mcps/{mcp_server_uuid}/tools | Get the tools available from the MCP server
[**get_agent_profile_mcps**](ConversationApi.md#get_agent_profile_mcps) | **GET** /conversation/agent/profiles/{user_id}/mcps | Get the list of MCP servers associated with this agent
[**get_agent_profiles**](ConversationApi.md#get_agent_profiles) | **GET** /conversation/agent/profiles | Get agent profiles
[**get_agent_websocket_authorization**](ConversationApi.md#get_agent_websocket_authorization) | **PUT** /conversation/agent/auth | Get agent websocket authorization
[**get_conversation**](ConversationApi.md#get_conversation) | **GET** /conversation/conversations/{conversation_uuid} | Retrieve a conversation
[**get_conversation_canned_messages**](ConversationApi.md#get_conversation_canned_messages) | **GET** /conversation/canned_messages | Retrieve a list of canned messages ordered by short_code
[**get_conversation_context**](ConversationApi.md#get_conversation_context) | **PUT** /conversation/conversations/{conversation_uuid}/context | Get a webchat conversation context
[**get_conversation_department_member_list**](ConversationApi.md#get_conversation_department_member_list) | **GET** /conversation/department_members | Retrieve a list of possible department members
[**get_conversation_departments**](ConversationApi.md#get_conversation_departments) | **GET** /conversation/departments | Retrieve a list of departments ordered by name
[**get_conversation_engagement**](ConversationApi.md#get_conversation_engagement) | **GET** /conversation/engagements/{conversation_engagement_oid} | Retrieve an engagement
[**get_conversation_engagements**](ConversationApi.md#get_conversation_engagements) | **GET** /conversation/engagements | Retrieve a list of engagements ordered by name
[**get_conversation_item_variations**](ConversationApi.md#get_conversation_item_variations) | **GET** /conversation/items/{merchant_item_id}/variations | Retrieve an item with sparse variations populated
[**get_conversation_knowledge_base_document_upload_url**](ConversationApi.md#get_conversation_knowledge_base_document_upload_url) | **GET** /conversation/agent/profiles/{user_id}/knowledge_base/upload_url/{extension} | Get a pre-signed conversation knowledge base document upload URL
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
[**get_pbx_address**](ConversationApi.md#get_pbx_address) | **GET** /conversation/pbx/address/{conversationPbxAddressUuid} | Get pbx address
[**get_pbx_addresses**](ConversationApi.md#get_pbx_addresses) | **GET** /conversation/pbx/address | Get pbx addresses
[**get_pbx_agent**](ConversationApi.md#get_pbx_agent) | **GET** /conversation/pbx/agent/{conversationPbxAgentUuid} | Get pbx agent
[**get_pbx_agent_voicemail**](ConversationApi.md#get_pbx_agent_voicemail) | **GET** /conversation/pbx/agent/voicemails/{recording_sid} | Get Agent Voicemail
[**get_pbx_agent_voicemails**](ConversationApi.md#get_pbx_agent_voicemails) | **GET** /conversation/pbx/agent/voicemails | Get Agent Voicemails
[**get_pbx_agents**](ConversationApi.md#get_pbx_agents) | **GET** /conversation/pbx/agent | Get pbx agents
[**get_pbx_audio**](ConversationApi.md#get_pbx_audio) | **GET** /conversation/pbx/audio/{conversationPbxAudioUuid} | Get pbx audio
[**get_pbx_audio_usage**](ConversationApi.md#get_pbx_audio_usage) | **GET** /conversation/pbx/audio/{conversationPbxAudioUuid}/usage | Get pbx audio usage
[**get_pbx_audios**](ConversationApi.md#get_pbx_audios) | **GET** /conversation/pbx/audio | Get pbx audios
[**get_pbx_call**](ConversationApi.md#get_pbx_call) | **GET** /conversation/pbx/call/{callUuid} | Get pbx call record
[**get_pbx_class_of_service**](ConversationApi.md#get_pbx_class_of_service) | **GET** /conversation/pbx/class_of_service/{classOfServiceUuid} | Get pbx class of service
[**get_pbx_classes_of_service**](ConversationApi.md#get_pbx_classes_of_service) | **GET** /conversation/pbx/class_of_service | Get pbx classes of service
[**get_pbx_cos_audit_logs**](ConversationApi.md#get_pbx_cos_audit_logs) | **GET** /conversation/pbx/class_of_service/audit_log | Get pbx class of service audit logs
[**get_pbx_hardware_phone**](ConversationApi.md#get_pbx_hardware_phone) | **GET** /conversation/pbx/hardware_phone/{conversationPbxHardwarePhoneUuid} | Get pbx hardware phone
[**get_pbx_hardware_phone_manufacturers**](ConversationApi.md#get_pbx_hardware_phone_manufacturers) | **GET** /conversation/pbx/hardware_phone/manufacturers | Get pbx hardware phone manufacturers
[**get_pbx_hardware_phones**](ConversationApi.md#get_pbx_hardware_phones) | **GET** /conversation/pbx/hardware_phone | Get pbx hardware phones
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
[**get_virtual_agent_budget**](ConversationApi.md#get_virtual_agent_budget) | **GET** /conversation/virtualagent/budget | Get virtual agent budget
[**get_virtual_agent_capabilities**](ConversationApi.md#get_virtual_agent_capabilities) | **GET** /conversation/virtualagent/capabilities | Get virtual agent capabilities
[**insert_agent_profile_knowledge_base_document**](ConversationApi.md#insert_agent_profile_knowledge_base_document) | **POST** /conversation/agent/profiles/{user_id}/knowledge_base | Insert a knowledge base document
[**insert_agent_profile_mcp**](ConversationApi.md#insert_agent_profile_mcp) | **POST** /conversation/agent/profiles/{user_id}/mcps | Insert an agent MCP server
[**insert_conversation_canned_message**](ConversationApi.md#insert_conversation_canned_message) | **POST** /conversation/canned_messages | Insert a canned message
[**insert_conversation_department**](ConversationApi.md#insert_conversation_department) | **POST** /conversation/departments | Insert a department
[**insert_conversation_engagement**](ConversationApi.md#insert_conversation_engagement) | **POST** /conversation/engagements | Insert a engagement
[**insert_pbx_address**](ConversationApi.md#insert_pbx_address) | **POST** /conversation/pbx/address | Insert pbx address
[**insert_pbx_audio**](ConversationApi.md#insert_pbx_audio) | **POST** /conversation/pbx/audio | Insert pbx audio
[**insert_pbx_class_of_service**](ConversationApi.md#insert_pbx_class_of_service) | **POST** /conversation/pbx/class_of_service | Insert pbx class of service
[**insert_pbx_hardware_phone**](ConversationApi.md#insert_pbx_hardware_phone) | **POST** /conversation/pbx/hardware_phone | Insert pbx hardware phone
[**insert_pbx_menu**](ConversationApi.md#insert_pbx_menu) | **POST** /conversation/pbx/menu | Insert pbx menu
[**insert_pbx_queue**](ConversationApi.md#insert_pbx_queue) | **POST** /conversation/pbx/queue | Insert pbx queue
[**insert_pbx_time_based**](ConversationApi.md#insert_pbx_time_based) | **POST** /conversation/pbx/time_based | Insert pbx timeBased
[**insert_pbx_time_range**](ConversationApi.md#insert_pbx_time_range) | **POST** /conversation/pbx/time_range | Insert pbx timeRange
[**insert_pbx_voicemail_mailbox**](ConversationApi.md#insert_pbx_voicemail_mailbox) | **POST** /conversation/pbx/voicemail_mailbox | Insert pbx voicemailMailbox
[**join_conversation**](ConversationApi.md#join_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/join | Join a conversation
[**leave_conversation**](ConversationApi.md#leave_conversation) | **DELETE** /conversation/conversations/{conversation_uuid}/leave | Leave a conversation
[**listened_pbx_agent_voicemail**](ConversationApi.md#listened_pbx_agent_voicemail) | **GET** /conversation/pbx/agent/voicemails/{recording_sid}/listened | Listened Agent Voicemail
[**listened_pbx_queue_voicemail**](ConversationApi.md#listened_pbx_queue_voicemail) | **GET** /conversation/pbx/queues/{queue_uuid}/voicemails/{recording_sid}/listened | Listened Queue Voicemail
[**mark_read_conversation**](ConversationApi.md#mark_read_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/markread | Mark a conversation as read
[**protect_pbx_phone_number**](ConversationApi.md#protect_pbx_phone_number) | **PUT** /conversation/pbx/phone_number/{conversationPbxPhoneNumberUuid}/protect | Protect pbx phoneNumber from deletion
[**purchase_pbx_phone_number**](ConversationApi.md#purchase_pbx_phone_number) | **POST** /conversation/pbx/phone_number | Purchase pbx phone number
[**regenerate_password_for_pbx_hardware_phone**](ConversationApi.md#regenerate_password_for_pbx_hardware_phone) | **POST** /conversation/pbx/hardware_phone/{conversationPbxHardwarePhoneUuid}/regenerate_password | Update pbx hardware phone
[**reset_conversation_pbx_queue_statistics**](ConversationApi.md#reset_conversation_pbx_queue_statistics) | **POST** /conversation/pbx/queues/{queue_uuid}/reset_statistics | reset statistics within the queue
[**search_conversation_canned_messages**](ConversationApi.md#search_conversation_canned_messages) | **POST** /conversation/canned_messages/search | Search for canned messages by short_code
[**search_pbx_available_phone_numbers**](ConversationApi.md#search_pbx_available_phone_numbers) | **GET** /conversation/pbx/phone_number/search | Search for available phone numbers
[**search_pbx_calls**](ConversationApi.md#search_pbx_calls) | **POST** /conversation/pbx/call/search | Search pbx call records
[**sms_unsubscribe_conversation**](ConversationApi.md#sms_unsubscribe_conversation) | **PUT** /conversation/conversations/{conversation_uuid}/sms_unsubscribe | Unsubscribe any SMS participants in this conversation
[**start_conversation**](ConversationApi.md#start_conversation) | **PUT** /conversation/conversations | Start a conversation
[**update_agent_profile**](ConversationApi.md#update_agent_profile) | **PUT** /conversation/agent/profile | Update agent profile
[**update_agent_profile_mcp**](ConversationApi.md#update_agent_profile_mcp) | **POST** /conversation/agent/profiles/{user_id}/mcps/{mcp_server_uuid} | Update an agent MCP server
[**update_conversation_canned_message**](ConversationApi.md#update_conversation_canned_message) | **PUT** /conversation/canned_messages/{conversation_canned_message_oid} | Update a canned message
[**update_conversation_department**](ConversationApi.md#update_conversation_department) | **PUT** /conversation/departments/{conversation_department_oid} | Update a department
[**update_conversation_engagement**](ConversationApi.md#update_conversation_engagement) | **PUT** /conversation/engagements/{conversation_engagement_oid} | Update a engagement
[**update_conversation_webchat_queue_status**](ConversationApi.md#update_conversation_webchat_queue_status) | **PUT** /conversation/conversations/queues/{queue_name}/status | Update status within the queue
[**update_pbx_address**](ConversationApi.md#update_pbx_address) | **PUT** /conversation/pbx/address/{conversationPbxAddressUuid} | Update pbx address
[**update_pbx_agent**](ConversationApi.md#update_pbx_agent) | **PUT** /conversation/pbx/agent/{conversationPbxAgentUuid} | Update pbx agent
[**update_pbx_audio**](ConversationApi.md#update_pbx_audio) | **PUT** /conversation/pbx/audio/{conversationPbxAudioUuid} | Update pbx audio
[**update_pbx_class_of_service**](ConversationApi.md#update_pbx_class_of_service) | **PUT** /conversation/pbx/class_of_service/{classOfServiceUuid} | Update pbx class of service
[**update_pbx_hardware_phone**](ConversationApi.md#update_pbx_hardware_phone) | **PUT** /conversation/pbx/hardware_phone/{conversationPbxHardwarePhoneUuid} | Update pbx hardware phone
[**update_pbx_menu**](ConversationApi.md#update_pbx_menu) | **PUT** /conversation/pbx/menu/{conversationPbxMenuUuid} | Update pbx menu
[**update_pbx_phone_number**](ConversationApi.md#update_pbx_phone_number) | **PUT** /conversation/pbx/phone_number/{conversationPbxPhoneNumberUuid} | Update pbx phoneNumber
[**update_pbx_queue**](ConversationApi.md#update_pbx_queue) | **PUT** /conversation/pbx/queue/{conversationPbxQueueUuid} | Update pbx queue
[**update_pbx_time_based**](ConversationApi.md#update_pbx_time_based) | **PUT** /conversation/pbx/time_based/{conversationPbxTimeBasedUuid} | Update pbx timeBased
[**update_pbx_time_range**](ConversationApi.md#update_pbx_time_range) | **PUT** /conversation/pbx/time_range/{conversationPbxTimeRangeUuid} | Update pbx timeRange
[**update_pbx_voicemail_mailbox**](ConversationApi.md#update_pbx_voicemail_mailbox) | **PUT** /conversation/pbx/voicemail_mailbox/{conversationPbxVoicemailMailboxUuid} | Update pbx voicemailMailbox
[**update_virtual_agent_budget**](ConversationApi.md#update_virtual_agent_budget) | **PUT** /conversation/virtualagent/budget | Update virtual agent budget
[**update_virtual_agent_capabilities**](ConversationApi.md#update_virtual_agent_capabilities) | **PUT** /conversation/virtualagent/capabilities | Update virtual agent capabilities


# **delete_agent_profile_knowledge_base_document**
> ConversationDeleteKnowledgeBaseDocumentResponse delete_agent_profile_knowledge_base_document(user_id, document_uuid)

Delete a knowledge base document

Delete a knowledge base document 

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

user_id = 56 # int | 
document_uuid = 'document_uuid_example' # str | 

try:
    # Delete a knowledge base document
    api_response = api_instance.delete_agent_profile_knowledge_base_document(user_id, document_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_agent_profile_knowledge_base_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **document_uuid** | **str**|  | 

### Return type

[**ConversationDeleteKnowledgeBaseDocumentResponse**](ConversationDeleteKnowledgeBaseDocumentResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_profile_mcp**
> delete_agent_profile_mcp(user_id, mcp_server_uuid)

Delete an agent MCP server

Delete an agent MCP server 

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

user_id = 56 # int | 
mcp_server_uuid = 'mcp_server_uuid_example' # str | 

try:
    # Delete an agent MCP server
    api_instance.delete_agent_profile_mcp(user_id, mcp_server_uuid)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_agent_profile_mcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **mcp_server_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_conversation_canned_message**
> delete_conversation_canned_message(conversation_canned_message_oid)

Delete a conversation canned message

Delete a conversation canned message 

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

conversation_canned_message_oid = 56 # int | 

try:
    # Delete a conversation canned message
    api_instance.delete_conversation_canned_message(conversation_canned_message_oid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_department**
> delete_department(conversation_department_oid)

Delete a conversation department

Delete a conversation department 

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

conversation_department_oid = 56 # int | 

try:
    # Delete a conversation department
    api_instance.delete_department(conversation_department_oid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_engagement**
> delete_engagement(conversation_engagement_oid)

Delete a conversation engagement

Delete a conversation engagement 

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

conversation_engagement_oid = 56 # int | 

try:
    # Delete a conversation engagement
    api_instance.delete_engagement(conversation_engagement_oid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_address**
> ConversationPbxAddressResponse delete_pbx_address(conversation_pbx_address_uuid)

Delete pbx address

Delete a pbx address 

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

conversation_pbx_address_uuid = 'conversation_pbx_address_uuid_example' # str | 

try:
    # Delete pbx address
    api_response = api_instance.delete_pbx_address(conversation_pbx_address_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_pbx_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_address_uuid** | **str**|  | 

### Return type

[**ConversationPbxAddressResponse**](ConversationPbxAddressResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_agent_voicemail**
> delete_pbx_agent_voicemail(recording_sid)

Delete Agent Voicemail

Delete pbx agent Voicemail 

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

recording_sid = 'recording_sid_example' # str | 

try:
    # Delete Agent Voicemail
    api_instance.delete_pbx_agent_voicemail(recording_sid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_audio**
> ConversationPbxAudioResponse delete_pbx_audio(conversation_pbx_audio_uuid)

Delete pbx audio

Delete a pbx audio 

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

conversation_pbx_audio_uuid = 'conversation_pbx_audio_uuid_example' # str | 

try:
    # Delete pbx audio
    api_response = api_instance.delete_pbx_audio(conversation_pbx_audio_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_class_of_service**
> BaseResponse delete_pbx_class_of_service(class_of_service_uuid)

Delete pbx class of service

Delete a class of service 

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

class_of_service_uuid = 'class_of_service_uuid_example' # str | 

try:
    # Delete pbx class of service
    api_response = api_instance.delete_pbx_class_of_service(class_of_service_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_pbx_class_of_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_of_service_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_hardware_phone**
> ConversationPbxHardwarePhoneResponse delete_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid)

Delete pbx hardware phone

Delete a pbx hardware phone 

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

conversation_pbx_hardware_phone_uuid = 'conversation_pbx_hardware_phone_uuid_example' # str | 

try:
    # Delete pbx hardware phone
    api_response = api_instance.delete_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_pbx_hardware_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_hardware_phone_uuid** | **str**|  | 

### Return type

[**ConversationPbxHardwarePhoneResponse**](ConversationPbxHardwarePhoneResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_menu**
> ConversationPbxMenuResponse delete_pbx_menu(conversation_pbx_menu_uuid)

Delete pbx menu

Delete a pbx menu 

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

conversation_pbx_menu_uuid = 'conversation_pbx_menu_uuid_example' # str | 

try:
    # Delete pbx menu
    api_response = api_instance.delete_pbx_menu(conversation_pbx_menu_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_phone_number**
> delete_pbx_phone_number(conversation_pbx_phone_number_uuid)

Delete pbx phoneNumber

Delete a pbx phoneNumber. Only works if deletion_protected is false. 

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

conversation_pbx_phone_number_uuid = 'conversation_pbx_phone_number_uuid_example' # str | 

try:
    # Delete pbx phoneNumber
    api_instance.delete_pbx_phone_number(conversation_pbx_phone_number_uuid)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_pbx_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_phone_number_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_queue**
> ConversationPbxQueueResponse delete_pbx_queue(conversation_pbx_queue_uuid)

Delete pbx queue

Delete a pbx queue 

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

conversation_pbx_queue_uuid = 'conversation_pbx_queue_uuid_example' # str | 

try:
    # Delete pbx queue
    api_response = api_instance.delete_pbx_queue(conversation_pbx_queue_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_queue_voicemail**
> delete_pbx_queue_voicemail(queue_uuid, recording_sid)

Delete Queue Voicemail

Delete pbx queue Voicemail 

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

queue_uuid = 'queue_uuid_example' # str | 
recording_sid = 'recording_sid_example' # str | 

try:
    # Delete Queue Voicemail
    api_instance.delete_pbx_queue_voicemail(queue_uuid, recording_sid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_time_based**
> ConversationPbxTimeBasedResponse delete_pbx_time_based(conversation_pbx_time_based_uuid)

Delete pbx timeBased

Delete a pbx timeBased 

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

conversation_pbx_time_based_uuid = 'conversation_pbx_time_based_uuid_example' # str | 

try:
    # Delete pbx timeBased
    api_response = api_instance.delete_pbx_time_based(conversation_pbx_time_based_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_time_range**
> ConversationPbxTimeRangeResponse delete_pbx_time_range(conversation_pbx_time_range_uuid)

Delete pbx timeRange

Delete a pbx timeRange 

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

conversation_pbx_time_range_uuid = 'conversation_pbx_time_range_uuid_example' # str | 

try:
    # Delete pbx timeRange
    api_response = api_instance.delete_pbx_time_range(conversation_pbx_time_range_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse delete_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)

Delete pbx voicemailMailbox

Delete a pbx voicemailMailbox 

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

conversation_pbx_voicemail_mailbox_uuid = 'conversation_pbx_voicemail_mailbox_uuid_example' # str | 

try:
    # Delete pbx voicemailMailbox
    api_response = api_instance.delete_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_agent_profile**
> ConversationAgentProfileResponse get_agent_profile()

Get agent profile

Retrieve the agents profile 

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
    # Get agent profile
    api_response = api_instance.get_agent_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationAgentProfileResponse**](ConversationAgentProfileResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_profile_knowledge_base**
> ConversationKnowledgeBaseDocumentsResponse get_agent_profile_knowledge_base(user_id)

Get the list of knowledge base documents associated with this agent profile

Retrieve knowledge base documents 

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

user_id = 56 # int | 

try:
    # Get the list of knowledge base documents associated with this agent profile
    api_response = api_instance.get_agent_profile_knowledge_base(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_profile_knowledge_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**ConversationKnowledgeBaseDocumentsResponse**](ConversationKnowledgeBaseDocumentsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_profile_mcp**
> ConversationMcpServerResponse get_agent_profile_mcp(user_id, mcp_server_uuid)

Get an MCP server associated with this agent

Retrieve MCP server associated with this agent 

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

user_id = 56 # int | 
mcp_server_uuid = 'mcp_server_uuid_example' # str | 

try:
    # Get an MCP server associated with this agent
    api_response = api_instance.get_agent_profile_mcp(user_id, mcp_server_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_profile_mcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **mcp_server_uuid** | **str**|  | 

### Return type

[**ConversationMcpServerResponse**](ConversationMcpServerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_profile_mcp_tools**
> ConversationMcpServerToolsResponse get_agent_profile_mcp_tools(user_id, mcp_server_uuid)

Get the tools available from the MCP server

Get the tools available from the MCP server 

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

user_id = 56 # int | 
mcp_server_uuid = 'mcp_server_uuid_example' # str | 

try:
    # Get the tools available from the MCP server
    api_response = api_instance.get_agent_profile_mcp_tools(user_id, mcp_server_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_profile_mcp_tools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **mcp_server_uuid** | **str**|  | 

### Return type

[**ConversationMcpServerToolsResponse**](ConversationMcpServerToolsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_profile_mcps**
> ConversationMcpServersResponse get_agent_profile_mcps(user_id)

Get the list of MCP servers associated with this agent

Retrieve MCP servers associated with this agent 

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

user_id = 56 # int | 

try:
    # Get the list of MCP servers associated with this agent
    api_response = api_instance.get_agent_profile_mcps(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_profile_mcps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**ConversationMcpServersResponse**](ConversationMcpServersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_profiles**
> ConversationAgentProfilesResponse get_agent_profiles()

Get agent profiles

Retrieve the agents profile 

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
    # Get agent profiles
    api_response = api_instance.get_agent_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_agent_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationAgentProfilesResponse**](ConversationAgentProfilesResponse.md)

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

# **get_conversation_canned_messages**
> ConversationCannedMessagesResponse get_conversation_canned_messages()

Retrieve a list of canned messages ordered by short_code

Retrieve a list of canned messages ordered by short_code 

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
    # Retrieve a list of canned messages ordered by short_code
    api_response = api_instance.get_conversation_canned_messages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_canned_messages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationCannedMessagesResponse**](ConversationCannedMessagesResponse.md)

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

# **get_conversation_department_member_list**
> ConversationDepartmentMembersResponse get_conversation_department_member_list()

Retrieve a list of possible department members

Retrieve a list of possible department members 

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
    # Retrieve a list of possible department members
    api_response = api_instance.get_conversation_department_member_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_department_member_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationDepartmentMembersResponse**](ConversationDepartmentMembersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_departments**
> ConversationDepartmentsResponse get_conversation_departments()

Retrieve a list of departments ordered by name

Retrieve a list of departments ordered by name 

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
    # Retrieve a list of departments ordered by name
    api_response = api_instance.get_conversation_departments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_departments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationDepartmentsResponse**](ConversationDepartmentsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_engagement**
> ConversationEngagementResponse get_conversation_engagement(conversation_engagement_oid)

Retrieve an engagement

Retrieve an engagement 

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

conversation_engagement_oid = 56 # int | 

try:
    # Retrieve an engagement
    api_response = api_instance.get_conversation_engagement(conversation_engagement_oid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_engagements**
> ConversationEngagementsResponse get_conversation_engagements()

Retrieve a list of engagements ordered by name

Retrieve a list of engagements ordered by name 

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
    # Retrieve a list of engagements ordered by name
    api_response = api_instance.get_conversation_engagements()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_engagements: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationEngagementsResponse**](ConversationEngagementsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_item_variations**
> ItemResponse get_conversation_item_variations(merchant_item_id)

Retrieve an item with sparse variations populated

Retrieve an item with sparse variations populated 

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

merchant_item_id = 'merchant_item_id_example' # str | 

try:
    # Retrieve an item with sparse variations populated
    api_response = api_instance.get_conversation_item_variations(merchant_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_item_variations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_item_id** | **str**|  | 

### Return type

[**ItemResponse**](ItemResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_knowledge_base_document_upload_url**
> ConversationKnowledgeBaseDocumentUploadUrlResponse get_conversation_knowledge_base_document_upload_url(user_id, extension)

Get a pre-signed conversation knowledge base document upload URL

Get a pre-signed conversation knowledge base document upload URL 

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

user_id = 56 # int | 
extension = 'extension_example' # str | 

try:
    # Get a pre-signed conversation knowledge base document upload URL
    api_response = api_instance.get_conversation_knowledge_base_document_upload_url(user_id, extension)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_knowledge_base_document_upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **extension** | **str**|  | 

### Return type

[**ConversationKnowledgeBaseDocumentUploadUrlResponse**](ConversationKnowledgeBaseDocumentUploadUrlResponse.md)

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

Get a presigned conversation multimedia upload URL

Get a presigned conversation multimedia upload URL 

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
    # Get a presigned conversation multimedia upload URL
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

# **get_conversation_pbx_audio_upload_url**
> ConversationPbxAudioUploadUrlResponse get_conversation_pbx_audio_upload_url(extension)

Get a pre-signed conversation multimedia upload URL

Get a pre-signed conversation multimedia upload URL 

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
    # Get a pre-signed conversation multimedia upload URL
    api_response = api_instance.get_conversation_pbx_audio_upload_url(extension)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_pbx_customer_snapshot**
> ConversationPbxCustomerSnapshotResponse get_conversation_pbx_customer_snapshot(pbx_customer_snapshot_request)

Get orders and customer information for a phone number

Retrieves all the orders, auto orders, and customer profile for a given phone number 

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

pbx_customer_snapshot_request = ultracart.ConversationPbxCustomerSnapshotRequest() # ConversationPbxCustomerSnapshotRequest | Conversation pbx customer snapshot request

try:
    # Get orders and customer information for a phone number
    api_response = api_instance.get_conversation_pbx_customer_snapshot(pbx_customer_snapshot_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_permissions**
> ConversationPermissionsResponse get_conversation_permissions()

Retrieve conversation permissions

Retrieve conversation permissions 

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
    # Retrieve conversation permissions
    api_response = api_instance.get_conversation_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_conversation_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPermissionsResponse**](ConversationPermissionsResponse.md)

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

# **get_conversations_autocomplete**
> ConversationAutocompleteResponse get_conversations_autocomplete(autocomplete_request)

Retrieve a list of matching terms for a search field

Retrieve a list of matching terms for a search field 

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

autocomplete_request = ultracart.ConversationAutocompleteRequest() # ConversationAutocompleteRequest | Autocomplete Request

try:
    # Retrieve a list of matching terms for a search field
    api_response = api_instance.get_conversations_autocomplete(autocomplete_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversations_search**
> ConversationSearchResponse get_conversations_search(search_request)

Search conversations

Search conversations 

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

search_request = ultracart.ConversationSearchRequest() # ConversationSearchRequest | Search Request

try:
    # Search conversations
    api_response = api_instance.get_conversations_search(search_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations_for_engagement**
> ConversationLocationsResponse get_locations_for_engagement()

Get location data for engagement configuration

Get location data for engagement configuration 

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
    # Get location data for engagement configuration
    api_response = api_instance.get_locations_for_engagement()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_locations_for_engagement: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationLocationsResponse**](ConversationLocationsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_address**
> ConversationPbxAddressResponse get_pbx_address(conversation_pbx_address_uuid)

Get pbx address

Retrieve a pbx address 

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

conversation_pbx_address_uuid = 'conversation_pbx_address_uuid_example' # str | 

try:
    # Get pbx address
    api_response = api_instance.get_pbx_address(conversation_pbx_address_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_address_uuid** | **str**|  | 

### Return type

[**ConversationPbxAddressResponse**](ConversationPbxAddressResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_addresses**
> ConversationPbxAddressesResponse get_pbx_addresses()

Get pbx addresses

Retrieve pbx addresses 

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
    # Get pbx addresses
    api_response = api_instance.get_pbx_addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxAddressesResponse**](ConversationPbxAddressesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_agent**
> ConversationPbxAgentResponse get_pbx_agent(conversation_pbx_agent_uuid)

Get pbx agent

Retrieve a pbx agent 

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

conversation_pbx_agent_uuid = 'conversation_pbx_agent_uuid_example' # str | 

try:
    # Get pbx agent
    api_response = api_instance.get_pbx_agent(conversation_pbx_agent_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_agent_voicemail**
> ConversationPbxVoicemailMessageResponse get_pbx_agent_voicemail(recording_sid)

Get Agent Voicemail

Retrieve pbx agent Voicemail 

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

recording_sid = 'recording_sid_example' # str | 

try:
    # Get Agent Voicemail
    api_response = api_instance.get_pbx_agent_voicemail(recording_sid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_agent_voicemails**
> ConversationPbxVoicemailMessageSummariesResponse get_pbx_agent_voicemails()

Get Agent Voicemails

Retrieve pbx agent Voicemails 

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
    # Get Agent Voicemails
    api_response = api_instance.get_pbx_agent_voicemails()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_agent_voicemails: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxVoicemailMessageSummariesResponse**](ConversationPbxVoicemailMessageSummariesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_agents**
> ConversationPbxAgentsResponse get_pbx_agents()

Get pbx agents

Retrieve pbx agents 

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
    # Get pbx agents
    api_response = api_instance.get_pbx_agents()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_agents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxAgentsResponse**](ConversationPbxAgentsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_audio**
> ConversationPbxAudioResponse get_pbx_audio(conversation_pbx_audio_uuid)

Get pbx audio

Retrieve a pbx audio 

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

conversation_pbx_audio_uuid = 'conversation_pbx_audio_uuid_example' # str | 

try:
    # Get pbx audio
    api_response = api_instance.get_pbx_audio(conversation_pbx_audio_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_audio_usage**
> ConversationPbxAudioUsageResponse get_pbx_audio_usage(conversation_pbx_audio_uuid)

Get pbx audio usage

Retrieve a pbx audio usage 

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

conversation_pbx_audio_uuid = 'conversation_pbx_audio_uuid_example' # str | 

try:
    # Get pbx audio usage
    api_response = api_instance.get_pbx_audio_usage(conversation_pbx_audio_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_audios**
> ConversationPbxAudiosResponse get_pbx_audios()

Get pbx audios

Retrieve pbx audios 

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
    # Get pbx audios
    api_response = api_instance.get_pbx_audios()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_audios: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxAudiosResponse**](ConversationPbxAudiosResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_call**
> ConversationPbxCallResponse get_pbx_call(call_uuid)

Get pbx call record

Retrieve a single PBX call record with full details 

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

call_uuid = 'call_uuid_example' # str | 

try:
    # Get pbx call record
    api_response = api_instance.get_pbx_call(call_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_uuid** | **str**|  | 

### Return type

[**ConversationPbxCallResponse**](ConversationPbxCallResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_class_of_service**
> ConversationPbxClassOfServiceResponse get_pbx_class_of_service(class_of_service_uuid)

Get pbx class of service

Retrieve a single class of service 

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

class_of_service_uuid = 'class_of_service_uuid_example' # str | 

try:
    # Get pbx class of service
    api_response = api_instance.get_pbx_class_of_service(class_of_service_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_class_of_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_of_service_uuid** | **str**|  | 

### Return type

[**ConversationPbxClassOfServiceResponse**](ConversationPbxClassOfServiceResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_classes_of_service**
> ConversationPbxClassOfServicesResponse get_pbx_classes_of_service()

Get pbx classes of service

Retrieve all classes of service for the merchant 

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
    # Get pbx classes of service
    api_response = api_instance.get_pbx_classes_of_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_classes_of_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxClassOfServicesResponse**](ConversationPbxClassOfServicesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_cos_audit_logs**
> ConversationPbxCosAuditLogsResponse get_pbx_cos_audit_logs(since=since, agent_login=agent_login, action=action, limit=limit)

Get pbx class of service audit logs

Retrieve audit log entries for class of service enforcement 

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

since = 'since_example' # str | ISO timestamp to filter entries since (optional)
agent_login = 'agent_login_example' # str | Filter by agent login (optional)
action = 'action_example' # str | Action (optional)
limit = 56 # int | Maximum number of entries to return (default 100) (optional)

try:
    # Get pbx class of service audit logs
    api_response = api_instance.get_pbx_cos_audit_logs(since=since, agent_login=agent_login, action=action, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_cos_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| ISO timestamp to filter entries since | [optional] 
 **agent_login** | **str**| Filter by agent login | [optional] 
 **action** | **str**| Action | [optional] 
 **limit** | **int**| Maximum number of entries to return (default 100) | [optional] 

### Return type

[**ConversationPbxCosAuditLogsResponse**](ConversationPbxCosAuditLogsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_hardware_phone**
> ConversationPbxHardwarePhoneResponse get_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid)

Get pbx hardware phone

Retrieve a pbx hardware phone 

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

conversation_pbx_hardware_phone_uuid = 'conversation_pbx_hardware_phone_uuid_example' # str | 

try:
    # Get pbx hardware phone
    api_response = api_instance.get_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_hardware_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_hardware_phone_uuid** | **str**|  | 

### Return type

[**ConversationPbxHardwarePhoneResponse**](ConversationPbxHardwarePhoneResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_hardware_phone_manufacturers**
> ConversationPbxPhoneManufacturersResponse get_pbx_hardware_phone_manufacturers()

Get pbx hardware phone manufacturers

Retrieve pbx hardware phone manufacturers and models for auto-provisioning 

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
    # Get pbx hardware phone manufacturers
    api_response = api_instance.get_pbx_hardware_phone_manufacturers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_hardware_phone_manufacturers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxPhoneManufacturersResponse**](ConversationPbxPhoneManufacturersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_hardware_phones**
> ConversationPbxHardwarePhonesResponse get_pbx_hardware_phones()

Get pbx hardware phones

Retrieve pbx hardware phones 

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
    # Get pbx hardware phones
    api_response = api_instance.get_pbx_hardware_phones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_hardware_phones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxHardwarePhonesResponse**](ConversationPbxHardwarePhonesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_menu**
> ConversationPbxMenuResponse get_pbx_menu(conversation_pbx_menu_uuid)

Get pbx menu

Retrieve a pbx menu 

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

conversation_pbx_menu_uuid = 'conversation_pbx_menu_uuid_example' # str | 

try:
    # Get pbx menu
    api_response = api_instance.get_pbx_menu(conversation_pbx_menu_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_menus**
> ConversationPbxMenusResponse get_pbx_menus()

Get pbx menus

Retrieve pbx menus 

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
    # Get pbx menus
    api_response = api_instance.get_pbx_menus()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_menus: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxMenusResponse**](ConversationPbxMenusResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_phone_number**
> ConversationPbxPhoneNumberResponse get_pbx_phone_number(conversation_pbx_phone_number_uuid)

Get pbx phoneNumber

Retrieve a pbx phoneNumber 

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

conversation_pbx_phone_number_uuid = 'conversation_pbx_phone_number_uuid_example' # str | 

try:
    # Get pbx phoneNumber
    api_response = api_instance.get_pbx_phone_number(conversation_pbx_phone_number_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_phone_numbers**
> ConversationPbxPhoneNumbersResponse get_pbx_phone_numbers()

Get pbx phoneNumbers

Retrieve pbx phoneNumbers 

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
    # Get pbx phoneNumbers
    api_response = api_instance.get_pbx_phone_numbers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_phone_numbers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxPhoneNumbersResponse**](ConversationPbxPhoneNumbersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_queue**
> ConversationPbxQueueResponse get_pbx_queue(conversation_pbx_queue_uuid)

Get pbx queue

Retrieve a pbx queue 

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

conversation_pbx_queue_uuid = 'conversation_pbx_queue_uuid_example' # str | 

try:
    # Get pbx queue
    api_response = api_instance.get_pbx_queue(conversation_pbx_queue_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_queue_voicemail**
> ConversationPbxVoicemailMessageResponse get_pbx_queue_voicemail(queue_uuid, recording_sid)

Get Queue Voicemail

Retrieve pbx queue Voicemail 

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

queue_uuid = 'queue_uuid_example' # str | 
recording_sid = 'recording_sid_example' # str | 

try:
    # Get Queue Voicemail
    api_response = api_instance.get_pbx_queue_voicemail(queue_uuid, recording_sid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_queue_voicemails**
> ConversationPbxVoicemailMessageSummariesResponse get_pbx_queue_voicemails(queue_uuid)

Get Queue Voicemails

Retrieve pbx queue voicemails 

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

queue_uuid = 'queue_uuid_example' # str | 

try:
    # Get Queue Voicemails
    api_response = api_instance.get_pbx_queue_voicemails(queue_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_queues**
> ConversationPbxQueuesResponse get_pbx_queues()

Get pbx queues

Retrieve pbx queues 

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
    # Get pbx queues
    api_response = api_instance.get_pbx_queues()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_queues: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxQueuesResponse**](ConversationPbxQueuesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_time_based**
> ConversationPbxTimeBasedResponse get_pbx_time_based(conversation_pbx_time_based_uuid)

Get pbx timeBased

Retrieve a pbx timeBased 

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

conversation_pbx_time_based_uuid = 'conversation_pbx_time_based_uuid_example' # str | 

try:
    # Get pbx timeBased
    api_response = api_instance.get_pbx_time_based(conversation_pbx_time_based_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_time_baseds**
> ConversationPbxTimeBasedsResponse get_pbx_time_baseds()

Get pbx timeBaseds

Retrieve pbx timeBaseds 

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
    # Get pbx timeBaseds
    api_response = api_instance.get_pbx_time_baseds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_time_baseds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxTimeBasedsResponse**](ConversationPbxTimeBasedsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_time_range**
> ConversationPbxTimeRangeResponse get_pbx_time_range(conversation_pbx_time_range_uuid)

Get pbx timeRange

Retrieve a pbx timeRange 

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

conversation_pbx_time_range_uuid = 'conversation_pbx_time_range_uuid_example' # str | 

try:
    # Get pbx timeRange
    api_response = api_instance.get_pbx_time_range(conversation_pbx_time_range_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_time_ranges**
> ConversationPbxTimeRangesResponse get_pbx_time_ranges()

Get pbx timeRanges

Retrieve pbx timeRanges 

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
    # Get pbx timeRanges
    api_response = api_instance.get_pbx_time_ranges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_time_ranges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxTimeRangesResponse**](ConversationPbxTimeRangesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse get_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)

Get pbx voicemailMailbox

Retrieve a pbx voicemailMailbox 

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

conversation_pbx_voicemail_mailbox_uuid = 'conversation_pbx_voicemail_mailbox_uuid_example' # str | 

try:
    # Get pbx voicemailMailbox
    api_response = api_instance.get_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbx_voicemail_mailboxes**
> ConversationPbxVoicemailMailboxesResponse get_pbx_voicemail_mailboxes()

Get pbx voicemailMailboxes

Retrieve pbx voicemailMailboxes 

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
    # Get pbx voicemailMailboxes
    api_response = api_instance.get_pbx_voicemail_mailboxes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_pbx_voicemail_mailboxes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationPbxVoicemailMailboxesResponse**](ConversationPbxVoicemailMailboxesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_agent_budget**
> ConversationVirtualAgentBudgetResponse get_virtual_agent_budget()

Get virtual agent budget

Retrieve virtual agent budget 

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
    # Get virtual agent budget
    api_response = api_instance.get_virtual_agent_budget()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_virtual_agent_budget: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationVirtualAgentBudgetResponse**](ConversationVirtualAgentBudgetResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_agent_capabilities**
> ConversationVirtualAgentCapabilitiesResponse get_virtual_agent_capabilities()

Get virtual agent capabilities

Retrieve virtual agent capabilities 

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
    # Get virtual agent capabilities
    api_response = api_instance.get_virtual_agent_capabilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_virtual_agent_capabilities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationVirtualAgentCapabilitiesResponse**](ConversationVirtualAgentCapabilitiesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_agent_profile_knowledge_base_document**
> ConversationInsertKnowledgeBaseDocumentResponse insert_agent_profile_knowledge_base_document(user_id, knowledge_base_document_request)

Insert a knowledge base document

Insert a knowledge base document 

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

user_id = 56 # int | 
knowledge_base_document_request = ultracart.ConversationInsertKnowledgeBaseDocumentRequest() # ConversationInsertKnowledgeBaseDocumentRequest | Insert request

try:
    # Insert a knowledge base document
    api_response = api_instance.insert_agent_profile_knowledge_base_document(user_id, knowledge_base_document_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->insert_agent_profile_knowledge_base_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **knowledge_base_document_request** | [**ConversationInsertKnowledgeBaseDocumentRequest**](ConversationInsertKnowledgeBaseDocumentRequest.md)| Insert request | 

### Return type

[**ConversationInsertKnowledgeBaseDocumentResponse**](ConversationInsertKnowledgeBaseDocumentResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_agent_profile_mcp**
> ConversationMcpServerResponse insert_agent_profile_mcp(user_id, mcp_server)

Insert an agent MCP server

Insert an agent MCP server 

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

user_id = 56 # int | 
mcp_server = ultracart.ConversationMcpServer() # ConversationMcpServer | MCP Server

try:
    # Insert an agent MCP server
    api_response = api_instance.insert_agent_profile_mcp(user_id, mcp_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->insert_agent_profile_mcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **mcp_server** | [**ConversationMcpServer**](ConversationMcpServer.md)| MCP Server | 

### Return type

[**ConversationMcpServerResponse**](ConversationMcpServerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_conversation_canned_message**
> ConversationCannedMessageResponse insert_conversation_canned_message(canned_message)

Insert a canned message

Insert a canned message 

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

canned_message = ultracart.ConversationCannedMessage() # ConversationCannedMessage | Canned message

try:
    # Insert a canned message
    api_response = api_instance.insert_conversation_canned_message(canned_message)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_conversation_department**
> ConversationDepartmentResponse insert_conversation_department(department)

Insert a department

Insert a department 

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

department = ultracart.ConversationDepartment() # ConversationDepartment | Department

try:
    # Insert a department
    api_response = api_instance.insert_conversation_department(department)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_conversation_engagement**
> ConversationEngagementResponse insert_conversation_engagement(engagement)

Insert a engagement

Insert a engagement 

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

engagement = ultracart.ConversationEngagement() # ConversationEngagement | Engagement

try:
    # Insert a engagement
    api_response = api_instance.insert_conversation_engagement(engagement)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_address**
> ConversationPbxAddressResponse insert_pbx_address(pbx_address)

Insert pbx address

Insert a pbx address 

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

pbx_address = ultracart.ConversationPbxAddress() # ConversationPbxAddress | Pbx Address

try:
    # Insert pbx address
    api_response = api_instance.insert_pbx_address(pbx_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->insert_pbx_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_address** | [**ConversationPbxAddress**](ConversationPbxAddress.md)| Pbx Address | 

### Return type

[**ConversationPbxAddressResponse**](ConversationPbxAddressResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_audio**
> ConversationPbxAudioResponse insert_pbx_audio(pbx_audio)

Insert pbx audio

Insert a pbx audio 

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

pbx_audio = ultracart.ConversationPbxAudio() # ConversationPbxAudio | Pbx Audio

try:
    # Insert pbx audio
    api_response = api_instance.insert_pbx_audio(pbx_audio)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_class_of_service**
> ConversationPbxClassOfServiceResponse insert_pbx_class_of_service(class_of_service)

Insert pbx class of service

Create a new class of service 

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

class_of_service = ultracart.ConversationPbxClassOfService() # ConversationPbxClassOfService | Class of service

try:
    # Insert pbx class of service
    api_response = api_instance.insert_pbx_class_of_service(class_of_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->insert_pbx_class_of_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_of_service** | [**ConversationPbxClassOfService**](ConversationPbxClassOfService.md)| Class of service | 

### Return type

[**ConversationPbxClassOfServiceResponse**](ConversationPbxClassOfServiceResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_hardware_phone**
> ConversationPbxHardwarePhoneResponse insert_pbx_hardware_phone(pbx_hardware_phone)

Insert pbx hardware phone

Insert a pbx hardware phone 

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

pbx_hardware_phone = ultracart.ConversationPbxHardwarePhone() # ConversationPbxHardwarePhone | Pbx Hardware Phone

try:
    # Insert pbx hardware phone
    api_response = api_instance.insert_pbx_hardware_phone(pbx_hardware_phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->insert_pbx_hardware_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbx_hardware_phone** | [**ConversationPbxHardwarePhone**](ConversationPbxHardwarePhone.md)| Pbx Hardware Phone | 

### Return type

[**ConversationPbxHardwarePhoneResponse**](ConversationPbxHardwarePhoneResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_menu**
> ConversationPbxMenuResponse insert_pbx_menu(pbx_menu)

Insert pbx menu

Insert a pbx menu 

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

pbx_menu = ultracart.ConversationPbxMenu() # ConversationPbxMenu | Pbx Menu

try:
    # Insert pbx menu
    api_response = api_instance.insert_pbx_menu(pbx_menu)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_queue**
> ConversationPbxQueueResponse insert_pbx_queue(pbx_queue)

Insert pbx queue

Insert a pbx queue 

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

pbx_queue = ultracart.ConversationPbxQueue() # ConversationPbxQueue | Pbx Queue

try:
    # Insert pbx queue
    api_response = api_instance.insert_pbx_queue(pbx_queue)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_time_based**
> ConversationPbxTimeBasedResponse insert_pbx_time_based(pbx_time_based)

Insert pbx timeBased

Insert a pbx timeBased 

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

pbx_time_based = ultracart.ConversationPbxTimeBased() # ConversationPbxTimeBased | Pbx TimeBased

try:
    # Insert pbx timeBased
    api_response = api_instance.insert_pbx_time_based(pbx_time_based)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_time_range**
> ConversationPbxTimeRangeResponse insert_pbx_time_range(pbx_time_range)

Insert pbx timeRange

Insert a pbx timeRange 

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

pbx_time_range = ultracart.ConversationPbxTimeRange() # ConversationPbxTimeRange | Pbx TimeRange

try:
    # Insert pbx timeRange
    api_response = api_instance.insert_pbx_time_range(pbx_time_range)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse insert_pbx_voicemail_mailbox(pbx_voicemail_mailbox)

Insert pbx voicemailMailbox

Insert a pbx voicemailMailbox 

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

pbx_voicemail_mailbox = ultracart.ConversationPbxVoicemailMailbox() # ConversationPbxVoicemailMailbox | Pbx VoicemailMailbox

try:
    # Insert pbx voicemailMailbox
    api_response = api_instance.insert_pbx_voicemail_mailbox(pbx_voicemail_mailbox)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_conversation**
> join_conversation(conversation_uuid, join_request=join_request)

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
join_request = ultracart.ConversationJoinRequest() # ConversationJoinRequest | Join request (optional)

try:
    # Join a conversation
    api_instance.join_conversation(conversation_uuid, join_request=join_request)
except ApiException as e:
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

# **listened_pbx_agent_voicemail**
> listened_pbx_agent_voicemail(recording_sid)

Listened Agent Voicemail

Listened pbx agent Voicemail 

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

recording_sid = 'recording_sid_example' # str | 

try:
    # Listened Agent Voicemail
    api_instance.listened_pbx_agent_voicemail(recording_sid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listened_pbx_queue_voicemail**
> listened_pbx_queue_voicemail(queue_uuid, recording_sid)

Listened Queue Voicemail

Listened pbx queue Voicemail 

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

queue_uuid = 'queue_uuid_example' # str | 
recording_sid = 'recording_sid_example' # str | 

try:
    # Listened Queue Voicemail
    api_instance.listened_pbx_queue_voicemail(queue_uuid, recording_sid)
except ApiException as e:
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

# **protect_pbx_phone_number**
> ConversationPbxPhoneNumberResponse protect_pbx_phone_number(conversation_pbx_phone_number_uuid)

Protect pbx phoneNumber from deletion

Protect a pbx phoneNumber from deletion. This is a one-way operation and cannot be undone through the API. 

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

conversation_pbx_phone_number_uuid = 'conversation_pbx_phone_number_uuid_example' # str | 

try:
    # Protect pbx phoneNumber from deletion
    api_response = api_instance.protect_pbx_phone_number(conversation_pbx_phone_number_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->protect_pbx_phone_number: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_pbx_phone_number**
> ConversationPbxPhoneNumberResponse purchase_pbx_phone_number(phone_number_purchase_request)

Purchase pbx phone number

Purchase a phone number from Twilio. The phone_number must be from the available phone number search results. 

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

phone_number_purchase_request = ultracart.ConversationPbxPhoneNumberPurchaseRequest() # ConversationPbxPhoneNumberPurchaseRequest | Phone number purchase request

try:
    # Purchase pbx phone number
    api_response = api_instance.purchase_pbx_phone_number(phone_number_purchase_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->purchase_pbx_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_purchase_request** | [**ConversationPbxPhoneNumberPurchaseRequest**](ConversationPbxPhoneNumberPurchaseRequest.md)| Phone number purchase request | 

### Return type

[**ConversationPbxPhoneNumberResponse**](ConversationPbxPhoneNumberResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_password_for_pbx_hardware_phone**
> ConversationPbxHardwarePhoneResponse regenerate_password_for_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid, pbx_hardware_phone)

Update pbx hardware phone

Update a pbx hardware phone 

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

conversation_pbx_hardware_phone_uuid = 'conversation_pbx_hardware_phone_uuid_example' # str | 
pbx_hardware_phone = ultracart.ConversationPbxHardwarePhone() # ConversationPbxHardwarePhone | Pbx Hardware Phone

try:
    # Update pbx hardware phone
    api_response = api_instance.regenerate_password_for_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid, pbx_hardware_phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->regenerate_password_for_pbx_hardware_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_hardware_phone_uuid** | **str**|  | 
 **pbx_hardware_phone** | [**ConversationPbxHardwarePhone**](ConversationPbxHardwarePhone.md)| Pbx Hardware Phone | 

### Return type

[**ConversationPbxHardwarePhoneResponse**](ConversationPbxHardwarePhoneResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_conversation_pbx_queue_statistics**
> reset_conversation_pbx_queue_statistics(queue_uuid)

reset statistics within the queue

reset statistics within the queue 

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

queue_uuid = 'queue_uuid_example' # str | 

try:
    # reset statistics within the queue
    api_instance.reset_conversation_pbx_queue_statistics(queue_uuid)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_conversation_canned_messages**
> ConversationCannedMessagesResponse search_conversation_canned_messages(search_request)

Search for canned messages by short_code

Search for canned messages by short_code 

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

search_request = ultracart.ConversationCannedMessagesSearch() # ConversationCannedMessagesSearch | Search request

try:
    # Search for canned messages by short_code
    api_response = api_instance.search_conversation_canned_messages(search_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_pbx_available_phone_numbers**
> ConversationPbxAvailablePhoneNumbersResponse search_pbx_available_phone_numbers(country, area_code=area_code, contains=contains, sms_enabled=sms_enabled, voice_enabled=voice_enabled, type=type, limit=limit)

Search for available phone numbers

Search for available phone numbers from Twilio that can be purchased 

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

country = 'country_example' # str | ISO country code (e.g., US, CA, GB)
area_code = 'area_code_example' # str | Area code filter (e.g., 614) (optional)
contains = 'contains_example' # str | Pattern to match (e.g., 555, *PIZZA) (optional)
sms_enabled = true # bool | Filter for SMS capability (optional)
voice_enabled = true # bool | Filter for voice capability (optional)
type = 'type_example' # str | Phone number type (optional)
limit = 56 # int | Max results (default 20, max 100) (optional)

try:
    # Search for available phone numbers
    api_response = api_instance.search_pbx_available_phone_numbers(country, area_code=area_code, contains=contains, sms_enabled=sms_enabled, voice_enabled=voice_enabled, type=type, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->search_pbx_available_phone_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO country code (e.g., US, CA, GB) | 
 **area_code** | **str**| Area code filter (e.g., 614) | [optional] 
 **contains** | **str**| Pattern to match (e.g., 555, *PIZZA) | [optional] 
 **sms_enabled** | **bool**| Filter for SMS capability | [optional] 
 **voice_enabled** | **bool**| Filter for voice capability | [optional] 
 **type** | **str**| Phone number type | [optional] 
 **limit** | **int**| Max results (default 20, max 100) | [optional] 

### Return type

[**ConversationPbxAvailablePhoneNumbersResponse**](ConversationPbxAvailablePhoneNumbersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_pbx_calls**
> ConversationPbxCallSearchResponse search_pbx_calls(search_request, limit=limit, offset=offset, sort=sort)

Search pbx call records

Search and list PBX call records with filtering, sorting, and pagination 

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

search_request = ultracart.ConversationPbxCallSearchRequest() # ConversationPbxCallSearchRequest | Search Request
limit = 100 # int | The maximum number of records to return on this one API call. (Maximum 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the calls. (optional)

try:
    # Search pbx call records
    api_response = api_instance.search_pbx_calls(search_request, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->search_pbx_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**ConversationPbxCallSearchRequest**](ConversationPbxCallSearchRequest.md)| Search Request | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the calls. | [optional] 

### Return type

[**ConversationPbxCallSearchResponse**](ConversationPbxCallSearchResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_unsubscribe_conversation**
> sms_unsubscribe_conversation(conversation_uuid)

Unsubscribe any SMS participants in this conversation

Unsubscribe any SMS participants in this conversation 

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
    # Unsubscribe any SMS participants in this conversation
    api_instance.sms_unsubscribe_conversation(conversation_uuid)
except ApiException as e:
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

# **update_agent_profile**
> ConversationAgentProfileResponse update_agent_profile(profile_request)

Update agent profile

Update agent profile 

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

profile_request = ultracart.ConversationAgentProfile() # ConversationAgentProfile | Profile request

try:
    # Update agent profile
    api_response = api_instance.update_agent_profile(profile_request)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_profile_mcp**
> ConversationMcpServerResponse update_agent_profile_mcp(user_id, mcp_server_uuid, mcp_server)

Update an agent MCP server

Update an agent MCP server 

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

user_id = 56 # int | 
mcp_server_uuid = 'mcp_server_uuid_example' # str | 
mcp_server = ultracart.ConversationMcpServer() # ConversationMcpServer | MCP Server

try:
    # Update an agent MCP server
    api_response = api_instance.update_agent_profile_mcp(user_id, mcp_server_uuid, mcp_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->update_agent_profile_mcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **mcp_server_uuid** | **str**|  | 
 **mcp_server** | [**ConversationMcpServer**](ConversationMcpServer.md)| MCP Server | 

### Return type

[**ConversationMcpServerResponse**](ConversationMcpServerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conversation_canned_message**
> ConversationCannedMessageResponse update_conversation_canned_message(conversation_canned_message_oid, canned_message)

Update a canned message

Update a canned message 

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

conversation_canned_message_oid = 56 # int | 
canned_message = ultracart.ConversationCannedMessage() # ConversationCannedMessage | Canned message

try:
    # Update a canned message
    api_response = api_instance.update_conversation_canned_message(conversation_canned_message_oid, canned_message)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conversation_department**
> ConversationDepartmentResponse update_conversation_department(conversation_department_oid, department)

Update a department

Update a department 

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

conversation_department_oid = 56 # int | 
department = ultracart.ConversationDepartment() # ConversationDepartment | Department

try:
    # Update a department
    api_response = api_instance.update_conversation_department(conversation_department_oid, department)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conversation_engagement**
> ConversationEngagementResponse update_conversation_engagement(conversation_engagement_oid, engagement)

Update a engagement

Update a engagement 

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

conversation_engagement_oid = 56 # int | 
engagement = ultracart.ConversationEngagement() # ConversationEngagement | Engagement

try:
    # Update a engagement
    api_response = api_instance.update_conversation_engagement(conversation_engagement_oid, engagement)
    pprint(api_response)
except ApiException as e:
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

# **update_pbx_address**
> ConversationPbxAddressResponse update_pbx_address(conversation_pbx_address_uuid, pbx_address)

Update pbx address

Update a pbx address 

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

conversation_pbx_address_uuid = 'conversation_pbx_address_uuid_example' # str | 
pbx_address = ultracart.ConversationPbxAddress() # ConversationPbxAddress | Pbx Address

try:
    # Update pbx address
    api_response = api_instance.update_pbx_address(conversation_pbx_address_uuid, pbx_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->update_pbx_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_address_uuid** | **str**|  | 
 **pbx_address** | [**ConversationPbxAddress**](ConversationPbxAddress.md)| Pbx Address | 

### Return type

[**ConversationPbxAddressResponse**](ConversationPbxAddressResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_agent**
> ConversationPbxAgentResponse update_pbx_agent(conversation_pbx_agent_uuid, pbx_agent)

Update pbx agent

Update a pbx agent 

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

conversation_pbx_agent_uuid = 'conversation_pbx_agent_uuid_example' # str | 
pbx_agent = ultracart.ConversationPbxAgent() # ConversationPbxAgent | Pbx Agent

try:
    # Update pbx agent
    api_response = api_instance.update_pbx_agent(conversation_pbx_agent_uuid, pbx_agent)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_audio**
> ConversationPbxAudioResponse update_pbx_audio(conversation_pbx_audio_uuid, pbx_audio)

Update pbx audio

Update a pbx audio 

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

conversation_pbx_audio_uuid = 'conversation_pbx_audio_uuid_example' # str | 
pbx_audio = ultracart.ConversationPbxAudio() # ConversationPbxAudio | Pbx Audio

try:
    # Update pbx audio
    api_response = api_instance.update_pbx_audio(conversation_pbx_audio_uuid, pbx_audio)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_class_of_service**
> ConversationPbxClassOfServiceResponse update_pbx_class_of_service(class_of_service_uuid, class_of_service)

Update pbx class of service

Update an existing class of service 

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

class_of_service_uuid = 'class_of_service_uuid_example' # str | 
class_of_service = ultracart.ConversationPbxClassOfService() # ConversationPbxClassOfService | Class of service

try:
    # Update pbx class of service
    api_response = api_instance.update_pbx_class_of_service(class_of_service_uuid, class_of_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->update_pbx_class_of_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_of_service_uuid** | **str**|  | 
 **class_of_service** | [**ConversationPbxClassOfService**](ConversationPbxClassOfService.md)| Class of service | 

### Return type

[**ConversationPbxClassOfServiceResponse**](ConversationPbxClassOfServiceResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_hardware_phone**
> ConversationPbxHardwarePhoneResponse update_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid, pbx_hardware_phone)

Update pbx hardware phone

Update a pbx hardware phone 

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

conversation_pbx_hardware_phone_uuid = 'conversation_pbx_hardware_phone_uuid_example' # str | 
pbx_hardware_phone = ultracart.ConversationPbxHardwarePhone() # ConversationPbxHardwarePhone | Pbx Hardware Phone

try:
    # Update pbx hardware phone
    api_response = api_instance.update_pbx_hardware_phone(conversation_pbx_hardware_phone_uuid, pbx_hardware_phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->update_pbx_hardware_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_pbx_hardware_phone_uuid** | **str**|  | 
 **pbx_hardware_phone** | [**ConversationPbxHardwarePhone**](ConversationPbxHardwarePhone.md)| Pbx Hardware Phone | 

### Return type

[**ConversationPbxHardwarePhoneResponse**](ConversationPbxHardwarePhoneResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_menu**
> ConversationPbxMenuResponse update_pbx_menu(conversation_pbx_menu_uuid, pbx_menu)

Update pbx menu

Update a pbx menu 

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

conversation_pbx_menu_uuid = 'conversation_pbx_menu_uuid_example' # str | 
pbx_menu = ultracart.ConversationPbxMenu() # ConversationPbxMenu | Pbx Menu

try:
    # Update pbx menu
    api_response = api_instance.update_pbx_menu(conversation_pbx_menu_uuid, pbx_menu)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_phone_number**
> ConversationPbxPhoneNumberResponse update_pbx_phone_number(conversation_pbx_phone_number_uuid, pbx_phone_number)

Update pbx phoneNumber

Update a pbx phoneNumber 

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

conversation_pbx_phone_number_uuid = 'conversation_pbx_phone_number_uuid_example' # str | 
pbx_phone_number = ultracart.ConversationPbxPhoneNumber() # ConversationPbxPhoneNumber | Pbx PhoneNumber

try:
    # Update pbx phoneNumber
    api_response = api_instance.update_pbx_phone_number(conversation_pbx_phone_number_uuid, pbx_phone_number)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_queue**
> ConversationPbxQueueResponse update_pbx_queue(conversation_pbx_queue_uuid, pbx_queue)

Update pbx queue

Update a pbx queue 

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

conversation_pbx_queue_uuid = 'conversation_pbx_queue_uuid_example' # str | 
pbx_queue = ultracart.ConversationPbxQueue() # ConversationPbxQueue | Pbx Queue

try:
    # Update pbx queue
    api_response = api_instance.update_pbx_queue(conversation_pbx_queue_uuid, pbx_queue)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_time_based**
> ConversationPbxTimeBasedResponse update_pbx_time_based(conversation_pbx_time_based_uuid, pbx_time_based)

Update pbx timeBased

Update a pbx timeBased 

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

conversation_pbx_time_based_uuid = 'conversation_pbx_time_based_uuid_example' # str | 
pbx_time_based = ultracart.ConversationPbxTimeBased() # ConversationPbxTimeBased | Pbx TimeBased

try:
    # Update pbx timeBased
    api_response = api_instance.update_pbx_time_based(conversation_pbx_time_based_uuid, pbx_time_based)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_time_range**
> ConversationPbxTimeRangeResponse update_pbx_time_range(conversation_pbx_time_range_uuid, pbx_time_range)

Update pbx timeRange

Update a pbx timeRange 

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

conversation_pbx_time_range_uuid = 'conversation_pbx_time_range_uuid_example' # str | 
pbx_time_range = ultracart.ConversationPbxTimeRange() # ConversationPbxTimeRange | Pbx TimeRange

try:
    # Update pbx timeRange
    api_response = api_instance.update_pbx_time_range(conversation_pbx_time_range_uuid, pbx_time_range)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbx_voicemail_mailbox**
> ConversationPbxVoicemailMailboxResponse update_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid, pbx_voicemail_mailbox)

Update pbx voicemailMailbox

Update a pbx voicemailMailbox 

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

conversation_pbx_voicemail_mailbox_uuid = 'conversation_pbx_voicemail_mailbox_uuid_example' # str | 
pbx_voicemail_mailbox = ultracart.ConversationPbxVoicemailMailbox() # ConversationPbxVoicemailMailbox | Pbx VoicemailMailbox

try:
    # Update pbx voicemailMailbox
    api_response = api_instance.update_pbx_voicemail_mailbox(conversation_pbx_voicemail_mailbox_uuid, pbx_voicemail_mailbox)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_agent_budget**
> ConversationVirtualAgentBudgetResponse update_virtual_agent_budget(virtual_agent_budget)

Update virtual agent budget

Update virtual agent budget 

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

virtual_agent_budget = ultracart.ConversationVirtualAgentBudget() # ConversationVirtualAgentBudget | Virtual Agent Budget

try:
    # Update virtual agent budget
    api_response = api_instance.update_virtual_agent_budget(virtual_agent_budget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->update_virtual_agent_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_agent_budget** | [**ConversationVirtualAgentBudget**](ConversationVirtualAgentBudget.md)| Virtual Agent Budget | 

### Return type

[**ConversationVirtualAgentBudgetResponse**](ConversationVirtualAgentBudgetResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_agent_capabilities**
> ConversationVirtualAgentCapabilitiesResponse update_virtual_agent_capabilities(virtual_agent_capabilities)

Update virtual agent capabilities

Update virtual agent capabilities 

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

virtual_agent_capabilities = ultracart.ConversationVirtualAgentCapabilities() # ConversationVirtualAgentCapabilities | Virtual Agent Capabilities

try:
    # Update virtual agent capabilities
    api_response = api_instance.update_virtual_agent_capabilities(virtual_agent_capabilities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->update_virtual_agent_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_agent_capabilities** | [**ConversationVirtualAgentCapabilities**](ConversationVirtualAgentCapabilities.md)| Virtual Agent Capabilities | 

### Return type

[**ConversationVirtualAgentCapabilitiesResponse**](ConversationVirtualAgentCapabilitiesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

