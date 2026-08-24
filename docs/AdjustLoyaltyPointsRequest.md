# AdjustLoyaltyPointsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of this adjustment, 200 characters max | [optional] 
**loyalty_points** | **int** | The number of loyalty points to add to the ledger.  Use a negative number to debit points.  Required and may not be zero. | [optional] 
**order_id** | **str** | Optional order id if this adjustment is related to a particular order | [optional] 
**vesting_days** | **int** | Optional days required for this adjustment to vest.  Leave null to use the merchant configured default.  Use zero for immediate vesting. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


