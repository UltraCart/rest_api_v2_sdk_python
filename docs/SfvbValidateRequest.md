# SfvbValidateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | The container JSON to validate. | [optional] 
**container_name** | **str** | Container name it will be stored under, for example upsell-offer or email-footer.  Some rules key off the name. | [optional] 
**include_warnings** | **bool** | Include quality warnings as well as errors.  Defaults to true. | [optional] 
**marketing_email** | **bool** | For email containers, whether this is a marketing email.  Marketing emails carry CAN-SPAM footer requirements that transactional emails do not. | [optional] 
**owner_type** | **str** | Where this container is destined to live.  Determines which contextual rules apply. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


