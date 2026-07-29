# AutoOrderRebillResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_order** | [**AutoOrder**](AutoOrder.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**failure_reason** | **str** | Why the rebill attempt did not succeed | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**rebill_attempted** | **bool** | True if a rebill was attempted during this call | [optional] 
**rebill_order_id** | **str** | The order id created by a successful rebill | [optional] 
**rebill_success** | **bool** | True if the rebill attempt produced an order | [optional] 
**success** | **bool** | Indicates if API call was successful | [optional] 
**warning** | [**Warning**](Warning.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


