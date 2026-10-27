# SfvbCampaignWriteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_once_customer_purchases** | **bool** | True to end the campaign for a customer once they buy from one of its emails. | [optional] 
**end_once_customer_purchases_anywhere** | **bool** | True to end the campaign for a customer once they buy from any source. | [optional] 
**memberships** | [**[SfvbCampaignMembership]**](SfvbCampaignMembership.md) | The lists and segments it sends to or leaves out.  Replaces the whole set.  An empty array clears it. | [optional] 
**name** | **str** | The campaign name, 1 to 250 characters.  Required to create. | [optional] 
**scheduled_dts** | **str** | When to send once started (ISO 8601).  An empty string clears the schedule. | [optional] 
**sending_domain_uuid** | **str** | The sending domain uuid.  Defaults to the storefront&#39;s marketing sending domain. | [optional] 
**sending_name** | **str** | The from name.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**sending_user** | **str** | The part of the from address before the at sign.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


