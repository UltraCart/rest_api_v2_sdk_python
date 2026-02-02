# ConversationPbxCallTranscript

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_transcript_s3_key** | **str** | S3 key for the full transcript text file | [optional] 
**job_name** | **str** | AWS Transcribe job name | [optional] 
**language_code** | **str** | Language code for transcription | [optional] 
**provider** | **str** | Transcription service provider | [optional] 
**segments** | [**list[ConversationPbxCallTranscriptSegment]**](ConversationPbxCallTranscriptSegment.md) | Transcript segments with speaker labels and timestamps | [optional] 
**status** | **str** | Status of the transcription | [optional] 
**transcript_json_s3_key** | **str** | S3 key for the detailed transcript JSON with speaker diarization | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


