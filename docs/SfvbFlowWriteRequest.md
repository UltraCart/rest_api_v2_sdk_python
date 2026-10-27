# SfvbFlowWriteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_concurrent_enrollments** | **bool** | True when a customer may be in this flow more than once at a time. | [optional] 
**end_once_customer_purchases** | **bool** | True to end the flow for a customer once they buy from one of its emails. | [optional] 
**end_once_customer_purchases_anywhere** | **bool** | True to end the flow for a customer once they buy from any source. | [optional] 
**name** | **str** | The flow name, 1 to 250 characters.  Required to create. | [optional] 
**reentry_delay_days** | **int** | Days before a customer may enter again, 1 to 1095.  Only with after_days. | [optional] 
**reentry_policy** | **str** | Whether a customer may enter again, anytime, after_days or never. | [optional] 
**sending_domain_uuid** | **str** | The sending domain uuid.  Defaults to the storefront&#39;s marketing sending domain. | [optional] 
**sending_name** | **str** | The from name.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**sending_user** | **str** | The part of the from address before the at sign.  Defaults to the storefront&#39;s marketing setting. | [optional] 
**trigger_parameter** | **str** | The list or segment uuid for a list or segment trigger.  Create only. | [optional] 
**trigger_type** | **str** | What enrolls a customer, such as cart abandoned.  Create only. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


