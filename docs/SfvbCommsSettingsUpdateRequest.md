# SfvbCommsSettingsUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Check the change and show it without writing or using an approval. | [optional] 
**marketing_sender** | [**SfvbCommsSenderUpdate**](SfvbCommsSenderUpdate.md) |  | [optional] 
**postcard_return_address** | [**SfvbPostcardAddress**](SfvbPostcardAddress.md) |  | [optional] 
**sms_phone_number** | **str** | The default SMS number, one of the account&#39;s Twilio numbers, or an empty string to clear it. | [optional] 
**transactional_sender** | [**SfvbCommsSenderUpdate**](SfvbCommsSenderUpdate.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


