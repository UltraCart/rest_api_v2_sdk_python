# SfvbSecretRequestCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **[str]** | Bulk.  One handle per key and sink, and each key is that handle&#39;s target, such as one sending domain per key.  At most 500 handles in all. | [optional] 
**label** | **str** | A short name the person sees, marked as unverified.  At most 120 characters. | [optional] 
**reason** | **str** | Why the agent needs it.  Shown to the person, marked as unverified.  At most 500 characters. | [optional] 
**sinks** | **[str]** | The secret fields to collect, by sink id.  GET secrets/kinds lists them.  All must take the same kind of target. | [optional] 
**target_id** | **str** | The object the values are for, such as a Twilio account uuid.  Required for sinks that need an authenticator code, unless keys names the targets.  Leave it out when keys is sent. | [optional] 
**ttl_seconds** | **int** | How long each handle stays usable once the values are entered.  60 to 86400, default 3600. | [optional] 
**uses** | **int** | How many writes each handle may make.  1 to 100, default 1. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


