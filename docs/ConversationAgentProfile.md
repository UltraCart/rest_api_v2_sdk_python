# ConversationAgentProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai** | **bool** | AI powered chat bot | [optional] 
**ai_capabilities** | [**ConversationVirtualAgentCapabilities**](ConversationVirtualAgentCapabilities.md) |  | [optional] 
**ai_chat_instructions** | **str** | Additional instructions for this AI when handle web chats | [optional] 
**ai_persona** | **str** | Persona of this AI agent | [optional] 
**ai_sms_instructions** | **str** | Additional instructions for this AI when handle SMS messages | [optional] 
**ai_ticket_instructions** | **str** | Additional instructions for this AI when handling ticket draft replies | [optional] 
**chat_limit** | **int** | The number of engagement chats that can be pushed on them at any given time. | [optional] 
**default_language_iso_code** | **str** | The default language the agent is chatting in | [optional] 
**default_status** | **str** | Default status when the agent loads conversations app. | [optional] 
**display_name** | **str** | An alternate name that the agent wants to use in chat. | [optional] 
**name** | **str** | Their actual user name for profile settings display as placeholder test | [optional] 
**profile_image_upload_key** | **str** | An upload key used to update the profile image. | [optional] 
**profile_image_url** | **str** | Their current profile image URL | [optional] 
**user_id** | **int** | User ID associated with the agent.  Populated by getAgentProfiles call only. | [optional] 
**zohodesk_classifications** | **[str]** | Restrict this agent to drafting replies only to tickets with these classifications | [optional] 
**zohodesk_departments** | **[str]** | Restrict this agent to drafting replies only to these department ids | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


