# SfvbCommsTestPostcardRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | The street address. | [optional] 
**address2** | **str** | The second address line. | [optional] 
**cart_item_ids** | **[str]** | Items for a cart flow&#39;s card. | [optional] 
**city** | **str** | The city. | [optional] 
**dry_run** | **bool** | Check everything, including that postcards are turned on, and show the cost, without mailing or using an approval. | [optional] 
**mail_card** | **bool** | Must be true.  Without it nothing is mailed; use the postcard proof to see the card. | [optional] 
**name** | **str** | The recipient&#39;s name. | [optional] 
**order_id** | **str** | A test order to render an order flow&#39;s card with.  A real customer&#39;s order is refused. | [optional] 
**postal_code** | **str** | The postal code. | [optional] 
**state** | **str** | The state. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


