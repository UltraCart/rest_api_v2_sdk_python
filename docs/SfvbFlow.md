# SfvbFlow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_concurrent_enrollments** | **bool** | True when a customer may be in this flow more than once at a time. | [optional] 
**communication_sequence_uuid** | **str** | The communication sequence the steps belong to. | [optional] 
**created_dts** | **str** | When the flow was created (ISO 8601, UTC). | [optional] 
**deleted** | **bool** | True when the flow was deleted. | [optional] 
**emails** | [**[SfvbCommsEmail]**](SfvbCommsEmail.md) | Its emails, in step order. | [optional] 
**end_once_customer_purchases** | **bool** | True when a customer leaves the flow once they buy from one of its emails. | [optional] 
**end_once_customer_purchases_anywhere** | **bool** | True when a customer leaves the flow once they buy from any source. | [optional] 
**flow_uuid** | **str** | The flow uuid. | [optional] 
**hash_sha256** | **str** | Send this as If-Match when changing, archiving or turning the flow on or off. | [optional] 
**live** | **bool** | True when the emails and postcards reach customers now, so a change to one shows at once.  False only in a status that sends nothing. | [optional] 
**name** | **str** | The flow name. | [optional] 
**notes** | **[str]** | What a write did beyond the fields it was asked to change, such as putting emails back to needing review or setting a scheduled campaign back to draft.  Only on a write. | [optional] 
**postcards** | [**[SfvbCommsPostcard]**](SfvbCommsPostcard.md) | Its postcards, in step order. | [optional] 
**reentry_delay_days** | **int** | Days before a customer may enter again, with after_days. | [optional] 
**reentry_policy** | **str** | Whether a customer may enter again, anytime, after_days or never. | [optional] 
**sending_domain_uuid** | **str** | The sending domain uuid.  Defaults to the storefront&#39;s marketing sending domain. | [optional] 
**sending_name** | **str** | The from name.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**sending_user** | **str** | The part of the from address before the at sign.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**status** | **str** | The status, such as draft, active, paused, draining or inactive. | [optional] 
**status_dts** | **str** | When the status last changed (ISO 8601, UTC). | [optional] 
**trigger_parameter** | **str** | The list or segment uuid, or other value, the trigger is limited to. | [optional] 
**trigger_parameter_name** | **str** | The name of the trigger parameter, when the trigger takes one. | [optional] 
**trigger_type** | **str** | What starts the flow, such as cart abandon or an order. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


