# SfvbTestOrdersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hint** | **str** | Present when nothing matched.  Says how to place a test order. | [optional] 
**searched_days** | **int** | How many days back were searched, 7, 30 or 90, widening until enough test orders were found. | [optional] 
**test_orders** | [**[SfvbTestOrder]**](SfvbTestOrder.md) | Test orders, newest first.  Only orders marked as test orders are ever listed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


