# AdjustInternalCertificateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_amount** | **float** | The adjustment amount | [optional] 
**description** | **str** | Description of this adjustment, 50 characters max | [optional] 
**entry_dts** | **str** | Optional timestamp for the adjustment, defaults to current time | [optional] 
**expiration_days** | **int** | Optional expiration days from the entry_dts when these adjustment becomes worthless | [optional] 
**order_id** | **str** | Optional order id if this adjustment is related to a particular order | [optional] 
**vesting_days** | **int** | Optional days required for this adjustment to vest | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


