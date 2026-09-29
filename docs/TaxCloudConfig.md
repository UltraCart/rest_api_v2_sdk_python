# TaxCloudConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | TaxCloud API key | [optional] 
**connection_id** | **str** | TaxCloud Connection ID (a UUID) identifying the TaxCloud connection to use; a test connection and a production connection have different IDs | [optional] 
**default_tic** | **str** | Default TaxCloud TIC (Taxability Information Code), used for items that do not have their own TIC; blank lets TaxCloud apply its default (0, general goods) | [optional] 
**estimate_only** | **bool** | True if this TaxCloud configuration is to estimate taxes only and not report placed orders to TaxCloud | [optional] 
**last_test_dts** | **str** | Date/time of the connection test to TaxCloud | [optional] 
**shipping_tic** | **str** | TaxCloud TIC used to classify shipping/handling charges (11000 &#x3D; shipping and handling); blank means shipping is not taxed | [optional] 
**test_results** | **str** | Test results of the last connection test to TaxCloud | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


