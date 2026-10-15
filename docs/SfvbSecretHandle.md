# SfvbSecretHandle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | When it stops being usable, ISO 8601 UTC. | [optional] 
**fingerprint** | **str** | The last few characters of the value, as a mask shows them, so the person can tell values apart.  Empty until entered. | [optional] 
**handle** | **str** | The handle.  Safe to log and keep in plans.  It works only for the sign-in that requested it. | [optional] 
**key** | **str** | The bulk key it is for, or empty. | [optional] 
**sink** | **str** | The secret field it can be written to. | [optional] 
**status** | **str** | pending (no value yet), ready, in_use (a write holds it), consumed, revoked or expired. | [optional] 
**target_id** | **str** | The object it can be written to, or empty when the request named none. | [optional] 
**uses_left** | **int** | Writes left.  Empty once the handle is gone. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


