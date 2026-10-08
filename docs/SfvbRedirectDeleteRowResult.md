# SfvbRedirectDeleteRowResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_sha256** | **str** | The rule&#39;s current hash.  Absent when not_found. | [optional] 
**note** | **str** | The rule&#39;s note. | [optional] 
**redirect_id** | **int** | The rule. | [optional] 
**result** | **str** | deletable, stale (the rule changed since its hash was read), not_found, or deleted after an apply. | [optional] 
**source** | **str** | The rule&#39;s source, for a backup. | [optional] 
**status** | **str** | The rule&#39;s status (301, 302 or rewrite). | [optional] 
**target** | **str** | The rule&#39;s target, for a backup. | [optional] 
**type** | **str** | exact or pattern. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


