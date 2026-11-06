# SfvbFlowBackfillResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capped** | **bool** | True when the plan&#39;s customer limit stopped the count. | [optional] 
**customers** | **int** | How many different customers those are. | [optional] 
**dry_run** | **bool** | True when nothing was enrolled. | [optional] 
**enrollments** | **int** | How many enrollments the backfill makes (a purchased product trigger makes one per item). | [optional] 
**flow_uuid** | **str** | The flow. | [optional] 
**notes** | **[str]** | What happens next, in sentences. | [optional] 
**order_days_old** | **int** | The days of orders, for an order trigger. | [optional] 
**relative_to_event** | **bool** | Whether the first wait is shortened by each order&#39;s age. | [optional] 
**segment_rebuild_required** | **bool** | True when the segment needs a rebuild, so the count is from its last one. | [optional] 
**started** | **bool** | True when the backfill started in the background.  The signed-in user is emailed when it ends. | [optional] 
**trigger_type** | **str** | The flow&#39;s trigger. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


