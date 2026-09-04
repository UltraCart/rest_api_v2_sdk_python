# SfvbThemeJobResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** | True once the job has stopped, whether it succeeded or failed. | [optional] 
**description** | **str** | Human readable description of the job. | [optional] 
**error_message** | **str** | Failure detail.  Populated only when status is error. | [optional] 
**finished_dts** | **str** | When the job stopped.  Null until it does. | [optional] 
**job_id** | **int** | Job handle.  Poll getSfvbThemeJob with this. | [optional] 
**progress** | **int** | Percent complete, 0-100. | [optional] 
**progress_description** | **str** | What the job is doing right now, for example &#39;Duplicating locale text&#39;. | [optional] 
**started_dts** | **str** | When the job started running.  Null until it does. | [optional] 
**status** | **str** | Raw job status. | [optional] 
**submitted_dts** | **str** | When the job was queued. | [optional] 
**success** | **bool** | True only when the job finished successfully.  Check complete first. | [optional] 
**target_path** | **str** | Path the new theme is being created at.  Returned when the job is started and on every poll, so you do not have to keep the response that started it.  The theme oid itself is NOT returned, so once the job completes you list themes and match on this path.  It is also what success is checked against - a finished job whose theme is not here reports success false rather than pretending. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


