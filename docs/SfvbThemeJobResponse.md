# SfvbThemeJobResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** | True once the job has stopped, whether it succeeded or failed. | [optional] 
**description** | **str** | Human readable description of the job. | [optional] 
**error_message** | **str** | What to do next when the job did not produce a theme.  The internal cause is not returned; it is recorded against the job id in the server log. | [optional] 
**finished_dts** | **str** | When the job stopped, ISO 8601 UTC.  Null until it does. | [optional] 
**job_id** | **int** | Job handle.  Poll getSfvbThemeJob with this. | [optional] 
**merge_conflicts** | **[str]** | Paths of the copy&#39;s files that still have unresolved merge conflicts, read fresh on every poll, so the list shrinks as you resolve them.  Each needs its conflict marker lines resolved and the file saved before the theme can be activated.  Empty when there are none. | [optional] 
**progress** | **int** | Percent complete, 0-100. | [optional] 
**progress_description** | **str** | What the job is doing right now, for example &#39;Duplicating locale text&#39;. | [optional] 
**started_dts** | **str** | When the job started running, ISO 8601 UTC.  Null until it does. | [optional] 
**status** | **str** | Raw job status. | [optional] 
**submitted_dts** | **str** | When the job was queued, ISO 8601 UTC. | [optional] 
**success** | **bool** | True only when the job finished successfully.  Check complete first. | [optional] 
**target_path** | **str** | Path the new theme is being created at.  Returned when the job is started and on every poll, so you do not have to keep the response that started it.  Once the job completes, the theme found at this path is reported as theme_oid.  It is also what success is checked against - a finished job whose theme is not here reports success false rather than pretending. | [optional] 
**theme_oid** | **int** | Oid of the theme the job created, once it is complete and the theme exists.  Null until then. | [optional] 
**upgrade_to_version** | **str** | The version the copy was asked to be upgraded to, when the duplicate asked for an upgrade.  Null for a plain copy.  A complete job reports success only when the copy is at this version. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


