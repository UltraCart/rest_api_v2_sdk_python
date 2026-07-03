# CartItemOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_if_specified** | [**Currency**](Currency.md) |  | [optional] 
**cost_per_letter** | [**Currency**](Currency.md) |  | [optional] 
**cost_per_line** | [**Currency**](Currency.md) |  | [optional] 
**ignore_if_default** | **bool** | True if the default answer is ignored | [optional] 
**label** | **str** | Display label for the option | [optional] 
**name** | **str** | Name of the option | [optional] 
**one_time_fee** | **bool** | Charge the fee a single time instead of multiplying by the quantity | [optional] 
**option_oid** | **int** | Unique identifier for the option | [optional] 
**required** | **bool** | True if the customer is required to select a value | [optional] 
**selected_value** | **str** | The value of the option specified by the customer | [optional] 
**type** | **str** | Type of option | [optional] 
**values** | [**[CartItemOptionValue]**](CartItemOptionValue.md) | Values that the customer can select from for radio or select type options | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


