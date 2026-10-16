# SfvbFlow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_sequence_uuid** | **str** | The communication sequence the steps belong to. | [optional] 
**created_dts** | **str** | When the flow was created (ISO 8601, UTC). | [optional] 
**deleted** | **bool** | True when the flow was deleted. | [optional] 
**emails** | [**[SfvbCommsEmail]**](SfvbCommsEmail.md) | Its emails, in step order. | [optional] 
**flow_uuid** | **str** | The flow uuid. | [optional] 
**live** | **bool** | True when the emails and postcards reach customers now, so a change to one shows at once.  False only in a status that sends nothing. | [optional] 
**name** | **str** | The flow name. | [optional] 
**postcards** | [**[SfvbCommsPostcard]**](SfvbCommsPostcard.md) | Its postcards, in step order. | [optional] 
**status** | **str** | The status, such as draft, active, paused, draining or inactive. | [optional] 
**status_dts** | **str** | When the status last changed (ISO 8601, UTC). | [optional] 
**trigger_parameter_name** | **str** | The name of the trigger parameter, when the trigger takes one. | [optional] 
**trigger_type** | **str** | What starts the flow, such as cart abandon or an order. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


