# SfvbPageRefreshResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A plain sentence saying what happened. | [optional] 
**path** | **str** | The page path the refresh used, after normalization. | [optional] 
**refreshed** | **bool** | True when a cached copy was dropped.  The next request renders the page fresh. | [optional] 
**was_cached** | **bool** | True when the page had a cache entry. | [optional] 
**was_valid** | **bool** | True when that entry was being served from cache. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


