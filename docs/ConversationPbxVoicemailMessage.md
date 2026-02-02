# ConversationPbxVoicemailMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_sid** | **str** | Call SID | [optional] 
**duration** | **int** | Duration in seconds | [optional] 
**_from** | **str** | From phone number in E.164 | [optional] 
**from_caller_id** | **str** | From caller id (if available) | [optional] 
**listened** | **bool** | True if the voicemail has been listened to in the user interface | [optional] 
**merchant_id** | **str** | Merchant ID | [optional] 
**recording_sid** | **str** | Recording SID | [optional] 
**recording_size_bytes** | **int** | Recording size in bytes | [optional] 
**recording_status** | **str** | Recording Status | [optional]  if omitted the server will use the default value of "completed"
**recording_url** | **str** | Recording URL (expires in 4 hours) | [optional] 
**transcript_json** | **str** | JSON version of the transcript | [optional] 
**transcript_text** | **str** | Formatted text of the transcript | [optional] 
**voicemail_dts** | **str** | Voicemail date/time | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


