# SfvbSecretRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | When the request was made, ISO 8601 UTC. | [optional] 
**delegated** | **bool** | True when the requester handed it to a colleague to fill in. | [optional] 
**description** | **str** | The sentence the person reads.  Written by the server, not the agent. | [optional] 
**expires_at** | **str** | When a pending request lapses, ISO 8601 UTC. | [optional] 
**expires_in_seconds** | **int** | Seconds until expires_at.  Zero once passed. | [optional] 
**fulfilled_at** | **str** | When the values were entered, ISO 8601 UTC. | [optional] 
**handle_count** | **int** | How many handles the request made. | [optional] 
**handles** | [**[SfvbSecretHandle]**](SfvbSecretHandle.md) | Every handle with its status.  Left out of the list endpoint; read one request for them. | [optional] 
**interval_seconds** | **int** | Poll no more often than this. | [optional] 
**keys** | **[str]** | The bulk keys, or empty. | [optional] 
**label** | **str** | The label the agent sent, as stored and shown. | [optional] 
**reason** | **str** | The reason the agent sent, as stored and shown. | [optional] 
**request_id** | **str** | The request id. | [optional] 
**request_url** | **str** | The page where the person enters the values.  Show it to them.  Never open or fill it in yourself. | [optional] 
**requires_totp** | **bool** | True when the person must enter a code from their authenticator app. | [optional] 
**sinks** | **[str]** | The secret fields being collected. | [optional] 
**status** | **str** | pending, fulfilled, cancelled or expired. | [optional] 
**target_id** | **str** | The object the values are for, or empty for a bulk request or an open one. | [optional] 
**user_code** | **str** | Short matching code.  Print it next to request_url so the person can check the page shows the same code. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


