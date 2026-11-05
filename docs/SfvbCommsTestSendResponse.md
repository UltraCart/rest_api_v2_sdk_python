# SfvbCommsTestSendResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | For an SMS, the message as sent. | [optional] 
**channel** | **str** | email, sms or postcard. | [optional] 
**cost** | **float** | For a postcard, what this card costs the account. | [optional] 
**dry_run** | **bool** | True when nothing was sent. | [optional] 
**notes** | **[str]** | What else happened, such as records created by the test. | [optional] 
**recipient** | **str** | Who it went to, as a user on this account (their login), or the postcard&#39;s city and state. | [optional] 
**sent** | **bool** | True when it was sent or mailed.  False on a dry run or when it was skipped. | [optional] 
**skipped_reason** | **str** | Why it wasn&#39;t sent or mailed, when it wasn&#39;t. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


