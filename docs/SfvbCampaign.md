# SfvbCampaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_uuid** | **str** | The campaign uuid. | [optional] 
**communication_sequence_uuid** | **str** | The communication sequence the steps belong to. | [optional] 
**created_dts** | **str** | When the campaign was created (ISO 8601, UTC). | [optional] 
**deleted** | **bool** | True when the campaign was deleted. | [optional] 
**emails** | [**[SfvbCommsEmail]**](SfvbCommsEmail.md) | Its emails, in step order. | [optional] 
**end_once_customer_purchases** | **bool** | True when a customer leaves the campaign once they buy from one of its emails. | [optional] 
**end_once_customer_purchases_anywhere** | **bool** | True when a customer leaves the campaign once they buy from any source. | [optional] 
**hash_sha256** | **str** | Send this as If-Match when changing or archiving the campaign. | [optional] 
**live** | **bool** | True when the emails and postcards reach customers now, so a change to one shows at once.  False only in a status that sends nothing. | [optional] 
**memberships** | [**[SfvbCampaignMembership]**](SfvbCampaignMembership.md) | The lists and segments it sends to or leaves out. | [optional] 
**name** | **str** | The campaign name. | [optional] 
**notes** | **[str]** | What a write did beyond the fields it was asked to change, such as putting emails back to needing review or setting a scheduled campaign back to draft.  Only on a write. | [optional] 
**postcards** | [**[SfvbCommsPostcard]**](SfvbCommsPostcard.md) | Its postcards, in step order. | [optional] 
**scheduled_dts** | **str** | When the campaign is scheduled to send (ISO 8601, UTC), when it is. | [optional] 
**sending_domain_uuid** | **str** | The sending domain uuid.  Defaults to the storefront&#39;s marketing sending domain. | [optional] 
**sending_name** | **str** | The from name.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**sending_user** | **str** | The part of the from address before the at sign.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**status** | **str** | The status, such as draft, scheduled, sending, sent or archived. | [optional] 
**status_dts** | **str** | When the status last changed (ISO 8601, UTC). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


