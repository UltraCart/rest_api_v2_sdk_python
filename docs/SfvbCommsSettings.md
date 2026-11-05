# SfvbCommsSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_sha256** | **str** | The hash of the settings.  Send it as If-Match to change them. | [optional] 
**machine_open_ignore** | **bool** | True when opens by mail privacy proxies are ignored.  Account-wide; changed in the admin. | [optional] 
**marketing_sender** | [**SfvbCommsSender**](SfvbCommsSender.md) |  | [optional] 
**postcard_return_address** | [**SfvbPostcardAddress**](SfvbPostcardAddress.md) |  | [optional] 
**postcard_return_address_complete** | **bool** | True when the name, street, city, state and postal code are all set.  Until then postcards fall back as the send code does. | [optional] 
**reviews_io_configured** | **bool** | True when a Reviews.io key is set for the account. | [optional] 
**sms_phone_number** | **str** | The default SMS number the admin offers for a new flow or campaign.  No send reads it.  An SMS step sends from its flow&#39;s or campaign&#39;s own number. | [optional] 
**sms_twilio_uuid** | **str** | The Twilio account that holds sms_phone_number. | [optional] 
**transactional_sender** | [**SfvbCommsSender**](SfvbCommsSender.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


