# SfvbRedirectResolveBatchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_found** | **int** | How many paths end on a 404 (lands_on not_found), the ones to redirect or create. | [optional] 
**redirected** | **int** | How many paths at least one rule redirects. | [optional] 
**results** | [**[SfvbRedirectResolveResponse]**](SfvbRedirectResolveResponse.md) | One result per path, in the order sent, the same as the single resolve&#39;s answer. | [optional] 
**total** | **int** | How many paths were resolved. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


