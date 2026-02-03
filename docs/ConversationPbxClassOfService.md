# ConversationPbxClassOfService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_countries** | **list[str]** | E.164 country calling codes (e.g. 1 for US/Canada, 44 for UK). Empty means domestic only. | [optional] 
**block_premium_numbers** | **bool** | Block calls to 900, 976, premium-rate, and shortcode destinations | [optional] 
**conversation_pbx_class_of_service_uuid** | **str** | Class of Service unique identifier | [optional] 
**default_flag** | **bool** | If true, this CoS applies to all agents without an explicit cos_uuid. Only one per merchant. | [optional] 
**description** | **str** | Description of the class of service | [optional] 
**merchant_id** | **str** | Merchant Id | [optional] 
**name** | **str** | Display name for the class of service | [optional] 
**outbound_enabled** | **bool** | Whether agents with this CoS can make outbound calls | [optional] 
**time_range_uuid** | **str** | UUID of a time range. If set, outbound calls only permitted during those time windows. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


