# CartUpsellAfter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finalize_after_dts** | **str** | The date/time after which the cart will finalize into an order. | [optional] 
**finalize_after_minutes** | **int** | The amount of inactivity in minutes after which the cart should be finalized into an order.  This will calculate the finalize_after_dts field. | [optional] 
**upsell_path_code** | **str** | Upsell path code (this is for legacy upsells only) | [optional] 
**upsell_path_name** | **str** | Upsell path name to start on (StoreFront Upsells).  Will only be respected on a handoff API call. | [optional] 
**upsell_path_variation** | **str** | Upsell path variation to start on (StoreFront Upsells).   Will only be respected on a handoff API call. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


