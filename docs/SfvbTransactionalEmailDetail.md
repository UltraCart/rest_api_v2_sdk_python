# SfvbTransactionalEmailDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_options** | [**[SfvbTransactionalDeliveryOption]**](SfvbTransactionalDeliveryOption.md) | Its delivery options.  Empty for an email that has none. | [optional] 
**file_name** | **str** | The HTML template file, such as receipt_html.vm. | [optional] 
**hash_sha256** | **str** | The hash of the subject, the options and the sender.  Send it as If-Match to change them. | [optional] 
**name** | **str** | The display name, such as Order - Receipt. | [optional] 
**sender** | [**SfvbTransactionalSender**](SfvbTransactionalSender.md) |  | [optional] 
**sender_shared_with** | **[str]** | Every storefront on this account that shares the sender, this one included. | [optional] 
**subject** | **str** | The subject line. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


