# SfvbErrorDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable machine readable code.  Namespaced sfvb.*  Safe to match on; these are never reworded. | [optional] 
**column** | **int** | 1-indexed column number.  Populated for Velocity problems. | [optional] 
**did_you_mean** | **[str]** | Close matches for an unrecognized value, best match first.  Populated for unknown element types and unknown configuration keys. | [optional] 
**expected** | **str** | Description of what was expected instead. | [optional] 
**found** | **str** | The value that was actually found, when the problem is about a value. | [optional] 
**line** | **int** | 1-indexed line number.  Populated for Velocity problems; null for CJSON problems, which carry a pointer instead. | [optional] 
**message** | **str** | Human readable description of the problem. | [optional] 
**pointer** | **str** | JSON Pointer (RFC 6901) to the offending node within the submitted CJSON.  Null for whole-document problems. | [optional] 
**severity** | **str** | error or warning.  Warnings never fail a request. | [optional] 
**suggestion** | **str** | Optional pointer at a known good example, typically a storefront library fragment that solves the same problem properly. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


