# ConversationWebchatQueueStatusAgent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_status** | **str** | Status of the agent | [optional] 
**agent_user_id** | **str** | Agent user id (populated by Java so the dispatch-scheduler Lambda can read it directly without parsing conversation_participant_arn) | [optional] 
**conversation_participant_arn** | **str** |  | [optional] 
**conversation_participant_name** | **str** |  | [optional] 
**custom_status_name** | **str** | Active custom status display name for this agent (denormalized) | [optional] 
**custom_status_uuid** | **str** | Active custom status uuid for this agent (null when on a system status) | [optional] 
**last_chat_dts** | **str** | Date/time that this agent took their last chat | [optional] 
**next_round_robin** | **bool** |  | [optional] 
**profile_image_url** | **str** | Profile image URL | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


