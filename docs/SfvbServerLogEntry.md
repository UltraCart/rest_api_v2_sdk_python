# SfvbServerLogEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The area that wrote the line, such as VELOCITY, FLOW, CACHE or RUNTIME.  Empty for SYSERR lines. | [optional] 
**level** | **str** | DEBUG, INFO, WARN, ERROR or SYSERR.  SYSERR is an internal logging failure and counts as an error. | [optional] 
**logged_at** | **str** | The line&#39;s own time as the log wrote it, yyyy/MM/dd hh.mm.ss on a 12 hour clock without AM or PM.  Use the log start_date and the entry order for real timing. | [optional] 
**message** | **str** | The line&#39;s text.  A message that spanned several lines keeps its line breaks. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


