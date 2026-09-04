# ConversationAgentTestSessionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart_id** | **str** | Cart established for this session, soft logged in as the chosen customer profile.  Real, and anything the agent adds to it persists. | [optional] 
**conversation_webchat_queue_uuid** | **str** | Queue entry created for this session | [optional] 
**customer_auth** | [**ConversationCustomerAuth**](ConversationCustomerAuth.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**storefront_host_name** | **str** | Storefront the session is running against | [optional] 
**success** | **bool** |  | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


