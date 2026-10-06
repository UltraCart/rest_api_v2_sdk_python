# SfvbRedirectImportResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | True when the rows were written. | [optional] 
**blocked** | **int** | How many rows have a blocking finding.  Any blocked row means nothing is applied. | [optional] 
**flagged** | **int** | How many rows have only warnings. | [optional] 
**limit** | **int** | The most rules a storefront may have through SFVB. | [optional] 
**plan_hash** | **str** | Send back with the same rows to apply exactly this plan. | [optional] 
**rows** | [**[SfvbRedirectImportRowResult]**](SfvbRedirectImportRowResult.md) | The rows with findings. | [optional] 
**rule_count** | **int** | How many rules the storefront has, or would have after applying. | [optional] 
**total** | **int** | How many rows were sent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


