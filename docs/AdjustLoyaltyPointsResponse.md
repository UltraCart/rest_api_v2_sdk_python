# AdjustLoyaltyPointsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_points** | **int** | The current (vested) points balance after the adjustment was made | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**loyalty_points** | **int** | The loyalty points adjustment that was written to the ledger | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**pending_points** | **int** | The pending (unvested) points balance after the adjustment was made | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


