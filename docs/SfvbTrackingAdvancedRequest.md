# SfvbTrackingAdvancedRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_url** | **str** | A path starting with / or an absolute http or https URL, up to 250 characters. | [optional] 
**continue_shopping_url** | **str** | A path starting with / or an absolute http or https URL, up to 250 characters. | [optional] 
**conversion_pixel_only_if_paid** | **bool** | True to run the receipt&#39;s conversion HTML only for orders whose payment succeeded. | [optional] 
**default_currency** | **str** | A currency code from the read&#39;s currencies. | [optional] 
**dry_run** | **bool** | True to check the change and report it without saving. | [optional] 
**omit_order_data** | **bool** | True to leave the order data off the custom thank you URL. | [optional] 
**payment_pending_url** | **str** | A path starting with / or an absolute http or https URL, up to 500 characters. | [optional] 
**thank_you_url** | **str** | A path starting with / or an absolute http or https URL, up to 500 characters. | [optional] 
**unset** | **[str]** | Text settings to clear, by key.  continue_shopping_url, catalog_url, thank_you_url, payment_pending_url or default_currency.  Not with a value for the same key. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


