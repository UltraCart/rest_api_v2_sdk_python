# SfvbCampaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_uuid** | **str** | The campaign uuid. | [optional] 
**communication_sequence_uuid** | **str** | The communication sequence the steps belong to. | [optional] 
**created_dts** | **str** | When the campaign was created (ISO 8601, UTC). | [optional] 
**deleted** | **bool** | True when the campaign was deleted. | [optional] 
**emails** | [**[SfvbCommsEmail]**](SfvbCommsEmail.md) | Its emails, in step order. | [optional] 
**live** | **bool** | True when the emails and postcards reach customers now, so a change to one shows at once.  False only in a status that sends nothing. | [optional] 
**name** | **str** | The campaign name. | [optional] 
**postcards** | [**[SfvbCommsPostcard]**](SfvbCommsPostcard.md) | Its postcards, in step order. | [optional] 
**scheduled_dts** | **str** | When the campaign is scheduled to send (ISO 8601, UTC), when it is. | [optional] 
**status** | **str** | The status, such as draft, scheduled, sending, sent or archived. | [optional] 
**status_dts** | **str** | When the status last changed (ISO 8601, UTC). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


