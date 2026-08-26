# SfvbPreviewSessionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_stored** | **int** | Bytes stored in this session by the request that returned this response. | [optional] 
**expires_in_seconds** | **int** | Seconds until this session expires. | [optional] 
**max_bytes** | **int** | Maximum bytes one preview session may hold. | [optional] 
**owner_login** | **str** | Login this session belongs to.  Sessions are keyed by user, not by token. | [optional] 
**preview_session_id** | **str** | The preview session id. | [optional] 
**skipped** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Containers that were sent but could not be stored, with the reason. | [optional] 
**stored_keys** | **[str]** | Preview map keys that were stored.  A container whose owner type could not be resolved is silently dropped by the underlying store, so compare this against what you sent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


