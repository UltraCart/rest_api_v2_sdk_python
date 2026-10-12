# SfvbEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_dts** | **str** | When it happened, ISO 8601. | [optional] 
**event_id** | **str** | Time-ordered id.  Pass the last one seen as after to replay what came since. | [optional] 
**object_id** | **str** | The id of what changed, such as the approval_id. | [optional] 
**object_type** | **str** | What changed, such as approval. | [optional] 
**storefront_oid** | **int** | The storefront it concerns.  Empty for merchant-level objects. | [optional] 
**type** | **str** | approval.decided (approved, denied, cancelled or refused by the script review) or approval.ready (the review finished and the person can decide). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


