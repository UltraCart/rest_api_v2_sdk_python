# AvalaraConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Avalara account ID | [optional] 
**active** | **bool** | True if Avalara is active for this merchant | [optional] 
**avalara_oid** | **int** | Unique identifier for this avalara config object | [optional] 
**company_id** | **str** | Avalara company ID | [optional] 
**enable_upc** | **bool** | True if this Avalara configuration is set to enable tax valuation by UPC | [optional] 
**estimate_only** | **bool** | True if this Avalara configuration is to estimate taxes only and not report placed orders to Avalara | [optional] 
**guest_customer_code** | **str** | Optional customer code for customers without profiles, defaults to GuestCustomer | [optional] 
**last_test_dts** | **str** | Date/time of the connection test to Avalara | [optional] 
**license_key** | **str** | Avalara license key | [optional] 
**sandbox** | **bool** | True if this Avalara instance is pointed at the Avalara Sandbox | [optional] 
**send_test_orders** | **bool** | Send test orders through to Avalara.  The default is to not transmit test orders to Avalara. | [optional] 
**service_url** | **str** | Avalara service URL | [optional] 
**test_results** | **str** | Test results of the last connection test to Avalara | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


