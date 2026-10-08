# SfvbRedirectDeleteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | True when this call deleted rules. | [optional] 
**deletable** | **int** | Rows that can be, or on an apply could be, deleted. | [optional] 
**deleted** | **int** | Rules deleted.  Zero on a dry run. | [optional] 
**limit** | **int** | The most rules a storefront can have for add and import to work. | [optional] 
**not_found** | **int** | Rows naming no rule on this storefront.  Skipped. | [optional] 
**plan_hash** | **str** | Send this to apply exactly these rows.  Also what an approval for them is bound to. | [optional] 
**rows** | [**[SfvbRedirectDeleteRowResult]**](SfvbRedirectDeleteRowResult.md) | One result per row, in request order. | [optional] 
**rule_count** | **int** | The storefront&#39;s redirect rules now.  After an apply, after the delete. | [optional] 
**stale** | **int** | Rows whose rule changed since its hash was read.  Skipped. | [optional] 
**total** | **int** | Rows in the request. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


