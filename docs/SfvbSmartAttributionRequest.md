# SfvbSmartAttributionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assist_percent** | **float** | 0 to 1, at most 4 decimals. | [optional] 
**attribution_model** | **str** | position_based, linear, time_decay or custom. | [optional] 
**closer_percent** | **float** | 0 to 1, at most 4 decimals. | [optional] 
**lookback_days** | **int** | 7 to 365. | [optional] 
**mode** | **str** | disabled, report_only or active.  Making it active, or any change while it is active, needs an approval. | [optional] 
**originator_percent** | **float** | 0 to 1, at most 4 decimals.  The three global percentages must total exactly 1, so send all three to change the split. | [optional] 
**platforms** | [**[SfvbSmartAttributionPlatform]**](SfvbSmartAttributionPlatform.md) | When sent, replaces the whole platform list.  Up to 100, each name and id once.  Left out, the list is unchanged. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


