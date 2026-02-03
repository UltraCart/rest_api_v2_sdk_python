# ConversationPbxCallRecording


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **int** | Number of audio channels in the recording (1 for mono, 2 for stereo/dual-channel) | [optional] 
**duration_seconds** | **int** | Duration of the recording in seconds | [optional] 
**is_primary** | **bool** | Whether this is the primary recording for the call | [optional] 
**recording_s3_key** | **str** | S3 key for the recording audio file | [optional] 
**recording_sid** | **str** | Twilio recording SID | [optional] 
**recording_url** | **str** | URL to access the recording | [optional] 
**status** | **str** | Status of the recording | [optional] 
**transcript** | [**ConversationPbxCallTranscript**](ConversationPbxCallTranscript.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


